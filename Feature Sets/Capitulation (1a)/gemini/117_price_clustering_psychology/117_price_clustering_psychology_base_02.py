"""
117_price_clustering_psychology — Base Features Part 2
Domain: price_clustering_psychology
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

def ppsy_121_digit_bias_last_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_121_digit_bias_last_lvl_5d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rolling_mean(base, 5)

def ppsy_122_digit_bias_last_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_122_digit_bias_last_zscore_5d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _zscore_rolling(base, 5)

def ppsy_123_digit_bias_last_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_123_digit_bias_last_rank_5d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rank_pct(base, 5)

def ppsy_124_digit_bias_last_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_124_digit_bias_last_lvl_21d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rolling_mean(base, 21)

def ppsy_125_digit_bias_last_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_125_digit_bias_last_zscore_21d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _zscore_rolling(base, 21)

def ppsy_126_digit_bias_last_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_126_digit_bias_last_rank_21d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rank_pct(base, 21)

def ppsy_127_digit_bias_last_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_127_digit_bias_last_lvl_63d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rolling_mean(base, 63)

def ppsy_128_digit_bias_last_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_128_digit_bias_last_zscore_63d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _zscore_rolling(base, 63)

def ppsy_129_digit_bias_last_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_129_digit_bias_last_rank_63d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rank_pct(base, 63)

def ppsy_130_digit_bias_last_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_130_digit_bias_last_lvl_126d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rolling_mean(base, 126)

def ppsy_131_digit_bias_last_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_131_digit_bias_last_zscore_126d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _zscore_rolling(base, 126)

def ppsy_132_digit_bias_last_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_132_digit_bias_last_rank_126d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rank_pct(base, 126)

def ppsy_133_digit_bias_last_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_133_digit_bias_last_lvl_252d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rolling_mean(base, 252)

def ppsy_134_digit_bias_last_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_134_digit_bias_last_zscore_252d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _zscore_rolling(base, 252)

def ppsy_135_digit_bias_last_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_135_digit_bias_last_rank_252d
    ECONOMIC RATIONALE: Bias in the final cent digit.
    """
    base = (close * 100 % 10).rolling(63).mean()
    return _rank_pct(base, 252)

def ppsy_136_price_magnet_effect_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_136_price_magnet_effect_lvl_5d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rolling_mean(base, 5)

def ppsy_137_price_magnet_effect_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_137_price_magnet_effect_zscore_5d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _zscore_rolling(base, 5)

def ppsy_138_price_magnet_effect_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_138_price_magnet_effect_rank_5d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rank_pct(base, 5)

def ppsy_139_price_magnet_effect_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_139_price_magnet_effect_lvl_21d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rolling_mean(base, 21)

def ppsy_140_price_magnet_effect_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_140_price_magnet_effect_zscore_21d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _zscore_rolling(base, 21)

def ppsy_141_price_magnet_effect_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_141_price_magnet_effect_rank_21d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rank_pct(base, 21)

def ppsy_142_price_magnet_effect_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_142_price_magnet_effect_lvl_63d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rolling_mean(base, 63)

def ppsy_143_price_magnet_effect_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_143_price_magnet_effect_zscore_63d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _zscore_rolling(base, 63)

def ppsy_144_price_magnet_effect_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_144_price_magnet_effect_rank_63d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rank_pct(base, 63)

def ppsy_145_price_magnet_effect_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_145_price_magnet_effect_lvl_126d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rolling_mean(base, 126)

def ppsy_146_price_magnet_effect_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_146_price_magnet_effect_zscore_126d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _zscore_rolling(base, 126)

def ppsy_147_price_magnet_effect_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_147_price_magnet_effect_rank_126d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rank_pct(base, 126)

def ppsy_148_price_magnet_effect_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_148_price_magnet_effect_lvl_252d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rolling_mean(base, 252)

def ppsy_149_price_magnet_effect_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_149_price_magnet_effect_zscore_252d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _zscore_rolling(base, 252)

