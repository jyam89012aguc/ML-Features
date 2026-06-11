"""
106_support_violation — Base Features Part 2
Domain: support_violation
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

def supv_121_support_reversal_trap_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_121_support_reversal_trap_lvl_5d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rolling_mean(base, 5)

def supv_122_support_reversal_trap_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_122_support_reversal_trap_zscore_5d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _zscore_rolling(base, 5)

def supv_123_support_reversal_trap_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_123_support_reversal_trap_rank_5d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rank_pct(base, 5)

def supv_124_support_reversal_trap_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_124_support_reversal_trap_lvl_21d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rolling_mean(base, 21)

def supv_125_support_reversal_trap_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_125_support_reversal_trap_zscore_21d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _zscore_rolling(base, 21)

def supv_126_support_reversal_trap_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_126_support_reversal_trap_rank_21d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rank_pct(base, 21)

def supv_127_support_reversal_trap_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_127_support_reversal_trap_lvl_63d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rolling_mean(base, 63)

def supv_128_support_reversal_trap_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_128_support_reversal_trap_zscore_63d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _zscore_rolling(base, 63)

def supv_129_support_reversal_trap_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_129_support_reversal_trap_rank_63d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rank_pct(base, 63)

def supv_130_support_reversal_trap_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_130_support_reversal_trap_lvl_126d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rolling_mean(base, 126)

def supv_131_support_reversal_trap_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_131_support_reversal_trap_zscore_126d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _zscore_rolling(base, 126)

def supv_132_support_reversal_trap_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_132_support_reversal_trap_rank_126d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rank_pct(base, 126)

def supv_133_support_reversal_trap_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_133_support_reversal_trap_lvl_252d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rolling_mean(base, 252)

def supv_134_support_reversal_trap_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_134_support_reversal_trap_zscore_252d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _zscore_rolling(base, 252)

def supv_135_support_reversal_trap_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_135_support_reversal_trap_rank_252d
    ECONOMIC RATIONALE: Attempted intraday reversal at support.
    """
    base = (low < low.rolling(63).min().shift(1)) & (close > open)
    return _rank_pct(base, 252)

def supv_136_support_gap_down_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_136_support_gap_down_lvl_5d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rolling_mean(base, 5)

def supv_137_support_gap_down_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_137_support_gap_down_zscore_5d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _zscore_rolling(base, 5)

def supv_138_support_gap_down_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_138_support_gap_down_rank_5d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rank_pct(base, 5)

def supv_139_support_gap_down_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_139_support_gap_down_lvl_21d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rolling_mean(base, 21)

def supv_140_support_gap_down_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_140_support_gap_down_zscore_21d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _zscore_rolling(base, 21)

def supv_141_support_gap_down_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_141_support_gap_down_rank_21d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rank_pct(base, 21)

def supv_142_support_gap_down_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_142_support_gap_down_lvl_63d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rolling_mean(base, 63)

def supv_143_support_gap_down_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_143_support_gap_down_zscore_63d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _zscore_rolling(base, 63)

def supv_144_support_gap_down_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_144_support_gap_down_rank_63d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rank_pct(base, 63)

def supv_145_support_gap_down_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_145_support_gap_down_lvl_126d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rolling_mean(base, 126)

def supv_146_support_gap_down_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_146_support_gap_down_zscore_126d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _zscore_rolling(base, 126)

def supv_147_support_gap_down_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_147_support_gap_down_rank_126d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rank_pct(base, 126)

def supv_148_support_gap_down_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_148_support_gap_down_lvl_252d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rolling_mean(base, 252)

def supv_149_support_gap_down_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_149_support_gap_down_zscore_252d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _zscore_rolling(base, 252)

