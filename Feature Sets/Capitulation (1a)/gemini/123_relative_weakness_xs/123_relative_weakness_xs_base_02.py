"""
123_relative_weakness_xs — Base Features Part 2
Domain: relative_weakness_xs
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

def rwxs_121_relative_strength_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_121_relative_strength_rank_lvl_5d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rolling_mean(base, 5)

def rwxs_122_relative_strength_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_122_relative_strength_rank_zscore_5d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _zscore_rolling(base, 5)

def rwxs_123_relative_strength_rank_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_123_relative_strength_rank_rank_5d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rank_pct(base, 5)

def rwxs_124_relative_strength_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_124_relative_strength_rank_lvl_21d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rolling_mean(base, 21)

def rwxs_125_relative_strength_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_125_relative_strength_rank_zscore_21d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _zscore_rolling(base, 21)

def rwxs_126_relative_strength_rank_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_126_relative_strength_rank_rank_21d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rank_pct(base, 21)

def rwxs_127_relative_strength_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_127_relative_strength_rank_lvl_63d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rolling_mean(base, 63)

def rwxs_128_relative_strength_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_128_relative_strength_rank_zscore_63d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _zscore_rolling(base, 63)

def rwxs_129_relative_strength_rank_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_129_relative_strength_rank_rank_63d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rank_pct(base, 63)

def rwxs_130_relative_strength_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_130_relative_strength_rank_lvl_126d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rolling_mean(base, 126)

def rwxs_131_relative_strength_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_131_relative_strength_rank_zscore_126d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _zscore_rolling(base, 126)

def rwxs_132_relative_strength_rank_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_132_relative_strength_rank_rank_126d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rank_pct(base, 126)

def rwxs_133_relative_strength_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_133_relative_strength_rank_lvl_252d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rolling_mean(base, 252)

def rwxs_134_relative_strength_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_134_relative_strength_rank_zscore_252d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _zscore_rolling(base, 252)

def rwxs_135_relative_strength_rank_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_135_relative_strength_rank_rank_252d
    ECONOMIC RATIONALE: Historical rank of relative price level.
    """
    base = _rank_pct(close/mkt_close, 252)
    return _rank_pct(base, 252)

def rwxs_136_market_decoupling_flag_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_136_market_decoupling_flag_lvl_5d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rolling_mean(base, 5)

def rwxs_137_market_decoupling_flag_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_137_market_decoupling_flag_zscore_5d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _zscore_rolling(base, 5)

def rwxs_138_market_decoupling_flag_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_138_market_decoupling_flag_rank_5d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rank_pct(base, 5)

def rwxs_139_market_decoupling_flag_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_139_market_decoupling_flag_lvl_21d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rolling_mean(base, 21)

def rwxs_140_market_decoupling_flag_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_140_market_decoupling_flag_zscore_21d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _zscore_rolling(base, 21)

def rwxs_141_market_decoupling_flag_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_141_market_decoupling_flag_rank_21d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rank_pct(base, 21)

def rwxs_142_market_decoupling_flag_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_142_market_decoupling_flag_lvl_63d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rolling_mean(base, 63)

def rwxs_143_market_decoupling_flag_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_143_market_decoupling_flag_zscore_63d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _zscore_rolling(base, 63)

def rwxs_144_market_decoupling_flag_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_144_market_decoupling_flag_rank_63d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rank_pct(base, 63)

def rwxs_145_market_decoupling_flag_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_145_market_decoupling_flag_lvl_126d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rolling_mean(base, 126)

def rwxs_146_market_decoupling_flag_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_146_market_decoupling_flag_zscore_126d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _zscore_rolling(base, 126)

def rwxs_147_market_decoupling_flag_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_147_market_decoupling_flag_rank_126d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rank_pct(base, 126)

def rwxs_148_market_decoupling_flag_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_148_market_decoupling_flag_lvl_252d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rolling_mean(base, 252)

def rwxs_149_market_decoupling_flag_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_149_market_decoupling_flag_zscore_252d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _zscore_rolling(base, 252)