def ppsy_150_price_magnet_effect_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_150_price_magnet_effect_rank_252d
    ECONOMIC RATIONALE: Attraction to nearest whole number.
    """
    base = abs(close - round(close))
    return _rank_pct(base, 252)

def ppsy_151_clustering_regime_shift_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_151_clustering_regime_shift_lvl_5d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rolling_mean(base, 5)

def ppsy_152_clustering_regime_shift_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_152_clustering_regime_shift_zscore_5d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _zscore_rolling(base, 5)

def ppsy_153_clustering_regime_shift_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_153_clustering_regime_shift_rank_5d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rank_pct(base, 5)

def ppsy_154_clustering_regime_shift_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_154_clustering_regime_shift_lvl_21d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rolling_mean(base, 21)

def ppsy_155_clustering_regime_shift_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_155_clustering_regime_shift_zscore_21d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _zscore_rolling(base, 21)

def ppsy_156_clustering_regime_shift_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_156_clustering_regime_shift_rank_21d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rank_pct(base, 21)

def ppsy_157_clustering_regime_shift_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_157_clustering_regime_shift_lvl_63d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rolling_mean(base, 63)

def ppsy_158_clustering_regime_shift_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_158_clustering_regime_shift_zscore_63d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _zscore_rolling(base, 63)

def ppsy_159_clustering_regime_shift_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_159_clustering_regime_shift_rank_63d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rank_pct(base, 63)

def ppsy_160_clustering_regime_shift_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_160_clustering_regime_shift_lvl_126d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rolling_mean(base, 126)

def ppsy_161_clustering_regime_shift_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_161_clustering_regime_shift_zscore_126d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _zscore_rolling(base, 126)

def ppsy_162_clustering_regime_shift_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_162_clustering_regime_shift_rank_126d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rank_pct(base, 126)

def ppsy_163_clustering_regime_shift_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_163_clustering_regime_shift_lvl_252d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rolling_mean(base, 252)

def ppsy_164_clustering_regime_shift_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_164_clustering_regime_shift_zscore_252d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _zscore_rolling(base, 252)

def ppsy_165_clustering_regime_shift_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_165_clustering_regime_shift_rank_252d
    ECONOMIC RATIONALE: Shift in price stability around clusters.
    """
    base = close.rolling(21).std().diff(21)
    return _rank_pct(base, 252)

def ppsy_166_psychological_breakthrough_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_166_psychological_breakthrough_lvl_5d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rolling_mean(base, 5)

def ppsy_167_psychological_breakthrough_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_167_psychological_breakthrough_zscore_5d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _zscore_rolling(base, 5)

def ppsy_168_psychological_breakthrough_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_168_psychological_breakthrough_rank_5d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rank_pct(base, 5)

def ppsy_169_psychological_breakthrough_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_169_psychological_breakthrough_lvl_21d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rolling_mean(base, 21)

def ppsy_170_psychological_breakthrough_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_170_psychological_breakthrough_zscore_21d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _zscore_rolling(base, 21)

def ppsy_171_psychological_breakthrough_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_171_psychological_breakthrough_rank_21d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rank_pct(base, 21)

def ppsy_172_psychological_breakthrough_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_172_psychological_breakthrough_lvl_63d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rolling_mean(base, 63)

def ppsy_173_psychological_breakthrough_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_173_psychological_breakthrough_zscore_63d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _zscore_rolling(base, 63)

def ppsy_174_psychological_breakthrough_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_174_psychological_breakthrough_rank_63d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rank_pct(base, 63)

def ppsy_175_psychological_breakthrough_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_175_psychological_breakthrough_lvl_126d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rolling_mean(base, 126)

def ppsy_176_psychological_breakthrough_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_176_psychological_breakthrough_zscore_126d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _zscore_rolling(base, 126)

def ppsy_177_psychological_breakthrough_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_177_psychological_breakthrough_rank_126d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rank_pct(base, 126)

def ppsy_178_psychological_breakthrough_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_178_psychological_breakthrough_lvl_252d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rolling_mean(base, 252)

def ppsy_179_psychological_breakthrough_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_179_psychological_breakthrough_zscore_252d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _zscore_rolling(base, 252)

