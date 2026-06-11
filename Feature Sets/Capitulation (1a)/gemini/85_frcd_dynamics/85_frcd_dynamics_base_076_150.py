"""
85_frcd_dynamics — Base Features 076-150
Domain: frcd_dynamics
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

def frcd_076_fi_abs_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_076_fi_abs_lvl_5d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rolling_mean(base, 5)

def frcd_077_fi_abs_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_077_fi_abs_zscore_5d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _zscore_rolling(base, 5)

def frcd_078_fi_abs_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_078_fi_abs_rank_5d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rank_pct(base, 5)

def frcd_079_fi_abs_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_079_fi_abs_lvl_21d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rolling_mean(base, 21)

def frcd_080_fi_abs_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_080_fi_abs_zscore_21d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _zscore_rolling(base, 21)

def frcd_081_fi_abs_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_081_fi_abs_rank_21d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rank_pct(base, 21)

def frcd_082_fi_abs_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_082_fi_abs_lvl_63d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rolling_mean(base, 63)

def frcd_083_fi_abs_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_083_fi_abs_zscore_63d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _zscore_rolling(base, 63)

def frcd_084_fi_abs_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_084_fi_abs_rank_63d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rank_pct(base, 63)

def frcd_085_fi_abs_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_085_fi_abs_lvl_126d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rolling_mean(base, 126)

def frcd_086_fi_abs_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_086_fi_abs_zscore_126d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _zscore_rolling(base, 126)

def frcd_087_fi_abs_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_087_fi_abs_rank_126d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rank_pct(base, 126)

def frcd_088_fi_abs_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_088_fi_abs_lvl_252d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rolling_mean(base, 252)

def frcd_089_fi_abs_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_089_fi_abs_zscore_252d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _zscore_rolling(base, 252)

def frcd_090_fi_abs_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_090_fi_abs_rank_252d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).abs()
    return _rank_pct(base, 252)

def frcd_091_fi_sma_rat_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_091_fi_sma_rat_lvl_5d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rolling_mean(base, 5)

def frcd_092_fi_sma_rat_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_092_fi_sma_rat_zscore_5d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _zscore_rolling(base, 5)

def frcd_093_fi_sma_rat_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_093_fi_sma_rat_rank_5d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rank_pct(base, 5)

def frcd_094_fi_sma_rat_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_094_fi_sma_rat_lvl_21d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rolling_mean(base, 21)

def frcd_095_fi_sma_rat_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_095_fi_sma_rat_zscore_21d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _zscore_rolling(base, 21)

def frcd_096_fi_sma_rat_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_096_fi_sma_rat_rank_21d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rank_pct(base, 21)

def frcd_097_fi_sma_rat_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_097_fi_sma_rat_lvl_63d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rolling_mean(base, 63)

def frcd_098_fi_sma_rat_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_098_fi_sma_rat_zscore_63d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _zscore_rolling(base, 63)

def frcd_099_fi_sma_rat_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_099_fi_sma_rat_rank_63d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rank_pct(base, 63)

def frcd_100_fi_sma_rat_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_100_fi_sma_rat_lvl_126d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rolling_mean(base, 126)

def frcd_101_fi_sma_rat_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_101_fi_sma_rat_zscore_126d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _zscore_rolling(base, 126)

def frcd_102_fi_sma_rat_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_102_fi_sma_rat_rank_126d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rank_pct(base, 126)

def frcd_103_fi_sma_rat_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_103_fi_sma_rat_lvl_252d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rolling_mean(base, 252)

def frcd_104_fi_sma_rat_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_104_fi_sma_rat_zscore_252d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _zscore_rolling(base, 252)

def frcd_105_fi_sma_rat_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_105_fi_sma_rat_rank_252d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_mean(_ewm_mean((close - close.shift(1)) * volume, 13), 20))
    return _rank_pct(base, 252)

def frcd_106_fi_rank_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_106_fi_rank_lvl_5d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rolling_mean(base, 5)

def frcd_107_fi_rank_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_107_fi_rank_zscore_5d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _zscore_rolling(base, 5)

def frcd_108_fi_rank_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_108_fi_rank_rank_5d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rank_pct(base, 5)

def frcd_109_fi_rank_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_109_fi_rank_lvl_21d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rolling_mean(base, 21)

def frcd_110_fi_rank_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_110_fi_rank_zscore_21d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _zscore_rolling(base, 21)

def frcd_111_fi_rank_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_111_fi_rank_rank_21d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rank_pct(base, 21)

def frcd_112_fi_rank_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_112_fi_rank_lvl_63d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rolling_mean(base, 63)

def frcd_113_fi_rank_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_113_fi_rank_zscore_63d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _zscore_rolling(base, 63)

def frcd_114_fi_rank_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_114_fi_rank_rank_63d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rank_pct(base, 63)

def frcd_115_fi_rank_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_115_fi_rank_lvl_126d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rolling_mean(base, 126)

def frcd_116_fi_rank_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_116_fi_rank_zscore_126d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _zscore_rolling(base, 126)

def frcd_117_fi_rank_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_117_fi_rank_rank_126d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rank_pct(base, 126)

def frcd_118_fi_rank_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_118_fi_rank_lvl_252d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rolling_mean(base, 252)

def frcd_119_fi_rank_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_119_fi_rank_zscore_252d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _zscore_rolling(base, 252)

def frcd_120_fi_rank_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_120_fi_rank_rank_252d"""
    base = _rank_pct(_ewm_mean((close - close.shift(1)) * volume, 13), 252)
    return _rank_pct(base, 252)

