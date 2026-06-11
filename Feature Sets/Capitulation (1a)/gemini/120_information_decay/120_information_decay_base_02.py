"""
120_information_decay — Base Features Part 2
Domain: information_decay
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

def idec_121_memory_length_proxy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_121_memory_length_proxy_lvl_5d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rolling_mean(base, 5)

def idec_122_memory_length_proxy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_122_memory_length_proxy_zscore_5d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _zscore_rolling(base, 5)

def idec_123_memory_length_proxy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_123_memory_length_proxy_rank_5d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rank_pct(base, 5)

def idec_124_memory_length_proxy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_124_memory_length_proxy_lvl_21d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rolling_mean(base, 21)

def idec_125_memory_length_proxy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_125_memory_length_proxy_zscore_21d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _zscore_rolling(base, 21)

def idec_126_memory_length_proxy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_126_memory_length_proxy_rank_21d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rank_pct(base, 21)

def idec_127_memory_length_proxy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_127_memory_length_proxy_lvl_63d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rolling_mean(base, 63)

def idec_128_memory_length_proxy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_128_memory_length_proxy_zscore_63d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _zscore_rolling(base, 63)

def idec_129_memory_length_proxy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_129_memory_length_proxy_rank_63d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rank_pct(base, 63)

def idec_130_memory_length_proxy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_130_memory_length_proxy_lvl_126d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rolling_mean(base, 126)

def idec_131_memory_length_proxy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_131_memory_length_proxy_zscore_126d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _zscore_rolling(base, 126)

def idec_132_memory_length_proxy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_132_memory_length_proxy_rank_126d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rank_pct(base, 126)

def idec_133_memory_length_proxy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_133_memory_length_proxy_lvl_252d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rolling_mean(base, 252)

def idec_134_memory_length_proxy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_134_memory_length_proxy_zscore_252d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _zscore_rolling(base, 252)

def idec_135_memory_length_proxy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_135_memory_length_proxy_rank_252d
    ECONOMIC RATIONALE: Estimated length of price memory.
    """
    base = close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))
    return _rank_pct(base, 252)

def idec_136_information_shock_persistence_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_136_information_shock_persistence_lvl_5d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 5)

def idec_137_information_shock_persistence_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_137_information_shock_persistence_zscore_5d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 5)

def idec_138_information_shock_persistence_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_138_information_shock_persistence_rank_5d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 5)

def idec_139_information_shock_persistence_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_139_information_shock_persistence_lvl_21d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 21)

def idec_140_information_shock_persistence_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_140_information_shock_persistence_zscore_21d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 21)

def idec_141_information_shock_persistence_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_141_information_shock_persistence_rank_21d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 21)

def idec_142_information_shock_persistence_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_142_information_shock_persistence_lvl_63d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 63)

def idec_143_information_shock_persistence_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_143_information_shock_persistence_zscore_63d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 63)

def idec_144_information_shock_persistence_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_144_information_shock_persistence_rank_63d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 63)

def idec_145_information_shock_persistence_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_145_information_shock_persistence_lvl_126d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 126)

def idec_146_information_shock_persistence_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_146_information_shock_persistence_zscore_126d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 126)

def idec_147_information_shock_persistence_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_147_information_shock_persistence_rank_126d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 126)

def idec_148_information_shock_persistence_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_148_information_shock_persistence_lvl_252d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 252)

def idec_149_information_shock_persistence_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_149_information_shock_persistence_zscore_252d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 252)

def idec_150_information_shock_persistence_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_150_information_shock_persistence_rank_252d
    ECONOMIC RATIONALE: Persistence of information-driven price volatility.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 252)

def idec_151_drift_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_151_drift_decay_lvl_5d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def idec_152_drift_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_152_drift_decay_zscore_5d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def idec_153_drift_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_153_drift_decay_rank_5d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rank_pct(base, 5)

def idec_154_drift_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_154_drift_decay_lvl_21d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def idec_155_drift_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_155_drift_decay_zscore_21d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def idec_156_drift_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_156_drift_decay_rank_21d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rank_pct(base, 21)

