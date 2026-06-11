"""
109_return_autocorrelation — Base Features Part 2
Domain: return_autocorrelation
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

def raut_121_autocorr_breakdown_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_121_autocorr_breakdown_lvl_5d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rolling_mean(base, 5)

def raut_122_autocorr_breakdown_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_122_autocorr_breakdown_zscore_5d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _zscore_rolling(base, 5)

def raut_123_autocorr_breakdown_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_123_autocorr_breakdown_rank_5d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rank_pct(base, 5)

def raut_124_autocorr_breakdown_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_124_autocorr_breakdown_lvl_21d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rolling_mean(base, 21)

def raut_125_autocorr_breakdown_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_125_autocorr_breakdown_zscore_21d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _zscore_rolling(base, 21)

def raut_126_autocorr_breakdown_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_126_autocorr_breakdown_rank_21d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rank_pct(base, 21)

def raut_127_autocorr_breakdown_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_127_autocorr_breakdown_lvl_63d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rolling_mean(base, 63)

def raut_128_autocorr_breakdown_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_128_autocorr_breakdown_zscore_63d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _zscore_rolling(base, 63)

def raut_129_autocorr_breakdown_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_129_autocorr_breakdown_rank_63d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rank_pct(base, 63)

def raut_130_autocorr_breakdown_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_130_autocorr_breakdown_lvl_126d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rolling_mean(base, 126)

def raut_131_autocorr_breakdown_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_131_autocorr_breakdown_zscore_126d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _zscore_rolling(base, 126)

def raut_132_autocorr_breakdown_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_132_autocorr_breakdown_rank_126d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rank_pct(base, 126)

def raut_133_autocorr_breakdown_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_133_autocorr_breakdown_lvl_252d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rolling_mean(base, 252)

def raut_134_autocorr_breakdown_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_134_autocorr_breakdown_zscore_252d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _zscore_rolling(base, 252)

def raut_135_autocorr_breakdown_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_135_autocorr_breakdown_rank_252d
    ECONOMIC RATIONALE: Sudden breakdown in return structure.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)
    return _rank_pct(base, 252)

def raut_136_return_clustering_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_136_return_clustering_lvl_5d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 5)

def raut_137_return_clustering_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_137_return_clustering_zscore_5d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 5)

def raut_138_return_clustering_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_138_return_clustering_rank_5d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rank_pct(base, 5)

def raut_139_return_clustering_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_139_return_clustering_lvl_21d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 21)

def raut_140_return_clustering_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_140_return_clustering_zscore_21d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 21)

def raut_141_return_clustering_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_141_return_clustering_rank_21d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rank_pct(base, 21)

def raut_142_return_clustering_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_142_return_clustering_lvl_63d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 63)

def raut_143_return_clustering_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_143_return_clustering_zscore_63d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 63)

def raut_144_return_clustering_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_144_return_clustering_rank_63d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rank_pct(base, 63)

def raut_145_return_clustering_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_145_return_clustering_lvl_126d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 126)

def raut_146_return_clustering_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_146_return_clustering_zscore_126d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 126)

def raut_147_return_clustering_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_147_return_clustering_rank_126d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rank_pct(base, 126)

def raut_148_return_clustering_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_148_return_clustering_lvl_252d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 252)

def raut_149_return_clustering_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_149_return_clustering_zscore_252d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 252)

def raut_150_return_clustering_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_150_return_clustering_rank_252d
    ECONOMIC RATIONALE: Autocorrelation of absolute returns (volatility clustering).
    """
    base = close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))
    return _rank_pct(base, 252)

def raut_151_autocorr_regime_rank_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_151_autocorr_regime_rank_lvl_5d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 5)

def raut_152_autocorr_regime_rank_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_152_autocorr_regime_rank_zscore_5d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 5)

def raut_153_autocorr_regime_rank_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_153_autocorr_regime_rank_rank_5d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 5)

def raut_154_autocorr_regime_rank_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_154_autocorr_regime_rank_lvl_21d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 21)

