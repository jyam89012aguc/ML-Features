"""
107_change_point_detection — Base Features Part 2
Domain: change_point_detection
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

def cpdt_121_volume_regime_break_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_121_volume_regime_break_lvl_5d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rolling_mean(base, 5)

def cpdt_122_volume_regime_break_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_122_volume_regime_break_zscore_5d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _zscore_rolling(base, 5)

def cpdt_123_volume_regime_break_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_123_volume_regime_break_rank_5d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rank_pct(base, 5)

def cpdt_124_volume_regime_break_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_124_volume_regime_break_lvl_21d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rolling_mean(base, 21)

def cpdt_125_volume_regime_break_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_125_volume_regime_break_zscore_21d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _zscore_rolling(base, 21)

def cpdt_126_volume_regime_break_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_126_volume_regime_break_rank_21d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rank_pct(base, 21)

def cpdt_127_volume_regime_break_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_127_volume_regime_break_lvl_63d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rolling_mean(base, 63)

def cpdt_128_volume_regime_break_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_128_volume_regime_break_zscore_63d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _zscore_rolling(base, 63)

def cpdt_129_volume_regime_break_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_129_volume_regime_break_rank_63d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rank_pct(base, 63)

def cpdt_130_volume_regime_break_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_130_volume_regime_break_lvl_126d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rolling_mean(base, 126)

def cpdt_131_volume_regime_break_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_131_volume_regime_break_zscore_126d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _zscore_rolling(base, 126)

def cpdt_132_volume_regime_break_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_132_volume_regime_break_rank_126d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rank_pct(base, 126)

def cpdt_133_volume_regime_break_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_133_volume_regime_break_lvl_252d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rolling_mean(base, 252)

def cpdt_134_volume_regime_break_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_134_volume_regime_break_zscore_252d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _zscore_rolling(base, 252)

def cpdt_135_volume_regime_break_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_135_volume_regime_break_rank_252d
    ECONOMIC RATIONALE: Significant change in average volume levels.
    """
    base = volume.rolling(21).mean() / volume.rolling(252).mean()
    return _rank_pct(base, 252)

def cpdt_136_price_level_stability_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_136_price_level_stability_lvl_5d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rolling_mean(base, 5)

def cpdt_137_price_level_stability_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_137_price_level_stability_zscore_5d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _zscore_rolling(base, 5)

def cpdt_138_price_level_stability_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_138_price_level_stability_rank_5d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rank_pct(base, 5)

def cpdt_139_price_level_stability_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_139_price_level_stability_lvl_21d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rolling_mean(base, 21)

def cpdt_140_price_level_stability_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_140_price_level_stability_zscore_21d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _zscore_rolling(base, 21)

def cpdt_141_price_level_stability_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_141_price_level_stability_rank_21d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rank_pct(base, 21)

def cpdt_142_price_level_stability_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_142_price_level_stability_lvl_63d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rolling_mean(base, 63)

def cpdt_143_price_level_stability_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_143_price_level_stability_zscore_63d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _zscore_rolling(base, 63)

def cpdt_144_price_level_stability_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_144_price_level_stability_rank_63d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rank_pct(base, 63)

def cpdt_145_price_level_stability_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_145_price_level_stability_lvl_126d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rolling_mean(base, 126)

def cpdt_146_price_level_stability_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_146_price_level_stability_zscore_126d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _zscore_rolling(base, 126)

def cpdt_147_price_level_stability_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_147_price_level_stability_rank_126d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rank_pct(base, 126)

def cpdt_148_price_level_stability_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_148_price_level_stability_lvl_252d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rolling_mean(base, 252)

def cpdt_149_price_level_stability_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_149_price_level_stability_zscore_252d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _zscore_rolling(base, 252)

