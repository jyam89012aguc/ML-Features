"""
116_extreme_day_density — Base Features Part 2
Domain: extreme_day_density
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

def exdd_121_extreme_range_day_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_121_extreme_range_day_lvl_5d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rolling_mean(base, 5)

def exdd_122_extreme_range_day_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_122_extreme_range_day_zscore_5d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _zscore_rolling(base, 5)

def exdd_123_extreme_range_day_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_123_extreme_range_day_rank_5d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rank_pct(base, 5)

def exdd_124_extreme_range_day_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_124_extreme_range_day_lvl_21d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rolling_mean(base, 21)

def exdd_125_extreme_range_day_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_125_extreme_range_day_zscore_21d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _zscore_rolling(base, 21)

def exdd_126_extreme_range_day_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_126_extreme_range_day_rank_21d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rank_pct(base, 21)

def exdd_127_extreme_range_day_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_127_extreme_range_day_lvl_63d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rolling_mean(base, 63)

def exdd_128_extreme_range_day_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_128_extreme_range_day_zscore_63d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _zscore_rolling(base, 63)

def exdd_129_extreme_range_day_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_129_extreme_range_day_rank_63d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rank_pct(base, 63)

def exdd_130_extreme_range_day_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_130_extreme_range_day_lvl_126d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rolling_mean(base, 126)

def exdd_131_extreme_range_day_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_131_extreme_range_day_zscore_126d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _zscore_rolling(base, 126)

def exdd_132_extreme_range_day_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_132_extreme_range_day_rank_126d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rank_pct(base, 126)

def exdd_133_extreme_range_day_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_133_extreme_range_day_lvl_252d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rolling_mean(base, 252)

def exdd_134_extreme_range_day_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_134_extreme_range_day_zscore_252d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _zscore_rolling(base, 252)

def exdd_135_extreme_range_day_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_135_extreme_range_day_rank_252d
    ECONOMIC RATIONALE: Frequency of days with >10% intraday ranges.
    """
    base = ((high - low) / close > 0.1).astype(float)
    return _rank_pct(base, 252)

def exdd_136_extreme_gap_day_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_136_extreme_gap_day_lvl_5d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rolling_mean(base, 5)

def exdd_137_extreme_gap_day_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_137_extreme_gap_day_zscore_5d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _zscore_rolling(base, 5)

def exdd_138_extreme_gap_day_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_138_extreme_gap_day_rank_5d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rank_pct(base, 5)

def exdd_139_extreme_gap_day_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_139_extreme_gap_day_lvl_21d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rolling_mean(base, 21)

def exdd_140_extreme_gap_day_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_140_extreme_gap_day_zscore_21d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _zscore_rolling(base, 21)

def exdd_141_extreme_gap_day_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_141_extreme_gap_day_rank_21d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rank_pct(base, 21)

def exdd_142_extreme_gap_day_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_142_extreme_gap_day_lvl_63d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rolling_mean(base, 63)

def exdd_143_extreme_gap_day_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_143_extreme_gap_day_zscore_63d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _zscore_rolling(base, 63)

def exdd_144_extreme_gap_day_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_144_extreme_gap_day_rank_63d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rank_pct(base, 63)

def exdd_145_extreme_gap_day_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_145_extreme_gap_day_lvl_126d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rolling_mean(base, 126)

def exdd_146_extreme_gap_day_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_146_extreme_gap_day_zscore_126d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _zscore_rolling(base, 126)

def exdd_147_extreme_gap_day_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_147_extreme_gap_day_rank_126d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rank_pct(base, 126)

def exdd_148_extreme_gap_day_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_148_extreme_gap_day_lvl_252d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rolling_mean(base, 252)

def exdd_149_extreme_gap_day_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_149_extreme_gap_day_zscore_252d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _zscore_rolling(base, 252)