def frcd_121_fi_vol_rat_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_121_fi_vol_rat_lvl_5d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 5)

def frcd_122_fi_vol_rat_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_122_fi_vol_rat_zscore_5d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 5)

def frcd_123_fi_vol_rat_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_123_fi_vol_rat_rank_5d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 5)

def frcd_124_fi_vol_rat_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_124_fi_vol_rat_lvl_21d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 21)

def frcd_125_fi_vol_rat_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_125_fi_vol_rat_zscore_21d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 21)

def frcd_126_fi_vol_rat_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_126_fi_vol_rat_rank_21d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 21)

def frcd_127_fi_vol_rat_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_127_fi_vol_rat_lvl_63d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 63)

def frcd_128_fi_vol_rat_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_128_fi_vol_rat_zscore_63d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 63)

def frcd_129_fi_vol_rat_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_129_fi_vol_rat_rank_63d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 63)

def frcd_130_fi_vol_rat_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_130_fi_vol_rat_lvl_126d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 126)

def frcd_131_fi_vol_rat_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_131_fi_vol_rat_zscore_126d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 126)

def frcd_132_fi_vol_rat_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_132_fi_vol_rat_rank_126d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 126)

def frcd_133_fi_vol_rat_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_133_fi_vol_rat_lvl_252d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 252)

def frcd_134_fi_vol_rat_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_134_fi_vol_rat_zscore_252d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 252)