def cpdt_150_price_level_stability_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_150_price_level_stability_rank_252d
    ECONOMIC RATIONALE: Inversely related to regime stability.
    """
    base = close.rolling(21).std() / close
    return _rank_pct(base, 252)

def cpdt_151_structural_break_score_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_151_structural_break_score_lvl_5d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 5)

def cpdt_152_structural_break_score_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_152_structural_break_score_zscore_5d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 5)

def cpdt_153_structural_break_score_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_153_structural_break_score_rank_5d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 5)

def cpdt_154_structural_break_score_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_154_structural_break_score_lvl_21d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 21)

def cpdt_155_structural_break_score_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_155_structural_break_score_zscore_21d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 21)

def cpdt_156_structural_break_score_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_156_structural_break_score_rank_21d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 21)

def cpdt_157_structural_break_score_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_157_structural_break_score_lvl_63d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 63)

def cpdt_158_structural_break_score_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_158_structural_break_score_zscore_63d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 63)

def cpdt_159_structural_break_score_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_159_structural_break_score_rank_63d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 63)

def cpdt_160_structural_break_score_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_160_structural_break_score_lvl_126d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 126)

def cpdt_161_structural_break_score_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_161_structural_break_score_zscore_126d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 126)

def cpdt_162_structural_break_score_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_162_structural_break_score_rank_126d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 126)

def cpdt_163_structural_break_score_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_163_structural_break_score_lvl_252d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 252)

def cpdt_164_structural_break_score_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_164_structural_break_score_zscore_252d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 252)

def cpdt_165_structural_break_score_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_165_structural_break_score_rank_252d
    ECONOMIC RATIONALE: Binary indicator of structural price breaks.
    """
    base = (close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 252)

def cpdt_166_regime_switching_proxy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_166_regime_switching_proxy_lvl_5d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rolling_mean(base, 5)

def cpdt_167_regime_switching_proxy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_167_regime_switching_proxy_zscore_5d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _zscore_rolling(base, 5)

def cpdt_168_regime_switching_proxy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_168_regime_switching_proxy_rank_5d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rank_pct(base, 5)

def cpdt_169_regime_switching_proxy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_169_regime_switching_proxy_lvl_21d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rolling_mean(base, 21)

def cpdt_170_regime_switching_proxy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_170_regime_switching_proxy_zscore_21d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _zscore_rolling(base, 21)

def cpdt_171_regime_switching_proxy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_171_regime_switching_proxy_rank_21d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rank_pct(base, 21)

def cpdt_172_regime_switching_proxy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_172_regime_switching_proxy_lvl_63d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rolling_mean(base, 63)

def cpdt_173_regime_switching_proxy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_173_regime_switching_proxy_zscore_63d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _zscore_rolling(base, 63)

def cpdt_174_regime_switching_proxy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_174_regime_switching_proxy_rank_63d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rank_pct(base, 63)

def cpdt_175_regime_switching_proxy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_175_regime_switching_proxy_lvl_126d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rolling_mean(base, 126)

def cpdt_176_regime_switching_proxy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_176_regime_switching_proxy_zscore_126d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _zscore_rolling(base, 126)

def cpdt_177_regime_switching_proxy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_177_regime_switching_proxy_rank_126d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rank_pct(base, 126)

def cpdt_178_regime_switching_proxy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_178_regime_switching_proxy_lvl_252d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rolling_mean(base, 252)

def cpdt_179_regime_switching_proxy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_179_regime_switching_proxy_zscore_252d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _zscore_rolling(base, 252)

