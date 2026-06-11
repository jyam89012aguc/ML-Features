"""
119_volume_shock_aftermath — Base Features Part 2
Domain: volume_shock_aftermath
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

def vsha_121_shock_clustering_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_121_shock_clustering_lvl_5d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rolling_mean(base, 5)

def vsha_122_shock_clustering_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_122_shock_clustering_zscore_5d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _zscore_rolling(base, 5)

def vsha_123_shock_clustering_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_123_shock_clustering_rank_5d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rank_pct(base, 5)

def vsha_124_shock_clustering_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_124_shock_clustering_lvl_21d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rolling_mean(base, 21)

def vsha_125_shock_clustering_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_125_shock_clustering_zscore_21d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _zscore_rolling(base, 21)

def vsha_126_shock_clustering_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_126_shock_clustering_rank_21d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rank_pct(base, 21)

def vsha_127_shock_clustering_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_127_shock_clustering_lvl_63d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rolling_mean(base, 63)

def vsha_128_shock_clustering_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_128_shock_clustering_zscore_63d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _zscore_rolling(base, 63)

def vsha_129_shock_clustering_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_129_shock_clustering_rank_63d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rank_pct(base, 63)

def vsha_130_shock_clustering_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_130_shock_clustering_lvl_126d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rolling_mean(base, 126)

def vsha_131_shock_clustering_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_131_shock_clustering_zscore_126d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _zscore_rolling(base, 126)

def vsha_132_shock_clustering_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_132_shock_clustering_rank_126d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rank_pct(base, 126)

def vsha_133_shock_clustering_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_133_shock_clustering_lvl_252d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rolling_mean(base, 252)

def vsha_134_shock_clustering_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_134_shock_clustering_zscore_252d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _zscore_rolling(base, 252)

def vsha_135_shock_clustering_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_135_shock_clustering_rank_252d
    ECONOMIC RATIONALE: Frequency of volume shocks in the last quarter.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(63).sum()
    return _rank_pct(base, 252)

def vsha_136_volume_shock_entropy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_136_volume_shock_entropy_lvl_5d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 5)

def vsha_137_volume_shock_entropy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_137_volume_shock_entropy_zscore_5d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 5)

def vsha_138_volume_shock_entropy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_138_volume_shock_entropy_rank_5d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 5)

def vsha_139_volume_shock_entropy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_139_volume_shock_entropy_lvl_21d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 21)

def vsha_140_volume_shock_entropy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_140_volume_shock_entropy_zscore_21d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 21)

def vsha_141_volume_shock_entropy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_141_volume_shock_entropy_rank_21d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 21)

def vsha_142_volume_shock_entropy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_142_volume_shock_entropy_lvl_63d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 63)

def vsha_143_volume_shock_entropy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_143_volume_shock_entropy_zscore_63d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 63)

def vsha_144_volume_shock_entropy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_144_volume_shock_entropy_rank_63d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 63)

def vsha_145_volume_shock_entropy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_145_volume_shock_entropy_lvl_126d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 126)

def vsha_146_volume_shock_entropy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_146_volume_shock_entropy_zscore_126d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 126)

def vsha_147_volume_shock_entropy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_147_volume_shock_entropy_rank_126d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 126)

def vsha_148_volume_shock_entropy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_148_volume_shock_entropy_lvl_252d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 252)

def vsha_149_volume_shock_entropy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_149_volume_shock_entropy_zscore_252d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 252)

def vsha_150_volume_shock_entropy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_150_volume_shock_entropy_rank_252d
    ECONOMIC RATIONALE: Unpredictability of volume during shocks.
    """
    base = volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 252)

def vsha_151_shock_exhaustion_proxy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_151_shock_exhaustion_proxy_lvl_5d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rolling_mean(base, 5)

def vsha_152_shock_exhaustion_proxy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_152_shock_exhaustion_proxy_zscore_5d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _zscore_rolling(base, 5)

