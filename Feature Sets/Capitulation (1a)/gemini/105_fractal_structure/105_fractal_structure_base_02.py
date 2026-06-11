"""
105_fractal_structure — Base Features Part 2
Domain: fractal_structure
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

def frac_121_entropy_proxy_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_121_entropy_proxy_lvl_5d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rolling_mean(base, 5)

def frac_122_entropy_proxy_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_122_entropy_proxy_zscore_5d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _zscore_rolling(base, 5)

def frac_123_entropy_proxy_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_123_entropy_proxy_rank_5d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rank_pct(base, 5)

def frac_124_entropy_proxy_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_124_entropy_proxy_lvl_21d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rolling_mean(base, 21)

def frac_125_entropy_proxy_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_125_entropy_proxy_zscore_21d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _zscore_rolling(base, 21)

def frac_126_entropy_proxy_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_126_entropy_proxy_rank_21d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rank_pct(base, 21)

def frac_127_entropy_proxy_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_127_entropy_proxy_lvl_63d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rolling_mean(base, 63)

def frac_128_entropy_proxy_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_128_entropy_proxy_zscore_63d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _zscore_rolling(base, 63)

def frac_129_entropy_proxy_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_129_entropy_proxy_rank_63d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rank_pct(base, 63)

def frac_130_entropy_proxy_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_130_entropy_proxy_lvl_126d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rolling_mean(base, 126)

def frac_131_entropy_proxy_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_131_entropy_proxy_zscore_126d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _zscore_rolling(base, 126)

def frac_132_entropy_proxy_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_132_entropy_proxy_rank_126d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rank_pct(base, 126)

def frac_133_entropy_proxy_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_133_entropy_proxy_lvl_252d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rolling_mean(base, 252)

def frac_134_entropy_proxy_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_134_entropy_proxy_zscore_252d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _zscore_rolling(base, 252)

def frac_135_entropy_proxy_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_135_entropy_proxy_rank_252d
    ECONOMIC RATIONALE: Approximate entropy of price distribution.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))
    return _rank_pct(base, 252)

def frac_136_fractal_energy_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_136_fractal_energy_lvl_5d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rolling_mean(base, 5)

def frac_137_fractal_energy_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_137_fractal_energy_zscore_5d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _zscore_rolling(base, 5)

def frac_138_fractal_energy_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_138_fractal_energy_rank_5d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rank_pct(base, 5)

def frac_139_fractal_energy_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_139_fractal_energy_lvl_21d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rolling_mean(base, 21)

def frac_140_fractal_energy_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_140_fractal_energy_zscore_21d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _zscore_rolling(base, 21)

def frac_141_fractal_energy_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_141_fractal_energy_rank_21d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rank_pct(base, 21)

def frac_142_fractal_energy_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_142_fractal_energy_lvl_63d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rolling_mean(base, 63)

def frac_143_fractal_energy_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_143_fractal_energy_zscore_63d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _zscore_rolling(base, 63)

def frac_144_fractal_energy_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_144_fractal_energy_rank_63d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rank_pct(base, 63)

def frac_145_fractal_energy_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_145_fractal_energy_lvl_126d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rolling_mean(base, 126)

def frac_146_fractal_energy_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_146_fractal_energy_zscore_126d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _zscore_rolling(base, 126)

def frac_147_fractal_energy_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_147_fractal_energy_rank_126d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rank_pct(base, 126)

def frac_148_fractal_energy_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_148_fractal_energy_lvl_252d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rolling_mean(base, 252)

def frac_149_fractal_energy_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_149_fractal_energy_zscore_252d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _zscore_rolling(base, 252)

def frac_150_fractal_energy_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_150_fractal_energy_rank_252d
    ECONOMIC RATIONALE: Energy dissipated in price movement.
    """
    base = close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)
    return _rank_pct(base, 252)

def frac_151_multi_scale_vol_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_151_multi_scale_vol_lvl_5d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rolling_mean(base, 5)

def frac_152_multi_scale_vol_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_152_multi_scale_vol_zscore_5d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _zscore_rolling(base, 5)

def frac_153_multi_scale_vol_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_153_multi_scale_vol_rank_5d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rank_pct(base, 5)

def frac_154_multi_scale_vol_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_154_multi_scale_vol_lvl_21d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rolling_mean(base, 21)

def frac_155_multi_scale_vol_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_155_multi_scale_vol_zscore_21d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _zscore_rolling(base, 21)

def frac_156_multi_scale_vol_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_156_multi_scale_vol_rank_21d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rank_pct(base, 21)