def ppsy_180_psychological_breakthrough_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_180_psychological_breakthrough_rank_252d
    ECONOMIC RATIONALE: Crossing of psychological whole-number barriers.
    """
    base = (close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))
    return _rank_pct(base, 252)

def ppsy_181_price_stickiness_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_181_price_stickiness_lvl_5d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rolling_mean(base, 5)

def ppsy_182_price_stickiness_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_182_price_stickiness_zscore_5d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _zscore_rolling(base, 5)

def ppsy_183_price_stickiness_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_183_price_stickiness_rank_5d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rank_pct(base, 5)

def ppsy_184_price_stickiness_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_184_price_stickiness_lvl_21d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rolling_mean(base, 21)

def ppsy_185_price_stickiness_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_185_price_stickiness_zscore_21d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _zscore_rolling(base, 21)

def ppsy_186_price_stickiness_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_186_price_stickiness_rank_21d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rank_pct(base, 21)

def ppsy_187_price_stickiness_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_187_price_stickiness_lvl_63d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rolling_mean(base, 63)

def ppsy_188_price_stickiness_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_188_price_stickiness_zscore_63d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _zscore_rolling(base, 63)

def ppsy_189_price_stickiness_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_189_price_stickiness_rank_63d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rank_pct(base, 63)

def ppsy_190_price_stickiness_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_190_price_stickiness_lvl_126d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rolling_mean(base, 126)

def ppsy_191_price_stickiness_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_191_price_stickiness_zscore_126d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _zscore_rolling(base, 126)

def ppsy_192_price_stickiness_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_192_price_stickiness_rank_126d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rank_pct(base, 126)

def ppsy_193_price_stickiness_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_193_price_stickiness_lvl_252d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rolling_mean(base, 252)

def ppsy_194_price_stickiness_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_194_price_stickiness_zscore_252d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _zscore_rolling(base, 252)

def ppsy_195_price_stickiness_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_195_price_stickiness_rank_252d
    ECONOMIC RATIONALE: Frequency of minimal price movement (price stickiness).
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).sum()
    return _rank_pct(base, 252)

def ppsy_196_clustering_vol_corr_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_196_clustering_vol_corr_lvl_5d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rolling_mean(base, 5)

def ppsy_197_clustering_vol_corr_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_197_clustering_vol_corr_zscore_5d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _zscore_rolling(base, 5)

def ppsy_198_clustering_vol_corr_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_198_clustering_vol_corr_rank_5d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rank_pct(base, 5)

def ppsy_199_clustering_vol_corr_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_199_clustering_vol_corr_lvl_21d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rolling_mean(base, 21)

def ppsy_200_clustering_vol_corr_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_200_clustering_vol_corr_zscore_21d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _zscore_rolling(base, 21)

def ppsy_201_clustering_vol_corr_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_201_clustering_vol_corr_rank_21d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rank_pct(base, 21)

def ppsy_202_clustering_vol_corr_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_202_clustering_vol_corr_lvl_63d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rolling_mean(base, 63)

def ppsy_203_clustering_vol_corr_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_203_clustering_vol_corr_zscore_63d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _zscore_rolling(base, 63)

def ppsy_204_clustering_vol_corr_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_204_clustering_vol_corr_rank_63d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rank_pct(base, 63)

def ppsy_205_clustering_vol_corr_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_205_clustering_vol_corr_lvl_126d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rolling_mean(base, 126)

def ppsy_206_clustering_vol_corr_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_206_clustering_vol_corr_zscore_126d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _zscore_rolling(base, 126)

def ppsy_207_clustering_vol_corr_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_207_clustering_vol_corr_rank_126d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rank_pct(base, 126)

def ppsy_208_clustering_vol_corr_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_208_clustering_vol_corr_lvl_252d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rolling_mean(base, 252)

def ppsy_209_clustering_vol_corr_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_209_clustering_vol_corr_zscore_252d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _zscore_rolling(base, 252)

def ppsy_210_clustering_vol_corr_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_210_clustering_vol_corr_rank_252d
    ECONOMIC RATIONALE: Correlation of volume with round-number proximity.
    """
    base = volume.rolling(21).corr(close % 1.0)
    return _rank_pct(base, 252)

def ppsy_211_psych_exhaustion_proxy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_211_psych_exhaustion_proxy_lvl_5d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rolling_mean(base, 5)

def ppsy_212_psych_exhaustion_proxy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_212_psych_exhaustion_proxy_zscore_5d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _zscore_rolling(base, 5)