def exdd_150_extreme_gap_day_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_150_extreme_gap_day_rank_252d
    ECONOMIC RATIONALE: Frequency of days with >3% overnight gaps.
    """
    base = (abs(open/close.shift(1)-1) > 0.03).astype(float)
    return _rank_pct(base, 252)

def exdd_151_extreme_day_persistence_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_151_extreme_day_persistence_lvl_5d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rolling_mean(base, 5)

def exdd_152_extreme_day_persistence_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_152_extreme_day_persistence_zscore_5d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _zscore_rolling(base, 5)

def exdd_153_extreme_day_persistence_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_153_extreme_day_persistence_rank_5d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rank_pct(base, 5)

def exdd_154_extreme_day_persistence_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_154_extreme_day_persistence_lvl_21d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rolling_mean(base, 21)

def exdd_155_extreme_day_persistence_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_155_extreme_day_persistence_zscore_21d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _zscore_rolling(base, 21)

def exdd_156_extreme_day_persistence_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_156_extreme_day_persistence_rank_21d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rank_pct(base, 21)

def exdd_157_extreme_day_persistence_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_157_extreme_day_persistence_lvl_63d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rolling_mean(base, 63)

def exdd_158_extreme_day_persistence_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_158_extreme_day_persistence_zscore_63d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _zscore_rolling(base, 63)

def exdd_159_extreme_day_persistence_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_159_extreme_day_persistence_rank_63d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rank_pct(base, 63)

def exdd_160_extreme_day_persistence_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_160_extreme_day_persistence_lvl_126d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rolling_mean(base, 126)

def exdd_161_extreme_day_persistence_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_161_extreme_day_persistence_zscore_126d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _zscore_rolling(base, 126)

def exdd_162_extreme_day_persistence_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_162_extreme_day_persistence_rank_126d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rank_pct(base, 126)

def exdd_163_extreme_day_persistence_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_163_extreme_day_persistence_lvl_252d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rolling_mean(base, 252)

def exdd_164_extreme_day_persistence_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_164_extreme_day_persistence_zscore_252d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _zscore_rolling(base, 252)

def exdd_165_extreme_day_persistence_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_165_extreme_day_persistence_rank_252d
    ECONOMIC RATIONALE: Sequential extreme price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)
    return _rank_pct(base, 252)

def exdd_166_extreme_day_decay_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_166_extreme_day_decay_lvl_5d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rolling_mean(base, 5)

def exdd_167_extreme_day_decay_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_167_extreme_day_decay_zscore_5d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _zscore_rolling(base, 5)

def exdd_168_extreme_day_decay_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_168_extreme_day_decay_rank_5d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rank_pct(base, 5)

def exdd_169_extreme_day_decay_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_169_extreme_day_decay_lvl_21d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rolling_mean(base, 21)

def exdd_170_extreme_day_decay_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_170_extreme_day_decay_zscore_21d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _zscore_rolling(base, 21)

def exdd_171_extreme_day_decay_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_171_extreme_day_decay_rank_21d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rank_pct(base, 21)

def exdd_172_extreme_day_decay_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_172_extreme_day_decay_lvl_63d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rolling_mean(base, 63)

def exdd_173_extreme_day_decay_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_173_extreme_day_decay_zscore_63d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _zscore_rolling(base, 63)

def exdd_174_extreme_day_decay_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_174_extreme_day_decay_rank_63d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rank_pct(base, 63)

def exdd_175_extreme_day_decay_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_175_extreme_day_decay_lvl_126d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rolling_mean(base, 126)

def exdd_176_extreme_day_decay_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_176_extreme_day_decay_zscore_126d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _zscore_rolling(base, 126)

def exdd_177_extreme_day_decay_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_177_extreme_day_decay_rank_126d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rank_pct(base, 126)

def exdd_178_extreme_day_decay_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_178_extreme_day_decay_lvl_252d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rolling_mean(base, 252)

def exdd_179_extreme_day_decay_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_179_extreme_day_decay_zscore_252d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _zscore_rolling(base, 252)

def exdd_180_extreme_day_decay_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_180_extreme_day_decay_rank_252d
    ECONOMIC RATIONALE: Time-weighted density of extreme events.
    """
    base = ((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()
    return _rank_pct(base, 252)

def exdd_181_extreme_day_vol_ratio_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_181_extreme_day_vol_ratio_lvl_5d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rolling_mean(base, 5)

def exdd_182_extreme_day_vol_ratio_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_182_extreme_day_vol_ratio_zscore_5d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _zscore_rolling(base, 5)

def exdd_183_extreme_day_vol_ratio_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_183_extreme_day_vol_ratio_rank_5d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rank_pct(base, 5)

def exdd_184_extreme_day_vol_ratio_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_184_extreme_day_vol_ratio_lvl_21d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rolling_mean(base, 21)

def exdd_185_extreme_day_vol_ratio_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_185_extreme_day_vol_ratio_zscore_21d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _zscore_rolling(base, 21)

def exdd_186_extreme_day_vol_ratio_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_186_extreme_day_vol_ratio_rank_21d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rank_pct(base, 21)

def exdd_187_extreme_day_vol_ratio_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_187_extreme_day_vol_ratio_lvl_63d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rolling_mean(base, 63)

def exdd_188_extreme_day_vol_ratio_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_188_extreme_day_vol_ratio_zscore_63d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _zscore_rolling(base, 63)

def exdd_189_extreme_day_vol_ratio_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_189_extreme_day_vol_ratio_rank_63d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rank_pct(base, 63)

def exdd_190_extreme_day_vol_ratio_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_190_extreme_day_vol_ratio_lvl_126d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rolling_mean(base, 126)

def exdd_191_extreme_day_vol_ratio_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_191_extreme_day_vol_ratio_zscore_126d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _zscore_rolling(base, 126)

def exdd_192_extreme_day_vol_ratio_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_192_extreme_day_vol_ratio_rank_126d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rank_pct(base, 126)

def exdd_193_extreme_day_vol_ratio_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_193_extreme_day_vol_ratio_lvl_252d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rolling_mean(base, 252)

def exdd_194_extreme_day_vol_ratio_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_194_extreme_day_vol_ratio_zscore_252d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _zscore_rolling(base, 252)

def exdd_195_extreme_day_vol_ratio_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_195_extreme_day_vol_ratio_rank_252d
    ECONOMIC RATIONALE: Volume intensity on extreme days.
    """
    base = volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()
    return _rank_pct(base, 252)

def exdd_196_extreme_day_regime_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_196_extreme_day_regime_lvl_5d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rolling_mean(base, 5)

def exdd_197_extreme_day_regime_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_197_extreme_day_regime_zscore_5d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _zscore_rolling(base, 5)

def exdd_198_extreme_day_regime_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_198_extreme_day_regime_rank_5d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rank_pct(base, 5)

def exdd_199_extreme_day_regime_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_199_extreme_day_regime_lvl_21d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rolling_mean(base, 21)

def exdd_200_extreme_day_regime_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_200_extreme_day_regime_zscore_21d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _zscore_rolling(base, 21)

def exdd_201_extreme_day_regime_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_201_extreme_day_regime_rank_21d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rank_pct(base, 21)

def exdd_202_extreme_day_regime_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_202_extreme_day_regime_lvl_63d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rolling_mean(base, 63)

def exdd_203_extreme_day_regime_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_203_extreme_day_regime_zscore_63d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _zscore_rolling(base, 63)

def exdd_204_extreme_day_regime_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_204_extreme_day_regime_rank_63d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rank_pct(base, 63)

def exdd_205_extreme_day_regime_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_205_extreme_day_regime_lvl_126d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rolling_mean(base, 126)

def exdd_206_extreme_day_regime_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_206_extreme_day_regime_zscore_126d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _zscore_rolling(base, 126)

def exdd_207_extreme_day_regime_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_207_extreme_day_regime_rank_126d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rank_pct(base, 126)

def exdd_208_extreme_day_regime_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_208_extreme_day_regime_lvl_252d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rolling_mean(base, 252)

def exdd_209_extreme_day_regime_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_209_extreme_day_regime_zscore_252d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _zscore_rolling(base, 252)

def exdd_210_extreme_day_regime_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_210_extreme_day_regime_rank_252d
    ECONOMIC RATIONALE: Proportion of days that are extreme.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63
    return _rank_pct(base, 252)

def exdd_211_extreme_day_exhaustion_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_211_extreme_day_exhaustion_lvl_5d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 5)

def exdd_212_extreme_day_exhaustion_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_212_extreme_day_exhaustion_zscore_5d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 5)

def exdd_213_extreme_day_exhaustion_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_213_extreme_day_exhaustion_rank_5d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 5)

def exdd_214_extreme_day_exhaustion_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_214_extreme_day_exhaustion_lvl_21d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 21)

def exdd_215_extreme_day_exhaustion_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_215_extreme_day_exhaustion_zscore_21d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 21)

def exdd_216_extreme_day_exhaustion_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_216_extreme_day_exhaustion_rank_21d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 21)

def exdd_217_extreme_day_exhaustion_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_217_extreme_day_exhaustion_lvl_63d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 63)

def exdd_218_extreme_day_exhaustion_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_218_extreme_day_exhaustion_zscore_63d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 63)

def exdd_219_extreme_day_exhaustion_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_219_extreme_day_exhaustion_rank_63d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 63)

def exdd_220_extreme_day_exhaustion_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_220_extreme_day_exhaustion_lvl_126d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 126)

def exdd_221_extreme_day_exhaustion_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_221_extreme_day_exhaustion_zscore_126d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 126)

def exdd_222_extreme_day_exhaustion_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_222_extreme_day_exhaustion_rank_126d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 126)

def exdd_223_extreme_day_exhaustion_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_223_extreme_day_exhaustion_lvl_252d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 252)

def exdd_224_extreme_day_exhaustion_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_224_extreme_day_exhaustion_zscore_252d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 252)

def exdd_225_extreme_day_exhaustion_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_225_extreme_day_exhaustion_rank_252d
    ECONOMIC RATIONALE: High density of extreme days followed by price stalling.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V116_REGISTRY_2 = {
    "exdd_121_extreme_range_day_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_121_extreme_range_day_lvl_5d},
    "exdd_122_extreme_range_day_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_122_extreme_range_day_zscore_5d},
    "exdd_123_extreme_range_day_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_123_extreme_range_day_rank_5d},
    "exdd_124_extreme_range_day_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_124_extreme_range_day_lvl_21d},
    "exdd_125_extreme_range_day_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_125_extreme_range_day_zscore_21d},
    "exdd_126_extreme_range_day_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_126_extreme_range_day_rank_21d},
    "exdd_127_extreme_range_day_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_127_extreme_range_day_lvl_63d},
    "exdd_128_extreme_range_day_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_128_extreme_range_day_zscore_63d},
    "exdd_129_extreme_range_day_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_129_extreme_range_day_rank_63d},
    "exdd_130_extreme_range_day_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_130_extreme_range_day_lvl_126d},
    "exdd_131_extreme_range_day_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_131_extreme_range_day_zscore_126d},
    "exdd_132_extreme_range_day_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_132_extreme_range_day_rank_126d},
    "exdd_133_extreme_range_day_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_133_extreme_range_day_lvl_252d},
    "exdd_134_extreme_range_day_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_134_extreme_range_day_zscore_252d},
    "exdd_135_extreme_range_day_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_135_extreme_range_day_rank_252d},
    "exdd_136_extreme_gap_day_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_136_extreme_gap_day_lvl_5d},
    "exdd_137_extreme_gap_day_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_137_extreme_gap_day_zscore_5d},
    "exdd_138_extreme_gap_day_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_138_extreme_gap_day_rank_5d},
    "exdd_139_extreme_gap_day_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_139_extreme_gap_day_lvl_21d},
    "exdd_140_extreme_gap_day_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_140_extreme_gap_day_zscore_21d},
    "exdd_141_extreme_gap_day_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_141_extreme_gap_day_rank_21d},
    "exdd_142_extreme_gap_day_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_142_extreme_gap_day_lvl_63d},
    "exdd_143_extreme_gap_day_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_143_extreme_gap_day_zscore_63d},
    "exdd_144_extreme_gap_day_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_144_extreme_gap_day_rank_63d},
    "exdd_145_extreme_gap_day_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_145_extreme_gap_day_lvl_126d},
    "exdd_146_extreme_gap_day_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_146_extreme_gap_day_zscore_126d},
    "exdd_147_extreme_gap_day_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_147_extreme_gap_day_rank_126d},
    "exdd_148_extreme_gap_day_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_148_extreme_gap_day_lvl_252d},
    "exdd_149_extreme_gap_day_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_149_extreme_gap_day_zscore_252d},
    "exdd_150_extreme_gap_day_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_150_extreme_gap_day_rank_252d},
    "exdd_151_extreme_day_persistence_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_151_extreme_day_persistence_lvl_5d},
    "exdd_152_extreme_day_persistence_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_152_extreme_day_persistence_zscore_5d},
    "exdd_153_extreme_day_persistence_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_153_extreme_day_persistence_rank_5d},
    "exdd_154_extreme_day_persistence_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_154_extreme_day_persistence_lvl_21d},
    "exdd_155_extreme_day_persistence_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_155_extreme_day_persistence_zscore_21d},
    "exdd_156_extreme_day_persistence_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_156_extreme_day_persistence_rank_21d},
    "exdd_157_extreme_day_persistence_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_157_extreme_day_persistence_lvl_63d},
    "exdd_158_extreme_day_persistence_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_158_extreme_day_persistence_zscore_63d},
    "exdd_159_extreme_day_persistence_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_159_extreme_day_persistence_rank_63d},
    "exdd_160_extreme_day_persistence_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_160_extreme_day_persistence_lvl_126d},
    "exdd_161_extreme_day_persistence_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_161_extreme_day_persistence_zscore_126d},
    "exdd_162_extreme_day_persistence_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_162_extreme_day_persistence_rank_126d},
    "exdd_163_extreme_day_persistence_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_163_extreme_day_persistence_lvl_252d},
    "exdd_164_extreme_day_persistence_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_164_extreme_day_persistence_zscore_252d},
    "exdd_165_extreme_day_persistence_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_165_extreme_day_persistence_rank_252d},
    "exdd_166_extreme_day_decay_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_166_extreme_day_decay_lvl_5d},
    "exdd_167_extreme_day_decay_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_167_extreme_day_decay_zscore_5d},
    "exdd_168_extreme_day_decay_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_168_extreme_day_decay_rank_5d},
    "exdd_169_extreme_day_decay_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_169_extreme_day_decay_lvl_21d},
    "exdd_170_extreme_day_decay_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_170_extreme_day_decay_zscore_21d},
    "exdd_171_extreme_day_decay_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_171_extreme_day_decay_rank_21d},
    "exdd_172_extreme_day_decay_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_172_extreme_day_decay_lvl_63d},
    "exdd_173_extreme_day_decay_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_173_extreme_day_decay_zscore_63d},
    "exdd_174_extreme_day_decay_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_174_extreme_day_decay_rank_63d},
    "exdd_175_extreme_day_decay_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_175_extreme_day_decay_lvl_126d},
    "exdd_176_extreme_day_decay_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_176_extreme_day_decay_zscore_126d},
    "exdd_177_extreme_day_decay_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_177_extreme_day_decay_rank_126d},
    "exdd_178_extreme_day_decay_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_178_extreme_day_decay_lvl_252d},
    "exdd_179_extreme_day_decay_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_179_extreme_day_decay_zscore_252d},
    "exdd_180_extreme_day_decay_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_180_extreme_day_decay_rank_252d},
    "exdd_181_extreme_day_vol_ratio_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_181_extreme_day_vol_ratio_lvl_5d},
    "exdd_182_extreme_day_vol_ratio_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_182_extreme_day_vol_ratio_zscore_5d},
    "exdd_183_extreme_day_vol_ratio_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_183_extreme_day_vol_ratio_rank_5d},
    "exdd_184_extreme_day_vol_ratio_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_184_extreme_day_vol_ratio_lvl_21d},
    "exdd_185_extreme_day_vol_ratio_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_185_extreme_day_vol_ratio_zscore_21d},
    "exdd_186_extreme_day_vol_ratio_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_186_extreme_day_vol_ratio_rank_21d},
    "exdd_187_extreme_day_vol_ratio_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_187_extreme_day_vol_ratio_lvl_63d},
    "exdd_188_extreme_day_vol_ratio_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_188_extreme_day_vol_ratio_zscore_63d},
    "exdd_189_extreme_day_vol_ratio_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_189_extreme_day_vol_ratio_rank_63d},
    "exdd_190_extreme_day_vol_ratio_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_190_extreme_day_vol_ratio_lvl_126d},
    "exdd_191_extreme_day_vol_ratio_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_191_extreme_day_vol_ratio_zscore_126d},
    "exdd_192_extreme_day_vol_ratio_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_192_extreme_day_vol_ratio_rank_126d},
    "exdd_193_extreme_day_vol_ratio_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_193_extreme_day_vol_ratio_lvl_252d},
    "exdd_194_extreme_day_vol_ratio_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_194_extreme_day_vol_ratio_zscore_252d},
    "exdd_195_extreme_day_vol_ratio_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_195_extreme_day_vol_ratio_rank_252d},
    "exdd_196_extreme_day_regime_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_196_extreme_day_regime_lvl_5d},
    "exdd_197_extreme_day_regime_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_197_extreme_day_regime_zscore_5d},
    "exdd_198_extreme_day_regime_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_198_extreme_day_regime_rank_5d},
    "exdd_199_extreme_day_regime_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_199_extreme_day_regime_lvl_21d},
    "exdd_200_extreme_day_regime_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_200_extreme_day_regime_zscore_21d},
    "exdd_201_extreme_day_regime_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_201_extreme_day_regime_rank_21d},
    "exdd_202_extreme_day_regime_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_202_extreme_day_regime_lvl_63d},
    "exdd_203_extreme_day_regime_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_203_extreme_day_regime_zscore_63d},
    "exdd_204_extreme_day_regime_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_204_extreme_day_regime_rank_63d},
    "exdd_205_extreme_day_regime_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_205_extreme_day_regime_lvl_126d},
    "exdd_206_extreme_day_regime_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_206_extreme_day_regime_zscore_126d},
    "exdd_207_extreme_day_regime_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_207_extreme_day_regime_rank_126d},
    "exdd_208_extreme_day_regime_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_208_extreme_day_regime_lvl_252d},
    "exdd_209_extreme_day_regime_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_209_extreme_day_regime_zscore_252d},
    "exdd_210_extreme_day_regime_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_210_extreme_day_regime_rank_252d},
    "exdd_211_extreme_day_exhaustion_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_211_extreme_day_exhaustion_lvl_5d},
    "exdd_212_extreme_day_exhaustion_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_212_extreme_day_exhaustion_zscore_5d},
    "exdd_213_extreme_day_exhaustion_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_213_extreme_day_exhaustion_rank_5d},
    "exdd_214_extreme_day_exhaustion_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_214_extreme_day_exhaustion_lvl_21d},
    "exdd_215_extreme_day_exhaustion_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_215_extreme_day_exhaustion_zscore_21d},
    "exdd_216_extreme_day_exhaustion_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_216_extreme_day_exhaustion_rank_21d},
    "exdd_217_extreme_day_exhaustion_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_217_extreme_day_exhaustion_lvl_63d},
    "exdd_218_extreme_day_exhaustion_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_218_extreme_day_exhaustion_zscore_63d},
    "exdd_219_extreme_day_exhaustion_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_219_extreme_day_exhaustion_rank_63d},
    "exdd_220_extreme_day_exhaustion_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_220_extreme_day_exhaustion_lvl_126d},
    "exdd_221_extreme_day_exhaustion_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_221_extreme_day_exhaustion_zscore_126d},
    "exdd_222_extreme_day_exhaustion_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_222_extreme_day_exhaustion_rank_126d},
    "exdd_223_extreme_day_exhaustion_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_223_extreme_day_exhaustion_lvl_252d},
    "exdd_224_extreme_day_exhaustion_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_224_extreme_day_exhaustion_zscore_252d},
    "exdd_225_extreme_day_exhaustion_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_225_extreme_day_exhaustion_rank_252d},
}