def cpdt_180_regime_switching_proxy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_180_regime_switching_proxy_rank_252d
    ECONOMIC RATIONALE: Stability of the current local trend.
    """
    base = close.rolling(10).mean().corr(np.arange(10))
    return _rank_pct(base, 252)

def cpdt_181_autocorr_regime_shift_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_181_autocorr_regime_shift_lvl_5d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 5)

def cpdt_182_autocorr_regime_shift_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_182_autocorr_regime_shift_zscore_5d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 5)

def cpdt_183_autocorr_regime_shift_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_183_autocorr_regime_shift_rank_5d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 5)

def cpdt_184_autocorr_regime_shift_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_184_autocorr_regime_shift_lvl_21d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 21)

def cpdt_185_autocorr_regime_shift_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_185_autocorr_regime_shift_zscore_21d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 21)

def cpdt_186_autocorr_regime_shift_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_186_autocorr_regime_shift_rank_21d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 21)

def cpdt_187_autocorr_regime_shift_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_187_autocorr_regime_shift_lvl_63d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 63)

def cpdt_188_autocorr_regime_shift_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_188_autocorr_regime_shift_zscore_63d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 63)

def cpdt_189_autocorr_regime_shift_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_189_autocorr_regime_shift_rank_63d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 63)

def cpdt_190_autocorr_regime_shift_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_190_autocorr_regime_shift_lvl_126d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 126)

def cpdt_191_autocorr_regime_shift_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_191_autocorr_regime_shift_zscore_126d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 126)

def cpdt_192_autocorr_regime_shift_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_192_autocorr_regime_shift_rank_126d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 126)

def cpdt_193_autocorr_regime_shift_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_193_autocorr_regime_shift_lvl_252d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 252)

def cpdt_194_autocorr_regime_shift_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_194_autocorr_regime_shift_zscore_252d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 252)

def cpdt_195_autocorr_regime_shift_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_195_autocorr_regime_shift_rank_252d
    ECONOMIC RATIONALE: Shift in the serial correlation of returns.
    """
    base = close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 252)

def cpdt_196_tail_event_density_change_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_196_tail_event_density_change_lvl_5d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rolling_mean(base, 5)

def cpdt_197_tail_event_density_change_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_197_tail_event_density_change_zscore_5d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _zscore_rolling(base, 5)

def cpdt_198_tail_event_density_change_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_198_tail_event_density_change_rank_5d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rank_pct(base, 5)

def cpdt_199_tail_event_density_change_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_199_tail_event_density_change_lvl_21d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rolling_mean(base, 21)

def cpdt_200_tail_event_density_change_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_200_tail_event_density_change_zscore_21d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _zscore_rolling(base, 21)

def cpdt_201_tail_event_density_change_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_201_tail_event_density_change_rank_21d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rank_pct(base, 21)

def cpdt_202_tail_event_density_change_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_202_tail_event_density_change_lvl_63d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rolling_mean(base, 63)

def cpdt_203_tail_event_density_change_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_203_tail_event_density_change_zscore_63d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _zscore_rolling(base, 63)

def cpdt_204_tail_event_density_change_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_204_tail_event_density_change_rank_63d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rank_pct(base, 63)

def cpdt_205_tail_event_density_change_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_205_tail_event_density_change_lvl_126d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rolling_mean(base, 126)

def cpdt_206_tail_event_density_change_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_206_tail_event_density_change_zscore_126d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _zscore_rolling(base, 126)

def cpdt_207_tail_event_density_change_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_207_tail_event_density_change_rank_126d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rank_pct(base, 126)

def cpdt_208_tail_event_density_change_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_208_tail_event_density_change_lvl_252d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rolling_mean(base, 252)

def cpdt_209_tail_event_density_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_209_tail_event_density_change_zscore_252d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _zscore_rolling(base, 252)