def supv_150_support_gap_down_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_150_support_gap_down_rank_252d
    ECONOMIC RATIONALE: Gapping down through major support.
    """
    base = (high < low.shift(1)) & (low < low.rolling(63).min())
    return _rank_pct(base, 252)

def supv_151_psychological_support_100_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_151_psychological_support_100_lvl_5d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rolling_mean(base, 5)

def supv_152_psychological_support_100_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_152_psychological_support_100_zscore_5d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _zscore_rolling(base, 5)

def supv_153_psychological_support_100_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_153_psychological_support_100_rank_5d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rank_pct(base, 5)

def supv_154_psychological_support_100_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_154_psychological_support_100_lvl_21d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rolling_mean(base, 21)

def supv_155_psychological_support_100_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_155_psychological_support_100_zscore_21d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _zscore_rolling(base, 21)

def supv_156_psychological_support_100_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_156_psychological_support_100_rank_21d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rank_pct(base, 21)

def supv_157_psychological_support_100_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_157_psychological_support_100_lvl_63d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rolling_mean(base, 63)

def supv_158_psychological_support_100_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_158_psychological_support_100_zscore_63d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _zscore_rolling(base, 63)

def supv_159_psychological_support_100_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_159_psychological_support_100_rank_63d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rank_pct(base, 63)

def supv_160_psychological_support_100_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_160_psychological_support_100_lvl_126d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rolling_mean(base, 126)

def supv_161_psychological_support_100_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_161_psychological_support_100_zscore_126d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _zscore_rolling(base, 126)

def supv_162_psychological_support_100_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_162_psychological_support_100_rank_126d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rank_pct(base, 126)

def supv_163_psychological_support_100_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_163_psychological_support_100_lvl_252d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rolling_mean(base, 252)

def supv_164_psychological_support_100_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_164_psychological_support_100_zscore_252d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _zscore_rolling(base, 252)

def supv_165_psychological_support_100_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_165_psychological_support_100_rank_252d
    ECONOMIC RATIONALE: Proximity to round number support levels.
    """
    base = (close % 100 < 2).astype(float)
    return _rank_pct(base, 252)

def supv_166_support_vol_z_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_166_support_vol_z_lvl_5d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rolling_mean(base, 5)

def supv_167_support_vol_z_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_167_support_vol_z_zscore_5d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _zscore_rolling(base, 5)

def supv_168_support_vol_z_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_168_support_vol_z_rank_5d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rank_pct(base, 5)

def supv_169_support_vol_z_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_169_support_vol_z_lvl_21d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rolling_mean(base, 21)

def supv_170_support_vol_z_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_170_support_vol_z_zscore_21d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _zscore_rolling(base, 21)

def supv_171_support_vol_z_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_171_support_vol_z_rank_21d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rank_pct(base, 21)

def supv_172_support_vol_z_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_172_support_vol_z_lvl_63d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rolling_mean(base, 63)

def supv_173_support_vol_z_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_173_support_vol_z_zscore_63d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _zscore_rolling(base, 63)

def supv_174_support_vol_z_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_174_support_vol_z_rank_63d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rank_pct(base, 63)

def supv_175_support_vol_z_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_175_support_vol_z_lvl_126d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rolling_mean(base, 126)

def supv_176_support_vol_z_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_176_support_vol_z_zscore_126d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _zscore_rolling(base, 126)

def supv_177_support_vol_z_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_177_support_vol_z_rank_126d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rank_pct(base, 126)

def supv_178_support_vol_z_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_178_support_vol_z_lvl_252d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rolling_mean(base, 252)

def supv_179_support_vol_z_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_179_support_vol_z_zscore_252d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _zscore_rolling(base, 252)

def supv_180_support_vol_z_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_180_support_vol_z_rank_252d
    ECONOMIC RATIONALE: Abnormal volume during support breaks.
    """
    base = _zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)
    return _rank_pct(base, 252)

def supv_181_structural_breakdown_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_181_structural_breakdown_lvl_5d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rolling_mean(base, 5)

def supv_182_structural_breakdown_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_182_structural_breakdown_zscore_5d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _zscore_rolling(base, 5)

def supv_183_structural_breakdown_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_183_structural_breakdown_rank_5d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rank_pct(base, 5)

def supv_184_structural_breakdown_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_184_structural_breakdown_lvl_21d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rolling_mean(base, 21)

def supv_185_structural_breakdown_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_185_structural_breakdown_zscore_21d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _zscore_rolling(base, 21)

def supv_186_structural_breakdown_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_186_structural_breakdown_rank_21d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rank_pct(base, 21)

def supv_187_structural_breakdown_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_187_structural_breakdown_lvl_63d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rolling_mean(base, 63)

def supv_188_structural_breakdown_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_188_structural_breakdown_zscore_63d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _zscore_rolling(base, 63)

def supv_189_structural_breakdown_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_189_structural_breakdown_rank_63d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rank_pct(base, 63)

def supv_190_structural_breakdown_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_190_structural_breakdown_lvl_126d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rolling_mean(base, 126)

def supv_191_structural_breakdown_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_191_structural_breakdown_zscore_126d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _zscore_rolling(base, 126)

def supv_192_structural_breakdown_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_192_structural_breakdown_rank_126d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rank_pct(base, 126)

def supv_193_structural_breakdown_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_193_structural_breakdown_lvl_252d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rolling_mean(base, 252)

def supv_194_structural_breakdown_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_194_structural_breakdown_zscore_252d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _zscore_rolling(base, 252)

def supv_195_structural_breakdown_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_195_structural_breakdown_rank_252d
    ECONOMIC RATIONALE: Breakdown below long-term structural envelopes.
    """
    base = close < low.rolling(252).mean() - 2*low.rolling(252).std()
    return _rank_pct(base, 252)