def frac_157_multi_scale_vol_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_157_multi_scale_vol_lvl_63d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rolling_mean(base, 63)

def frac_158_multi_scale_vol_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_158_multi_scale_vol_zscore_63d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _zscore_rolling(base, 63)

def frac_159_multi_scale_vol_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_159_multi_scale_vol_rank_63d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rank_pct(base, 63)

def frac_160_multi_scale_vol_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_160_multi_scale_vol_lvl_126d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rolling_mean(base, 126)

def frac_161_multi_scale_vol_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_161_multi_scale_vol_zscore_126d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _zscore_rolling(base, 126)

def frac_162_multi_scale_vol_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_162_multi_scale_vol_rank_126d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rank_pct(base, 126)

def frac_163_multi_scale_vol_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_163_multi_scale_vol_lvl_252d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rolling_mean(base, 252)

def frac_164_multi_scale_vol_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_164_multi_scale_vol_zscore_252d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _zscore_rolling(base, 252)

def frac_165_multi_scale_vol_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_165_multi_scale_vol_rank_252d
    ECONOMIC RATIONALE: Ratio of short-term to long-term volatility structure.
    """
    base = close.rolling(5).std() / close.rolling(63).std()
    return _rank_pct(base, 252)

def frac_166_fractal_regime_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_166_fractal_regime_lvl_5d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rolling_mean(base, 5)

def frac_167_fractal_regime_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_167_fractal_regime_zscore_5d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _zscore_rolling(base, 5)

def frac_168_fractal_regime_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_168_fractal_regime_rank_5d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rank_pct(base, 5)

def frac_169_fractal_regime_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_169_fractal_regime_lvl_21d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rolling_mean(base, 21)

def frac_170_fractal_regime_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_170_fractal_regime_zscore_21d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _zscore_rolling(base, 21)

def frac_171_fractal_regime_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_171_fractal_regime_rank_21d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rank_pct(base, 21)

def frac_172_fractal_regime_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_172_fractal_regime_lvl_63d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rolling_mean(base, 63)

def frac_173_fractal_regime_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_173_fractal_regime_zscore_63d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _zscore_rolling(base, 63)

def frac_174_fractal_regime_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_174_fractal_regime_rank_63d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rank_pct(base, 63)

def frac_175_fractal_regime_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_175_fractal_regime_lvl_126d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rolling_mean(base, 126)

def frac_176_fractal_regime_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_176_fractal_regime_zscore_126d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _zscore_rolling(base, 126)

def frac_177_fractal_regime_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_177_fractal_regime_rank_126d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rank_pct(base, 126)

def frac_178_fractal_regime_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_178_fractal_regime_lvl_252d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rolling_mean(base, 252)

def frac_179_fractal_regime_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_179_fractal_regime_zscore_252d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _zscore_rolling(base, 252)

def frac_180_fractal_regime_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_180_fractal_regime_rank_252d
    ECONOMIC RATIONALE: Fractal trend of moving average changes.
    """
    base = close.rolling(21).mean().diff(5).rolling(63).mean()
    return _rank_pct(base, 252)

def frac_181_box_counting_proxy_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_181_box_counting_proxy_lvl_5d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rolling_mean(base, 5)

def frac_182_box_counting_proxy_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_182_box_counting_proxy_zscore_5d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _zscore_rolling(base, 5)

def frac_183_box_counting_proxy_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_183_box_counting_proxy_rank_5d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rank_pct(base, 5)

def frac_184_box_counting_proxy_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_184_box_counting_proxy_lvl_21d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rolling_mean(base, 21)

def frac_185_box_counting_proxy_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_185_box_counting_proxy_zscore_21d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _zscore_rolling(base, 21)

def frac_186_box_counting_proxy_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_186_box_counting_proxy_rank_21d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rank_pct(base, 21)

def frac_187_box_counting_proxy_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_187_box_counting_proxy_lvl_63d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rolling_mean(base, 63)

def frac_188_box_counting_proxy_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_188_box_counting_proxy_zscore_63d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _zscore_rolling(base, 63)

def frac_189_box_counting_proxy_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_189_box_counting_proxy_rank_63d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rank_pct(base, 63)

def frac_190_box_counting_proxy_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_190_box_counting_proxy_lvl_126d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rolling_mean(base, 126)

def frac_191_box_counting_proxy_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_191_box_counting_proxy_zscore_126d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _zscore_rolling(base, 126)

def frac_192_box_counting_proxy_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_192_box_counting_proxy_rank_126d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rank_pct(base, 126)

