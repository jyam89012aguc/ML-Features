"""
104_mean_reversion_potential — Base Features Part 2
Domain: mean_reversion_potential
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

def mrpt_121_mean_reversion_rank_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_121_mean_reversion_rank_lvl_5d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rolling_mean(base, 5)

def mrpt_122_mean_reversion_rank_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_122_mean_reversion_rank_zscore_5d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _zscore_rolling(base, 5)

def mrpt_123_mean_reversion_rank_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_123_mean_reversion_rank_rank_5d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rank_pct(base, 5)

def mrpt_124_mean_reversion_rank_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_124_mean_reversion_rank_lvl_21d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rolling_mean(base, 21)

def mrpt_125_mean_reversion_rank_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_125_mean_reversion_rank_zscore_21d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _zscore_rolling(base, 21)

def mrpt_126_mean_reversion_rank_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_126_mean_reversion_rank_rank_21d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rank_pct(base, 21)

def mrpt_127_mean_reversion_rank_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_127_mean_reversion_rank_lvl_63d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rolling_mean(base, 63)

def mrpt_128_mean_reversion_rank_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_128_mean_reversion_rank_zscore_63d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _zscore_rolling(base, 63)

def mrpt_129_mean_reversion_rank_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_129_mean_reversion_rank_rank_63d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rank_pct(base, 63)

def mrpt_130_mean_reversion_rank_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_130_mean_reversion_rank_lvl_126d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rolling_mean(base, 126)

def mrpt_131_mean_reversion_rank_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_131_mean_reversion_rank_zscore_126d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _zscore_rolling(base, 126)

def mrpt_132_mean_reversion_rank_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_132_mean_reversion_rank_rank_126d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rank_pct(base, 126)

def mrpt_133_mean_reversion_rank_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_133_mean_reversion_rank_lvl_252d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rolling_mean(base, 252)

def mrpt_134_mean_reversion_rank_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_134_mean_reversion_rank_zscore_252d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _zscore_rolling(base, 252)

def mrpt_135_mean_reversion_rank_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_135_mean_reversion_rank_rank_252d
    ECONOMIC RATIONALE: Historical rank of current mean deviation.
    """
    base = _rank_pct(close / close.rolling(63).mean(), 252)
    return _rank_pct(base, 252)

def mrpt_136_volatility_adjusted_stretch_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_136_volatility_adjusted_stretch_lvl_5d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rolling_mean(base, 5)

def mrpt_137_volatility_adjusted_stretch_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_137_volatility_adjusted_stretch_zscore_5d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _zscore_rolling(base, 5)

def mrpt_138_volatility_adjusted_stretch_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_138_volatility_adjusted_stretch_rank_5d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rank_pct(base, 5)

def mrpt_139_volatility_adjusted_stretch_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_139_volatility_adjusted_stretch_lvl_21d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rolling_mean(base, 21)

def mrpt_140_volatility_adjusted_stretch_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_140_volatility_adjusted_stretch_zscore_21d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _zscore_rolling(base, 21)

def mrpt_141_volatility_adjusted_stretch_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_141_volatility_adjusted_stretch_rank_21d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rank_pct(base, 21)

def mrpt_142_volatility_adjusted_stretch_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_142_volatility_adjusted_stretch_lvl_63d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rolling_mean(base, 63)

def mrpt_143_volatility_adjusted_stretch_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_143_volatility_adjusted_stretch_zscore_63d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _zscore_rolling(base, 63)

def mrpt_144_volatility_adjusted_stretch_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_144_volatility_adjusted_stretch_rank_63d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rank_pct(base, 63)

def mrpt_145_volatility_adjusted_stretch_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_145_volatility_adjusted_stretch_lvl_126d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rolling_mean(base, 126)

def mrpt_146_volatility_adjusted_stretch_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_146_volatility_adjusted_stretch_zscore_126d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _zscore_rolling(base, 126)

def mrpt_147_volatility_adjusted_stretch_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_147_volatility_adjusted_stretch_rank_126d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rank_pct(base, 126)

def mrpt_148_volatility_adjusted_stretch_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_148_volatility_adjusted_stretch_lvl_252d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rolling_mean(base, 252)