def rwxs_150_market_decoupling_flag_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_150_market_decoupling_flag_rank_252d
    ECONOMIC RATIONALE: Loss of correlation with market indices during distress.
    """
    base = (close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)
    return _rank_pct(base, 252)

def rwxs_151_relative_low_test_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_151_relative_low_test_lvl_5d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def rwxs_152_relative_low_test_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_152_relative_low_test_zscore_5d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def rwxs_153_relative_low_test_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_153_relative_low_test_rank_5d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def rwxs_154_relative_low_test_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_154_relative_low_test_lvl_21d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def rwxs_155_relative_low_test_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_155_relative_low_test_zscore_21d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def rwxs_156_relative_low_test_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_156_relative_low_test_rank_21d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def rwxs_157_relative_low_test_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_157_relative_low_test_lvl_63d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def rwxs_158_relative_low_test_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_158_relative_low_test_zscore_63d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def rwxs_159_relative_low_test_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_159_relative_low_test_rank_63d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def rwxs_160_relative_low_test_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_160_relative_low_test_lvl_126d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def rwxs_161_relative_low_test_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_161_relative_low_test_zscore_126d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def rwxs_162_relative_low_test_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_162_relative_low_test_rank_126d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def rwxs_163_relative_low_test_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_163_relative_low_test_lvl_252d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def rwxs_164_relative_low_test_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_164_relative_low_test_zscore_252d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def rwxs_165_relative_low_test_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_165_relative_low_test_rank_252d
    ECONOMIC RATIONALE: Proximity to lows relative to the market.
    """
    base = (close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def rwxs_166_relative_weakness_score_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_166_relative_weakness_score_lvl_5d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rolling_mean(base, 5)

def rwxs_167_relative_weakness_score_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_167_relative_weakness_score_zscore_5d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _zscore_rolling(base, 5)

def rwxs_168_relative_weakness_score_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_168_relative_weakness_score_rank_5d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rank_pct(base, 5)

def rwxs_169_relative_weakness_score_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_169_relative_weakness_score_lvl_21d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rolling_mean(base, 21)

def rwxs_170_relative_weakness_score_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_170_relative_weakness_score_zscore_21d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _zscore_rolling(base, 21)

def rwxs_171_relative_weakness_score_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_171_relative_weakness_score_rank_21d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rank_pct(base, 21)

def rwxs_172_relative_weakness_score_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_172_relative_weakness_score_lvl_63d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rolling_mean(base, 63)

def rwxs_173_relative_weakness_score_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_173_relative_weakness_score_zscore_63d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _zscore_rolling(base, 63)

def rwxs_174_relative_weakness_score_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_174_relative_weakness_score_rank_63d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rank_pct(base, 63)

def rwxs_175_relative_weakness_score_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_175_relative_weakness_score_lvl_126d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rolling_mean(base, 126)

def rwxs_176_relative_weakness_score_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_176_relative_weakness_score_zscore_126d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _zscore_rolling(base, 126)

def rwxs_177_relative_weakness_score_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_177_relative_weakness_score_rank_126d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rank_pct(base, 126)

def rwxs_178_relative_weakness_score_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_178_relative_weakness_score_lvl_252d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rolling_mean(base, 252)

def rwxs_179_relative_weakness_score_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_179_relative_weakness_score_zscore_252d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _zscore_rolling(base, 252)

def rwxs_180_relative_weakness_score_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_180_relative_weakness_score_rank_252d
    ECONOMIC RATIONALE: Binary flag for absolute and relative weakness.
    """
    base = ((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)
    return _rank_pct(base, 252)

def rwxs_181_excess_volatility_z_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_181_excess_volatility_z_lvl_5d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rolling_mean(base, 5)

def rwxs_182_excess_volatility_z_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_182_excess_volatility_z_zscore_5d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _zscore_rolling(base, 5)

def rwxs_183_excess_volatility_z_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_183_excess_volatility_z_rank_5d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rank_pct(base, 5)

def rwxs_184_excess_volatility_z_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_184_excess_volatility_z_lvl_21d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rolling_mean(base, 21)

def rwxs_185_excess_volatility_z_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_185_excess_volatility_z_zscore_21d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _zscore_rolling(base, 21)

def rwxs_186_excess_volatility_z_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_186_excess_volatility_z_rank_21d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rank_pct(base, 21)

def rwxs_187_excess_volatility_z_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_187_excess_volatility_z_lvl_63d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rolling_mean(base, 63)

def rwxs_188_excess_volatility_z_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_188_excess_volatility_z_zscore_63d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _zscore_rolling(base, 63)

def rwxs_189_excess_volatility_z_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_189_excess_volatility_z_rank_63d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rank_pct(base, 63)

def rwxs_190_excess_volatility_z_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_190_excess_volatility_z_lvl_126d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rolling_mean(base, 126)

def rwxs_191_excess_volatility_z_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_191_excess_volatility_z_zscore_126d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _zscore_rolling(base, 126)

def rwxs_192_excess_volatility_z_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_192_excess_volatility_z_rank_126d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rank_pct(base, 126)

def rwxs_193_excess_volatility_z_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_193_excess_volatility_z_lvl_252d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rolling_mean(base, 252)

def rwxs_194_excess_volatility_z_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_194_excess_volatility_z_zscore_252d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _zscore_rolling(base, 252)

def rwxs_195_excess_volatility_z_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_195_excess_volatility_z_rank_252d
    ECONOMIC RATIONALE: Abnormal excess volatility over the market.
    """
    base = _zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)
    return _rank_pct(base, 252)