def frac_193_box_counting_proxy_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_193_box_counting_proxy_lvl_252d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rolling_mean(base, 252)

def frac_194_box_counting_proxy_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_194_box_counting_proxy_zscore_252d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _zscore_rolling(base, 252)

def frac_195_box_counting_proxy_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_195_box_counting_proxy_rank_252d
    ECONOMIC RATIONALE: Box-counting dimension approximation.
    """
    base = ((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())
    return _rank_pct(base, 252)

def frac_196_fractal_trend_index_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_196_fractal_trend_index_lvl_5d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 5)

def frac_197_fractal_trend_index_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_197_fractal_trend_index_zscore_5d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 5)

def frac_198_fractal_trend_index_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_198_fractal_trend_index_rank_5d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 5)

def frac_199_fractal_trend_index_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_199_fractal_trend_index_lvl_21d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 21)

def frac_200_fractal_trend_index_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_200_fractal_trend_index_zscore_21d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 21)

def frac_201_fractal_trend_index_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_201_fractal_trend_index_rank_21d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 21)

def frac_202_fractal_trend_index_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_202_fractal_trend_index_lvl_63d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 63)

def frac_203_fractal_trend_index_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_203_fractal_trend_index_zscore_63d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 63)

def frac_204_fractal_trend_index_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_204_fractal_trend_index_rank_63d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 63)

def frac_205_fractal_trend_index_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_205_fractal_trend_index_lvl_126d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 126)

def frac_206_fractal_trend_index_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_206_fractal_trend_index_zscore_126d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 126)

def frac_207_fractal_trend_index_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_207_fractal_trend_index_rank_126d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 126)

def frac_208_fractal_trend_index_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_208_fractal_trend_index_lvl_252d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 252)

def frac_209_fractal_trend_index_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_209_fractal_trend_index_zscore_252d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 252)

def frac_210_fractal_trend_index_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_210_fractal_trend_index_rank_252d
    ECONOMIC RATIONALE: Trend magnitude relative to structural range.
    """
    base = close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 252)

def frac_211_fractal_noise_ratio_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_211_fractal_noise_ratio_lvl_5d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rolling_mean(base, 5)

def frac_212_fractal_noise_ratio_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_212_fractal_noise_ratio_zscore_5d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _zscore_rolling(base, 5)

def frac_213_fractal_noise_ratio_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_213_fractal_noise_ratio_rank_5d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rank_pct(base, 5)

def frac_214_fractal_noise_ratio_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_214_fractal_noise_ratio_lvl_21d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rolling_mean(base, 21)

def frac_215_fractal_noise_ratio_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_215_fractal_noise_ratio_zscore_21d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _zscore_rolling(base, 21)

def frac_216_fractal_noise_ratio_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_216_fractal_noise_ratio_rank_21d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rank_pct(base, 21)

def frac_217_fractal_noise_ratio_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_217_fractal_noise_ratio_lvl_63d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rolling_mean(base, 63)

def frac_218_fractal_noise_ratio_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_218_fractal_noise_ratio_zscore_63d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _zscore_rolling(base, 63)

def frac_219_fractal_noise_ratio_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_219_fractal_noise_ratio_rank_63d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rank_pct(base, 63)

def frac_220_fractal_noise_ratio_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_220_fractal_noise_ratio_lvl_126d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rolling_mean(base, 126)

def frac_221_fractal_noise_ratio_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_221_fractal_noise_ratio_zscore_126d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _zscore_rolling(base, 126)

def frac_222_fractal_noise_ratio_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_222_fractal_noise_ratio_rank_126d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rank_pct(base, 126)

def frac_223_fractal_noise_ratio_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_223_fractal_noise_ratio_lvl_252d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rolling_mean(base, 252)

def frac_224_fractal_noise_ratio_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_224_fractal_noise_ratio_zscore_252d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _zscore_rolling(base, 252)