def vsha_153_shock_exhaustion_proxy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_153_shock_exhaustion_proxy_rank_5d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rank_pct(base, 5)

def vsha_154_shock_exhaustion_proxy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_154_shock_exhaustion_proxy_lvl_21d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rolling_mean(base, 21)

def vsha_155_shock_exhaustion_proxy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_155_shock_exhaustion_proxy_zscore_21d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _zscore_rolling(base, 21)

def vsha_156_shock_exhaustion_proxy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_156_shock_exhaustion_proxy_rank_21d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rank_pct(base, 21)

def vsha_157_shock_exhaustion_proxy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_157_shock_exhaustion_proxy_lvl_63d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rolling_mean(base, 63)

def vsha_158_shock_exhaustion_proxy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_158_shock_exhaustion_proxy_zscore_63d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _zscore_rolling(base, 63)

def vsha_159_shock_exhaustion_proxy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_159_shock_exhaustion_proxy_rank_63d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rank_pct(base, 63)

def vsha_160_shock_exhaustion_proxy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_160_shock_exhaustion_proxy_lvl_126d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rolling_mean(base, 126)

def vsha_161_shock_exhaustion_proxy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_161_shock_exhaustion_proxy_zscore_126d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _zscore_rolling(base, 126)

def vsha_162_shock_exhaustion_proxy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_162_shock_exhaustion_proxy_rank_126d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rank_pct(base, 126)

def vsha_163_shock_exhaustion_proxy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_163_shock_exhaustion_proxy_lvl_252d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rolling_mean(base, 252)

def vsha_164_shock_exhaustion_proxy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_164_shock_exhaustion_proxy_zscore_252d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _zscore_rolling(base, 252)

def vsha_165_shock_exhaustion_proxy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_165_shock_exhaustion_proxy_rank_252d
    ECONOMIC RATIONALE: Large volume shock with minimal price impact.
    """
    base = (volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)
    return _rank_pct(base, 252)

def vsha_166_shock_recovery_rate_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_166_shock_recovery_rate_lvl_5d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rolling_mean(base, 5)

def vsha_167_shock_recovery_rate_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_167_shock_recovery_rate_zscore_5d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _zscore_rolling(base, 5)

def vsha_168_shock_recovery_rate_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_168_shock_recovery_rate_rank_5d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rank_pct(base, 5)

def vsha_169_shock_recovery_rate_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_169_shock_recovery_rate_lvl_21d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rolling_mean(base, 21)

def vsha_170_shock_recovery_rate_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_170_shock_recovery_rate_zscore_21d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _zscore_rolling(base, 21)

def vsha_171_shock_recovery_rate_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_171_shock_recovery_rate_rank_21d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rank_pct(base, 21)

def vsha_172_shock_recovery_rate_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_172_shock_recovery_rate_lvl_63d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rolling_mean(base, 63)

def vsha_173_shock_recovery_rate_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_173_shock_recovery_rate_zscore_63d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _zscore_rolling(base, 63)

def vsha_174_shock_recovery_rate_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_174_shock_recovery_rate_rank_63d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rank_pct(base, 63)

def vsha_175_shock_recovery_rate_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_175_shock_recovery_rate_lvl_126d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rolling_mean(base, 126)

def vsha_176_shock_recovery_rate_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_176_shock_recovery_rate_zscore_126d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _zscore_rolling(base, 126)

def vsha_177_shock_recovery_rate_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_177_shock_recovery_rate_rank_126d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rank_pct(base, 126)

def vsha_178_shock_recovery_rate_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_178_shock_recovery_rate_lvl_252d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rolling_mean(base, 252)

def vsha_179_shock_recovery_rate_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_179_shock_recovery_rate_zscore_252d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _zscore_rolling(base, 252)

def vsha_180_shock_recovery_rate_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_180_shock_recovery_rate_rank_252d
    ECONOMIC RATIONALE: Recovery relative to the price at the last volume peak.
    """
    base = close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))
    return _rank_pct(base, 252)

