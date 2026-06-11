"""
86_adln_dynamics — Base Features 076-150
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

def adln_076_adl_level_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_076_adl_level_lvl_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 5)

def adln_077_adl_level_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_077_adl_level_zscore_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 5)

def adln_078_adl_level_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_078_adl_level_rank_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 5)

def adln_079_adl_level_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_079_adl_level_lvl_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 21)

def adln_080_adl_level_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_080_adl_level_zscore_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 21)

def adln_081_adl_level_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_081_adl_level_rank_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 21)

def adln_082_adl_level_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_082_adl_level_lvl_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 63)

def adln_083_adl_level_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_083_adl_level_zscore_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 63)

def adln_084_adl_level_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_084_adl_level_rank_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 63)

def adln_085_adl_level_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_085_adl_level_lvl_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 126)

def adln_086_adl_level_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_086_adl_level_zscore_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 126)

def adln_087_adl_level_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_087_adl_level_rank_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 126)

def adln_088_adl_level_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_088_adl_level_lvl_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 252)

def adln_089_adl_level_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_089_adl_level_zscore_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 252)

def adln_090_adl_level_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_090_adl_level_rank_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 252)

def adln_091_adl_vol_rat_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_091_adl_vol_rat_lvl_5d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rolling_mean(base, 5)

def adln_092_adl_vol_rat_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_092_adl_vol_rat_zscore_5d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _zscore_rolling(base, 5)

def adln_093_adl_vol_rat_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_093_adl_vol_rat_rank_5d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rank_pct(base, 5)

def adln_094_adl_vol_rat_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_094_adl_vol_rat_lvl_21d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rolling_mean(base, 21)

def adln_095_adl_vol_rat_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_095_adl_vol_rat_zscore_21d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _zscore_rolling(base, 21)

def adln_096_adl_vol_rat_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_096_adl_vol_rat_rank_21d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rank_pct(base, 21)

def adln_097_adl_vol_rat_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_097_adl_vol_rat_lvl_63d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rolling_mean(base, 63)

def adln_098_adl_vol_rat_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_098_adl_vol_rat_zscore_63d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _zscore_rolling(base, 63)

def adln_099_adl_vol_rat_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_099_adl_vol_rat_rank_63d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rank_pct(base, 63)

def adln_100_adl_vol_rat_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_100_adl_vol_rat_lvl_126d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rolling_mean(base, 126)

def adln_101_adl_vol_rat_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_101_adl_vol_rat_zscore_126d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _zscore_rolling(base, 126)

def adln_102_adl_vol_rat_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_102_adl_vol_rat_rank_126d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rank_pct(base, 126)

def adln_103_adl_vol_rat_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_103_adl_vol_rat_lvl_252d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rolling_mean(base, 252)

def adln_104_adl_vol_rat_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_104_adl_vol_rat_zscore_252d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _zscore_rolling(base, 252)

def adln_105_adl_vol_rat_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_105_adl_vol_rat_rank_252d"""
    base = _safe_div((((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume), volume)
    return _rank_pct(base, 252)

def adln_106_adl_range_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_106_adl_range_lvl_5d"""
    base = high - low
    return _rolling_mean(base, 5)

def adln_107_adl_range_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_107_adl_range_zscore_5d"""
    base = high - low
    return _zscore_rolling(base, 5)

def adln_108_adl_range_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_108_adl_range_rank_5d"""
    base = high - low
    return _rank_pct(base, 5)

def adln_109_adl_range_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_109_adl_range_lvl_21d"""
    base = high - low
    return _rolling_mean(base, 21)

def adln_110_adl_range_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_110_adl_range_zscore_21d"""
    base = high - low
    return _zscore_rolling(base, 21)

def adln_111_adl_range_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_111_adl_range_rank_21d"""
    base = high - low
    return _rank_pct(base, 21)

def adln_112_adl_range_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_112_adl_range_lvl_63d"""
    base = high - low
    return _rolling_mean(base, 63)

def adln_113_adl_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_113_adl_range_zscore_63d"""
    base = high - low
    return _zscore_rolling(base, 63)

def adln_114_adl_range_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_114_adl_range_rank_63d"""
    base = high - low
    return _rank_pct(base, 63)

def adln_115_adl_range_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_115_adl_range_lvl_126d"""
    base = high - low
    return _rolling_mean(base, 126)

def adln_116_adl_range_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_116_adl_range_zscore_126d"""
    base = high - low
    return _zscore_rolling(base, 126)

def adln_117_adl_range_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_117_adl_range_rank_126d"""
    base = high - low
    return _rank_pct(base, 126)

def adln_118_adl_range_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_118_adl_range_lvl_252d"""
    base = high - low
    return _rolling_mean(base, 252)

def adln_119_adl_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_119_adl_range_zscore_252d"""
    base = high - low
    return _zscore_rolling(base, 252)

def adln_120_adl_range_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_120_adl_range_rank_252d"""
    base = high - low
    return _rank_pct(base, 252)

def adln_121_adl_close_pos_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_121_adl_close_pos_lvl_5d"""
    base = _safe_div(close - low, high - low)
    return _rolling_mean(base, 5)

def adln_122_adl_close_pos_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_122_adl_close_pos_zscore_5d"""
    base = _safe_div(close - low, high - low)
    return _zscore_rolling(base, 5)

def adln_123_adl_close_pos_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_123_adl_close_pos_rank_5d"""
    base = _safe_div(close - low, high - low)
    return _rank_pct(base, 5)

def adln_124_adl_close_pos_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_124_adl_close_pos_lvl_21d"""
    base = _safe_div(close - low, high - low)
    return _rolling_mean(base, 21)

def adln_125_adl_close_pos_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_125_adl_close_pos_zscore_21d"""
    base = _safe_div(close - low, high - low)
    return _zscore_rolling(base, 21)

def adln_126_adl_close_pos_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_126_adl_close_pos_rank_21d"""
    base = _safe_div(close - low, high - low)
    return _rank_pct(base, 21)

def adln_127_adl_close_pos_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_127_adl_close_pos_lvl_63d"""
    base = _safe_div(close - low, high - low)
    return _rolling_mean(base, 63)

def adln_128_adl_close_pos_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_128_adl_close_pos_zscore_63d"""
    base = _safe_div(close - low, high - low)
    return _zscore_rolling(base, 63)

def adln_129_adl_close_pos_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_129_adl_close_pos_rank_63d"""
    base = _safe_div(close - low, high - low)
    return _rank_pct(base, 63)

def adln_130_adl_close_pos_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_130_adl_close_pos_lvl_126d"""
    base = _safe_div(close - low, high - low)
    return _rolling_mean(base, 126)

def adln_131_adl_close_pos_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_131_adl_close_pos_zscore_126d"""
    base = _safe_div(close - low, high - low)
    return _zscore_rolling(base, 126)

def adln_132_adl_close_pos_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_132_adl_close_pos_rank_126d"""
    base = _safe_div(close - low, high - low)
    return _rank_pct(base, 126)

def adln_133_adl_close_pos_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_133_adl_close_pos_lvl_252d"""
    base = _safe_div(close - low, high - low)
    return _rolling_mean(base, 252)

def adln_134_adl_close_pos_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_134_adl_close_pos_zscore_252d"""
    base = _safe_div(close - low, high - low)
    return _zscore_rolling(base, 252)

def adln_135_adl_close_pos_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_135_adl_close_pos_rank_252d"""
    base = _safe_div(close - low, high - low)
    return _rank_pct(base, 252)

def adln_136_adl_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_136_adl_dist_lvl_5d"""
    base = close - (high + low) / 2
    return _rolling_mean(base, 5)

def adln_137_adl_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_137_adl_dist_zscore_5d"""
    base = close - (high + low) / 2
    return _zscore_rolling(base, 5)

def adln_138_adl_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_138_adl_dist_rank_5d"""
    base = close - (high + low) / 2
    return _rank_pct(base, 5)

def adln_139_adl_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_139_adl_dist_lvl_21d"""
    base = close - (high + low) / 2
    return _rolling_mean(base, 21)

def adln_140_adl_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_140_adl_dist_zscore_21d"""
    base = close - (high + low) / 2
    return _zscore_rolling(base, 21)

def adln_141_adl_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_141_adl_dist_rank_21d"""
    base = close - (high + low) / 2
    return _rank_pct(base, 21)

def adln_142_adl_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_142_adl_dist_lvl_63d"""
    base = close - (high + low) / 2
    return _rolling_mean(base, 63)

def adln_143_adl_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_143_adl_dist_zscore_63d"""
    base = close - (high + low) / 2
    return _zscore_rolling(base, 63)

def adln_144_adl_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_144_adl_dist_rank_63d"""
    base = close - (high + low) / 2
    return _rank_pct(base, 63)

def adln_145_adl_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_145_adl_dist_lvl_126d"""
    base = close - (high + low) / 2
    return _rolling_mean(base, 126)

def adln_146_adl_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_146_adl_dist_zscore_126d"""
    base = close - (high + low) / 2
    return _zscore_rolling(base, 126)

def adln_147_adl_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_147_adl_dist_rank_126d"""
    base = close - (high + low) / 2
    return _rank_pct(base, 126)

def adln_148_adl_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_148_adl_dist_lvl_252d"""
    base = close - (high + low) / 2
    return _rolling_mean(base, 252)

def adln_149_adl_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_149_adl_dist_zscore_252d"""
    base = close - (high + low) / 2
    return _zscore_rolling(base, 252)

def adln_150_adl_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_150_adl_dist_rank_252d"""
    base = close - (high + low) / 2
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V86_REGISTRY_2 = {
    "adln_076_adl_level_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_076_adl_level_lvl_5d},
    "adln_077_adl_level_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_077_adl_level_zscore_5d},
    "adln_078_adl_level_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_078_adl_level_rank_5d},
    "adln_079_adl_level_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_079_adl_level_lvl_21d},
    "adln_080_adl_level_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_080_adl_level_zscore_21d},
    "adln_081_adl_level_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_081_adl_level_rank_21d},
    "adln_082_adl_level_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_082_adl_level_lvl_63d},
    "adln_083_adl_level_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_083_adl_level_zscore_63d},
    "adln_084_adl_level_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_084_adl_level_rank_63d},
    "adln_085_adl_level_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_085_adl_level_lvl_126d},
    "adln_086_adl_level_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_086_adl_level_zscore_126d},
    "adln_087_adl_level_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_087_adl_level_rank_126d},
    "adln_088_adl_level_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_088_adl_level_lvl_252d},
    "adln_089_adl_level_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_089_adl_level_zscore_252d},
    "adln_090_adl_level_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_090_adl_level_rank_252d},
    "adln_091_adl_vol_rat_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_091_adl_vol_rat_lvl_5d},
    "adln_092_adl_vol_rat_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_092_adl_vol_rat_zscore_5d},
    "adln_093_adl_vol_rat_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_093_adl_vol_rat_rank_5d},
    "adln_094_adl_vol_rat_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_094_adl_vol_rat_lvl_21d},
    "adln_095_adl_vol_rat_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_095_adl_vol_rat_zscore_21d},
    "adln_096_adl_vol_rat_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_096_adl_vol_rat_rank_21d},
    "adln_097_adl_vol_rat_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_097_adl_vol_rat_lvl_63d},
    "adln_098_adl_vol_rat_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_098_adl_vol_rat_zscore_63d},
    "adln_099_adl_vol_rat_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_099_adl_vol_rat_rank_63d},
    "adln_100_adl_vol_rat_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_100_adl_vol_rat_lvl_126d},
    "adln_101_adl_vol_rat_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_101_adl_vol_rat_zscore_126d},
    "adln_102_adl_vol_rat_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_102_adl_vol_rat_rank_126d},
    "adln_103_adl_vol_rat_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_103_adl_vol_rat_lvl_252d},
    "adln_104_adl_vol_rat_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_104_adl_vol_rat_zscore_252d},
    "adln_105_adl_vol_rat_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_105_adl_vol_rat_rank_252d},
    "adln_106_adl_range_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_106_adl_range_lvl_5d},
    "adln_107_adl_range_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_107_adl_range_zscore_5d},
    "adln_108_adl_range_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_108_adl_range_rank_5d},
    "adln_109_adl_range_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_109_adl_range_lvl_21d},
    "adln_110_adl_range_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_110_adl_range_zscore_21d},
    "adln_111_adl_range_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_111_adl_range_rank_21d},
    "adln_112_adl_range_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_112_adl_range_lvl_63d},
    "adln_113_adl_range_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_113_adl_range_zscore_63d},
    "adln_114_adl_range_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_114_adl_range_rank_63d},
    "adln_115_adl_range_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_115_adl_range_lvl_126d},
    "adln_116_adl_range_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_116_adl_range_zscore_126d},
    "adln_117_adl_range_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_117_adl_range_rank_126d},
    "adln_118_adl_range_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_118_adl_range_lvl_252d},
    "adln_119_adl_range_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_119_adl_range_zscore_252d},
    "adln_120_adl_range_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_120_adl_range_rank_252d},
    "adln_121_adl_close_pos_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_121_adl_close_pos_lvl_5d},
    "adln_122_adl_close_pos_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_122_adl_close_pos_zscore_5d},
    "adln_123_adl_close_pos_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_123_adl_close_pos_rank_5d},
    "adln_124_adl_close_pos_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_124_adl_close_pos_lvl_21d},
    "adln_125_adl_close_pos_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_125_adl_close_pos_zscore_21d},
    "adln_126_adl_close_pos_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_126_adl_close_pos_rank_21d},
    "adln_127_adl_close_pos_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_127_adl_close_pos_lvl_63d},
    "adln_128_adl_close_pos_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_128_adl_close_pos_zscore_63d},
    "adln_129_adl_close_pos_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_129_adl_close_pos_rank_63d},
    "adln_130_adl_close_pos_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_130_adl_close_pos_lvl_126d},
    "adln_131_adl_close_pos_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_131_adl_close_pos_zscore_126d},
    "adln_132_adl_close_pos_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_132_adl_close_pos_rank_126d},
    "adln_133_adl_close_pos_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_133_adl_close_pos_lvl_252d},
    "adln_134_adl_close_pos_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_134_adl_close_pos_zscore_252d},
    "adln_135_adl_close_pos_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_135_adl_close_pos_rank_252d},
    "adln_136_adl_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_136_adl_dist_lvl_5d},
    "adln_137_adl_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_137_adl_dist_zscore_5d},
    "adln_138_adl_dist_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_138_adl_dist_rank_5d},
    "adln_139_adl_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_139_adl_dist_lvl_21d},
    "adln_140_adl_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_140_adl_dist_zscore_21d},
    "adln_141_adl_dist_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_141_adl_dist_rank_21d},
    "adln_142_adl_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_142_adl_dist_lvl_63d},
    "adln_143_adl_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_143_adl_dist_zscore_63d},
    "adln_144_adl_dist_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_144_adl_dist_rank_63d},
    "adln_145_adl_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_145_adl_dist_lvl_126d},
    "adln_146_adl_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_146_adl_dist_zscore_126d},
    "adln_147_adl_dist_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_147_adl_dist_rank_126d},
    "adln_148_adl_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_148_adl_dist_lvl_252d},
    "adln_149_adl_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_149_adl_dist_zscore_252d},
    "adln_150_adl_dist_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_150_adl_dist_rank_252d},
}