def raut_155_autocorr_regime_rank_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_155_autocorr_regime_rank_zscore_21d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 21)

def raut_156_autocorr_regime_rank_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_156_autocorr_regime_rank_rank_21d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 21)

def raut_157_autocorr_regime_rank_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_157_autocorr_regime_rank_lvl_63d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 63)

def raut_158_autocorr_regime_rank_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_158_autocorr_regime_rank_zscore_63d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 63)

def raut_159_autocorr_regime_rank_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_159_autocorr_regime_rank_rank_63d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 63)

def raut_160_autocorr_regime_rank_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_160_autocorr_regime_rank_lvl_126d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 126)

def raut_161_autocorr_regime_rank_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_161_autocorr_regime_rank_zscore_126d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 126)

def raut_162_autocorr_regime_rank_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_162_autocorr_regime_rank_rank_126d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 126)

def raut_163_autocorr_regime_rank_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_163_autocorr_regime_rank_lvl_252d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 252)

def raut_164_autocorr_regime_rank_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_164_autocorr_regime_rank_zscore_252d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 252)

def raut_165_autocorr_regime_rank_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_165_autocorr_regime_rank_rank_252d
    ECONOMIC RATIONALE: Historical rank of current return persistence.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 252)

def raut_166_autocorr_momentum_div_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_166_autocorr_momentum_div_lvl_5d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 5)

def raut_167_autocorr_momentum_div_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_167_autocorr_momentum_div_zscore_5d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 5)

def raut_168_autocorr_momentum_div_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_168_autocorr_momentum_div_rank_5d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 5)

def raut_169_autocorr_momentum_div_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_169_autocorr_momentum_div_lvl_21d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 21)

def raut_170_autocorr_momentum_div_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_170_autocorr_momentum_div_zscore_21d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 21)

def raut_171_autocorr_momentum_div_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_171_autocorr_momentum_div_rank_21d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 21)

def raut_172_autocorr_momentum_div_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_172_autocorr_momentum_div_lvl_63d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 63)

def raut_173_autocorr_momentum_div_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_173_autocorr_momentum_div_zscore_63d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 63)

def raut_174_autocorr_momentum_div_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_174_autocorr_momentum_div_rank_63d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 63)

def raut_175_autocorr_momentum_div_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_175_autocorr_momentum_div_lvl_126d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 126)

def raut_176_autocorr_momentum_div_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_176_autocorr_momentum_div_zscore_126d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 126)

def raut_177_autocorr_momentum_div_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_177_autocorr_momentum_div_rank_126d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 126)

def raut_178_autocorr_momentum_div_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_178_autocorr_momentum_div_lvl_252d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 252)

def raut_179_autocorr_momentum_div_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_179_autocorr_momentum_div_zscore_252d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 252)

def raut_180_autocorr_momentum_div_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_180_autocorr_momentum_div_rank_252d
    ECONOMIC RATIONALE: Momentum weighted by its own persistence.
    """
    base = close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 252)

def raut_181_mean_reversion_edge_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_181_mean_reversion_edge_lvl_5d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rolling_mean(base, 5)

def raut_182_mean_reversion_edge_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_182_mean_reversion_edge_zscore_5d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _zscore_rolling(base, 5)

def raut_183_mean_reversion_edge_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_183_mean_reversion_edge_rank_5d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rank_pct(base, 5)

def raut_184_mean_reversion_edge_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_184_mean_reversion_edge_lvl_21d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rolling_mean(base, 21)

def raut_185_mean_reversion_edge_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_185_mean_reversion_edge_zscore_21d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _zscore_rolling(base, 21)

def raut_186_mean_reversion_edge_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_186_mean_reversion_edge_rank_21d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rank_pct(base, 21)

def raut_187_mean_reversion_edge_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_187_mean_reversion_edge_lvl_63d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rolling_mean(base, 63)

def raut_188_mean_reversion_edge_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_188_mean_reversion_edge_zscore_63d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _zscore_rolling(base, 63)

def raut_189_mean_reversion_edge_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_189_mean_reversion_edge_rank_63d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rank_pct(base, 63)

def raut_190_mean_reversion_edge_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_190_mean_reversion_edge_lvl_126d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rolling_mean(base, 126)

def raut_191_mean_reversion_edge_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_191_mean_reversion_edge_zscore_126d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _zscore_rolling(base, 126)

def raut_192_mean_reversion_edge_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_192_mean_reversion_edge_rank_126d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rank_pct(base, 126)

def raut_193_mean_reversion_edge_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_193_mean_reversion_edge_lvl_252d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rolling_mean(base, 252)

def raut_194_mean_reversion_edge_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_194_mean_reversion_edge_zscore_252d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _zscore_rolling(base, 252)

def raut_195_mean_reversion_edge_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_195_mean_reversion_edge_rank_252d
    ECONOMIC RATIONALE: Short-term mean reversion signal.
    """
    base = close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0
    return _rank_pct(base, 252)

