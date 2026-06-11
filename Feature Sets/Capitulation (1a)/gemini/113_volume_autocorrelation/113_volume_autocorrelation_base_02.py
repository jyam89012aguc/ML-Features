"""
113_volume_autocorrelation — Base Features Part 2
Domain: volume_autocorrelation
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

def vaut_121_vol_trend_persistence_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_121_vol_trend_persistence_lvl_5d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rolling_mean(base, 5)

def vaut_122_vol_trend_persistence_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_122_vol_trend_persistence_zscore_5d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _zscore_rolling(base, 5)

def vaut_123_vol_trend_persistence_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_123_vol_trend_persistence_rank_5d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rank_pct(base, 5)

def vaut_124_vol_trend_persistence_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_124_vol_trend_persistence_lvl_21d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rolling_mean(base, 21)

def vaut_125_vol_trend_persistence_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_125_vol_trend_persistence_zscore_21d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _zscore_rolling(base, 21)

def vaut_126_vol_trend_persistence_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_126_vol_trend_persistence_rank_21d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rank_pct(base, 21)

def vaut_127_vol_trend_persistence_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_127_vol_trend_persistence_lvl_63d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rolling_mean(base, 63)

def vaut_128_vol_trend_persistence_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_128_vol_trend_persistence_zscore_63d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _zscore_rolling(base, 63)

def vaut_129_vol_trend_persistence_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_129_vol_trend_persistence_rank_63d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rank_pct(base, 63)

def vaut_130_vol_trend_persistence_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_130_vol_trend_persistence_lvl_126d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rolling_mean(base, 126)

def vaut_131_vol_trend_persistence_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_131_vol_trend_persistence_zscore_126d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _zscore_rolling(base, 126)

def vaut_132_vol_trend_persistence_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_132_vol_trend_persistence_rank_126d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rank_pct(base, 126)

def vaut_133_vol_trend_persistence_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_133_vol_trend_persistence_lvl_252d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rolling_mean(base, 252)

def vaut_134_vol_trend_persistence_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_134_vol_trend_persistence_zscore_252d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _zscore_rolling(base, 252)

def vaut_135_vol_trend_persistence_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_135_vol_trend_persistence_rank_252d
    ECONOMIC RATIONALE: Volume trending regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)
    return _rank_pct(base, 252)

def vaut_136_vol_autocorr_vs_price_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_136_vol_autocorr_vs_price_lvl_5d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rolling_mean(base, 5)

def vaut_137_vol_autocorr_vs_price_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_137_vol_autocorr_vs_price_zscore_5d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _zscore_rolling(base, 5)

def vaut_138_vol_autocorr_vs_price_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_138_vol_autocorr_vs_price_rank_5d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rank_pct(base, 5)

def vaut_139_vol_autocorr_vs_price_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_139_vol_autocorr_vs_price_lvl_21d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rolling_mean(base, 21)

def vaut_140_vol_autocorr_vs_price_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_140_vol_autocorr_vs_price_zscore_21d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _zscore_rolling(base, 21)

def vaut_141_vol_autocorr_vs_price_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_141_vol_autocorr_vs_price_rank_21d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rank_pct(base, 21)

def vaut_142_vol_autocorr_vs_price_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_142_vol_autocorr_vs_price_lvl_63d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rolling_mean(base, 63)

def vaut_143_vol_autocorr_vs_price_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_143_vol_autocorr_vs_price_zscore_63d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _zscore_rolling(base, 63)

def vaut_144_vol_autocorr_vs_price_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_144_vol_autocorr_vs_price_rank_63d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rank_pct(base, 63)

def vaut_145_vol_autocorr_vs_price_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_145_vol_autocorr_vs_price_lvl_126d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rolling_mean(base, 126)

def vaut_146_vol_autocorr_vs_price_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_146_vol_autocorr_vs_price_zscore_126d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _zscore_rolling(base, 126)

def vaut_147_vol_autocorr_vs_price_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_147_vol_autocorr_vs_price_rank_126d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rank_pct(base, 126)

def vaut_148_vol_autocorr_vs_price_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_148_vol_autocorr_vs_price_lvl_252d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rolling_mean(base, 252)

def vaut_149_vol_autocorr_vs_price_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_149_vol_autocorr_vs_price_zscore_252d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _zscore_rolling(base, 252)

def vaut_150_vol_autocorr_vs_price_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_150_vol_autocorr_vs_price_rank_252d
    ECONOMIC RATIONALE: Relationship between volume persistence and price direction.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))
    return _rank_pct(base, 252)

def vaut_151_vol_autocorr_peak_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_151_vol_autocorr_peak_lvl_5d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rolling_mean(base, 5)

def vaut_152_vol_autocorr_peak_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_152_vol_autocorr_peak_zscore_5d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _zscore_rolling(base, 5)

def vaut_153_vol_autocorr_peak_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_153_vol_autocorr_peak_rank_5d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rank_pct(base, 5)

def vaut_154_vol_autocorr_peak_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_154_vol_autocorr_peak_lvl_21d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rolling_mean(base, 21)

def vaut_155_vol_autocorr_peak_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_155_vol_autocorr_peak_zscore_21d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _zscore_rolling(base, 21)

def vaut_156_vol_autocorr_peak_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_156_vol_autocorr_peak_rank_21d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rank_pct(base, 21)

def vaut_157_vol_autocorr_peak_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_157_vol_autocorr_peak_lvl_63d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rolling_mean(base, 63)

def vaut_158_vol_autocorr_peak_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_158_vol_autocorr_peak_zscore_63d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _zscore_rolling(base, 63)

def vaut_159_vol_autocorr_peak_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_159_vol_autocorr_peak_rank_63d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rank_pct(base, 63)

def vaut_160_vol_autocorr_peak_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_160_vol_autocorr_peak_lvl_126d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rolling_mean(base, 126)

def vaut_161_vol_autocorr_peak_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_161_vol_autocorr_peak_zscore_126d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _zscore_rolling(base, 126)

def vaut_162_vol_autocorr_peak_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_162_vol_autocorr_peak_rank_126d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rank_pct(base, 126)

def vaut_163_vol_autocorr_peak_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_163_vol_autocorr_peak_lvl_252d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rolling_mean(base, 252)

def vaut_164_vol_autocorr_peak_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_164_vol_autocorr_peak_zscore_252d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _zscore_rolling(base, 252)

def vaut_165_vol_autocorr_peak_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_165_vol_autocorr_peak_rank_252d
    ECONOMIC RATIONALE: Maximum volume persistence in the last quarter.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()
    return _rank_pct(base, 252)

def vaut_166_vol_autocorr_entropy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_166_vol_autocorr_entropy_lvl_5d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rolling_mean(base, 5)

def vaut_167_vol_autocorr_entropy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_167_vol_autocorr_entropy_zscore_5d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _zscore_rolling(base, 5)

def vaut_168_vol_autocorr_entropy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_168_vol_autocorr_entropy_rank_5d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rank_pct(base, 5)

def vaut_169_vol_autocorr_entropy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_169_vol_autocorr_entropy_lvl_21d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rolling_mean(base, 21)

def vaut_170_vol_autocorr_entropy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_170_vol_autocorr_entropy_zscore_21d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _zscore_rolling(base, 21)

def vaut_171_vol_autocorr_entropy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_171_vol_autocorr_entropy_rank_21d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rank_pct(base, 21)

def vaut_172_vol_autocorr_entropy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_172_vol_autocorr_entropy_lvl_63d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rolling_mean(base, 63)

def vaut_173_vol_autocorr_entropy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_173_vol_autocorr_entropy_zscore_63d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _zscore_rolling(base, 63)

def vaut_174_vol_autocorr_entropy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_174_vol_autocorr_entropy_rank_63d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rank_pct(base, 63)

def vaut_175_vol_autocorr_entropy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_175_vol_autocorr_entropy_lvl_126d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rolling_mean(base, 126)

def vaut_176_vol_autocorr_entropy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_176_vol_autocorr_entropy_zscore_126d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _zscore_rolling(base, 126)

def vaut_177_vol_autocorr_entropy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_177_vol_autocorr_entropy_rank_126d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rank_pct(base, 126)

def vaut_178_vol_autocorr_entropy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_178_vol_autocorr_entropy_lvl_252d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rolling_mean(base, 252)

def vaut_179_vol_autocorr_entropy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_179_vol_autocorr_entropy_zscore_252d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _zscore_rolling(base, 252)

def vaut_180_vol_autocorr_entropy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_180_vol_autocorr_entropy_rank_252d
    ECONOMIC RATIONALE: Unpredictability of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))
    return _rank_pct(base, 252)

def vaut_181_vol_autocorr_regime_switch_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_181_vol_autocorr_regime_switch_lvl_5d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rolling_mean(base, 5)

def vaut_182_vol_autocorr_regime_switch_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_182_vol_autocorr_regime_switch_zscore_5d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _zscore_rolling(base, 5)

def vaut_183_vol_autocorr_regime_switch_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_183_vol_autocorr_regime_switch_rank_5d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rank_pct(base, 5)

def vaut_184_vol_autocorr_regime_switch_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_184_vol_autocorr_regime_switch_lvl_21d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rolling_mean(base, 21)

def vaut_185_vol_autocorr_regime_switch_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_185_vol_autocorr_regime_switch_zscore_21d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _zscore_rolling(base, 21)

def vaut_186_vol_autocorr_regime_switch_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_186_vol_autocorr_regime_switch_rank_21d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rank_pct(base, 21)

def vaut_187_vol_autocorr_regime_switch_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_187_vol_autocorr_regime_switch_lvl_63d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rolling_mean(base, 63)

def vaut_188_vol_autocorr_regime_switch_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_188_vol_autocorr_regime_switch_zscore_63d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _zscore_rolling(base, 63)

def vaut_189_vol_autocorr_regime_switch_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_189_vol_autocorr_regime_switch_rank_63d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rank_pct(base, 63)

def vaut_190_vol_autocorr_regime_switch_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_190_vol_autocorr_regime_switch_lvl_126d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rolling_mean(base, 126)

def vaut_191_vol_autocorr_regime_switch_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_191_vol_autocorr_regime_switch_zscore_126d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _zscore_rolling(base, 126)

def vaut_192_vol_autocorr_regime_switch_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_192_vol_autocorr_regime_switch_rank_126d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rank_pct(base, 126)

def vaut_193_vol_autocorr_regime_switch_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_193_vol_autocorr_regime_switch_lvl_252d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rolling_mean(base, 252)

def vaut_194_vol_autocorr_regime_switch_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_194_vol_autocorr_regime_switch_zscore_252d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _zscore_rolling(base, 252)

def vaut_195_vol_autocorr_regime_switch_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_195_vol_autocorr_regime_switch_rank_252d
    ECONOMIC RATIONALE: Sudden switch in volume behavior.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)
    return _rank_pct(base, 252)

def vaut_196_vol_autocorr_ma_spread_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_196_vol_autocorr_ma_spread_lvl_5d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 5)

def vaut_197_vol_autocorr_ma_spread_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_197_vol_autocorr_ma_spread_zscore_5d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 5)

def vaut_198_vol_autocorr_ma_spread_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_198_vol_autocorr_ma_spread_rank_5d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 5)

def vaut_199_vol_autocorr_ma_spread_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_199_vol_autocorr_ma_spread_lvl_21d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 21)

def vaut_200_vol_autocorr_ma_spread_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_200_vol_autocorr_ma_spread_zscore_21d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 21)

def vaut_201_vol_autocorr_ma_spread_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_201_vol_autocorr_ma_spread_rank_21d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 21)

def vaut_202_vol_autocorr_ma_spread_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_202_vol_autocorr_ma_spread_lvl_63d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 63)

def vaut_203_vol_autocorr_ma_spread_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_203_vol_autocorr_ma_spread_zscore_63d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 63)

def vaut_204_vol_autocorr_ma_spread_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_204_vol_autocorr_ma_spread_rank_63d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 63)

def vaut_205_vol_autocorr_ma_spread_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_205_vol_autocorr_ma_spread_lvl_126d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 126)

def vaut_206_vol_autocorr_ma_spread_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_206_vol_autocorr_ma_spread_zscore_126d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 126)

def vaut_207_vol_autocorr_ma_spread_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_207_vol_autocorr_ma_spread_rank_126d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 126)

def vaut_208_vol_autocorr_ma_spread_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_208_vol_autocorr_ma_spread_lvl_252d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 252)

def vaut_209_vol_autocorr_ma_spread_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_209_vol_autocorr_ma_spread_zscore_252d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 252)

def vaut_210_vol_autocorr_ma_spread_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_210_vol_autocorr_ma_spread_rank_252d
    ECONOMIC RATIONALE: Spread between short and long term volume persistence.
    """
    base = volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 252)