def frcd_135_fi_vol_rat_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_135_fi_vol_rat_rank_252d"""
    base = _safe_div((close - close.shift(1)) * volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 252)

def frcd_136_fi_disp_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_136_fi_disp_lvl_5d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rolling_mean(base, 5)

def frcd_137_fi_disp_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_137_fi_disp_zscore_5d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _zscore_rolling(base, 5)

def frcd_138_fi_disp_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_138_fi_disp_rank_5d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rank_pct(base, 5)

def frcd_139_fi_disp_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_139_fi_disp_lvl_21d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rolling_mean(base, 21)

def frcd_140_fi_disp_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_140_fi_disp_zscore_21d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _zscore_rolling(base, 21)

def frcd_141_fi_disp_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_141_fi_disp_rank_21d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rank_pct(base, 21)

def frcd_142_fi_disp_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_142_fi_disp_lvl_63d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rolling_mean(base, 63)

def frcd_143_fi_disp_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_143_fi_disp_zscore_63d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _zscore_rolling(base, 63)

def frcd_144_fi_disp_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_144_fi_disp_rank_63d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rank_pct(base, 63)

def frcd_145_fi_disp_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_145_fi_disp_lvl_126d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rolling_mean(base, 126)

def frcd_146_fi_disp_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_146_fi_disp_zscore_126d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _zscore_rolling(base, 126)

def frcd_147_fi_disp_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_147_fi_disp_rank_126d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rank_pct(base, 126)

def frcd_148_fi_disp_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_148_fi_disp_lvl_252d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rolling_mean(base, 252)

def frcd_149_fi_disp_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_149_fi_disp_zscore_252d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _zscore_rolling(base, 252)

def frcd_150_fi_disp_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_150_fi_disp_rank_252d"""
    base = _safe_div(_ewm_mean((close - close.shift(1)) * volume, 13), _rolling_std((close - close.shift(1)) * volume, 63))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V85_REGISTRY_2 = {
    "frcd_076_fi_abs_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_076_fi_abs_lvl_5d},
    "frcd_077_fi_abs_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_077_fi_abs_zscore_5d},
    "frcd_078_fi_abs_rank_5d": {"inputs": ["close", "volume"], "func": frcd_078_fi_abs_rank_5d},
    "frcd_079_fi_abs_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_079_fi_abs_lvl_21d},
    "frcd_080_fi_abs_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_080_fi_abs_zscore_21d},
    "frcd_081_fi_abs_rank_21d": {"inputs": ["close", "volume"], "func": frcd_081_fi_abs_rank_21d},
    "frcd_082_fi_abs_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_082_fi_abs_lvl_63d},
    "frcd_083_fi_abs_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_083_fi_abs_zscore_63d},
    "frcd_084_fi_abs_rank_63d": {"inputs": ["close", "volume"], "func": frcd_084_fi_abs_rank_63d},
    "frcd_085_fi_abs_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_085_fi_abs_lvl_126d},
    "frcd_086_fi_abs_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_086_fi_abs_zscore_126d},
    "frcd_087_fi_abs_rank_126d": {"inputs": ["close", "volume"], "func": frcd_087_fi_abs_rank_126d},
    "frcd_088_fi_abs_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_088_fi_abs_lvl_252d},
    "frcd_089_fi_abs_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_089_fi_abs_zscore_252d},
    "frcd_090_fi_abs_rank_252d": {"inputs": ["close", "volume"], "func": frcd_090_fi_abs_rank_252d},
    "frcd_091_fi_sma_rat_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_091_fi_sma_rat_lvl_5d},
    "frcd_092_fi_sma_rat_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_092_fi_sma_rat_zscore_5d},
    "frcd_093_fi_sma_rat_rank_5d": {"inputs": ["close", "volume"], "func": frcd_093_fi_sma_rat_rank_5d},
    "frcd_094_fi_sma_rat_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_094_fi_sma_rat_lvl_21d},
    "frcd_095_fi_sma_rat_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_095_fi_sma_rat_zscore_21d},
    "frcd_096_fi_sma_rat_rank_21d": {"inputs": ["close", "volume"], "func": frcd_096_fi_sma_rat_rank_21d},
    "frcd_097_fi_sma_rat_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_097_fi_sma_rat_lvl_63d},
    "frcd_098_fi_sma_rat_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_098_fi_sma_rat_zscore_63d},
    "frcd_099_fi_sma_rat_rank_63d": {"inputs": ["close", "volume"], "func": frcd_099_fi_sma_rat_rank_63d},
    "frcd_100_fi_sma_rat_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_100_fi_sma_rat_lvl_126d},
    "frcd_101_fi_sma_rat_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_101_fi_sma_rat_zscore_126d},
    "frcd_102_fi_sma_rat_rank_126d": {"inputs": ["close", "volume"], "func": frcd_102_fi_sma_rat_rank_126d},
    "frcd_103_fi_sma_rat_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_103_fi_sma_rat_lvl_252d},
    "frcd_104_fi_sma_rat_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_104_fi_sma_rat_zscore_252d},
    "frcd_105_fi_sma_rat_rank_252d": {"inputs": ["close", "volume"], "func": frcd_105_fi_sma_rat_rank_252d},
    "frcd_106_fi_rank_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_106_fi_rank_lvl_5d},
    "frcd_107_fi_rank_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_107_fi_rank_zscore_5d},
    "frcd_108_fi_rank_rank_5d": {"inputs": ["close", "volume"], "func": frcd_108_fi_rank_rank_5d},
    "frcd_109_fi_rank_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_109_fi_rank_lvl_21d},
    "frcd_110_fi_rank_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_110_fi_rank_zscore_21d},
    "frcd_111_fi_rank_rank_21d": {"inputs": ["close", "volume"], "func": frcd_111_fi_rank_rank_21d},
    "frcd_112_fi_rank_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_112_fi_rank_lvl_63d},
    "frcd_113_fi_rank_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_113_fi_rank_zscore_63d},
    "frcd_114_fi_rank_rank_63d": {"inputs": ["close", "volume"], "func": frcd_114_fi_rank_rank_63d},
    "frcd_115_fi_rank_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_115_fi_rank_lvl_126d},
    "frcd_116_fi_rank_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_116_fi_rank_zscore_126d},
    "frcd_117_fi_rank_rank_126d": {"inputs": ["close", "volume"], "func": frcd_117_fi_rank_rank_126d},
    "frcd_118_fi_rank_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_118_fi_rank_lvl_252d},
    "frcd_119_fi_rank_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_119_fi_rank_zscore_252d},
    "frcd_120_fi_rank_rank_252d": {"inputs": ["close", "volume"], "func": frcd_120_fi_rank_rank_252d},
    "frcd_121_fi_vol_rat_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_121_fi_vol_rat_lvl_5d},
    "frcd_122_fi_vol_rat_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_122_fi_vol_rat_zscore_5d},
    "frcd_123_fi_vol_rat_rank_5d": {"inputs": ["close", "volume"], "func": frcd_123_fi_vol_rat_rank_5d},
    "frcd_124_fi_vol_rat_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_124_fi_vol_rat_lvl_21d},
    "frcd_125_fi_vol_rat_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_125_fi_vol_rat_zscore_21d},
    "frcd_126_fi_vol_rat_rank_21d": {"inputs": ["close", "volume"], "func": frcd_126_fi_vol_rat_rank_21d},
    "frcd_127_fi_vol_rat_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_127_fi_vol_rat_lvl_63d},
    "frcd_128_fi_vol_rat_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_128_fi_vol_rat_zscore_63d},
    "frcd_129_fi_vol_rat_rank_63d": {"inputs": ["close", "volume"], "func": frcd_129_fi_vol_rat_rank_63d},
    "frcd_130_fi_vol_rat_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_130_fi_vol_rat_lvl_126d},
    "frcd_131_fi_vol_rat_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_131_fi_vol_rat_zscore_126d},
    "frcd_132_fi_vol_rat_rank_126d": {"inputs": ["close", "volume"], "func": frcd_132_fi_vol_rat_rank_126d},
    "frcd_133_fi_vol_rat_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_133_fi_vol_rat_lvl_252d},
    "frcd_134_fi_vol_rat_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_134_fi_vol_rat_zscore_252d},
    "frcd_135_fi_vol_rat_rank_252d": {"inputs": ["close", "volume"], "func": frcd_135_fi_vol_rat_rank_252d},
    "frcd_136_fi_disp_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_136_fi_disp_lvl_5d},
    "frcd_137_fi_disp_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_137_fi_disp_zscore_5d},
    "frcd_138_fi_disp_rank_5d": {"inputs": ["close", "volume"], "func": frcd_138_fi_disp_rank_5d},
    "frcd_139_fi_disp_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_139_fi_disp_lvl_21d},
    "frcd_140_fi_disp_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_140_fi_disp_zscore_21d},
    "frcd_141_fi_disp_rank_21d": {"inputs": ["close", "volume"], "func": frcd_141_fi_disp_rank_21d},
    "frcd_142_fi_disp_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_142_fi_disp_lvl_63d},
    "frcd_143_fi_disp_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_143_fi_disp_zscore_63d},
    "frcd_144_fi_disp_rank_63d": {"inputs": ["close", "volume"], "func": frcd_144_fi_disp_rank_63d},
    "frcd_145_fi_disp_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_145_fi_disp_lvl_126d},
    "frcd_146_fi_disp_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_146_fi_disp_zscore_126d},
    "frcd_147_fi_disp_rank_126d": {"inputs": ["close", "volume"], "func": frcd_147_fi_disp_rank_126d},
    "frcd_148_fi_disp_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_148_fi_disp_lvl_252d},
    "frcd_149_fi_disp_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_149_fi_disp_zscore_252d},
    "frcd_150_fi_disp_rank_252d": {"inputs": ["close", "volume"], "func": frcd_150_fi_disp_rank_252d},
}