def rwxs_196_relative_strength_roc_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_196_relative_strength_roc_lvl_5d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rolling_mean(base, 5)

def rwxs_197_relative_strength_roc_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_197_relative_strength_roc_zscore_5d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _zscore_rolling(base, 5)

def rwxs_198_relative_strength_roc_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_198_relative_strength_roc_rank_5d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rank_pct(base, 5)

def rwxs_199_relative_strength_roc_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_199_relative_strength_roc_lvl_21d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rolling_mean(base, 21)

def rwxs_200_relative_strength_roc_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_200_relative_strength_roc_zscore_21d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _zscore_rolling(base, 21)

def rwxs_201_relative_strength_roc_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_201_relative_strength_roc_rank_21d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rank_pct(base, 21)

def rwxs_202_relative_strength_roc_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_202_relative_strength_roc_lvl_63d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rolling_mean(base, 63)

def rwxs_203_relative_strength_roc_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_203_relative_strength_roc_zscore_63d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _zscore_rolling(base, 63)

def rwxs_204_relative_strength_roc_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_204_relative_strength_roc_rank_63d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rank_pct(base, 63)

def rwxs_205_relative_strength_roc_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_205_relative_strength_roc_lvl_126d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rolling_mean(base, 126)

def rwxs_206_relative_strength_roc_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_206_relative_strength_roc_zscore_126d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _zscore_rolling(base, 126)

def rwxs_207_relative_strength_roc_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_207_relative_strength_roc_rank_126d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rank_pct(base, 126)

def rwxs_208_relative_strength_roc_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_208_relative_strength_roc_lvl_252d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rolling_mean(base, 252)

def rwxs_209_relative_strength_roc_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_209_relative_strength_roc_zscore_252d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _zscore_rolling(base, 252)