def vaut_211_vol_autocorr_low_liquidity_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_211_vol_autocorr_low_liquidity_lvl_5d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rolling_mean(base, 5)

def vaut_212_vol_autocorr_low_liquidity_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_212_vol_autocorr_low_liquidity_zscore_5d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _zscore_rolling(base, 5)

def vaut_213_vol_autocorr_low_liquidity_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_213_vol_autocorr_low_liquidity_rank_5d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rank_pct(base, 5)

def vaut_214_vol_autocorr_low_liquidity_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_214_vol_autocorr_low_liquidity_lvl_21d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rolling_mean(base, 21)

def vaut_215_vol_autocorr_low_liquidity_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_215_vol_autocorr_low_liquidity_zscore_21d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _zscore_rolling(base, 21)

def vaut_216_vol_autocorr_low_liquidity_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_216_vol_autocorr_low_liquidity_rank_21d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rank_pct(base, 21)

def vaut_217_vol_autocorr_low_liquidity_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_217_vol_autocorr_low_liquidity_lvl_63d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rolling_mean(base, 63)

def vaut_218_vol_autocorr_low_liquidity_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_218_vol_autocorr_low_liquidity_zscore_63d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _zscore_rolling(base, 63)

def vaut_219_vol_autocorr_low_liquidity_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_219_vol_autocorr_low_liquidity_rank_63d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rank_pct(base, 63)