def supv_196_support_recovery_rate_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_196_support_recovery_rate_lvl_5d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rolling_mean(base, 5)

def supv_197_support_recovery_rate_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_197_support_recovery_rate_zscore_5d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _zscore_rolling(base, 5)

def supv_198_support_recovery_rate_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_198_support_recovery_rate_rank_5d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rank_pct(base, 5)

def supv_199_support_recovery_rate_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_199_support_recovery_rate_lvl_21d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rolling_mean(base, 21)

def supv_200_support_recovery_rate_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_200_support_recovery_rate_zscore_21d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _zscore_rolling(base, 21)

def supv_201_support_recovery_rate_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_201_support_recovery_rate_rank_21d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rank_pct(base, 21)

def supv_202_support_recovery_rate_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_202_support_recovery_rate_lvl_63d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rolling_mean(base, 63)

def supv_203_support_recovery_rate_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_203_support_recovery_rate_zscore_63d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _zscore_rolling(base, 63)

def supv_204_support_recovery_rate_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_204_support_recovery_rate_rank_63d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rank_pct(base, 63)

def supv_205_support_recovery_rate_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_205_support_recovery_rate_lvl_126d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rolling_mean(base, 126)

def supv_206_support_recovery_rate_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_206_support_recovery_rate_zscore_126d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _zscore_rolling(base, 126)

def supv_207_support_recovery_rate_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_207_support_recovery_rate_rank_126d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rank_pct(base, 126)

def supv_208_support_recovery_rate_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_208_support_recovery_rate_lvl_252d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rolling_mean(base, 252)

def supv_209_support_recovery_rate_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_209_support_recovery_rate_zscore_252d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _zscore_rolling(base, 252)