def vsha_181_volume_shock_momentum_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_181_volume_shock_momentum_lvl_5d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rolling_mean(base, 5)

def vsha_182_volume_shock_momentum_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_182_volume_shock_momentum_zscore_5d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _zscore_rolling(base, 5)

def vsha_183_volume_shock_momentum_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_183_volume_shock_momentum_rank_5d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rank_pct(base, 5)

def vsha_184_volume_shock_momentum_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_184_volume_shock_momentum_lvl_21d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rolling_mean(base, 21)

def vsha_185_volume_shock_momentum_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_185_volume_shock_momentum_zscore_21d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _zscore_rolling(base, 21)

def vsha_186_volume_shock_momentum_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_186_volume_shock_momentum_rank_21d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rank_pct(base, 21)

def vsha_187_volume_shock_momentum_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_187_volume_shock_momentum_lvl_63d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rolling_mean(base, 63)

def vsha_188_volume_shock_momentum_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_188_volume_shock_momentum_zscore_63d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _zscore_rolling(base, 63)

def vsha_189_volume_shock_momentum_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_189_volume_shock_momentum_rank_63d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rank_pct(base, 63)

def vsha_190_volume_shock_momentum_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_190_volume_shock_momentum_lvl_126d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rolling_mean(base, 126)

def vsha_191_volume_shock_momentum_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_191_volume_shock_momentum_zscore_126d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _zscore_rolling(base, 126)

def vsha_192_volume_shock_momentum_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_192_volume_shock_momentum_rank_126d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rank_pct(base, 126)

def vsha_193_volume_shock_momentum_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_193_volume_shock_momentum_lvl_252d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rolling_mean(base, 252)

def vsha_194_volume_shock_momentum_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_194_volume_shock_momentum_zscore_252d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _zscore_rolling(base, 252)

def vsha_195_volume_shock_momentum_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_195_volume_shock_momentum_rank_252d
    ECONOMIC RATIONALE: Synchronized volume and price momentum.
    """
    base = volume.pct_change(5) * close.pct_change(5)
    return _rank_pct(base, 252)

def vsha_196_shock_regime_shift_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_196_shock_regime_shift_lvl_5d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rolling_mean(base, 5)

def vsha_197_shock_regime_shift_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_197_shock_regime_shift_zscore_5d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _zscore_rolling(base, 5)

def vsha_198_shock_regime_shift_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_198_shock_regime_shift_rank_5d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rank_pct(base, 5)

def vsha_199_shock_regime_shift_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_199_shock_regime_shift_lvl_21d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rolling_mean(base, 21)

def vsha_200_shock_regime_shift_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_200_shock_regime_shift_zscore_21d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _zscore_rolling(base, 21)

def vsha_201_shock_regime_shift_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_201_shock_regime_shift_rank_21d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rank_pct(base, 21)

def vsha_202_shock_regime_shift_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_202_shock_regime_shift_lvl_63d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rolling_mean(base, 63)

def vsha_203_shock_regime_shift_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_203_shock_regime_shift_zscore_63d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _zscore_rolling(base, 63)

def vsha_204_shock_regime_shift_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_204_shock_regime_shift_rank_63d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rank_pct(base, 63)

def vsha_205_shock_regime_shift_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_205_shock_regime_shift_lvl_126d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rolling_mean(base, 126)

def vsha_206_shock_regime_shift_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_206_shock_regime_shift_zscore_126d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _zscore_rolling(base, 126)

def vsha_207_shock_regime_shift_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_207_shock_regime_shift_rank_126d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rank_pct(base, 126)

def vsha_208_shock_regime_shift_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_208_shock_regime_shift_lvl_252d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rolling_mean(base, 252)

def vsha_209_shock_regime_shift_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_209_shock_regime_shift_zscore_252d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _zscore_rolling(base, 252)

def vsha_210_shock_regime_shift_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_210_shock_regime_shift_rank_252d
    ECONOMIC RATIONALE: Structural shift in average volume levels.
    """
    base = volume.rolling(21).mean().diff(21) / volume.rolling(252).std()
    return _rank_pct(base, 252)