def ppsy_213_psych_exhaustion_proxy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_213_psych_exhaustion_proxy_rank_5d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rank_pct(base, 5)

def ppsy_214_psych_exhaustion_proxy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_214_psych_exhaustion_proxy_lvl_21d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rolling_mean(base, 21)

def ppsy_215_psych_exhaustion_proxy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_215_psych_exhaustion_proxy_zscore_21d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _zscore_rolling(base, 21)

def ppsy_216_psych_exhaustion_proxy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_216_psych_exhaustion_proxy_rank_21d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rank_pct(base, 21)

def ppsy_217_psych_exhaustion_proxy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_217_psych_exhaustion_proxy_lvl_63d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rolling_mean(base, 63)

def ppsy_218_psych_exhaustion_proxy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_218_psych_exhaustion_proxy_zscore_63d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _zscore_rolling(base, 63)

def ppsy_219_psych_exhaustion_proxy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_219_psych_exhaustion_proxy_rank_63d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rank_pct(base, 63)

def ppsy_220_psych_exhaustion_proxy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_220_psych_exhaustion_proxy_lvl_126d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rolling_mean(base, 126)

def ppsy_221_psych_exhaustion_proxy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_221_psych_exhaustion_proxy_zscore_126d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _zscore_rolling(base, 126)

def ppsy_222_psych_exhaustion_proxy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_222_psych_exhaustion_proxy_rank_126d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rank_pct(base, 126)

def ppsy_223_psych_exhaustion_proxy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_223_psych_exhaustion_proxy_lvl_252d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rolling_mean(base, 252)

def ppsy_224_psych_exhaustion_proxy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_224_psych_exhaustion_proxy_zscore_252d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _zscore_rolling(base, 252)