def idec_157_drift_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_157_drift_decay_lvl_63d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def idec_158_drift_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_158_drift_decay_zscore_63d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def idec_159_drift_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_159_drift_decay_rank_63d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rank_pct(base, 63)

def idec_160_drift_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_160_drift_decay_lvl_126d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def idec_161_drift_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_161_drift_decay_zscore_126d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def idec_162_drift_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_162_drift_decay_rank_126d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rank_pct(base, 126)

def idec_163_drift_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_163_drift_decay_lvl_252d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def idec_164_drift_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_164_drift_decay_zscore_252d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def idec_165_drift_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_165_drift_decay_rank_252d
    ECONOMIC RATIONALE: Decay of short-term drift relative to quarterly trend.
    """
    base = close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)
    return _rank_pct(base, 252)

def idec_166_information_entropy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_166_information_entropy_lvl_5d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 5)

def idec_167_information_entropy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_167_information_entropy_zscore_5d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 5)

def idec_168_information_entropy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_168_information_entropy_rank_5d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 5)

def idec_169_information_entropy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_169_information_entropy_lvl_21d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 21)

def idec_170_information_entropy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_170_information_entropy_zscore_21d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 21)

def idec_171_information_entropy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_171_information_entropy_rank_21d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 21)

def idec_172_information_entropy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_172_information_entropy_lvl_63d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 63)

def idec_173_information_entropy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_173_information_entropy_zscore_63d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 63)

def idec_174_information_entropy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_174_information_entropy_rank_63d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 63)

def idec_175_information_entropy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_175_information_entropy_lvl_126d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 126)

def idec_176_information_entropy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_176_information_entropy_zscore_126d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 126)

def idec_177_information_entropy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_177_information_entropy_rank_126d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 126)

def idec_178_information_entropy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_178_information_entropy_lvl_252d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 252)

def idec_179_information_entropy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_179_information_entropy_zscore_252d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 252)

def idec_180_information_entropy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_180_information_entropy_rank_252d
    ECONOMIC RATIONALE: Uncertainty or decay of information in price returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 252)

def idec_181_volume_memory_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_181_volume_memory_decay_lvl_5d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rolling_mean(base, 5)

def idec_182_volume_memory_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_182_volume_memory_decay_zscore_5d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _zscore_rolling(base, 5)

def idec_183_volume_memory_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_183_volume_memory_decay_rank_5d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rank_pct(base, 5)

def idec_184_volume_memory_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_184_volume_memory_decay_lvl_21d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rolling_mean(base, 21)

def idec_185_volume_memory_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_185_volume_memory_decay_zscore_21d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _zscore_rolling(base, 21)

def idec_186_volume_memory_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_186_volume_memory_decay_rank_21d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rank_pct(base, 21)

def idec_187_volume_memory_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_187_volume_memory_decay_lvl_63d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rolling_mean(base, 63)

def idec_188_volume_memory_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_188_volume_memory_decay_zscore_63d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _zscore_rolling(base, 63)

def idec_189_volume_memory_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_189_volume_memory_decay_rank_63d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rank_pct(base, 63)

def idec_190_volume_memory_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_190_volume_memory_decay_lvl_126d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rolling_mean(base, 126)

def idec_191_volume_memory_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_191_volume_memory_decay_zscore_126d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _zscore_rolling(base, 126)

def idec_192_volume_memory_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_192_volume_memory_decay_rank_126d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rank_pct(base, 126)

def idec_193_volume_memory_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_193_volume_memory_decay_lvl_252d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rolling_mean(base, 252)

def idec_194_volume_memory_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_194_volume_memory_decay_zscore_252d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _zscore_rolling(base, 252)

def idec_195_volume_memory_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_195_volume_memory_decay_rank_252d
    ECONOMIC RATIONALE: Persistence of volume regimes.
    """
    base = volume.rolling(21).corr(volume.shift(21))
    return _rank_pct(base, 252)

def idec_196_price_stickiness_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_196_price_stickiness_decay_lvl_5d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rolling_mean(base, 5)

def idec_197_price_stickiness_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_197_price_stickiness_decay_zscore_5d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _zscore_rolling(base, 5)