def vaut_220_vol_autocorr_low_liquidity_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_220_vol_autocorr_low_liquidity_lvl_126d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rolling_mean(base, 126)

def vaut_221_vol_autocorr_low_liquidity_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_221_vol_autocorr_low_liquidity_zscore_126d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _zscore_rolling(base, 126)

def vaut_222_vol_autocorr_low_liquidity_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_222_vol_autocorr_low_liquidity_rank_126d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rank_pct(base, 126)

def vaut_223_vol_autocorr_low_liquidity_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_223_vol_autocorr_low_liquidity_lvl_252d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rolling_mean(base, 252)

def vaut_224_vol_autocorr_low_liquidity_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_224_vol_autocorr_low_liquidity_zscore_252d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _zscore_rolling(base, 252)

def vaut_225_vol_autocorr_low_liquidity_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_225_vol_autocorr_low_liquidity_rank_252d
    ECONOMIC RATIONALE: Persistence during low volume periods.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V113_REGISTRY_2 = {
    "vaut_121_vol_trend_persistence_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_121_vol_trend_persistence_lvl_5d},
    "vaut_122_vol_trend_persistence_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_122_vol_trend_persistence_zscore_5d},
    "vaut_123_vol_trend_persistence_rank_5d": {"inputs": ["close", "volume"], "func": vaut_123_vol_trend_persistence_rank_5d},
    "vaut_124_vol_trend_persistence_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_124_vol_trend_persistence_lvl_21d},
    "vaut_125_vol_trend_persistence_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_125_vol_trend_persistence_zscore_21d},
    "vaut_126_vol_trend_persistence_rank_21d": {"inputs": ["close", "volume"], "func": vaut_126_vol_trend_persistence_rank_21d},
    "vaut_127_vol_trend_persistence_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_127_vol_trend_persistence_lvl_63d},
    "vaut_128_vol_trend_persistence_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_128_vol_trend_persistence_zscore_63d},
    "vaut_129_vol_trend_persistence_rank_63d": {"inputs": ["close", "volume"], "func": vaut_129_vol_trend_persistence_rank_63d},
    "vaut_130_vol_trend_persistence_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_130_vol_trend_persistence_lvl_126d},
    "vaut_131_vol_trend_persistence_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_131_vol_trend_persistence_zscore_126d},
    "vaut_132_vol_trend_persistence_rank_126d": {"inputs": ["close", "volume"], "func": vaut_132_vol_trend_persistence_rank_126d},
    "vaut_133_vol_trend_persistence_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_133_vol_trend_persistence_lvl_252d},
    "vaut_134_vol_trend_persistence_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_134_vol_trend_persistence_zscore_252d},
    "vaut_135_vol_trend_persistence_rank_252d": {"inputs": ["close", "volume"], "func": vaut_135_vol_trend_persistence_rank_252d},
    "vaut_136_vol_autocorr_vs_price_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_136_vol_autocorr_vs_price_lvl_5d},
    "vaut_137_vol_autocorr_vs_price_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_137_vol_autocorr_vs_price_zscore_5d},
    "vaut_138_vol_autocorr_vs_price_rank_5d": {"inputs": ["close", "volume"], "func": vaut_138_vol_autocorr_vs_price_rank_5d},
    "vaut_139_vol_autocorr_vs_price_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_139_vol_autocorr_vs_price_lvl_21d},
    "vaut_140_vol_autocorr_vs_price_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_140_vol_autocorr_vs_price_zscore_21d},
    "vaut_141_vol_autocorr_vs_price_rank_21d": {"inputs": ["close", "volume"], "func": vaut_141_vol_autocorr_vs_price_rank_21d},
    "vaut_142_vol_autocorr_vs_price_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_142_vol_autocorr_vs_price_lvl_63d},
    "vaut_143_vol_autocorr_vs_price_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_143_vol_autocorr_vs_price_zscore_63d},
    "vaut_144_vol_autocorr_vs_price_rank_63d": {"inputs": ["close", "volume"], "func": vaut_144_vol_autocorr_vs_price_rank_63d},
    "vaut_145_vol_autocorr_vs_price_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_145_vol_autocorr_vs_price_lvl_126d},
    "vaut_146_vol_autocorr_vs_price_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_146_vol_autocorr_vs_price_zscore_126d},
    "vaut_147_vol_autocorr_vs_price_rank_126d": {"inputs": ["close", "volume"], "func": vaut_147_vol_autocorr_vs_price_rank_126d},
    "vaut_148_vol_autocorr_vs_price_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_148_vol_autocorr_vs_price_lvl_252d},
    "vaut_149_vol_autocorr_vs_price_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_149_vol_autocorr_vs_price_zscore_252d},
    "vaut_150_vol_autocorr_vs_price_rank_252d": {"inputs": ["close", "volume"], "func": vaut_150_vol_autocorr_vs_price_rank_252d},
    "vaut_151_vol_autocorr_peak_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_151_vol_autocorr_peak_lvl_5d},
    "vaut_152_vol_autocorr_peak_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_152_vol_autocorr_peak_zscore_5d},
    "vaut_153_vol_autocorr_peak_rank_5d": {"inputs": ["close", "volume"], "func": vaut_153_vol_autocorr_peak_rank_5d},
    "vaut_154_vol_autocorr_peak_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_154_vol_autocorr_peak_lvl_21d},
    "vaut_155_vol_autocorr_peak_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_155_vol_autocorr_peak_zscore_21d},
    "vaut_156_vol_autocorr_peak_rank_21d": {"inputs": ["close", "volume"], "func": vaut_156_vol_autocorr_peak_rank_21d},
    "vaut_157_vol_autocorr_peak_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_157_vol_autocorr_peak_lvl_63d},
    "vaut_158_vol_autocorr_peak_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_158_vol_autocorr_peak_zscore_63d},
    "vaut_159_vol_autocorr_peak_rank_63d": {"inputs": ["close", "volume"], "func": vaut_159_vol_autocorr_peak_rank_63d},
    "vaut_160_vol_autocorr_peak_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_160_vol_autocorr_peak_lvl_126d},
    "vaut_161_vol_autocorr_peak_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_161_vol_autocorr_peak_zscore_126d},
    "vaut_162_vol_autocorr_peak_rank_126d": {"inputs": ["close", "volume"], "func": vaut_162_vol_autocorr_peak_rank_126d},
    "vaut_163_vol_autocorr_peak_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_163_vol_autocorr_peak_lvl_252d},
    "vaut_164_vol_autocorr_peak_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_164_vol_autocorr_peak_zscore_252d},
    "vaut_165_vol_autocorr_peak_rank_252d": {"inputs": ["close", "volume"], "func": vaut_165_vol_autocorr_peak_rank_252d},
    "vaut_166_vol_autocorr_entropy_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_166_vol_autocorr_entropy_lvl_5d},
    "vaut_167_vol_autocorr_entropy_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_167_vol_autocorr_entropy_zscore_5d},
    "vaut_168_vol_autocorr_entropy_rank_5d": {"inputs": ["close", "volume"], "func": vaut_168_vol_autocorr_entropy_rank_5d},
    "vaut_169_vol_autocorr_entropy_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_169_vol_autocorr_entropy_lvl_21d},
    "vaut_170_vol_autocorr_entropy_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_170_vol_autocorr_entropy_zscore_21d},
    "vaut_171_vol_autocorr_entropy_rank_21d": {"inputs": ["close", "volume"], "func": vaut_171_vol_autocorr_entropy_rank_21d},
    "vaut_172_vol_autocorr_entropy_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_172_vol_autocorr_entropy_lvl_63d},
    "vaut_173_vol_autocorr_entropy_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_173_vol_autocorr_entropy_zscore_63d},
    "vaut_174_vol_autocorr_entropy_rank_63d": {"inputs": ["close", "volume"], "func": vaut_174_vol_autocorr_entropy_rank_63d},
    "vaut_175_vol_autocorr_entropy_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_175_vol_autocorr_entropy_lvl_126d},
    "vaut_176_vol_autocorr_entropy_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_176_vol_autocorr_entropy_zscore_126d},
    "vaut_177_vol_autocorr_entropy_rank_126d": {"inputs": ["close", "volume"], "func": vaut_177_vol_autocorr_entropy_rank_126d},
    "vaut_178_vol_autocorr_entropy_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_178_vol_autocorr_entropy_lvl_252d},
    "vaut_179_vol_autocorr_entropy_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_179_vol_autocorr_entropy_zscore_252d},
    "vaut_180_vol_autocorr_entropy_rank_252d": {"inputs": ["close", "volume"], "func": vaut_180_vol_autocorr_entropy_rank_252d},
    "vaut_181_vol_autocorr_regime_switch_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_181_vol_autocorr_regime_switch_lvl_5d},
    "vaut_182_vol_autocorr_regime_switch_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_182_vol_autocorr_regime_switch_zscore_5d},
    "vaut_183_vol_autocorr_regime_switch_rank_5d": {"inputs": ["close", "volume"], "func": vaut_183_vol_autocorr_regime_switch_rank_5d},
    "vaut_184_vol_autocorr_regime_switch_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_184_vol_autocorr_regime_switch_lvl_21d},
    "vaut_185_vol_autocorr_regime_switch_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_185_vol_autocorr_regime_switch_zscore_21d},
    "vaut_186_vol_autocorr_regime_switch_rank_21d": {"inputs": ["close", "volume"], "func": vaut_186_vol_autocorr_regime_switch_rank_21d},
    "vaut_187_vol_autocorr_regime_switch_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_187_vol_autocorr_regime_switch_lvl_63d},
    "vaut_188_vol_autocorr_regime_switch_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_188_vol_autocorr_regime_switch_zscore_63d},
    "vaut_189_vol_autocorr_regime_switch_rank_63d": {"inputs": ["close", "volume"], "func": vaut_189_vol_autocorr_regime_switch_rank_63d},
    "vaut_190_vol_autocorr_regime_switch_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_190_vol_autocorr_regime_switch_lvl_126d},
    "vaut_191_vol_autocorr_regime_switch_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_191_vol_autocorr_regime_switch_zscore_126d},
    "vaut_192_vol_autocorr_regime_switch_rank_126d": {"inputs": ["close", "volume"], "func": vaut_192_vol_autocorr_regime_switch_rank_126d},
    "vaut_193_vol_autocorr_regime_switch_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_193_vol_autocorr_regime_switch_lvl_252d},
    "vaut_194_vol_autocorr_regime_switch_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_194_vol_autocorr_regime_switch_zscore_252d},
    "vaut_195_vol_autocorr_regime_switch_rank_252d": {"inputs": ["close", "volume"], "func": vaut_195_vol_autocorr_regime_switch_rank_252d},
    "vaut_196_vol_autocorr_ma_spread_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_196_vol_autocorr_ma_spread_lvl_5d},
    "vaut_197_vol_autocorr_ma_spread_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_197_vol_autocorr_ma_spread_zscore_5d},
    "vaut_198_vol_autocorr_ma_spread_rank_5d": {"inputs": ["close", "volume"], "func": vaut_198_vol_autocorr_ma_spread_rank_5d},
    "vaut_199_vol_autocorr_ma_spread_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_199_vol_autocorr_ma_spread_lvl_21d},
    "vaut_200_vol_autocorr_ma_spread_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_200_vol_autocorr_ma_spread_zscore_21d},
    "vaut_201_vol_autocorr_ma_spread_rank_21d": {"inputs": ["close", "volume"], "func": vaut_201_vol_autocorr_ma_spread_rank_21d},
    "vaut_202_vol_autocorr_ma_spread_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_202_vol_autocorr_ma_spread_lvl_63d},
    "vaut_203_vol_autocorr_ma_spread_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_203_vol_autocorr_ma_spread_zscore_63d},
    "vaut_204_vol_autocorr_ma_spread_rank_63d": {"inputs": ["close", "volume"], "func": vaut_204_vol_autocorr_ma_spread_rank_63d},
    "vaut_205_vol_autocorr_ma_spread_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_205_vol_autocorr_ma_spread_lvl_126d},
    "vaut_206_vol_autocorr_ma_spread_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_206_vol_autocorr_ma_spread_zscore_126d},
    "vaut_207_vol_autocorr_ma_spread_rank_126d": {"inputs": ["close", "volume"], "func": vaut_207_vol_autocorr_ma_spread_rank_126d},
    "vaut_208_vol_autocorr_ma_spread_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_208_vol_autocorr_ma_spread_lvl_252d},
    "vaut_209_vol_autocorr_ma_spread_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_209_vol_autocorr_ma_spread_zscore_252d},
    "vaut_210_vol_autocorr_ma_spread_rank_252d": {"inputs": ["close", "volume"], "func": vaut_210_vol_autocorr_ma_spread_rank_252d},
    "vaut_211_vol_autocorr_low_liquidity_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_211_vol_autocorr_low_liquidity_lvl_5d},
    "vaut_212_vol_autocorr_low_liquidity_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_212_vol_autocorr_low_liquidity_zscore_5d},
    "vaut_213_vol_autocorr_low_liquidity_rank_5d": {"inputs": ["close", "volume"], "func": vaut_213_vol_autocorr_low_liquidity_rank_5d},
    "vaut_214_vol_autocorr_low_liquidity_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_214_vol_autocorr_low_liquidity_lvl_21d},
    "vaut_215_vol_autocorr_low_liquidity_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_215_vol_autocorr_low_liquidity_zscore_21d},
    "vaut_216_vol_autocorr_low_liquidity_rank_21d": {"inputs": ["close", "volume"], "func": vaut_216_vol_autocorr_low_liquidity_rank_21d},
    "vaut_217_vol_autocorr_low_liquidity_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_217_vol_autocorr_low_liquidity_lvl_63d},
    "vaut_218_vol_autocorr_low_liquidity_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_218_vol_autocorr_low_liquidity_zscore_63d},
    "vaut_219_vol_autocorr_low_liquidity_rank_63d": {"inputs": ["close", "volume"], "func": vaut_219_vol_autocorr_low_liquidity_rank_63d},
    "vaut_220_vol_autocorr_low_liquidity_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_220_vol_autocorr_low_liquidity_lvl_126d},
    "vaut_221_vol_autocorr_low_liquidity_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_221_vol_autocorr_low_liquidity_zscore_126d},
    "vaut_222_vol_autocorr_low_liquidity_rank_126d": {"inputs": ["close", "volume"], "func": vaut_222_vol_autocorr_low_liquidity_rank_126d},
    "vaut_223_vol_autocorr_low_liquidity_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_223_vol_autocorr_low_liquidity_lvl_252d},
    "vaut_224_vol_autocorr_low_liquidity_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_224_vol_autocorr_low_liquidity_zscore_252d},
    "vaut_225_vol_autocorr_low_liquidity_rank_252d": {"inputs": ["close", "volume"], "func": vaut_225_vol_autocorr_low_liquidity_rank_252d},
}