def rwxs_210_relative_strength_roc_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_210_relative_strength_roc_rank_252d
    ECONOMIC RATIONALE: Rate of change in the relative strength line.
    """
    base = (close/mkt_close).pct_change(21)
    return _rank_pct(base, 252)

def rwxs_211_market_beta_zscore_lvl_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_211_market_beta_zscore_lvl_5d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rolling_mean(base, 5)

def rwxs_212_market_beta_zscore_zscore_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_212_market_beta_zscore_zscore_5d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _zscore_rolling(base, 5)

def rwxs_213_market_beta_zscore_rank_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_213_market_beta_zscore_rank_5d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rank_pct(base, 5)

def rwxs_214_market_beta_zscore_lvl_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_214_market_beta_zscore_lvl_21d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rolling_mean(base, 21)

def rwxs_215_market_beta_zscore_zscore_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_215_market_beta_zscore_zscore_21d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _zscore_rolling(base, 21)

def rwxs_216_market_beta_zscore_rank_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_216_market_beta_zscore_rank_21d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rank_pct(base, 21)

def rwxs_217_market_beta_zscore_lvl_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_217_market_beta_zscore_lvl_63d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rolling_mean(base, 63)

def rwxs_218_market_beta_zscore_zscore_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_218_market_beta_zscore_zscore_63d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _zscore_rolling(base, 63)

def rwxs_219_market_beta_zscore_rank_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_219_market_beta_zscore_rank_63d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rank_pct(base, 63)

def rwxs_220_market_beta_zscore_lvl_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_220_market_beta_zscore_lvl_126d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rolling_mean(base, 126)

def rwxs_221_market_beta_zscore_zscore_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_221_market_beta_zscore_zscore_126d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _zscore_rolling(base, 126)

def rwxs_222_market_beta_zscore_rank_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_222_market_beta_zscore_rank_126d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rank_pct(base, 126)

def rwxs_223_market_beta_zscore_lvl_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_223_market_beta_zscore_lvl_252d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rolling_mean(base, 252)

def rwxs_224_market_beta_zscore_zscore_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_224_market_beta_zscore_zscore_252d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _zscore_rolling(base, 252)

def rwxs_225_market_beta_zscore_rank_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_225_market_beta_zscore_rank_252d
    ECONOMIC RATIONALE: Anomaly in market sensitivity.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V123_REGISTRY_2 = {
    "rwxs_121_relative_strength_rank_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_121_relative_strength_rank_lvl_5d},
    "rwxs_122_relative_strength_rank_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_122_relative_strength_rank_zscore_5d},
    "rwxs_123_relative_strength_rank_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_123_relative_strength_rank_rank_5d},
    "rwxs_124_relative_strength_rank_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_124_relative_strength_rank_lvl_21d},
    "rwxs_125_relative_strength_rank_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_125_relative_strength_rank_zscore_21d},
    "rwxs_126_relative_strength_rank_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_126_relative_strength_rank_rank_21d},
    "rwxs_127_relative_strength_rank_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_127_relative_strength_rank_lvl_63d},
    "rwxs_128_relative_strength_rank_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_128_relative_strength_rank_zscore_63d},
    "rwxs_129_relative_strength_rank_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_129_relative_strength_rank_rank_63d},
    "rwxs_130_relative_strength_rank_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_130_relative_strength_rank_lvl_126d},
    "rwxs_131_relative_strength_rank_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_131_relative_strength_rank_zscore_126d},
    "rwxs_132_relative_strength_rank_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_132_relative_strength_rank_rank_126d},
    "rwxs_133_relative_strength_rank_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_133_relative_strength_rank_lvl_252d},
    "rwxs_134_relative_strength_rank_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_134_relative_strength_rank_zscore_252d},
    "rwxs_135_relative_strength_rank_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_135_relative_strength_rank_rank_252d},
    "rwxs_136_market_decoupling_flag_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_136_market_decoupling_flag_lvl_5d},
    "rwxs_137_market_decoupling_flag_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_137_market_decoupling_flag_zscore_5d},
    "rwxs_138_market_decoupling_flag_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_138_market_decoupling_flag_rank_5d},
    "rwxs_139_market_decoupling_flag_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_139_market_decoupling_flag_lvl_21d},
    "rwxs_140_market_decoupling_flag_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_140_market_decoupling_flag_zscore_21d},
    "rwxs_141_market_decoupling_flag_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_141_market_decoupling_flag_rank_21d},
    "rwxs_142_market_decoupling_flag_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_142_market_decoupling_flag_lvl_63d},
    "rwxs_143_market_decoupling_flag_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_143_market_decoupling_flag_zscore_63d},
    "rwxs_144_market_decoupling_flag_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_144_market_decoupling_flag_rank_63d},
    "rwxs_145_market_decoupling_flag_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_145_market_decoupling_flag_lvl_126d},
    "rwxs_146_market_decoupling_flag_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_146_market_decoupling_flag_zscore_126d},
    "rwxs_147_market_decoupling_flag_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_147_market_decoupling_flag_rank_126d},
    "rwxs_148_market_decoupling_flag_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_148_market_decoupling_flag_lvl_252d},
    "rwxs_149_market_decoupling_flag_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_149_market_decoupling_flag_zscore_252d},
    "rwxs_150_market_decoupling_flag_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_150_market_decoupling_flag_rank_252d},
    "rwxs_151_relative_low_test_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_151_relative_low_test_lvl_5d},
    "rwxs_152_relative_low_test_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_152_relative_low_test_zscore_5d},
    "rwxs_153_relative_low_test_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_153_relative_low_test_rank_5d},
    "rwxs_154_relative_low_test_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_154_relative_low_test_lvl_21d},
    "rwxs_155_relative_low_test_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_155_relative_low_test_zscore_21d},
    "rwxs_156_relative_low_test_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_156_relative_low_test_rank_21d},
    "rwxs_157_relative_low_test_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_157_relative_low_test_lvl_63d},
    "rwxs_158_relative_low_test_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_158_relative_low_test_zscore_63d},
    "rwxs_159_relative_low_test_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_159_relative_low_test_rank_63d},
    "rwxs_160_relative_low_test_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_160_relative_low_test_lvl_126d},
    "rwxs_161_relative_low_test_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_161_relative_low_test_zscore_126d},
    "rwxs_162_relative_low_test_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_162_relative_low_test_rank_126d},
    "rwxs_163_relative_low_test_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_163_relative_low_test_lvl_252d},
    "rwxs_164_relative_low_test_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_164_relative_low_test_zscore_252d},
    "rwxs_165_relative_low_test_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_165_relative_low_test_rank_252d},
    "rwxs_166_relative_weakness_score_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_166_relative_weakness_score_lvl_5d},
    "rwxs_167_relative_weakness_score_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_167_relative_weakness_score_zscore_5d},
    "rwxs_168_relative_weakness_score_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_168_relative_weakness_score_rank_5d},
    "rwxs_169_relative_weakness_score_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_169_relative_weakness_score_lvl_21d},
    "rwxs_170_relative_weakness_score_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_170_relative_weakness_score_zscore_21d},
    "rwxs_171_relative_weakness_score_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_171_relative_weakness_score_rank_21d},
    "rwxs_172_relative_weakness_score_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_172_relative_weakness_score_lvl_63d},
    "rwxs_173_relative_weakness_score_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_173_relative_weakness_score_zscore_63d},
    "rwxs_174_relative_weakness_score_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_174_relative_weakness_score_rank_63d},
    "rwxs_175_relative_weakness_score_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_175_relative_weakness_score_lvl_126d},
    "rwxs_176_relative_weakness_score_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_176_relative_weakness_score_zscore_126d},
    "rwxs_177_relative_weakness_score_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_177_relative_weakness_score_rank_126d},
    "rwxs_178_relative_weakness_score_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_178_relative_weakness_score_lvl_252d},
    "rwxs_179_relative_weakness_score_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_179_relative_weakness_score_zscore_252d},
    "rwxs_180_relative_weakness_score_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_180_relative_weakness_score_rank_252d},
    "rwxs_181_excess_volatility_z_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_181_excess_volatility_z_lvl_5d},
    "rwxs_182_excess_volatility_z_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_182_excess_volatility_z_zscore_5d},
    "rwxs_183_excess_volatility_z_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_183_excess_volatility_z_rank_5d},
    "rwxs_184_excess_volatility_z_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_184_excess_volatility_z_lvl_21d},
    "rwxs_185_excess_volatility_z_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_185_excess_volatility_z_zscore_21d},
    "rwxs_186_excess_volatility_z_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_186_excess_volatility_z_rank_21d},
    "rwxs_187_excess_volatility_z_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_187_excess_volatility_z_lvl_63d},
    "rwxs_188_excess_volatility_z_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_188_excess_volatility_z_zscore_63d},
    "rwxs_189_excess_volatility_z_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_189_excess_volatility_z_rank_63d},
    "rwxs_190_excess_volatility_z_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_190_excess_volatility_z_lvl_126d},
    "rwxs_191_excess_volatility_z_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_191_excess_volatility_z_zscore_126d},
    "rwxs_192_excess_volatility_z_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_192_excess_volatility_z_rank_126d},
    "rwxs_193_excess_volatility_z_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_193_excess_volatility_z_lvl_252d},
    "rwxs_194_excess_volatility_z_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_194_excess_volatility_z_zscore_252d},
    "rwxs_195_excess_volatility_z_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_195_excess_volatility_z_rank_252d},
    "rwxs_196_relative_strength_roc_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_196_relative_strength_roc_lvl_5d},
    "rwxs_197_relative_strength_roc_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_197_relative_strength_roc_zscore_5d},
    "rwxs_198_relative_strength_roc_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_198_relative_strength_roc_rank_5d},
    "rwxs_199_relative_strength_roc_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_199_relative_strength_roc_lvl_21d},
    "rwxs_200_relative_strength_roc_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_200_relative_strength_roc_zscore_21d},
    "rwxs_201_relative_strength_roc_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_201_relative_strength_roc_rank_21d},
    "rwxs_202_relative_strength_roc_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_202_relative_strength_roc_lvl_63d},
    "rwxs_203_relative_strength_roc_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_203_relative_strength_roc_zscore_63d},
    "rwxs_204_relative_strength_roc_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_204_relative_strength_roc_rank_63d},
    "rwxs_205_relative_strength_roc_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_205_relative_strength_roc_lvl_126d},
    "rwxs_206_relative_strength_roc_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_206_relative_strength_roc_zscore_126d},
    "rwxs_207_relative_strength_roc_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_207_relative_strength_roc_rank_126d},
    "rwxs_208_relative_strength_roc_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_208_relative_strength_roc_lvl_252d},
    "rwxs_209_relative_strength_roc_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_209_relative_strength_roc_zscore_252d},
    "rwxs_210_relative_strength_roc_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_210_relative_strength_roc_rank_252d},
    "rwxs_211_market_beta_zscore_lvl_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_211_market_beta_zscore_lvl_5d},
    "rwxs_212_market_beta_zscore_zscore_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_212_market_beta_zscore_zscore_5d},
    "rwxs_213_market_beta_zscore_rank_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_213_market_beta_zscore_rank_5d},
    "rwxs_214_market_beta_zscore_lvl_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_214_market_beta_zscore_lvl_21d},
    "rwxs_215_market_beta_zscore_zscore_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_215_market_beta_zscore_zscore_21d},
    "rwxs_216_market_beta_zscore_rank_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_216_market_beta_zscore_rank_21d},
    "rwxs_217_market_beta_zscore_lvl_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_217_market_beta_zscore_lvl_63d},
    "rwxs_218_market_beta_zscore_zscore_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_218_market_beta_zscore_zscore_63d},
    "rwxs_219_market_beta_zscore_rank_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_219_market_beta_zscore_rank_63d},
    "rwxs_220_market_beta_zscore_lvl_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_220_market_beta_zscore_lvl_126d},
    "rwxs_221_market_beta_zscore_zscore_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_221_market_beta_zscore_zscore_126d},
    "rwxs_222_market_beta_zscore_rank_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_222_market_beta_zscore_rank_126d},
    "rwxs_223_market_beta_zscore_lvl_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_223_market_beta_zscore_lvl_252d},
    "rwxs_224_market_beta_zscore_zscore_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_224_market_beta_zscore_zscore_252d},
    "rwxs_225_market_beta_zscore_rank_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_225_market_beta_zscore_rank_252d},
}