def raut_196_autocorr_stability_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_196_autocorr_stability_lvl_5d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 5)

def raut_197_autocorr_stability_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_197_autocorr_stability_zscore_5d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 5)

def raut_198_autocorr_stability_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_198_autocorr_stability_rank_5d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 5)

def raut_199_autocorr_stability_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_199_autocorr_stability_lvl_21d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 21)

def raut_200_autocorr_stability_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_200_autocorr_stability_zscore_21d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 21)

def raut_201_autocorr_stability_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_201_autocorr_stability_rank_21d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 21)

def raut_202_autocorr_stability_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_202_autocorr_stability_lvl_63d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 63)

def raut_203_autocorr_stability_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_203_autocorr_stability_zscore_63d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 63)

def raut_204_autocorr_stability_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_204_autocorr_stability_rank_63d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 63)

def raut_205_autocorr_stability_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_205_autocorr_stability_lvl_126d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 126)

def raut_206_autocorr_stability_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_206_autocorr_stability_zscore_126d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 126)

def raut_207_autocorr_stability_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_207_autocorr_stability_rank_126d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 126)

def raut_208_autocorr_stability_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_208_autocorr_stability_lvl_252d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 252)

def raut_209_autocorr_stability_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_209_autocorr_stability_zscore_252d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 252)

def raut_210_autocorr_stability_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_210_autocorr_stability_rank_252d
    ECONOMIC RATIONALE: Stability of the return persistence regime.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 252)

def raut_211_autocorr_acceleration_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_211_autocorr_acceleration_lvl_5d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 5)

def raut_212_autocorr_acceleration_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_212_autocorr_acceleration_zscore_5d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 5)

def raut_213_autocorr_acceleration_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_213_autocorr_acceleration_rank_5d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 5)

def raut_214_autocorr_acceleration_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_214_autocorr_acceleration_lvl_21d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 21)

def raut_215_autocorr_acceleration_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_215_autocorr_acceleration_zscore_21d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 21)

def raut_216_autocorr_acceleration_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_216_autocorr_acceleration_rank_21d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 21)

def raut_217_autocorr_acceleration_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_217_autocorr_acceleration_lvl_63d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 63)

def raut_218_autocorr_acceleration_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_218_autocorr_acceleration_zscore_63d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 63)

def raut_219_autocorr_acceleration_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_219_autocorr_acceleration_rank_63d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 63)

def raut_220_autocorr_acceleration_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_220_autocorr_acceleration_lvl_126d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 126)

def raut_221_autocorr_acceleration_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_221_autocorr_acceleration_zscore_126d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 126)

def raut_222_autocorr_acceleration_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_222_autocorr_acceleration_rank_126d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 126)

def raut_223_autocorr_acceleration_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_223_autocorr_acceleration_lvl_252d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 252)

def raut_224_autocorr_acceleration_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_224_autocorr_acceleration_zscore_252d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 252)