def idec_198_price_stickiness_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_198_price_stickiness_decay_rank_5d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rank_pct(base, 5)

def idec_199_price_stickiness_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_199_price_stickiness_decay_lvl_21d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rolling_mean(base, 21)

def idec_200_price_stickiness_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_200_price_stickiness_decay_zscore_21d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _zscore_rolling(base, 21)

def idec_201_price_stickiness_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_201_price_stickiness_decay_rank_21d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rank_pct(base, 21)

def idec_202_price_stickiness_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_202_price_stickiness_decay_lvl_63d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rolling_mean(base, 63)

def idec_203_price_stickiness_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_203_price_stickiness_decay_zscore_63d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _zscore_rolling(base, 63)

def idec_204_price_stickiness_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_204_price_stickiness_decay_rank_63d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rank_pct(base, 63)

def idec_205_price_stickiness_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_205_price_stickiness_decay_lvl_126d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rolling_mean(base, 126)

def idec_206_price_stickiness_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_206_price_stickiness_decay_zscore_126d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _zscore_rolling(base, 126)

def idec_207_price_stickiness_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_207_price_stickiness_decay_rank_126d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rank_pct(base, 126)

def idec_208_price_stickiness_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_208_price_stickiness_decay_lvl_252d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rolling_mean(base, 252)

def idec_209_price_stickiness_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_209_price_stickiness_decay_zscore_252d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _zscore_rolling(base, 252)