def vsha_211_volume_shock_tail_corr_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_211_volume_shock_tail_corr_lvl_5d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rolling_mean(base, 5)

def vsha_212_volume_shock_tail_corr_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_212_volume_shock_tail_corr_zscore_5d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _zscore_rolling(base, 5)

def vsha_213_volume_shock_tail_corr_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_213_volume_shock_tail_corr_rank_5d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rank_pct(base, 5)

def vsha_214_volume_shock_tail_corr_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_214_volume_shock_tail_corr_lvl_21d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rolling_mean(base, 21)

def vsha_215_volume_shock_tail_corr_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_215_volume_shock_tail_corr_zscore_21d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _zscore_rolling(base, 21)

def vsha_216_volume_shock_tail_corr_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_216_volume_shock_tail_corr_rank_21d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rank_pct(base, 21)

def vsha_217_volume_shock_tail_corr_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_217_volume_shock_tail_corr_lvl_63d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rolling_mean(base, 63)

def vsha_218_volume_shock_tail_corr_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_218_volume_shock_tail_corr_zscore_63d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _zscore_rolling(base, 63)

def vsha_219_volume_shock_tail_corr_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_219_volume_shock_tail_corr_rank_63d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rank_pct(base, 63)

def vsha_220_volume_shock_tail_corr_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_220_volume_shock_tail_corr_lvl_126d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rolling_mean(base, 126)

def vsha_221_volume_shock_tail_corr_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_221_volume_shock_tail_corr_zscore_126d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _zscore_rolling(base, 126)

def vsha_222_volume_shock_tail_corr_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_222_volume_shock_tail_corr_rank_126d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rank_pct(base, 126)

def vsha_223_volume_shock_tail_corr_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_223_volume_shock_tail_corr_lvl_252d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rolling_mean(base, 252)

def vsha_224_volume_shock_tail_corr_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_224_volume_shock_tail_corr_zscore_252d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _zscore_rolling(base, 252)