def raut_225_autocorr_acceleration_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_225_autocorr_acceleration_rank_252d
    ECONOMIC RATIONALE: Short-term change in return persistence.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V109_REGISTRY_2 = {
    "raut_121_autocorr_breakdown_lvl_5d": {"inputs": ["close"], "func": raut_121_autocorr_breakdown_lvl_5d},
    "raut_122_autocorr_breakdown_zscore_5d": {"inputs": ["close"], "func": raut_122_autocorr_breakdown_zscore_5d},
    "raut_123_autocorr_breakdown_rank_5d": {"inputs": ["close"], "func": raut_123_autocorr_breakdown_rank_5d},
    "raut_124_autocorr_breakdown_lvl_21d": {"inputs": ["close"], "func": raut_124_autocorr_breakdown_lvl_21d},
    "raut_125_autocorr_breakdown_zscore_21d": {"inputs": ["close"], "func": raut_125_autocorr_breakdown_zscore_21d},
    "raut_126_autocorr_breakdown_rank_21d": {"inputs": ["close"], "func": raut_126_autocorr_breakdown_rank_21d},
    "raut_127_autocorr_breakdown_lvl_63d": {"inputs": ["close"], "func": raut_127_autocorr_breakdown_lvl_63d},
    "raut_128_autocorr_breakdown_zscore_63d": {"inputs": ["close"], "func": raut_128_autocorr_breakdown_zscore_63d},
    "raut_129_autocorr_breakdown_rank_63d": {"inputs": ["close"], "func": raut_129_autocorr_breakdown_rank_63d},
    "raut_130_autocorr_breakdown_lvl_126d": {"inputs": ["close"], "func": raut_130_autocorr_breakdown_lvl_126d},
    "raut_131_autocorr_breakdown_zscore_126d": {"inputs": ["close"], "func": raut_131_autocorr_breakdown_zscore_126d},
    "raut_132_autocorr_breakdown_rank_126d": {"inputs": ["close"], "func": raut_132_autocorr_breakdown_rank_126d},
    "raut_133_autocorr_breakdown_lvl_252d": {"inputs": ["close"], "func": raut_133_autocorr_breakdown_lvl_252d},
    "raut_134_autocorr_breakdown_zscore_252d": {"inputs": ["close"], "func": raut_134_autocorr_breakdown_zscore_252d},
    "raut_135_autocorr_breakdown_rank_252d": {"inputs": ["close"], "func": raut_135_autocorr_breakdown_rank_252d},
    "raut_136_return_clustering_lvl_5d": {"inputs": ["close"], "func": raut_136_return_clustering_lvl_5d},
    "raut_137_return_clustering_zscore_5d": {"inputs": ["close"], "func": raut_137_return_clustering_zscore_5d},
    "raut_138_return_clustering_rank_5d": {"inputs": ["close"], "func": raut_138_return_clustering_rank_5d},
    "raut_139_return_clustering_lvl_21d": {"inputs": ["close"], "func": raut_139_return_clustering_lvl_21d},
    "raut_140_return_clustering_zscore_21d": {"inputs": ["close"], "func": raut_140_return_clustering_zscore_21d},
    "raut_141_return_clustering_rank_21d": {"inputs": ["close"], "func": raut_141_return_clustering_rank_21d},
    "raut_142_return_clustering_lvl_63d": {"inputs": ["close"], "func": raut_142_return_clustering_lvl_63d},
    "raut_143_return_clustering_zscore_63d": {"inputs": ["close"], "func": raut_143_return_clustering_zscore_63d},
    "raut_144_return_clustering_rank_63d": {"inputs": ["close"], "func": raut_144_return_clustering_rank_63d},
    "raut_145_return_clustering_lvl_126d": {"inputs": ["close"], "func": raut_145_return_clustering_lvl_126d},
    "raut_146_return_clustering_zscore_126d": {"inputs": ["close"], "func": raut_146_return_clustering_zscore_126d},
    "raut_147_return_clustering_rank_126d": {"inputs": ["close"], "func": raut_147_return_clustering_rank_126d},
    "raut_148_return_clustering_lvl_252d": {"inputs": ["close"], "func": raut_148_return_clustering_lvl_252d},
    "raut_149_return_clustering_zscore_252d": {"inputs": ["close"], "func": raut_149_return_clustering_zscore_252d},
    "raut_150_return_clustering_rank_252d": {"inputs": ["close"], "func": raut_150_return_clustering_rank_252d},
    "raut_151_autocorr_regime_rank_lvl_5d": {"inputs": ["close"], "func": raut_151_autocorr_regime_rank_lvl_5d},
    "raut_152_autocorr_regime_rank_zscore_5d": {"inputs": ["close"], "func": raut_152_autocorr_regime_rank_zscore_5d},
    "raut_153_autocorr_regime_rank_rank_5d": {"inputs": ["close"], "func": raut_153_autocorr_regime_rank_rank_5d},
    "raut_154_autocorr_regime_rank_lvl_21d": {"inputs": ["close"], "func": raut_154_autocorr_regime_rank_lvl_21d},
    "raut_155_autocorr_regime_rank_zscore_21d": {"inputs": ["close"], "func": raut_155_autocorr_regime_rank_zscore_21d},
    "raut_156_autocorr_regime_rank_rank_21d": {"inputs": ["close"], "func": raut_156_autocorr_regime_rank_rank_21d},
    "raut_157_autocorr_regime_rank_lvl_63d": {"inputs": ["close"], "func": raut_157_autocorr_regime_rank_lvl_63d},
    "raut_158_autocorr_regime_rank_zscore_63d": {"inputs": ["close"], "func": raut_158_autocorr_regime_rank_zscore_63d},
    "raut_159_autocorr_regime_rank_rank_63d": {"inputs": ["close"], "func": raut_159_autocorr_regime_rank_rank_63d},
    "raut_160_autocorr_regime_rank_lvl_126d": {"inputs": ["close"], "func": raut_160_autocorr_regime_rank_lvl_126d},
    "raut_161_autocorr_regime_rank_zscore_126d": {"inputs": ["close"], "func": raut_161_autocorr_regime_rank_zscore_126d},
    "raut_162_autocorr_regime_rank_rank_126d": {"inputs": ["close"], "func": raut_162_autocorr_regime_rank_rank_126d},
    "raut_163_autocorr_regime_rank_lvl_252d": {"inputs": ["close"], "func": raut_163_autocorr_regime_rank_lvl_252d},
    "raut_164_autocorr_regime_rank_zscore_252d": {"inputs": ["close"], "func": raut_164_autocorr_regime_rank_zscore_252d},
    "raut_165_autocorr_regime_rank_rank_252d": {"inputs": ["close"], "func": raut_165_autocorr_regime_rank_rank_252d},
    "raut_166_autocorr_momentum_div_lvl_5d": {"inputs": ["close"], "func": raut_166_autocorr_momentum_div_lvl_5d},
    "raut_167_autocorr_momentum_div_zscore_5d": {"inputs": ["close"], "func": raut_167_autocorr_momentum_div_zscore_5d},
    "raut_168_autocorr_momentum_div_rank_5d": {"inputs": ["close"], "func": raut_168_autocorr_momentum_div_rank_5d},
    "raut_169_autocorr_momentum_div_lvl_21d": {"inputs": ["close"], "func": raut_169_autocorr_momentum_div_lvl_21d},
    "raut_170_autocorr_momentum_div_zscore_21d": {"inputs": ["close"], "func": raut_170_autocorr_momentum_div_zscore_21d},
    "raut_171_autocorr_momentum_div_rank_21d": {"inputs": ["close"], "func": raut_171_autocorr_momentum_div_rank_21d},
    "raut_172_autocorr_momentum_div_lvl_63d": {"inputs": ["close"], "func": raut_172_autocorr_momentum_div_lvl_63d},
    "raut_173_autocorr_momentum_div_zscore_63d": {"inputs": ["close"], "func": raut_173_autocorr_momentum_div_zscore_63d},
    "raut_174_autocorr_momentum_div_rank_63d": {"inputs": ["close"], "func": raut_174_autocorr_momentum_div_rank_63d},
    "raut_175_autocorr_momentum_div_lvl_126d": {"inputs": ["close"], "func": raut_175_autocorr_momentum_div_lvl_126d},
    "raut_176_autocorr_momentum_div_zscore_126d": {"inputs": ["close"], "func": raut_176_autocorr_momentum_div_zscore_126d},
    "raut_177_autocorr_momentum_div_rank_126d": {"inputs": ["close"], "func": raut_177_autocorr_momentum_div_rank_126d},
    "raut_178_autocorr_momentum_div_lvl_252d": {"inputs": ["close"], "func": raut_178_autocorr_momentum_div_lvl_252d},
    "raut_179_autocorr_momentum_div_zscore_252d": {"inputs": ["close"], "func": raut_179_autocorr_momentum_div_zscore_252d},
    "raut_180_autocorr_momentum_div_rank_252d": {"inputs": ["close"], "func": raut_180_autocorr_momentum_div_rank_252d},
    "raut_181_mean_reversion_edge_lvl_5d": {"inputs": ["close"], "func": raut_181_mean_reversion_edge_lvl_5d},
    "raut_182_mean_reversion_edge_zscore_5d": {"inputs": ["close"], "func": raut_182_mean_reversion_edge_zscore_5d},
    "raut_183_mean_reversion_edge_rank_5d": {"inputs": ["close"], "func": raut_183_mean_reversion_edge_rank_5d},
    "raut_184_mean_reversion_edge_lvl_21d": {"inputs": ["close"], "func": raut_184_mean_reversion_edge_lvl_21d},
    "raut_185_mean_reversion_edge_zscore_21d": {"inputs": ["close"], "func": raut_185_mean_reversion_edge_zscore_21d},
    "raut_186_mean_reversion_edge_rank_21d": {"inputs": ["close"], "func": raut_186_mean_reversion_edge_rank_21d},
    "raut_187_mean_reversion_edge_lvl_63d": {"inputs": ["close"], "func": raut_187_mean_reversion_edge_lvl_63d},
    "raut_188_mean_reversion_edge_zscore_63d": {"inputs": ["close"], "func": raut_188_mean_reversion_edge_zscore_63d},
    "raut_189_mean_reversion_edge_rank_63d": {"inputs": ["close"], "func": raut_189_mean_reversion_edge_rank_63d},
    "raut_190_mean_reversion_edge_lvl_126d": {"inputs": ["close"], "func": raut_190_mean_reversion_edge_lvl_126d},
    "raut_191_mean_reversion_edge_zscore_126d": {"inputs": ["close"], "func": raut_191_mean_reversion_edge_zscore_126d},
    "raut_192_mean_reversion_edge_rank_126d": {"inputs": ["close"], "func": raut_192_mean_reversion_edge_rank_126d},
    "raut_193_mean_reversion_edge_lvl_252d": {"inputs": ["close"], "func": raut_193_mean_reversion_edge_lvl_252d},
    "raut_194_mean_reversion_edge_zscore_252d": {"inputs": ["close"], "func": raut_194_mean_reversion_edge_zscore_252d},
    "raut_195_mean_reversion_edge_rank_252d": {"inputs": ["close"], "func": raut_195_mean_reversion_edge_rank_252d},
    "raut_196_autocorr_stability_lvl_5d": {"inputs": ["close"], "func": raut_196_autocorr_stability_lvl_5d},
    "raut_197_autocorr_stability_zscore_5d": {"inputs": ["close"], "func": raut_197_autocorr_stability_zscore_5d},
    "raut_198_autocorr_stability_rank_5d": {"inputs": ["close"], "func": raut_198_autocorr_stability_rank_5d},
    "raut_199_autocorr_stability_lvl_21d": {"inputs": ["close"], "func": raut_199_autocorr_stability_lvl_21d},
    "raut_200_autocorr_stability_zscore_21d": {"inputs": ["close"], "func": raut_200_autocorr_stability_zscore_21d},
    "raut_201_autocorr_stability_rank_21d": {"inputs": ["close"], "func": raut_201_autocorr_stability_rank_21d},
    "raut_202_autocorr_stability_lvl_63d": {"inputs": ["close"], "func": raut_202_autocorr_stability_lvl_63d},
    "raut_203_autocorr_stability_zscore_63d": {"inputs": ["close"], "func": raut_203_autocorr_stability_zscore_63d},
    "raut_204_autocorr_stability_rank_63d": {"inputs": ["close"], "func": raut_204_autocorr_stability_rank_63d},
    "raut_205_autocorr_stability_lvl_126d": {"inputs": ["close"], "func": raut_205_autocorr_stability_lvl_126d},
    "raut_206_autocorr_stability_zscore_126d": {"inputs": ["close"], "func": raut_206_autocorr_stability_zscore_126d},
    "raut_207_autocorr_stability_rank_126d": {"inputs": ["close"], "func": raut_207_autocorr_stability_rank_126d},
    "raut_208_autocorr_stability_lvl_252d": {"inputs": ["close"], "func": raut_208_autocorr_stability_lvl_252d},
    "raut_209_autocorr_stability_zscore_252d": {"inputs": ["close"], "func": raut_209_autocorr_stability_zscore_252d},
    "raut_210_autocorr_stability_rank_252d": {"inputs": ["close"], "func": raut_210_autocorr_stability_rank_252d},
    "raut_211_autocorr_acceleration_lvl_5d": {"inputs": ["close"], "func": raut_211_autocorr_acceleration_lvl_5d},
    "raut_212_autocorr_acceleration_zscore_5d": {"inputs": ["close"], "func": raut_212_autocorr_acceleration_zscore_5d},
    "raut_213_autocorr_acceleration_rank_5d": {"inputs": ["close"], "func": raut_213_autocorr_acceleration_rank_5d},
    "raut_214_autocorr_acceleration_lvl_21d": {"inputs": ["close"], "func": raut_214_autocorr_acceleration_lvl_21d},
    "raut_215_autocorr_acceleration_zscore_21d": {"inputs": ["close"], "func": raut_215_autocorr_acceleration_zscore_21d},
    "raut_216_autocorr_acceleration_rank_21d": {"inputs": ["close"], "func": raut_216_autocorr_acceleration_rank_21d},
    "raut_217_autocorr_acceleration_lvl_63d": {"inputs": ["close"], "func": raut_217_autocorr_acceleration_lvl_63d},
    "raut_218_autocorr_acceleration_zscore_63d": {"inputs": ["close"], "func": raut_218_autocorr_acceleration_zscore_63d},
    "raut_219_autocorr_acceleration_rank_63d": {"inputs": ["close"], "func": raut_219_autocorr_acceleration_rank_63d},
    "raut_220_autocorr_acceleration_lvl_126d": {"inputs": ["close"], "func": raut_220_autocorr_acceleration_lvl_126d},
    "raut_221_autocorr_acceleration_zscore_126d": {"inputs": ["close"], "func": raut_221_autocorr_acceleration_zscore_126d},
    "raut_222_autocorr_acceleration_rank_126d": {"inputs": ["close"], "func": raut_222_autocorr_acceleration_rank_126d},
    "raut_223_autocorr_acceleration_lvl_252d": {"inputs": ["close"], "func": raut_223_autocorr_acceleration_lvl_252d},
    "raut_224_autocorr_acceleration_zscore_252d": {"inputs": ["close"], "func": raut_224_autocorr_acceleration_zscore_252d},
    "raut_225_autocorr_acceleration_rank_252d": {"inputs": ["close"], "func": raut_225_autocorr_acceleration_rank_252d},
}