def cpdt_210_tail_event_density_change_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_210_tail_event_density_change_rank_252d
    ECONOMIC RATIONALE: Change in the frequency of tail events.
    """
    base = (close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()
    return _rank_pct(base, 252)

def cpdt_211_price_volume_regime_corr_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_211_price_volume_regime_corr_lvl_5d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rolling_mean(base, 5)

def cpdt_212_price_volume_regime_corr_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_212_price_volume_regime_corr_zscore_5d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _zscore_rolling(base, 5)

def cpdt_213_price_volume_regime_corr_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_213_price_volume_regime_corr_rank_5d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rank_pct(base, 5)

def cpdt_214_price_volume_regime_corr_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_214_price_volume_regime_corr_lvl_21d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rolling_mean(base, 21)

def cpdt_215_price_volume_regime_corr_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_215_price_volume_regime_corr_zscore_21d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _zscore_rolling(base, 21)

def cpdt_216_price_volume_regime_corr_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_216_price_volume_regime_corr_rank_21d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rank_pct(base, 21)

def cpdt_217_price_volume_regime_corr_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_217_price_volume_regime_corr_lvl_63d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rolling_mean(base, 63)

def cpdt_218_price_volume_regime_corr_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_218_price_volume_regime_corr_zscore_63d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _zscore_rolling(base, 63)

def cpdt_219_price_volume_regime_corr_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_219_price_volume_regime_corr_rank_63d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rank_pct(base, 63)

def cpdt_220_price_volume_regime_corr_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_220_price_volume_regime_corr_lvl_126d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rolling_mean(base, 126)

def cpdt_221_price_volume_regime_corr_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_221_price_volume_regime_corr_zscore_126d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _zscore_rolling(base, 126)

def cpdt_222_price_volume_regime_corr_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_222_price_volume_regime_corr_rank_126d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rank_pct(base, 126)

def cpdt_223_price_volume_regime_corr_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_223_price_volume_regime_corr_lvl_252d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rolling_mean(base, 252)

def cpdt_224_price_volume_regime_corr_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_224_price_volume_regime_corr_zscore_252d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _zscore_rolling(base, 252)

def cpdt_225_price_volume_regime_corr_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_225_price_volume_regime_corr_rank_252d
    ECONOMIC RATIONALE: Shift in the relationship between price and volume.
    """
    base = close.rolling(21).corr(volume).diff(21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V107_REGISTRY_2 = {
    "cpdt_121_volume_regime_break_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_121_volume_regime_break_lvl_5d},
    "cpdt_122_volume_regime_break_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_122_volume_regime_break_zscore_5d},
    "cpdt_123_volume_regime_break_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_123_volume_regime_break_rank_5d},
    "cpdt_124_volume_regime_break_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_124_volume_regime_break_lvl_21d},
    "cpdt_125_volume_regime_break_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_125_volume_regime_break_zscore_21d},
    "cpdt_126_volume_regime_break_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_126_volume_regime_break_rank_21d},
    "cpdt_127_volume_regime_break_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_127_volume_regime_break_lvl_63d},
    "cpdt_128_volume_regime_break_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_128_volume_regime_break_zscore_63d},
    "cpdt_129_volume_regime_break_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_129_volume_regime_break_rank_63d},
    "cpdt_130_volume_regime_break_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_130_volume_regime_break_lvl_126d},
    "cpdt_131_volume_regime_break_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_131_volume_regime_break_zscore_126d},
    "cpdt_132_volume_regime_break_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_132_volume_regime_break_rank_126d},
    "cpdt_133_volume_regime_break_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_133_volume_regime_break_lvl_252d},
    "cpdt_134_volume_regime_break_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_134_volume_regime_break_zscore_252d},
    "cpdt_135_volume_regime_break_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_135_volume_regime_break_rank_252d},
    "cpdt_136_price_level_stability_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_136_price_level_stability_lvl_5d},
    "cpdt_137_price_level_stability_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_137_price_level_stability_zscore_5d},
    "cpdt_138_price_level_stability_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_138_price_level_stability_rank_5d},
    "cpdt_139_price_level_stability_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_139_price_level_stability_lvl_21d},
    "cpdt_140_price_level_stability_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_140_price_level_stability_zscore_21d},
    "cpdt_141_price_level_stability_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_141_price_level_stability_rank_21d},
    "cpdt_142_price_level_stability_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_142_price_level_stability_lvl_63d},
    "cpdt_143_price_level_stability_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_143_price_level_stability_zscore_63d},
    "cpdt_144_price_level_stability_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_144_price_level_stability_rank_63d},
    "cpdt_145_price_level_stability_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_145_price_level_stability_lvl_126d},
    "cpdt_146_price_level_stability_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_146_price_level_stability_zscore_126d},
    "cpdt_147_price_level_stability_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_147_price_level_stability_rank_126d},
    "cpdt_148_price_level_stability_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_148_price_level_stability_lvl_252d},
    "cpdt_149_price_level_stability_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_149_price_level_stability_zscore_252d},
    "cpdt_150_price_level_stability_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_150_price_level_stability_rank_252d},
    "cpdt_151_structural_break_score_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_151_structural_break_score_lvl_5d},
    "cpdt_152_structural_break_score_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_152_structural_break_score_zscore_5d},
    "cpdt_153_structural_break_score_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_153_structural_break_score_rank_5d},
    "cpdt_154_structural_break_score_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_154_structural_break_score_lvl_21d},
    "cpdt_155_structural_break_score_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_155_structural_break_score_zscore_21d},
    "cpdt_156_structural_break_score_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_156_structural_break_score_rank_21d},
    "cpdt_157_structural_break_score_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_157_structural_break_score_lvl_63d},
    "cpdt_158_structural_break_score_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_158_structural_break_score_zscore_63d},
    "cpdt_159_structural_break_score_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_159_structural_break_score_rank_63d},
    "cpdt_160_structural_break_score_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_160_structural_break_score_lvl_126d},
    "cpdt_161_structural_break_score_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_161_structural_break_score_zscore_126d},
    "cpdt_162_structural_break_score_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_162_structural_break_score_rank_126d},
    "cpdt_163_structural_break_score_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_163_structural_break_score_lvl_252d},
    "cpdt_164_structural_break_score_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_164_structural_break_score_zscore_252d},
    "cpdt_165_structural_break_score_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_165_structural_break_score_rank_252d},
    "cpdt_166_regime_switching_proxy_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_166_regime_switching_proxy_lvl_5d},
    "cpdt_167_regime_switching_proxy_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_167_regime_switching_proxy_zscore_5d},
    "cpdt_168_regime_switching_proxy_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_168_regime_switching_proxy_rank_5d},
    "cpdt_169_regime_switching_proxy_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_169_regime_switching_proxy_lvl_21d},
    "cpdt_170_regime_switching_proxy_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_170_regime_switching_proxy_zscore_21d},
    "cpdt_171_regime_switching_proxy_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_171_regime_switching_proxy_rank_21d},
    "cpdt_172_regime_switching_proxy_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_172_regime_switching_proxy_lvl_63d},
    "cpdt_173_regime_switching_proxy_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_173_regime_switching_proxy_zscore_63d},
    "cpdt_174_regime_switching_proxy_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_174_regime_switching_proxy_rank_63d},
    "cpdt_175_regime_switching_proxy_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_175_regime_switching_proxy_lvl_126d},
    "cpdt_176_regime_switching_proxy_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_176_regime_switching_proxy_zscore_126d},
    "cpdt_177_regime_switching_proxy_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_177_regime_switching_proxy_rank_126d},
    "cpdt_178_regime_switching_proxy_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_178_regime_switching_proxy_lvl_252d},
    "cpdt_179_regime_switching_proxy_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_179_regime_switching_proxy_zscore_252d},
    "cpdt_180_regime_switching_proxy_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_180_regime_switching_proxy_rank_252d},
    "cpdt_181_autocorr_regime_shift_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_181_autocorr_regime_shift_lvl_5d},
    "cpdt_182_autocorr_regime_shift_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_182_autocorr_regime_shift_zscore_5d},
    "cpdt_183_autocorr_regime_shift_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_183_autocorr_regime_shift_rank_5d},
    "cpdt_184_autocorr_regime_shift_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_184_autocorr_regime_shift_lvl_21d},
    "cpdt_185_autocorr_regime_shift_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_185_autocorr_regime_shift_zscore_21d},
    "cpdt_186_autocorr_regime_shift_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_186_autocorr_regime_shift_rank_21d},
    "cpdt_187_autocorr_regime_shift_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_187_autocorr_regime_shift_lvl_63d},
    "cpdt_188_autocorr_regime_shift_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_188_autocorr_regime_shift_zscore_63d},
    "cpdt_189_autocorr_regime_shift_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_189_autocorr_regime_shift_rank_63d},
    "cpdt_190_autocorr_regime_shift_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_190_autocorr_regime_shift_lvl_126d},
    "cpdt_191_autocorr_regime_shift_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_191_autocorr_regime_shift_zscore_126d},
    "cpdt_192_autocorr_regime_shift_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_192_autocorr_regime_shift_rank_126d},
    "cpdt_193_autocorr_regime_shift_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_193_autocorr_regime_shift_lvl_252d},
    "cpdt_194_autocorr_regime_shift_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_194_autocorr_regime_shift_zscore_252d},
    "cpdt_195_autocorr_regime_shift_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_195_autocorr_regime_shift_rank_252d},
    "cpdt_196_tail_event_density_change_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_196_tail_event_density_change_lvl_5d},
    "cpdt_197_tail_event_density_change_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_197_tail_event_density_change_zscore_5d},
    "cpdt_198_tail_event_density_change_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_198_tail_event_density_change_rank_5d},
    "cpdt_199_tail_event_density_change_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_199_tail_event_density_change_lvl_21d},
    "cpdt_200_tail_event_density_change_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_200_tail_event_density_change_zscore_21d},
    "cpdt_201_tail_event_density_change_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_201_tail_event_density_change_rank_21d},
    "cpdt_202_tail_event_density_change_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_202_tail_event_density_change_lvl_63d},
    "cpdt_203_tail_event_density_change_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_203_tail_event_density_change_zscore_63d},
    "cpdt_204_tail_event_density_change_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_204_tail_event_density_change_rank_63d},
    "cpdt_205_tail_event_density_change_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_205_tail_event_density_change_lvl_126d},
    "cpdt_206_tail_event_density_change_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_206_tail_event_density_change_zscore_126d},
    "cpdt_207_tail_event_density_change_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_207_tail_event_density_change_rank_126d},
    "cpdt_208_tail_event_density_change_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_208_tail_event_density_change_lvl_252d},
    "cpdt_209_tail_event_density_change_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_209_tail_event_density_change_zscore_252d},
    "cpdt_210_tail_event_density_change_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_210_tail_event_density_change_rank_252d},
    "cpdt_211_price_volume_regime_corr_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_211_price_volume_regime_corr_lvl_5d},
    "cpdt_212_price_volume_regime_corr_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_212_price_volume_regime_corr_zscore_5d},
    "cpdt_213_price_volume_regime_corr_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_213_price_volume_regime_corr_rank_5d},
    "cpdt_214_price_volume_regime_corr_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_214_price_volume_regime_corr_lvl_21d},
    "cpdt_215_price_volume_regime_corr_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_215_price_volume_regime_corr_zscore_21d},
    "cpdt_216_price_volume_regime_corr_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_216_price_volume_regime_corr_rank_21d},
    "cpdt_217_price_volume_regime_corr_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_217_price_volume_regime_corr_lvl_63d},
    "cpdt_218_price_volume_regime_corr_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_218_price_volume_regime_corr_zscore_63d},
    "cpdt_219_price_volume_regime_corr_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_219_price_volume_regime_corr_rank_63d},
    "cpdt_220_price_volume_regime_corr_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_220_price_volume_regime_corr_lvl_126d},
    "cpdt_221_price_volume_regime_corr_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_221_price_volume_regime_corr_zscore_126d},
    "cpdt_222_price_volume_regime_corr_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_222_price_volume_regime_corr_rank_126d},
    "cpdt_223_price_volume_regime_corr_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_223_price_volume_regime_corr_lvl_252d},
    "cpdt_224_price_volume_regime_corr_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_224_price_volume_regime_corr_zscore_252d},
    "cpdt_225_price_volume_regime_corr_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_225_price_volume_regime_corr_rank_252d},
}