def supv_210_support_recovery_rate_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_210_support_recovery_rate_rank_252d
    ECONOMIC RATIONALE: Ratio of current price to quarterly support.
    """
    base = close / low.rolling(63).min()
    return _rank_pct(base, 252)

def supv_211_support_cascade_risk_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_211_support_cascade_risk_lvl_5d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rolling_mean(base, 5)

def supv_212_support_cascade_risk_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_212_support_cascade_risk_zscore_5d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _zscore_rolling(base, 5)

def supv_213_support_cascade_risk_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_213_support_cascade_risk_rank_5d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rank_pct(base, 5)

def supv_214_support_cascade_risk_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_214_support_cascade_risk_lvl_21d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rolling_mean(base, 21)

def supv_215_support_cascade_risk_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_215_support_cascade_risk_zscore_21d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _zscore_rolling(base, 21)

def supv_216_support_cascade_risk_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_216_support_cascade_risk_rank_21d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rank_pct(base, 21)

def supv_217_support_cascade_risk_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_217_support_cascade_risk_lvl_63d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rolling_mean(base, 63)

def supv_218_support_cascade_risk_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_218_support_cascade_risk_zscore_63d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _zscore_rolling(base, 63)

def supv_219_support_cascade_risk_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_219_support_cascade_risk_rank_63d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rank_pct(base, 63)

def supv_220_support_cascade_risk_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_220_support_cascade_risk_lvl_126d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rolling_mean(base, 126)

def supv_221_support_cascade_risk_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_221_support_cascade_risk_zscore_126d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _zscore_rolling(base, 126)

def supv_222_support_cascade_risk_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_222_support_cascade_risk_rank_126d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rank_pct(base, 126)

def supv_223_support_cascade_risk_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_223_support_cascade_risk_lvl_252d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rolling_mean(base, 252)

def supv_224_support_cascade_risk_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_224_support_cascade_risk_zscore_252d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _zscore_rolling(base, 252)

def supv_225_support_cascade_risk_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_225_support_cascade_risk_rank_252d
    ECONOMIC RATIONALE: Sequential support violations indicating a cascade.
    """
    base = (low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V106_REGISTRY_2 = {
    "supv_121_support_reversal_trap_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_121_support_reversal_trap_lvl_5d},
    "supv_122_support_reversal_trap_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_122_support_reversal_trap_zscore_5d},
    "supv_123_support_reversal_trap_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_123_support_reversal_trap_rank_5d},
    "supv_124_support_reversal_trap_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_124_support_reversal_trap_lvl_21d},
    "supv_125_support_reversal_trap_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_125_support_reversal_trap_zscore_21d},
    "supv_126_support_reversal_trap_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_126_support_reversal_trap_rank_21d},
    "supv_127_support_reversal_trap_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_127_support_reversal_trap_lvl_63d},
    "supv_128_support_reversal_trap_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_128_support_reversal_trap_zscore_63d},
    "supv_129_support_reversal_trap_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_129_support_reversal_trap_rank_63d},
    "supv_130_support_reversal_trap_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_130_support_reversal_trap_lvl_126d},
    "supv_131_support_reversal_trap_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_131_support_reversal_trap_zscore_126d},
    "supv_132_support_reversal_trap_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_132_support_reversal_trap_rank_126d},
    "supv_133_support_reversal_trap_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_133_support_reversal_trap_lvl_252d},
    "supv_134_support_reversal_trap_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_134_support_reversal_trap_zscore_252d},
    "supv_135_support_reversal_trap_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_135_support_reversal_trap_rank_252d},
    "supv_136_support_gap_down_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_136_support_gap_down_lvl_5d},
    "supv_137_support_gap_down_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_137_support_gap_down_zscore_5d},
    "supv_138_support_gap_down_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_138_support_gap_down_rank_5d},
    "supv_139_support_gap_down_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_139_support_gap_down_lvl_21d},
    "supv_140_support_gap_down_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_140_support_gap_down_zscore_21d},
    "supv_141_support_gap_down_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_141_support_gap_down_rank_21d},
    "supv_142_support_gap_down_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_142_support_gap_down_lvl_63d},
    "supv_143_support_gap_down_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_143_support_gap_down_zscore_63d},
    "supv_144_support_gap_down_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_144_support_gap_down_rank_63d},
    "supv_145_support_gap_down_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_145_support_gap_down_lvl_126d},
    "supv_146_support_gap_down_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_146_support_gap_down_zscore_126d},
    "supv_147_support_gap_down_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_147_support_gap_down_rank_126d},
    "supv_148_support_gap_down_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_148_support_gap_down_lvl_252d},
    "supv_149_support_gap_down_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_149_support_gap_down_zscore_252d},
    "supv_150_support_gap_down_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_150_support_gap_down_rank_252d},
    "supv_151_psychological_support_100_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_151_psychological_support_100_lvl_5d},
    "supv_152_psychological_support_100_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_152_psychological_support_100_zscore_5d},
    "supv_153_psychological_support_100_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_153_psychological_support_100_rank_5d},
    "supv_154_psychological_support_100_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_154_psychological_support_100_lvl_21d},
    "supv_155_psychological_support_100_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_155_psychological_support_100_zscore_21d},
    "supv_156_psychological_support_100_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_156_psychological_support_100_rank_21d},
    "supv_157_psychological_support_100_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_157_psychological_support_100_lvl_63d},
    "supv_158_psychological_support_100_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_158_psychological_support_100_zscore_63d},
    "supv_159_psychological_support_100_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_159_psychological_support_100_rank_63d},
    "supv_160_psychological_support_100_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_160_psychological_support_100_lvl_126d},
    "supv_161_psychological_support_100_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_161_psychological_support_100_zscore_126d},
    "supv_162_psychological_support_100_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_162_psychological_support_100_rank_126d},
    "supv_163_psychological_support_100_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_163_psychological_support_100_lvl_252d},
    "supv_164_psychological_support_100_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_164_psychological_support_100_zscore_252d},
    "supv_165_psychological_support_100_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_165_psychological_support_100_rank_252d},
    "supv_166_support_vol_z_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_166_support_vol_z_lvl_5d},
    "supv_167_support_vol_z_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_167_support_vol_z_zscore_5d},
    "supv_168_support_vol_z_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_168_support_vol_z_rank_5d},
    "supv_169_support_vol_z_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_169_support_vol_z_lvl_21d},
    "supv_170_support_vol_z_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_170_support_vol_z_zscore_21d},
    "supv_171_support_vol_z_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_171_support_vol_z_rank_21d},
    "supv_172_support_vol_z_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_172_support_vol_z_lvl_63d},
    "supv_173_support_vol_z_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_173_support_vol_z_zscore_63d},
    "supv_174_support_vol_z_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_174_support_vol_z_rank_63d},
    "supv_175_support_vol_z_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_175_support_vol_z_lvl_126d},
    "supv_176_support_vol_z_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_176_support_vol_z_zscore_126d},
    "supv_177_support_vol_z_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_177_support_vol_z_rank_126d},
    "supv_178_support_vol_z_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_178_support_vol_z_lvl_252d},
    "supv_179_support_vol_z_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_179_support_vol_z_zscore_252d},
    "supv_180_support_vol_z_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_180_support_vol_z_rank_252d},
    "supv_181_structural_breakdown_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_181_structural_breakdown_lvl_5d},
    "supv_182_structural_breakdown_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_182_structural_breakdown_zscore_5d},
    "supv_183_structural_breakdown_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_183_structural_breakdown_rank_5d},
    "supv_184_structural_breakdown_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_184_structural_breakdown_lvl_21d},
    "supv_185_structural_breakdown_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_185_structural_breakdown_zscore_21d},
    "supv_186_structural_breakdown_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_186_structural_breakdown_rank_21d},
    "supv_187_structural_breakdown_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_187_structural_breakdown_lvl_63d},
    "supv_188_structural_breakdown_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_188_structural_breakdown_zscore_63d},
    "supv_189_structural_breakdown_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_189_structural_breakdown_rank_63d},
    "supv_190_structural_breakdown_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_190_structural_breakdown_lvl_126d},
    "supv_191_structural_breakdown_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_191_structural_breakdown_zscore_126d},
    "supv_192_structural_breakdown_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_192_structural_breakdown_rank_126d},
    "supv_193_structural_breakdown_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_193_structural_breakdown_lvl_252d},
    "supv_194_structural_breakdown_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_194_structural_breakdown_zscore_252d},
    "supv_195_structural_breakdown_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_195_structural_breakdown_rank_252d},
    "supv_196_support_recovery_rate_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_196_support_recovery_rate_lvl_5d},
    "supv_197_support_recovery_rate_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_197_support_recovery_rate_zscore_5d},
    "supv_198_support_recovery_rate_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_198_support_recovery_rate_rank_5d},
    "supv_199_support_recovery_rate_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_199_support_recovery_rate_lvl_21d},
    "supv_200_support_recovery_rate_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_200_support_recovery_rate_zscore_21d},
    "supv_201_support_recovery_rate_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_201_support_recovery_rate_rank_21d},
    "supv_202_support_recovery_rate_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_202_support_recovery_rate_lvl_63d},
    "supv_203_support_recovery_rate_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_203_support_recovery_rate_zscore_63d},
    "supv_204_support_recovery_rate_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_204_support_recovery_rate_rank_63d},
    "supv_205_support_recovery_rate_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_205_support_recovery_rate_lvl_126d},
    "supv_206_support_recovery_rate_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_206_support_recovery_rate_zscore_126d},
    "supv_207_support_recovery_rate_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_207_support_recovery_rate_rank_126d},
    "supv_208_support_recovery_rate_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_208_support_recovery_rate_lvl_252d},
    "supv_209_support_recovery_rate_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_209_support_recovery_rate_zscore_252d},
    "supv_210_support_recovery_rate_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_210_support_recovery_rate_rank_252d},
    "supv_211_support_cascade_risk_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_211_support_cascade_risk_lvl_5d},
    "supv_212_support_cascade_risk_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_212_support_cascade_risk_zscore_5d},
    "supv_213_support_cascade_risk_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_213_support_cascade_risk_rank_5d},
    "supv_214_support_cascade_risk_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_214_support_cascade_risk_lvl_21d},
    "supv_215_support_cascade_risk_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_215_support_cascade_risk_zscore_21d},
    "supv_216_support_cascade_risk_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_216_support_cascade_risk_rank_21d},
    "supv_217_support_cascade_risk_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_217_support_cascade_risk_lvl_63d},
    "supv_218_support_cascade_risk_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_218_support_cascade_risk_zscore_63d},
    "supv_219_support_cascade_risk_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_219_support_cascade_risk_rank_63d},
    "supv_220_support_cascade_risk_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_220_support_cascade_risk_lvl_126d},
    "supv_221_support_cascade_risk_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_221_support_cascade_risk_zscore_126d},
    "supv_222_support_cascade_risk_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_222_support_cascade_risk_rank_126d},
    "supv_223_support_cascade_risk_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_223_support_cascade_risk_lvl_252d},
    "supv_224_support_cascade_risk_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_224_support_cascade_risk_zscore_252d},
    "supv_225_support_cascade_risk_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_225_support_cascade_risk_rank_252d},
}