def mrpt_149_volatility_adjusted_stretch_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_149_volatility_adjusted_stretch_zscore_252d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _zscore_rolling(base, 252)

def mrpt_150_volatility_adjusted_stretch_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_150_volatility_adjusted_stretch_rank_252d
    ECONOMIC RATIONALE: Price stretch adjusted for historical volatility.
    """
    base = (close - close.rolling(63).mean()) / close.rolling(63).std()
    return _rank_pct(base, 252)

def mrpt_151_mean_reversion_score_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_151_mean_reversion_score_lvl_5d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rolling_mean(base, 5)

def mrpt_152_mean_reversion_score_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_152_mean_reversion_score_zscore_5d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _zscore_rolling(base, 5)

def mrpt_153_mean_reversion_score_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_153_mean_reversion_score_rank_5d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rank_pct(base, 5)

def mrpt_154_mean_reversion_score_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_154_mean_reversion_score_lvl_21d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rolling_mean(base, 21)

def mrpt_155_mean_reversion_score_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_155_mean_reversion_score_zscore_21d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _zscore_rolling(base, 21)

def mrpt_156_mean_reversion_score_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_156_mean_reversion_score_rank_21d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rank_pct(base, 21)

def mrpt_157_mean_reversion_score_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_157_mean_reversion_score_lvl_63d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rolling_mean(base, 63)

def mrpt_158_mean_reversion_score_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_158_mean_reversion_score_zscore_63d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _zscore_rolling(base, 63)

def mrpt_159_mean_reversion_score_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_159_mean_reversion_score_rank_63d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rank_pct(base, 63)

def mrpt_160_mean_reversion_score_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_160_mean_reversion_score_lvl_126d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rolling_mean(base, 126)

def mrpt_161_mean_reversion_score_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_161_mean_reversion_score_zscore_126d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _zscore_rolling(base, 126)

def mrpt_162_mean_reversion_score_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_162_mean_reversion_score_rank_126d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rank_pct(base, 126)

def mrpt_163_mean_reversion_score_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_163_mean_reversion_score_lvl_252d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rolling_mean(base, 252)

def mrpt_164_mean_reversion_score_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_164_mean_reversion_score_zscore_252d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _zscore_rolling(base, 252)

def mrpt_165_mean_reversion_score_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_165_mean_reversion_score_rank_252d
    ECONOMIC RATIONALE: Binary signal for extreme mean reversion setups.
    """
    base = ((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)
    return _rank_pct(base, 252)

def mrpt_166_price_to_median_ratio_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_166_price_to_median_ratio_lvl_5d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rolling_mean(base, 5)

def mrpt_167_price_to_median_ratio_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_167_price_to_median_ratio_zscore_5d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _zscore_rolling(base, 5)

def mrpt_168_price_to_median_ratio_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_168_price_to_median_ratio_rank_5d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rank_pct(base, 5)

def mrpt_169_price_to_median_ratio_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_169_price_to_median_ratio_lvl_21d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rolling_mean(base, 21)

def mrpt_170_price_to_median_ratio_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_170_price_to_median_ratio_zscore_21d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _zscore_rolling(base, 21)

def mrpt_171_price_to_median_ratio_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_171_price_to_median_ratio_rank_21d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rank_pct(base, 21)

def mrpt_172_price_to_median_ratio_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_172_price_to_median_ratio_lvl_63d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rolling_mean(base, 63)

def mrpt_173_price_to_median_ratio_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_173_price_to_median_ratio_zscore_63d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _zscore_rolling(base, 63)

def mrpt_174_price_to_median_ratio_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_174_price_to_median_ratio_rank_63d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rank_pct(base, 63)

def mrpt_175_price_to_median_ratio_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_175_price_to_median_ratio_lvl_126d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rolling_mean(base, 126)

def mrpt_176_price_to_median_ratio_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_176_price_to_median_ratio_zscore_126d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _zscore_rolling(base, 126)

def mrpt_177_price_to_median_ratio_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_177_price_to_median_ratio_rank_126d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rank_pct(base, 126)

def mrpt_178_price_to_median_ratio_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_178_price_to_median_ratio_lvl_252d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rolling_mean(base, 252)

def mrpt_179_price_to_median_ratio_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_179_price_to_median_ratio_zscore_252d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _zscore_rolling(base, 252)

def mrpt_180_price_to_median_ratio_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_180_price_to_median_ratio_rank_252d
    ECONOMIC RATIONALE: Ratio of price to medium-term median.
    """
    base = close / close.rolling(126).median()
    return _rank_pct(base, 252)

def mrpt_181_reversion_potential_index_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_181_reversion_potential_index_lvl_5d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rolling_mean(base, 5)

def mrpt_182_reversion_potential_index_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_182_reversion_potential_index_zscore_5d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _zscore_rolling(base, 5)

def mrpt_183_reversion_potential_index_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_183_reversion_potential_index_rank_5d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rank_pct(base, 5)

def mrpt_184_reversion_potential_index_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_184_reversion_potential_index_lvl_21d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rolling_mean(base, 21)

def mrpt_185_reversion_potential_index_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_185_reversion_potential_index_zscore_21d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _zscore_rolling(base, 21)

def mrpt_186_reversion_potential_index_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_186_reversion_potential_index_rank_21d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rank_pct(base, 21)

def mrpt_187_reversion_potential_index_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_187_reversion_potential_index_lvl_63d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rolling_mean(base, 63)

def mrpt_188_reversion_potential_index_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_188_reversion_potential_index_zscore_63d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _zscore_rolling(base, 63)

def mrpt_189_reversion_potential_index_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_189_reversion_potential_index_rank_63d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rank_pct(base, 63)

def mrpt_190_reversion_potential_index_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_190_reversion_potential_index_lvl_126d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rolling_mean(base, 126)

def mrpt_191_reversion_potential_index_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_191_reversion_potential_index_zscore_126d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _zscore_rolling(base, 126)

def mrpt_192_reversion_potential_index_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_192_reversion_potential_index_rank_126d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rank_pct(base, 126)

def mrpt_193_reversion_potential_index_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_193_reversion_potential_index_lvl_252d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rolling_mean(base, 252)

def mrpt_194_reversion_potential_index_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_194_reversion_potential_index_zscore_252d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _zscore_rolling(base, 252)

def mrpt_195_reversion_potential_index_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_195_reversion_potential_index_rank_252d
    ECONOMIC RATIONALE: Potential energy for mean reversion.
    """
    base = abs(close - close.rolling(252).mean()) * close.rolling(252).std()
    return _rank_pct(base, 252)

def mrpt_196_linear_regression_slope_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_196_linear_regression_slope_lvl_5d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rolling_mean(base, 5)

def mrpt_197_linear_regression_slope_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_197_linear_regression_slope_zscore_5d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _zscore_rolling(base, 5)

def mrpt_198_linear_regression_slope_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_198_linear_regression_slope_rank_5d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rank_pct(base, 5)

def mrpt_199_linear_regression_slope_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_199_linear_regression_slope_lvl_21d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rolling_mean(base, 21)

def mrpt_200_linear_regression_slope_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_200_linear_regression_slope_zscore_21d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _zscore_rolling(base, 21)

def mrpt_201_linear_regression_slope_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_201_linear_regression_slope_rank_21d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rank_pct(base, 21)

def mrpt_202_linear_regression_slope_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_202_linear_regression_slope_lvl_63d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rolling_mean(base, 63)

def mrpt_203_linear_regression_slope_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_203_linear_regression_slope_zscore_63d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _zscore_rolling(base, 63)

def mrpt_204_linear_regression_slope_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_204_linear_regression_slope_rank_63d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rank_pct(base, 63)

def mrpt_205_linear_regression_slope_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_205_linear_regression_slope_lvl_126d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rolling_mean(base, 126)

def mrpt_206_linear_regression_slope_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_206_linear_regression_slope_zscore_126d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _zscore_rolling(base, 126)

def mrpt_207_linear_regression_slope_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_207_linear_regression_slope_rank_126d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rank_pct(base, 126)

def mrpt_208_linear_regression_slope_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_208_linear_regression_slope_lvl_252d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rolling_mean(base, 252)

def mrpt_209_linear_regression_slope_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_209_linear_regression_slope_zscore_252d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _zscore_rolling(base, 252)

def mrpt_210_linear_regression_slope_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_210_linear_regression_slope_rank_252d
    ECONOMIC RATIONALE: Slope of recent price trend.
    """
    base = close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])
    return _rank_pct(base, 252)

def mrpt_211_standard_error_channel_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_211_standard_error_channel_lvl_5d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rolling_mean(base, 5)

def mrpt_212_standard_error_channel_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_212_standard_error_channel_zscore_5d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _zscore_rolling(base, 5)

def mrpt_213_standard_error_channel_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_213_standard_error_channel_rank_5d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rank_pct(base, 5)

def mrpt_214_standard_error_channel_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_214_standard_error_channel_lvl_21d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rolling_mean(base, 21)

def mrpt_215_standard_error_channel_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_215_standard_error_channel_zscore_21d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _zscore_rolling(base, 21)

def mrpt_216_standard_error_channel_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_216_standard_error_channel_rank_21d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rank_pct(base, 21)

def mrpt_217_standard_error_channel_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_217_standard_error_channel_lvl_63d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rolling_mean(base, 63)

def mrpt_218_standard_error_channel_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_218_standard_error_channel_zscore_63d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _zscore_rolling(base, 63)

def mrpt_219_standard_error_channel_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_219_standard_error_channel_rank_63d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rank_pct(base, 63)

def mrpt_220_standard_error_channel_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_220_standard_error_channel_lvl_126d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rolling_mean(base, 126)

def mrpt_221_standard_error_channel_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_221_standard_error_channel_zscore_126d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _zscore_rolling(base, 126)

def mrpt_222_standard_error_channel_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_222_standard_error_channel_rank_126d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rank_pct(base, 126)

def mrpt_223_standard_error_channel_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_223_standard_error_channel_lvl_252d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rolling_mean(base, 252)

def mrpt_224_standard_error_channel_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_224_standard_error_channel_zscore_252d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _zscore_rolling(base, 252)

def mrpt_225_standard_error_channel_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_225_standard_error_channel_rank_252d
    ECONOMIC RATIONALE: Residuals from linear regression trend.
    """
    base = (close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V104_REGISTRY_2 = {
    "mrpt_121_mean_reversion_rank_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_121_mean_reversion_rank_lvl_5d},
    "mrpt_122_mean_reversion_rank_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_122_mean_reversion_rank_zscore_5d},
    "mrpt_123_mean_reversion_rank_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_123_mean_reversion_rank_rank_5d},
    "mrpt_124_mean_reversion_rank_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_124_mean_reversion_rank_lvl_21d},
    "mrpt_125_mean_reversion_rank_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_125_mean_reversion_rank_zscore_21d},
    "mrpt_126_mean_reversion_rank_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_126_mean_reversion_rank_rank_21d},
    "mrpt_127_mean_reversion_rank_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_127_mean_reversion_rank_lvl_63d},
    "mrpt_128_mean_reversion_rank_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_128_mean_reversion_rank_zscore_63d},
    "mrpt_129_mean_reversion_rank_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_129_mean_reversion_rank_rank_63d},
    "mrpt_130_mean_reversion_rank_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_130_mean_reversion_rank_lvl_126d},
    "mrpt_131_mean_reversion_rank_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_131_mean_reversion_rank_zscore_126d},
    "mrpt_132_mean_reversion_rank_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_132_mean_reversion_rank_rank_126d},
    "mrpt_133_mean_reversion_rank_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_133_mean_reversion_rank_lvl_252d},
    "mrpt_134_mean_reversion_rank_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_134_mean_reversion_rank_zscore_252d},
    "mrpt_135_mean_reversion_rank_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_135_mean_reversion_rank_rank_252d},
    "mrpt_136_volatility_adjusted_stretch_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_136_volatility_adjusted_stretch_lvl_5d},
    "mrpt_137_volatility_adjusted_stretch_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_137_volatility_adjusted_stretch_zscore_5d},
    "mrpt_138_volatility_adjusted_stretch_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_138_volatility_adjusted_stretch_rank_5d},
    "mrpt_139_volatility_adjusted_stretch_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_139_volatility_adjusted_stretch_lvl_21d},
    "mrpt_140_volatility_adjusted_stretch_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_140_volatility_adjusted_stretch_zscore_21d},
    "mrpt_141_volatility_adjusted_stretch_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_141_volatility_adjusted_stretch_rank_21d},
    "mrpt_142_volatility_adjusted_stretch_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_142_volatility_adjusted_stretch_lvl_63d},
    "mrpt_143_volatility_adjusted_stretch_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_143_volatility_adjusted_stretch_zscore_63d},
    "mrpt_144_volatility_adjusted_stretch_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_144_volatility_adjusted_stretch_rank_63d},
    "mrpt_145_volatility_adjusted_stretch_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_145_volatility_adjusted_stretch_lvl_126d},
    "mrpt_146_volatility_adjusted_stretch_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_146_volatility_adjusted_stretch_zscore_126d},
    "mrpt_147_volatility_adjusted_stretch_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_147_volatility_adjusted_stretch_rank_126d},
    "mrpt_148_volatility_adjusted_stretch_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_148_volatility_adjusted_stretch_lvl_252d},
    "mrpt_149_volatility_adjusted_stretch_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_149_volatility_adjusted_stretch_zscore_252d},
    "mrpt_150_volatility_adjusted_stretch_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_150_volatility_adjusted_stretch_rank_252d},
    "mrpt_151_mean_reversion_score_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_151_mean_reversion_score_lvl_5d},
    "mrpt_152_mean_reversion_score_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_152_mean_reversion_score_zscore_5d},
    "mrpt_153_mean_reversion_score_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_153_mean_reversion_score_rank_5d},
    "mrpt_154_mean_reversion_score_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_154_mean_reversion_score_lvl_21d},
    "mrpt_155_mean_reversion_score_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_155_mean_reversion_score_zscore_21d},
    "mrpt_156_mean_reversion_score_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_156_mean_reversion_score_rank_21d},
    "mrpt_157_mean_reversion_score_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_157_mean_reversion_score_lvl_63d},
    "mrpt_158_mean_reversion_score_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_158_mean_reversion_score_zscore_63d},
    "mrpt_159_mean_reversion_score_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_159_mean_reversion_score_rank_63d},
    "mrpt_160_mean_reversion_score_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_160_mean_reversion_score_lvl_126d},
    "mrpt_161_mean_reversion_score_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_161_mean_reversion_score_zscore_126d},
    "mrpt_162_mean_reversion_score_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_162_mean_reversion_score_rank_126d},
    "mrpt_163_mean_reversion_score_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_163_mean_reversion_score_lvl_252d},
    "mrpt_164_mean_reversion_score_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_164_mean_reversion_score_zscore_252d},
    "mrpt_165_mean_reversion_score_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_165_mean_reversion_score_rank_252d},
    "mrpt_166_price_to_median_ratio_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_166_price_to_median_ratio_lvl_5d},
    "mrpt_167_price_to_median_ratio_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_167_price_to_median_ratio_zscore_5d},
    "mrpt_168_price_to_median_ratio_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_168_price_to_median_ratio_rank_5d},
    "mrpt_169_price_to_median_ratio_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_169_price_to_median_ratio_lvl_21d},
    "mrpt_170_price_to_median_ratio_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_170_price_to_median_ratio_zscore_21d},
    "mrpt_171_price_to_median_ratio_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_171_price_to_median_ratio_rank_21d},
    "mrpt_172_price_to_median_ratio_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_172_price_to_median_ratio_lvl_63d},
    "mrpt_173_price_to_median_ratio_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_173_price_to_median_ratio_zscore_63d},
    "mrpt_174_price_to_median_ratio_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_174_price_to_median_ratio_rank_63d},
    "mrpt_175_price_to_median_ratio_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_175_price_to_median_ratio_lvl_126d},
    "mrpt_176_price_to_median_ratio_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_176_price_to_median_ratio_zscore_126d},
    "mrpt_177_price_to_median_ratio_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_177_price_to_median_ratio_rank_126d},
    "mrpt_178_price_to_median_ratio_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_178_price_to_median_ratio_lvl_252d},
    "mrpt_179_price_to_median_ratio_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_179_price_to_median_ratio_zscore_252d},
    "mrpt_180_price_to_median_ratio_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_180_price_to_median_ratio_rank_252d},
    "mrpt_181_reversion_potential_index_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_181_reversion_potential_index_lvl_5d},
    "mrpt_182_reversion_potential_index_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_182_reversion_potential_index_zscore_5d},
    "mrpt_183_reversion_potential_index_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_183_reversion_potential_index_rank_5d},
    "mrpt_184_reversion_potential_index_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_184_reversion_potential_index_lvl_21d},
    "mrpt_185_reversion_potential_index_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_185_reversion_potential_index_zscore_21d},
    "mrpt_186_reversion_potential_index_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_186_reversion_potential_index_rank_21d},
    "mrpt_187_reversion_potential_index_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_187_reversion_potential_index_lvl_63d},
    "mrpt_188_reversion_potential_index_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_188_reversion_potential_index_zscore_63d},
    "mrpt_189_reversion_potential_index_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_189_reversion_potential_index_rank_63d},
    "mrpt_190_reversion_potential_index_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_190_reversion_potential_index_lvl_126d},
    "mrpt_191_reversion_potential_index_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_191_reversion_potential_index_zscore_126d},
    "mrpt_192_reversion_potential_index_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_192_reversion_potential_index_rank_126d},
    "mrpt_193_reversion_potential_index_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_193_reversion_potential_index_lvl_252d},
    "mrpt_194_reversion_potential_index_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_194_reversion_potential_index_zscore_252d},
    "mrpt_195_reversion_potential_index_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_195_reversion_potential_index_rank_252d},
    "mrpt_196_linear_regression_slope_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_196_linear_regression_slope_lvl_5d},
    "mrpt_197_linear_regression_slope_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_197_linear_regression_slope_zscore_5d},
    "mrpt_198_linear_regression_slope_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_198_linear_regression_slope_rank_5d},
    "mrpt_199_linear_regression_slope_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_199_linear_regression_slope_lvl_21d},
    "mrpt_200_linear_regression_slope_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_200_linear_regression_slope_zscore_21d},
    "mrpt_201_linear_regression_slope_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_201_linear_regression_slope_rank_21d},
    "mrpt_202_linear_regression_slope_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_202_linear_regression_slope_lvl_63d},
    "mrpt_203_linear_regression_slope_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_203_linear_regression_slope_zscore_63d},
    "mrpt_204_linear_regression_slope_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_204_linear_regression_slope_rank_63d},
    "mrpt_205_linear_regression_slope_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_205_linear_regression_slope_lvl_126d},
    "mrpt_206_linear_regression_slope_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_206_linear_regression_slope_zscore_126d},
    "mrpt_207_linear_regression_slope_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_207_linear_regression_slope_rank_126d},
    "mrpt_208_linear_regression_slope_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_208_linear_regression_slope_lvl_252d},
    "mrpt_209_linear_regression_slope_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_209_linear_regression_slope_zscore_252d},
    "mrpt_210_linear_regression_slope_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_210_linear_regression_slope_rank_252d},
    "mrpt_211_standard_error_channel_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_211_standard_error_channel_lvl_5d},
    "mrpt_212_standard_error_channel_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_212_standard_error_channel_zscore_5d},
    "mrpt_213_standard_error_channel_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_213_standard_error_channel_rank_5d},
    "mrpt_214_standard_error_channel_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_214_standard_error_channel_lvl_21d},
    "mrpt_215_standard_error_channel_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_215_standard_error_channel_zscore_21d},
    "mrpt_216_standard_error_channel_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_216_standard_error_channel_rank_21d},
    "mrpt_217_standard_error_channel_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_217_standard_error_channel_lvl_63d},
    "mrpt_218_standard_error_channel_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_218_standard_error_channel_zscore_63d},
    "mrpt_219_standard_error_channel_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_219_standard_error_channel_rank_63d},
    "mrpt_220_standard_error_channel_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_220_standard_error_channel_lvl_126d},
    "mrpt_221_standard_error_channel_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_221_standard_error_channel_zscore_126d},
    "mrpt_222_standard_error_channel_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_222_standard_error_channel_rank_126d},
    "mrpt_223_standard_error_channel_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_223_standard_error_channel_lvl_252d},
    "mrpt_224_standard_error_channel_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_224_standard_error_channel_zscore_252d},
    "mrpt_225_standard_error_channel_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_225_standard_error_channel_rank_252d},
}