def idec_210_price_stickiness_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_210_price_stickiness_decay_rank_252d
    ECONOMIC RATIONALE: Change in the rate of price stagnation.
    """
    base = (close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)
    return _rank_pct(base, 252)

def idec_211_information_flow_acceleration_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_211_information_flow_acceleration_lvl_5d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rolling_mean(base, 5)

def idec_212_information_flow_acceleration_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_212_information_flow_acceleration_zscore_5d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _zscore_rolling(base, 5)

def idec_213_information_flow_acceleration_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_213_information_flow_acceleration_rank_5d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rank_pct(base, 5)

def idec_214_information_flow_acceleration_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_214_information_flow_acceleration_lvl_21d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rolling_mean(base, 21)

def idec_215_information_flow_acceleration_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_215_information_flow_acceleration_zscore_21d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _zscore_rolling(base, 21)

def idec_216_information_flow_acceleration_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_216_information_flow_acceleration_rank_21d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rank_pct(base, 21)

def idec_217_information_flow_acceleration_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_217_information_flow_acceleration_lvl_63d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rolling_mean(base, 63)

def idec_218_information_flow_acceleration_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_218_information_flow_acceleration_zscore_63d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _zscore_rolling(base, 63)

def idec_219_information_flow_acceleration_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_219_information_flow_acceleration_rank_63d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rank_pct(base, 63)

def idec_220_information_flow_acceleration_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_220_information_flow_acceleration_lvl_126d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rolling_mean(base, 126)

def idec_221_information_flow_acceleration_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_221_information_flow_acceleration_zscore_126d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _zscore_rolling(base, 126)

def idec_222_information_flow_acceleration_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_222_information_flow_acceleration_rank_126d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rank_pct(base, 126)

def idec_223_information_flow_acceleration_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_223_information_flow_acceleration_lvl_252d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rolling_mean(base, 252)

def idec_224_information_flow_acceleration_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_224_information_flow_acceleration_zscore_252d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _zscore_rolling(base, 252)

def idec_225_information_flow_acceleration_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_225_information_flow_acceleration_rank_252d
    ECONOMIC RATIONALE: Acceleration of information flow into price.
    """
    base = close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V120_REGISTRY_2 = {
    "idec_121_memory_length_proxy_lvl_5d": {"inputs": ["close", "volume"], "func": idec_121_memory_length_proxy_lvl_5d},
    "idec_122_memory_length_proxy_zscore_5d": {"inputs": ["close", "volume"], "func": idec_122_memory_length_proxy_zscore_5d},
    "idec_123_memory_length_proxy_rank_5d": {"inputs": ["close", "volume"], "func": idec_123_memory_length_proxy_rank_5d},
    "idec_124_memory_length_proxy_lvl_21d": {"inputs": ["close", "volume"], "func": idec_124_memory_length_proxy_lvl_21d},
    "idec_125_memory_length_proxy_zscore_21d": {"inputs": ["close", "volume"], "func": idec_125_memory_length_proxy_zscore_21d},
    "idec_126_memory_length_proxy_rank_21d": {"inputs": ["close", "volume"], "func": idec_126_memory_length_proxy_rank_21d},
    "idec_127_memory_length_proxy_lvl_63d": {"inputs": ["close", "volume"], "func": idec_127_memory_length_proxy_lvl_63d},
    "idec_128_memory_length_proxy_zscore_63d": {"inputs": ["close", "volume"], "func": idec_128_memory_length_proxy_zscore_63d},
    "idec_129_memory_length_proxy_rank_63d": {"inputs": ["close", "volume"], "func": idec_129_memory_length_proxy_rank_63d},
    "idec_130_memory_length_proxy_lvl_126d": {"inputs": ["close", "volume"], "func": idec_130_memory_length_proxy_lvl_126d},
    "idec_131_memory_length_proxy_zscore_126d": {"inputs": ["close", "volume"], "func": idec_131_memory_length_proxy_zscore_126d},
    "idec_132_memory_length_proxy_rank_126d": {"inputs": ["close", "volume"], "func": idec_132_memory_length_proxy_rank_126d},
    "idec_133_memory_length_proxy_lvl_252d": {"inputs": ["close", "volume"], "func": idec_133_memory_length_proxy_lvl_252d},
    "idec_134_memory_length_proxy_zscore_252d": {"inputs": ["close", "volume"], "func": idec_134_memory_length_proxy_zscore_252d},
    "idec_135_memory_length_proxy_rank_252d": {"inputs": ["close", "volume"], "func": idec_135_memory_length_proxy_rank_252d},
    "idec_136_information_shock_persistence_lvl_5d": {"inputs": ["close", "volume"], "func": idec_136_information_shock_persistence_lvl_5d},
    "idec_137_information_shock_persistence_zscore_5d": {"inputs": ["close", "volume"], "func": idec_137_information_shock_persistence_zscore_5d},
    "idec_138_information_shock_persistence_rank_5d": {"inputs": ["close", "volume"], "func": idec_138_information_shock_persistence_rank_5d},
    "idec_139_information_shock_persistence_lvl_21d": {"inputs": ["close", "volume"], "func": idec_139_information_shock_persistence_lvl_21d},
    "idec_140_information_shock_persistence_zscore_21d": {"inputs": ["close", "volume"], "func": idec_140_information_shock_persistence_zscore_21d},
    "idec_141_information_shock_persistence_rank_21d": {"inputs": ["close", "volume"], "func": idec_141_information_shock_persistence_rank_21d},
    "idec_142_information_shock_persistence_lvl_63d": {"inputs": ["close", "volume"], "func": idec_142_information_shock_persistence_lvl_63d},
    "idec_143_information_shock_persistence_zscore_63d": {"inputs": ["close", "volume"], "func": idec_143_information_shock_persistence_zscore_63d},
    "idec_144_information_shock_persistence_rank_63d": {"inputs": ["close", "volume"], "func": idec_144_information_shock_persistence_rank_63d},
    "idec_145_information_shock_persistence_lvl_126d": {"inputs": ["close", "volume"], "func": idec_145_information_shock_persistence_lvl_126d},
    "idec_146_information_shock_persistence_zscore_126d": {"inputs": ["close", "volume"], "func": idec_146_information_shock_persistence_zscore_126d},
    "idec_147_information_shock_persistence_rank_126d": {"inputs": ["close", "volume"], "func": idec_147_information_shock_persistence_rank_126d},
    "idec_148_information_shock_persistence_lvl_252d": {"inputs": ["close", "volume"], "func": idec_148_information_shock_persistence_lvl_252d},
    "idec_149_information_shock_persistence_zscore_252d": {"inputs": ["close", "volume"], "func": idec_149_information_shock_persistence_zscore_252d},
    "idec_150_information_shock_persistence_rank_252d": {"inputs": ["close", "volume"], "func": idec_150_information_shock_persistence_rank_252d},
    "idec_151_drift_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_151_drift_decay_lvl_5d},
    "idec_152_drift_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_152_drift_decay_zscore_5d},
    "idec_153_drift_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_153_drift_decay_rank_5d},
    "idec_154_drift_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_154_drift_decay_lvl_21d},
    "idec_155_drift_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_155_drift_decay_zscore_21d},
    "idec_156_drift_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_156_drift_decay_rank_21d},
    "idec_157_drift_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_157_drift_decay_lvl_63d},
    "idec_158_drift_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_158_drift_decay_zscore_63d},
    "idec_159_drift_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_159_drift_decay_rank_63d},
    "idec_160_drift_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_160_drift_decay_lvl_126d},
    "idec_161_drift_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_161_drift_decay_zscore_126d},
    "idec_162_drift_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_162_drift_decay_rank_126d},
    "idec_163_drift_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_163_drift_decay_lvl_252d},
    "idec_164_drift_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_164_drift_decay_zscore_252d},
    "idec_165_drift_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_165_drift_decay_rank_252d},
    "idec_166_information_entropy_lvl_5d": {"inputs": ["close", "volume"], "func": idec_166_information_entropy_lvl_5d},
    "idec_167_information_entropy_zscore_5d": {"inputs": ["close", "volume"], "func": idec_167_information_entropy_zscore_5d},
    "idec_168_information_entropy_rank_5d": {"inputs": ["close", "volume"], "func": idec_168_information_entropy_rank_5d},
    "idec_169_information_entropy_lvl_21d": {"inputs": ["close", "volume"], "func": idec_169_information_entropy_lvl_21d},
    "idec_170_information_entropy_zscore_21d": {"inputs": ["close", "volume"], "func": idec_170_information_entropy_zscore_21d},
    "idec_171_information_entropy_rank_21d": {"inputs": ["close", "volume"], "func": idec_171_information_entropy_rank_21d},
    "idec_172_information_entropy_lvl_63d": {"inputs": ["close", "volume"], "func": idec_172_information_entropy_lvl_63d},
    "idec_173_information_entropy_zscore_63d": {"inputs": ["close", "volume"], "func": idec_173_information_entropy_zscore_63d},
    "idec_174_information_entropy_rank_63d": {"inputs": ["close", "volume"], "func": idec_174_information_entropy_rank_63d},
    "idec_175_information_entropy_lvl_126d": {"inputs": ["close", "volume"], "func": idec_175_information_entropy_lvl_126d},
    "idec_176_information_entropy_zscore_126d": {"inputs": ["close", "volume"], "func": idec_176_information_entropy_zscore_126d},
    "idec_177_information_entropy_rank_126d": {"inputs": ["close", "volume"], "func": idec_177_information_entropy_rank_126d},
    "idec_178_information_entropy_lvl_252d": {"inputs": ["close", "volume"], "func": idec_178_information_entropy_lvl_252d},
    "idec_179_information_entropy_zscore_252d": {"inputs": ["close", "volume"], "func": idec_179_information_entropy_zscore_252d},
    "idec_180_information_entropy_rank_252d": {"inputs": ["close", "volume"], "func": idec_180_information_entropy_rank_252d},
    "idec_181_volume_memory_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_181_volume_memory_decay_lvl_5d},
    "idec_182_volume_memory_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_182_volume_memory_decay_zscore_5d},
    "idec_183_volume_memory_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_183_volume_memory_decay_rank_5d},
    "idec_184_volume_memory_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_184_volume_memory_decay_lvl_21d},
    "idec_185_volume_memory_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_185_volume_memory_decay_zscore_21d},
    "idec_186_volume_memory_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_186_volume_memory_decay_rank_21d},
    "idec_187_volume_memory_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_187_volume_memory_decay_lvl_63d},
    "idec_188_volume_memory_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_188_volume_memory_decay_zscore_63d},
    "idec_189_volume_memory_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_189_volume_memory_decay_rank_63d},
    "idec_190_volume_memory_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_190_volume_memory_decay_lvl_126d},
    "idec_191_volume_memory_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_191_volume_memory_decay_zscore_126d},
    "idec_192_volume_memory_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_192_volume_memory_decay_rank_126d},
    "idec_193_volume_memory_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_193_volume_memory_decay_lvl_252d},
    "idec_194_volume_memory_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_194_volume_memory_decay_zscore_252d},
    "idec_195_volume_memory_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_195_volume_memory_decay_rank_252d},
    "idec_196_price_stickiness_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_196_price_stickiness_decay_lvl_5d},
    "idec_197_price_stickiness_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_197_price_stickiness_decay_zscore_5d},
    "idec_198_price_stickiness_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_198_price_stickiness_decay_rank_5d},
    "idec_199_price_stickiness_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_199_price_stickiness_decay_lvl_21d},
    "idec_200_price_stickiness_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_200_price_stickiness_decay_zscore_21d},
    "idec_201_price_stickiness_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_201_price_stickiness_decay_rank_21d},
    "idec_202_price_stickiness_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_202_price_stickiness_decay_lvl_63d},
    "idec_203_price_stickiness_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_203_price_stickiness_decay_zscore_63d},
    "idec_204_price_stickiness_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_204_price_stickiness_decay_rank_63d},
    "idec_205_price_stickiness_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_205_price_stickiness_decay_lvl_126d},
    "idec_206_price_stickiness_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_206_price_stickiness_decay_zscore_126d},
    "idec_207_price_stickiness_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_207_price_stickiness_decay_rank_126d},
    "idec_208_price_stickiness_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_208_price_stickiness_decay_lvl_252d},
    "idec_209_price_stickiness_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_209_price_stickiness_decay_zscore_252d},
    "idec_210_price_stickiness_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_210_price_stickiness_decay_rank_252d},
    "idec_211_information_flow_acceleration_lvl_5d": {"inputs": ["close", "volume"], "func": idec_211_information_flow_acceleration_lvl_5d},
    "idec_212_information_flow_acceleration_zscore_5d": {"inputs": ["close", "volume"], "func": idec_212_information_flow_acceleration_zscore_5d},
    "idec_213_information_flow_acceleration_rank_5d": {"inputs": ["close", "volume"], "func": idec_213_information_flow_acceleration_rank_5d},
    "idec_214_information_flow_acceleration_lvl_21d": {"inputs": ["close", "volume"], "func": idec_214_information_flow_acceleration_lvl_21d},
    "idec_215_information_flow_acceleration_zscore_21d": {"inputs": ["close", "volume"], "func": idec_215_information_flow_acceleration_zscore_21d},
    "idec_216_information_flow_acceleration_rank_21d": {"inputs": ["close", "volume"], "func": idec_216_information_flow_acceleration_rank_21d},
    "idec_217_information_flow_acceleration_lvl_63d": {"inputs": ["close", "volume"], "func": idec_217_information_flow_acceleration_lvl_63d},
    "idec_218_information_flow_acceleration_zscore_63d": {"inputs": ["close", "volume"], "func": idec_218_information_flow_acceleration_zscore_63d},
    "idec_219_information_flow_acceleration_rank_63d": {"inputs": ["close", "volume"], "func": idec_219_information_flow_acceleration_rank_63d},
    "idec_220_information_flow_acceleration_lvl_126d": {"inputs": ["close", "volume"], "func": idec_220_information_flow_acceleration_lvl_126d},
    "idec_221_information_flow_acceleration_zscore_126d": {"inputs": ["close", "volume"], "func": idec_221_information_flow_acceleration_zscore_126d},
    "idec_222_information_flow_acceleration_rank_126d": {"inputs": ["close", "volume"], "func": idec_222_information_flow_acceleration_rank_126d},
    "idec_223_information_flow_acceleration_lvl_252d": {"inputs": ["close", "volume"], "func": idec_223_information_flow_acceleration_lvl_252d},
    "idec_224_information_flow_acceleration_zscore_252d": {"inputs": ["close", "volume"], "func": idec_224_information_flow_acceleration_zscore_252d},
    "idec_225_information_flow_acceleration_rank_252d": {"inputs": ["close", "volume"], "func": idec_225_information_flow_acceleration_rank_252d},
}