def frac_225_fractal_noise_ratio_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_225_fractal_noise_ratio_rank_252d
    ECONOMIC RATIONALE: Proportion of price movement attributed to noise.
    """
    base = 1 - efficiency_ratio
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V105_REGISTRY_2 = {
    "frac_121_entropy_proxy_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_121_entropy_proxy_lvl_5d},
    "frac_122_entropy_proxy_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_122_entropy_proxy_zscore_5d},
    "frac_123_entropy_proxy_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_123_entropy_proxy_rank_5d},
    "frac_124_entropy_proxy_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_124_entropy_proxy_lvl_21d},
    "frac_125_entropy_proxy_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_125_entropy_proxy_zscore_21d},
    "frac_126_entropy_proxy_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_126_entropy_proxy_rank_21d},
    "frac_127_entropy_proxy_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_127_entropy_proxy_lvl_63d},
    "frac_128_entropy_proxy_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_128_entropy_proxy_zscore_63d},
    "frac_129_entropy_proxy_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_129_entropy_proxy_rank_63d},
    "frac_130_entropy_proxy_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_130_entropy_proxy_lvl_126d},
    "frac_131_entropy_proxy_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_131_entropy_proxy_zscore_126d},
    "frac_132_entropy_proxy_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_132_entropy_proxy_rank_126d},
    "frac_133_entropy_proxy_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_133_entropy_proxy_lvl_252d},
    "frac_134_entropy_proxy_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_134_entropy_proxy_zscore_252d},
    "frac_135_entropy_proxy_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_135_entropy_proxy_rank_252d},
    "frac_136_fractal_energy_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_136_fractal_energy_lvl_5d},
    "frac_137_fractal_energy_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_137_fractal_energy_zscore_5d},
    "frac_138_fractal_energy_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_138_fractal_energy_rank_5d},
    "frac_139_fractal_energy_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_139_fractal_energy_lvl_21d},
    "frac_140_fractal_energy_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_140_fractal_energy_zscore_21d},
    "frac_141_fractal_energy_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_141_fractal_energy_rank_21d},
    "frac_142_fractal_energy_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_142_fractal_energy_lvl_63d},
    "frac_143_fractal_energy_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_143_fractal_energy_zscore_63d},
    "frac_144_fractal_energy_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_144_fractal_energy_rank_63d},
    "frac_145_fractal_energy_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_145_fractal_energy_lvl_126d},
    "frac_146_fractal_energy_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_146_fractal_energy_zscore_126d},
    "frac_147_fractal_energy_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_147_fractal_energy_rank_126d},
    "frac_148_fractal_energy_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_148_fractal_energy_lvl_252d},
    "frac_149_fractal_energy_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_149_fractal_energy_zscore_252d},
    "frac_150_fractal_energy_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_150_fractal_energy_rank_252d},
    "frac_151_multi_scale_vol_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_151_multi_scale_vol_lvl_5d},
    "frac_152_multi_scale_vol_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_152_multi_scale_vol_zscore_5d},
    "frac_153_multi_scale_vol_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_153_multi_scale_vol_rank_5d},
    "frac_154_multi_scale_vol_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_154_multi_scale_vol_lvl_21d},
    "frac_155_multi_scale_vol_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_155_multi_scale_vol_zscore_21d},
    "frac_156_multi_scale_vol_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_156_multi_scale_vol_rank_21d},
    "frac_157_multi_scale_vol_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_157_multi_scale_vol_lvl_63d},
    "frac_158_multi_scale_vol_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_158_multi_scale_vol_zscore_63d},
    "frac_159_multi_scale_vol_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_159_multi_scale_vol_rank_63d},
    "frac_160_multi_scale_vol_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_160_multi_scale_vol_lvl_126d},
    "frac_161_multi_scale_vol_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_161_multi_scale_vol_zscore_126d},
    "frac_162_multi_scale_vol_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_162_multi_scale_vol_rank_126d},
    "frac_163_multi_scale_vol_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_163_multi_scale_vol_lvl_252d},
    "frac_164_multi_scale_vol_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_164_multi_scale_vol_zscore_252d},
    "frac_165_multi_scale_vol_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_165_multi_scale_vol_rank_252d},
    "frac_166_fractal_regime_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_166_fractal_regime_lvl_5d},
    "frac_167_fractal_regime_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_167_fractal_regime_zscore_5d},
    "frac_168_fractal_regime_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_168_fractal_regime_rank_5d},
    "frac_169_fractal_regime_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_169_fractal_regime_lvl_21d},
    "frac_170_fractal_regime_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_170_fractal_regime_zscore_21d},
    "frac_171_fractal_regime_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_171_fractal_regime_rank_21d},
    "frac_172_fractal_regime_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_172_fractal_regime_lvl_63d},
    "frac_173_fractal_regime_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_173_fractal_regime_zscore_63d},
    "frac_174_fractal_regime_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_174_fractal_regime_rank_63d},
    "frac_175_fractal_regime_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_175_fractal_regime_lvl_126d},
    "frac_176_fractal_regime_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_176_fractal_regime_zscore_126d},
    "frac_177_fractal_regime_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_177_fractal_regime_rank_126d},
    "frac_178_fractal_regime_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_178_fractal_regime_lvl_252d},
    "frac_179_fractal_regime_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_179_fractal_regime_zscore_252d},
    "frac_180_fractal_regime_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_180_fractal_regime_rank_252d},
    "frac_181_box_counting_proxy_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_181_box_counting_proxy_lvl_5d},
    "frac_182_box_counting_proxy_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_182_box_counting_proxy_zscore_5d},
    "frac_183_box_counting_proxy_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_183_box_counting_proxy_rank_5d},
    "frac_184_box_counting_proxy_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_184_box_counting_proxy_lvl_21d},
    "frac_185_box_counting_proxy_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_185_box_counting_proxy_zscore_21d},
    "frac_186_box_counting_proxy_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_186_box_counting_proxy_rank_21d},
    "frac_187_box_counting_proxy_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_187_box_counting_proxy_lvl_63d},
    "frac_188_box_counting_proxy_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_188_box_counting_proxy_zscore_63d},
    "frac_189_box_counting_proxy_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_189_box_counting_proxy_rank_63d},
    "frac_190_box_counting_proxy_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_190_box_counting_proxy_lvl_126d},
    "frac_191_box_counting_proxy_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_191_box_counting_proxy_zscore_126d},
    "frac_192_box_counting_proxy_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_192_box_counting_proxy_rank_126d},
    "frac_193_box_counting_proxy_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_193_box_counting_proxy_lvl_252d},
    "frac_194_box_counting_proxy_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_194_box_counting_proxy_zscore_252d},
    "frac_195_box_counting_proxy_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_195_box_counting_proxy_rank_252d},
    "frac_196_fractal_trend_index_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_196_fractal_trend_index_lvl_5d},
    "frac_197_fractal_trend_index_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_197_fractal_trend_index_zscore_5d},
    "frac_198_fractal_trend_index_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_198_fractal_trend_index_rank_5d},
    "frac_199_fractal_trend_index_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_199_fractal_trend_index_lvl_21d},
    "frac_200_fractal_trend_index_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_200_fractal_trend_index_zscore_21d},
    "frac_201_fractal_trend_index_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_201_fractal_trend_index_rank_21d},
    "frac_202_fractal_trend_index_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_202_fractal_trend_index_lvl_63d},
    "frac_203_fractal_trend_index_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_203_fractal_trend_index_zscore_63d},
    "frac_204_fractal_trend_index_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_204_fractal_trend_index_rank_63d},
    "frac_205_fractal_trend_index_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_205_fractal_trend_index_lvl_126d},
    "frac_206_fractal_trend_index_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_206_fractal_trend_index_zscore_126d},
    "frac_207_fractal_trend_index_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_207_fractal_trend_index_rank_126d},
    "frac_208_fractal_trend_index_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_208_fractal_trend_index_lvl_252d},
    "frac_209_fractal_trend_index_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_209_fractal_trend_index_zscore_252d},
    "frac_210_fractal_trend_index_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_210_fractal_trend_index_rank_252d},
    "frac_211_fractal_noise_ratio_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_211_fractal_noise_ratio_lvl_5d},
    "frac_212_fractal_noise_ratio_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_212_fractal_noise_ratio_zscore_5d},
    "frac_213_fractal_noise_ratio_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_213_fractal_noise_ratio_rank_5d},
    "frac_214_fractal_noise_ratio_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_214_fractal_noise_ratio_lvl_21d},
    "frac_215_fractal_noise_ratio_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_215_fractal_noise_ratio_zscore_21d},
    "frac_216_fractal_noise_ratio_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_216_fractal_noise_ratio_rank_21d},
    "frac_217_fractal_noise_ratio_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_217_fractal_noise_ratio_lvl_63d},
    "frac_218_fractal_noise_ratio_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_218_fractal_noise_ratio_zscore_63d},
    "frac_219_fractal_noise_ratio_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_219_fractal_noise_ratio_rank_63d},
    "frac_220_fractal_noise_ratio_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_220_fractal_noise_ratio_lvl_126d},
    "frac_221_fractal_noise_ratio_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_221_fractal_noise_ratio_zscore_126d},
    "frac_222_fractal_noise_ratio_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_222_fractal_noise_ratio_rank_126d},
    "frac_223_fractal_noise_ratio_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_223_fractal_noise_ratio_lvl_252d},
    "frac_224_fractal_noise_ratio_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_224_fractal_noise_ratio_zscore_252d},
    "frac_225_fractal_noise_ratio_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_225_fractal_noise_ratio_rank_252d},
}