def ppsy_225_psych_exhaustion_proxy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_225_psych_exhaustion_proxy_rank_252d
    ECONOMIC RATIONALE: Persistent hovering near round numbers.
    """
    base = (close % 1.0 < 0.05).rolling(10).sum()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V117_REGISTRY_2 = {
    "ppsy_121_digit_bias_last_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_121_digit_bias_last_lvl_5d},
    "ppsy_122_digit_bias_last_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_122_digit_bias_last_zscore_5d},
    "ppsy_123_digit_bias_last_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_123_digit_bias_last_rank_5d},
    "ppsy_124_digit_bias_last_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_124_digit_bias_last_lvl_21d},
    "ppsy_125_digit_bias_last_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_125_digit_bias_last_zscore_21d},
    "ppsy_126_digit_bias_last_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_126_digit_bias_last_rank_21d},
    "ppsy_127_digit_bias_last_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_127_digit_bias_last_lvl_63d},
    "ppsy_128_digit_bias_last_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_128_digit_bias_last_zscore_63d},
    "ppsy_129_digit_bias_last_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_129_digit_bias_last_rank_63d},
    "ppsy_130_digit_bias_last_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_130_digit_bias_last_lvl_126d},
    "ppsy_131_digit_bias_last_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_131_digit_bias_last_zscore_126d},
    "ppsy_132_digit_bias_last_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_132_digit_bias_last_rank_126d},
    "ppsy_133_digit_bias_last_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_133_digit_bias_last_lvl_252d},
    "ppsy_134_digit_bias_last_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_134_digit_bias_last_zscore_252d},
    "ppsy_135_digit_bias_last_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_135_digit_bias_last_rank_252d},
    "ppsy_136_price_magnet_effect_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_136_price_magnet_effect_lvl_5d},
    "ppsy_137_price_magnet_effect_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_137_price_magnet_effect_zscore_5d},
    "ppsy_138_price_magnet_effect_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_138_price_magnet_effect_rank_5d},
    "ppsy_139_price_magnet_effect_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_139_price_magnet_effect_lvl_21d},
    "ppsy_140_price_magnet_effect_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_140_price_magnet_effect_zscore_21d},
    "ppsy_141_price_magnet_effect_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_141_price_magnet_effect_rank_21d},
    "ppsy_142_price_magnet_effect_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_142_price_magnet_effect_lvl_63d},
    "ppsy_143_price_magnet_effect_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_143_price_magnet_effect_zscore_63d},
    "ppsy_144_price_magnet_effect_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_144_price_magnet_effect_rank_63d},
    "ppsy_145_price_magnet_effect_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_145_price_magnet_effect_lvl_126d},
    "ppsy_146_price_magnet_effect_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_146_price_magnet_effect_zscore_126d},
    "ppsy_147_price_magnet_effect_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_147_price_magnet_effect_rank_126d},
    "ppsy_148_price_magnet_effect_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_148_price_magnet_effect_lvl_252d},
    "ppsy_149_price_magnet_effect_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_149_price_magnet_effect_zscore_252d},
    "ppsy_150_price_magnet_effect_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_150_price_magnet_effect_rank_252d},
    "ppsy_151_clustering_regime_shift_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_151_clustering_regime_shift_lvl_5d},
    "ppsy_152_clustering_regime_shift_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_152_clustering_regime_shift_zscore_5d},
    "ppsy_153_clustering_regime_shift_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_153_clustering_regime_shift_rank_5d},
    "ppsy_154_clustering_regime_shift_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_154_clustering_regime_shift_lvl_21d},
    "ppsy_155_clustering_regime_shift_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_155_clustering_regime_shift_zscore_21d},
    "ppsy_156_clustering_regime_shift_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_156_clustering_regime_shift_rank_21d},
    "ppsy_157_clustering_regime_shift_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_157_clustering_regime_shift_lvl_63d},
    "ppsy_158_clustering_regime_shift_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_158_clustering_regime_shift_zscore_63d},
    "ppsy_159_clustering_regime_shift_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_159_clustering_regime_shift_rank_63d},
    "ppsy_160_clustering_regime_shift_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_160_clustering_regime_shift_lvl_126d},
    "ppsy_161_clustering_regime_shift_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_161_clustering_regime_shift_zscore_126d},
    "ppsy_162_clustering_regime_shift_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_162_clustering_regime_shift_rank_126d},
    "ppsy_163_clustering_regime_shift_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_163_clustering_regime_shift_lvl_252d},
    "ppsy_164_clustering_regime_shift_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_164_clustering_regime_shift_zscore_252d},
    "ppsy_165_clustering_regime_shift_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_165_clustering_regime_shift_rank_252d},
    "ppsy_166_psychological_breakthrough_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_166_psychological_breakthrough_lvl_5d},
    "ppsy_167_psychological_breakthrough_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_167_psychological_breakthrough_zscore_5d},
    "ppsy_168_psychological_breakthrough_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_168_psychological_breakthrough_rank_5d},
    "ppsy_169_psychological_breakthrough_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_169_psychological_breakthrough_lvl_21d},
    "ppsy_170_psychological_breakthrough_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_170_psychological_breakthrough_zscore_21d},
    "ppsy_171_psychological_breakthrough_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_171_psychological_breakthrough_rank_21d},
    "ppsy_172_psychological_breakthrough_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_172_psychological_breakthrough_lvl_63d},
    "ppsy_173_psychological_breakthrough_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_173_psychological_breakthrough_zscore_63d},
    "ppsy_174_psychological_breakthrough_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_174_psychological_breakthrough_rank_63d},
    "ppsy_175_psychological_breakthrough_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_175_psychological_breakthrough_lvl_126d},
    "ppsy_176_psychological_breakthrough_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_176_psychological_breakthrough_zscore_126d},
    "ppsy_177_psychological_breakthrough_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_177_psychological_breakthrough_rank_126d},
    "ppsy_178_psychological_breakthrough_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_178_psychological_breakthrough_lvl_252d},
    "ppsy_179_psychological_breakthrough_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_179_psychological_breakthrough_zscore_252d},
    "ppsy_180_psychological_breakthrough_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_180_psychological_breakthrough_rank_252d},
    "ppsy_181_price_stickiness_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_181_price_stickiness_lvl_5d},
    "ppsy_182_price_stickiness_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_182_price_stickiness_zscore_5d},
    "ppsy_183_price_stickiness_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_183_price_stickiness_rank_5d},
    "ppsy_184_price_stickiness_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_184_price_stickiness_lvl_21d},
    "ppsy_185_price_stickiness_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_185_price_stickiness_zscore_21d},
    "ppsy_186_price_stickiness_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_186_price_stickiness_rank_21d},
    "ppsy_187_price_stickiness_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_187_price_stickiness_lvl_63d},
    "ppsy_188_price_stickiness_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_188_price_stickiness_zscore_63d},
    "ppsy_189_price_stickiness_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_189_price_stickiness_rank_63d},
    "ppsy_190_price_stickiness_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_190_price_stickiness_lvl_126d},
    "ppsy_191_price_stickiness_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_191_price_stickiness_zscore_126d},
    "ppsy_192_price_stickiness_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_192_price_stickiness_rank_126d},
    "ppsy_193_price_stickiness_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_193_price_stickiness_lvl_252d},
    "ppsy_194_price_stickiness_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_194_price_stickiness_zscore_252d},
    "ppsy_195_price_stickiness_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_195_price_stickiness_rank_252d},
    "ppsy_196_clustering_vol_corr_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_196_clustering_vol_corr_lvl_5d},
    "ppsy_197_clustering_vol_corr_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_197_clustering_vol_corr_zscore_5d},
    "ppsy_198_clustering_vol_corr_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_198_clustering_vol_corr_rank_5d},
    "ppsy_199_clustering_vol_corr_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_199_clustering_vol_corr_lvl_21d},
    "ppsy_200_clustering_vol_corr_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_200_clustering_vol_corr_zscore_21d},
    "ppsy_201_clustering_vol_corr_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_201_clustering_vol_corr_rank_21d},
    "ppsy_202_clustering_vol_corr_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_202_clustering_vol_corr_lvl_63d},
    "ppsy_203_clustering_vol_corr_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_203_clustering_vol_corr_zscore_63d},
    "ppsy_204_clustering_vol_corr_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_204_clustering_vol_corr_rank_63d},
    "ppsy_205_clustering_vol_corr_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_205_clustering_vol_corr_lvl_126d},
    "ppsy_206_clustering_vol_corr_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_206_clustering_vol_corr_zscore_126d},
    "ppsy_207_clustering_vol_corr_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_207_clustering_vol_corr_rank_126d},
    "ppsy_208_clustering_vol_corr_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_208_clustering_vol_corr_lvl_252d},
    "ppsy_209_clustering_vol_corr_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_209_clustering_vol_corr_zscore_252d},
    "ppsy_210_clustering_vol_corr_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_210_clustering_vol_corr_rank_252d},
    "ppsy_211_psych_exhaustion_proxy_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_211_psych_exhaustion_proxy_lvl_5d},
    "ppsy_212_psych_exhaustion_proxy_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_212_psych_exhaustion_proxy_zscore_5d},
    "ppsy_213_psych_exhaustion_proxy_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_213_psych_exhaustion_proxy_rank_5d},
    "ppsy_214_psych_exhaustion_proxy_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_214_psych_exhaustion_proxy_lvl_21d},
    "ppsy_215_psych_exhaustion_proxy_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_215_psych_exhaustion_proxy_zscore_21d},
    "ppsy_216_psych_exhaustion_proxy_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_216_psych_exhaustion_proxy_rank_21d},
    "ppsy_217_psych_exhaustion_proxy_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_217_psych_exhaustion_proxy_lvl_63d},
    "ppsy_218_psych_exhaustion_proxy_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_218_psych_exhaustion_proxy_zscore_63d},
    "ppsy_219_psych_exhaustion_proxy_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_219_psych_exhaustion_proxy_rank_63d},
    "ppsy_220_psych_exhaustion_proxy_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_220_psych_exhaustion_proxy_lvl_126d},
    "ppsy_221_psych_exhaustion_proxy_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_221_psych_exhaustion_proxy_zscore_126d},
    "ppsy_222_psych_exhaustion_proxy_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_222_psych_exhaustion_proxy_rank_126d},
    "ppsy_223_psych_exhaustion_proxy_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_223_psych_exhaustion_proxy_lvl_252d},
    "ppsy_224_psych_exhaustion_proxy_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_224_psych_exhaustion_proxy_zscore_252d},
    "ppsy_225_psych_exhaustion_proxy_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_225_psych_exhaustion_proxy_rank_252d},
}