def vsha_225_volume_shock_tail_corr_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_225_volume_shock_tail_corr_rank_252d
    ECONOMIC RATIONALE: Correlation between volume shocks and price magnitude.
    """
    base = volume.rolling(21).corr(close.pct_change(1).abs())
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V119_REGISTRY_2 = {
    "vsha_121_shock_clustering_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_121_shock_clustering_lvl_5d},
    "vsha_122_shock_clustering_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_122_shock_clustering_zscore_5d},
    "vsha_123_shock_clustering_rank_5d": {"inputs": ["close", "volume"], "func": vsha_123_shock_clustering_rank_5d},
    "vsha_124_shock_clustering_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_124_shock_clustering_lvl_21d},
    "vsha_125_shock_clustering_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_125_shock_clustering_zscore_21d},
    "vsha_126_shock_clustering_rank_21d": {"inputs": ["close", "volume"], "func": vsha_126_shock_clustering_rank_21d},
    "vsha_127_shock_clustering_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_127_shock_clustering_lvl_63d},
    "vsha_128_shock_clustering_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_128_shock_clustering_zscore_63d},
    "vsha_129_shock_clustering_rank_63d": {"inputs": ["close", "volume"], "func": vsha_129_shock_clustering_rank_63d},
    "vsha_130_shock_clustering_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_130_shock_clustering_lvl_126d},
    "vsha_131_shock_clustering_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_131_shock_clustering_zscore_126d},
    "vsha_132_shock_clustering_rank_126d": {"inputs": ["close", "volume"], "func": vsha_132_shock_clustering_rank_126d},
    "vsha_133_shock_clustering_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_133_shock_clustering_lvl_252d},
    "vsha_134_shock_clustering_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_134_shock_clustering_zscore_252d},
    "vsha_135_shock_clustering_rank_252d": {"inputs": ["close", "volume"], "func": vsha_135_shock_clustering_rank_252d},
    "vsha_136_volume_shock_entropy_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_136_volume_shock_entropy_lvl_5d},
    "vsha_137_volume_shock_entropy_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_137_volume_shock_entropy_zscore_5d},
    "vsha_138_volume_shock_entropy_rank_5d": {"inputs": ["close", "volume"], "func": vsha_138_volume_shock_entropy_rank_5d},
    "vsha_139_volume_shock_entropy_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_139_volume_shock_entropy_lvl_21d},
    "vsha_140_volume_shock_entropy_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_140_volume_shock_entropy_zscore_21d},
    "vsha_141_volume_shock_entropy_rank_21d": {"inputs": ["close", "volume"], "func": vsha_141_volume_shock_entropy_rank_21d},
    "vsha_142_volume_shock_entropy_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_142_volume_shock_entropy_lvl_63d},
    "vsha_143_volume_shock_entropy_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_143_volume_shock_entropy_zscore_63d},
    "vsha_144_volume_shock_entropy_rank_63d": {"inputs": ["close", "volume"], "func": vsha_144_volume_shock_entropy_rank_63d},
    "vsha_145_volume_shock_entropy_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_145_volume_shock_entropy_lvl_126d},
    "vsha_146_volume_shock_entropy_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_146_volume_shock_entropy_zscore_126d},
    "vsha_147_volume_shock_entropy_rank_126d": {"inputs": ["close", "volume"], "func": vsha_147_volume_shock_entropy_rank_126d},
    "vsha_148_volume_shock_entropy_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_148_volume_shock_entropy_lvl_252d},
    "vsha_149_volume_shock_entropy_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_149_volume_shock_entropy_zscore_252d},
    "vsha_150_volume_shock_entropy_rank_252d": {"inputs": ["close", "volume"], "func": vsha_150_volume_shock_entropy_rank_252d},
    "vsha_151_shock_exhaustion_proxy_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_151_shock_exhaustion_proxy_lvl_5d},
    "vsha_152_shock_exhaustion_proxy_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_152_shock_exhaustion_proxy_zscore_5d},
    "vsha_153_shock_exhaustion_proxy_rank_5d": {"inputs": ["close", "volume"], "func": vsha_153_shock_exhaustion_proxy_rank_5d},
    "vsha_154_shock_exhaustion_proxy_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_154_shock_exhaustion_proxy_lvl_21d},
    "vsha_155_shock_exhaustion_proxy_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_155_shock_exhaustion_proxy_zscore_21d},
    "vsha_156_shock_exhaustion_proxy_rank_21d": {"inputs": ["close", "volume"], "func": vsha_156_shock_exhaustion_proxy_rank_21d},
    "vsha_157_shock_exhaustion_proxy_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_157_shock_exhaustion_proxy_lvl_63d},
    "vsha_158_shock_exhaustion_proxy_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_158_shock_exhaustion_proxy_zscore_63d},
    "vsha_159_shock_exhaustion_proxy_rank_63d": {"inputs": ["close", "volume"], "func": vsha_159_shock_exhaustion_proxy_rank_63d},
    "vsha_160_shock_exhaustion_proxy_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_160_shock_exhaustion_proxy_lvl_126d},
    "vsha_161_shock_exhaustion_proxy_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_161_shock_exhaustion_proxy_zscore_126d},
    "vsha_162_shock_exhaustion_proxy_rank_126d": {"inputs": ["close", "volume"], "func": vsha_162_shock_exhaustion_proxy_rank_126d},
    "vsha_163_shock_exhaustion_proxy_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_163_shock_exhaustion_proxy_lvl_252d},
    "vsha_164_shock_exhaustion_proxy_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_164_shock_exhaustion_proxy_zscore_252d},
    "vsha_165_shock_exhaustion_proxy_rank_252d": {"inputs": ["close", "volume"], "func": vsha_165_shock_exhaustion_proxy_rank_252d},
    "vsha_166_shock_recovery_rate_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_166_shock_recovery_rate_lvl_5d},
    "vsha_167_shock_recovery_rate_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_167_shock_recovery_rate_zscore_5d},
    "vsha_168_shock_recovery_rate_rank_5d": {"inputs": ["close", "volume"], "func": vsha_168_shock_recovery_rate_rank_5d},
    "vsha_169_shock_recovery_rate_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_169_shock_recovery_rate_lvl_21d},
    "vsha_170_shock_recovery_rate_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_170_shock_recovery_rate_zscore_21d},
    "vsha_171_shock_recovery_rate_rank_21d": {"inputs": ["close", "volume"], "func": vsha_171_shock_recovery_rate_rank_21d},
    "vsha_172_shock_recovery_rate_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_172_shock_recovery_rate_lvl_63d},
    "vsha_173_shock_recovery_rate_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_173_shock_recovery_rate_zscore_63d},
    "vsha_174_shock_recovery_rate_rank_63d": {"inputs": ["close", "volume"], "func": vsha_174_shock_recovery_rate_rank_63d},
    "vsha_175_shock_recovery_rate_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_175_shock_recovery_rate_lvl_126d},
    "vsha_176_shock_recovery_rate_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_176_shock_recovery_rate_zscore_126d},
    "vsha_177_shock_recovery_rate_rank_126d": {"inputs": ["close", "volume"], "func": vsha_177_shock_recovery_rate_rank_126d},
    "vsha_178_shock_recovery_rate_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_178_shock_recovery_rate_lvl_252d},
    "vsha_179_shock_recovery_rate_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_179_shock_recovery_rate_zscore_252d},
    "vsha_180_shock_recovery_rate_rank_252d": {"inputs": ["close", "volume"], "func": vsha_180_shock_recovery_rate_rank_252d},
    "vsha_181_volume_shock_momentum_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_181_volume_shock_momentum_lvl_5d},
    "vsha_182_volume_shock_momentum_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_182_volume_shock_momentum_zscore_5d},
    "vsha_183_volume_shock_momentum_rank_5d": {"inputs": ["close", "volume"], "func": vsha_183_volume_shock_momentum_rank_5d},
    "vsha_184_volume_shock_momentum_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_184_volume_shock_momentum_lvl_21d},
    "vsha_185_volume_shock_momentum_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_185_volume_shock_momentum_zscore_21d},
    "vsha_186_volume_shock_momentum_rank_21d": {"inputs": ["close", "volume"], "func": vsha_186_volume_shock_momentum_rank_21d},
    "vsha_187_volume_shock_momentum_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_187_volume_shock_momentum_lvl_63d},
    "vsha_188_volume_shock_momentum_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_188_volume_shock_momentum_zscore_63d},
    "vsha_189_volume_shock_momentum_rank_63d": {"inputs": ["close", "volume"], "func": vsha_189_volume_shock_momentum_rank_63d},
    "vsha_190_volume_shock_momentum_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_190_volume_shock_momentum_lvl_126d},
    "vsha_191_volume_shock_momentum_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_191_volume_shock_momentum_zscore_126d},
    "vsha_192_volume_shock_momentum_rank_126d": {"inputs": ["close", "volume"], "func": vsha_192_volume_shock_momentum_rank_126d},
    "vsha_193_volume_shock_momentum_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_193_volume_shock_momentum_lvl_252d},
    "vsha_194_volume_shock_momentum_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_194_volume_shock_momentum_zscore_252d},
    "vsha_195_volume_shock_momentum_rank_252d": {"inputs": ["close", "volume"], "func": vsha_195_volume_shock_momentum_rank_252d},
    "vsha_196_shock_regime_shift_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_196_shock_regime_shift_lvl_5d},
    "vsha_197_shock_regime_shift_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_197_shock_regime_shift_zscore_5d},
    "vsha_198_shock_regime_shift_rank_5d": {"inputs": ["close", "volume"], "func": vsha_198_shock_regime_shift_rank_5d},
    "vsha_199_shock_regime_shift_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_199_shock_regime_shift_lvl_21d},
    "vsha_200_shock_regime_shift_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_200_shock_regime_shift_zscore_21d},
    "vsha_201_shock_regime_shift_rank_21d": {"inputs": ["close", "volume"], "func": vsha_201_shock_regime_shift_rank_21d},
    "vsha_202_shock_regime_shift_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_202_shock_regime_shift_lvl_63d},
    "vsha_203_shock_regime_shift_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_203_shock_regime_shift_zscore_63d},
    "vsha_204_shock_regime_shift_rank_63d": {"inputs": ["close", "volume"], "func": vsha_204_shock_regime_shift_rank_63d},
    "vsha_205_shock_regime_shift_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_205_shock_regime_shift_lvl_126d},
    "vsha_206_shock_regime_shift_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_206_shock_regime_shift_zscore_126d},
    "vsha_207_shock_regime_shift_rank_126d": {"inputs": ["close", "volume"], "func": vsha_207_shock_regime_shift_rank_126d},
    "vsha_208_shock_regime_shift_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_208_shock_regime_shift_lvl_252d},
    "vsha_209_shock_regime_shift_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_209_shock_regime_shift_zscore_252d},
    "vsha_210_shock_regime_shift_rank_252d": {"inputs": ["close", "volume"], "func": vsha_210_shock_regime_shift_rank_252d},
    "vsha_211_volume_shock_tail_corr_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_211_volume_shock_tail_corr_lvl_5d},
    "vsha_212_volume_shock_tail_corr_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_212_volume_shock_tail_corr_zscore_5d},
    "vsha_213_volume_shock_tail_corr_rank_5d": {"inputs": ["close", "volume"], "func": vsha_213_volume_shock_tail_corr_rank_5d},
    "vsha_214_volume_shock_tail_corr_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_214_volume_shock_tail_corr_lvl_21d},
    "vsha_215_volume_shock_tail_corr_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_215_volume_shock_tail_corr_zscore_21d},
    "vsha_216_volume_shock_tail_corr_rank_21d": {"inputs": ["close", "volume"], "func": vsha_216_volume_shock_tail_corr_rank_21d},
    "vsha_217_volume_shock_tail_corr_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_217_volume_shock_tail_corr_lvl_63d},
    "vsha_218_volume_shock_tail_corr_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_218_volume_shock_tail_corr_zscore_63d},
    "vsha_219_volume_shock_tail_corr_rank_63d": {"inputs": ["close", "volume"], "func": vsha_219_volume_shock_tail_corr_rank_63d},
    "vsha_220_volume_shock_tail_corr_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_220_volume_shock_tail_corr_lvl_126d},
    "vsha_221_volume_shock_tail_corr_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_221_volume_shock_tail_corr_zscore_126d},
    "vsha_222_volume_shock_tail_corr_rank_126d": {"inputs": ["close", "volume"], "func": vsha_222_volume_shock_tail_corr_rank_126d},
    "vsha_223_volume_shock_tail_corr_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_223_volume_shock_tail_corr_lvl_252d},
    "vsha_224_volume_shock_tail_corr_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_224_volume_shock_tail_corr_zscore_252d},
    "vsha_225_volume_shock_tail_corr_rank_252d": {"inputs": ["close", "volume"], "func": vsha_225_volume_shock_tail_corr_rank_252d},
}
