"""
108_drawdown_history_rank — Base Features Part 2
Domain: drawdown_history_rank
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

def dhrk_121_drawdown_persistence_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_121_drawdown_persistence_lvl_5d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rolling_mean(base, 5)

def dhrk_122_drawdown_persistence_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_122_drawdown_persistence_zscore_5d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _zscore_rolling(base, 5)

def dhrk_123_drawdown_persistence_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_123_drawdown_persistence_rank_5d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rank_pct(base, 5)

def dhrk_124_drawdown_persistence_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_124_drawdown_persistence_lvl_21d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rolling_mean(base, 21)

def dhrk_125_drawdown_persistence_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_125_drawdown_persistence_zscore_21d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _zscore_rolling(base, 21)

def dhrk_126_drawdown_persistence_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_126_drawdown_persistence_rank_21d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rank_pct(base, 21)

def dhrk_127_drawdown_persistence_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_127_drawdown_persistence_lvl_63d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rolling_mean(base, 63)

def dhrk_128_drawdown_persistence_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_128_drawdown_persistence_zscore_63d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _zscore_rolling(base, 63)

def dhrk_129_drawdown_persistence_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_129_drawdown_persistence_rank_63d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rank_pct(base, 63)

def dhrk_130_drawdown_persistence_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_130_drawdown_persistence_lvl_126d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rolling_mean(base, 126)

def dhrk_131_drawdown_persistence_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_131_drawdown_persistence_zscore_126d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _zscore_rolling(base, 126)

def dhrk_132_drawdown_persistence_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_132_drawdown_persistence_rank_126d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rank_pct(base, 126)

def dhrk_133_drawdown_persistence_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_133_drawdown_persistence_lvl_252d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rolling_mean(base, 252)

def dhrk_134_drawdown_persistence_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_134_drawdown_persistence_zscore_252d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _zscore_rolling(base, 252)

def dhrk_135_drawdown_persistence_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_135_drawdown_persistence_rank_252d
    ECONOMIC RATIONALE: Time spent in 'bear market' territory.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()
    return _rank_pct(base, 252)

def dhrk_136_drawdown_regime_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_136_drawdown_regime_lvl_5d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rolling_mean(base, 5)

def dhrk_137_drawdown_regime_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_137_drawdown_regime_zscore_5d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _zscore_rolling(base, 5)

def dhrk_138_drawdown_regime_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_138_drawdown_regime_rank_5d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rank_pct(base, 5)

def dhrk_139_drawdown_regime_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_139_drawdown_regime_lvl_21d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rolling_mean(base, 21)

def dhrk_140_drawdown_regime_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_140_drawdown_regime_zscore_21d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _zscore_rolling(base, 21)

def dhrk_141_drawdown_regime_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_141_drawdown_regime_rank_21d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rank_pct(base, 21)

def dhrk_142_drawdown_regime_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_142_drawdown_regime_lvl_63d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rolling_mean(base, 63)

def dhrk_143_drawdown_regime_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_143_drawdown_regime_zscore_63d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _zscore_rolling(base, 63)

def dhrk_144_drawdown_regime_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_144_drawdown_regime_rank_63d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rank_pct(base, 63)

def dhrk_145_drawdown_regime_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_145_drawdown_regime_lvl_126d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rolling_mean(base, 126)

def dhrk_146_drawdown_regime_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_146_drawdown_regime_zscore_126d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _zscore_rolling(base, 126)

def dhrk_147_drawdown_regime_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_147_drawdown_regime_rank_126d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rank_pct(base, 126)

def dhrk_148_drawdown_regime_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_148_drawdown_regime_lvl_252d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rolling_mean(base, 252)

def dhrk_149_drawdown_regime_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_149_drawdown_regime_zscore_252d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _zscore_rolling(base, 252)

def dhrk_150_drawdown_regime_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_150_drawdown_regime_rank_252d
    ECONOMIC RATIONALE: Deviation from average drawdown level.
    """
    base = (close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()
    return _rank_pct(base, 252)

def dhrk_151_drawdown_impact_score_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_151_drawdown_impact_score_lvl_5d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rolling_mean(base, 5)

def dhrk_152_drawdown_impact_score_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_152_drawdown_impact_score_zscore_5d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _zscore_rolling(base, 5)

def dhrk_153_drawdown_impact_score_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_153_drawdown_impact_score_rank_5d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rank_pct(base, 5)

def dhrk_154_drawdown_impact_score_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_154_drawdown_impact_score_lvl_21d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rolling_mean(base, 21)

def dhrk_155_drawdown_impact_score_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_155_drawdown_impact_score_zscore_21d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _zscore_rolling(base, 21)

def dhrk_156_drawdown_impact_score_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_156_drawdown_impact_score_rank_21d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rank_pct(base, 21)

def dhrk_157_drawdown_impact_score_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_157_drawdown_impact_score_lvl_63d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rolling_mean(base, 63)

def dhrk_158_drawdown_impact_score_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_158_drawdown_impact_score_zscore_63d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _zscore_rolling(base, 63)

def dhrk_159_drawdown_impact_score_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_159_drawdown_impact_score_rank_63d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rank_pct(base, 63)

def dhrk_160_drawdown_impact_score_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_160_drawdown_impact_score_lvl_126d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rolling_mean(base, 126)

def dhrk_161_drawdown_impact_score_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_161_drawdown_impact_score_zscore_126d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _zscore_rolling(base, 126)

def dhrk_162_drawdown_impact_score_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_162_drawdown_impact_score_rank_126d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rank_pct(base, 126)

def dhrk_163_drawdown_impact_score_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_163_drawdown_impact_score_lvl_252d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rolling_mean(base, 252)

def dhrk_164_drawdown_impact_score_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_164_drawdown_impact_score_zscore_252d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _zscore_rolling(base, 252)

def dhrk_165_drawdown_impact_score_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_165_drawdown_impact_score_rank_252d
    ECONOMIC RATIONALE: Depth combined with recent negative momentum.
    """
    base = (close / close.rolling(252).max() - 1) * close.pct_change(21)
    return _rank_pct(base, 252)

def dhrk_166_historical_max_drawdown_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_166_historical_max_drawdown_lvl_5d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rolling_mean(base, 5)

def dhrk_167_historical_max_drawdown_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_167_historical_max_drawdown_zscore_5d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _zscore_rolling(base, 5)

def dhrk_168_historical_max_drawdown_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_168_historical_max_drawdown_rank_5d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rank_pct(base, 5)

def dhrk_169_historical_max_drawdown_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_169_historical_max_drawdown_lvl_21d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rolling_mean(base, 21)

def dhrk_170_historical_max_drawdown_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_170_historical_max_drawdown_zscore_21d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _zscore_rolling(base, 21)

def dhrk_171_historical_max_drawdown_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_171_historical_max_drawdown_rank_21d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rank_pct(base, 21)

def dhrk_172_historical_max_drawdown_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_172_historical_max_drawdown_lvl_63d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rolling_mean(base, 63)

def dhrk_173_historical_max_drawdown_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_173_historical_max_drawdown_zscore_63d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _zscore_rolling(base, 63)

def dhrk_174_historical_max_drawdown_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_174_historical_max_drawdown_rank_63d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rank_pct(base, 63)

def dhrk_175_historical_max_drawdown_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_175_historical_max_drawdown_lvl_126d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rolling_mean(base, 126)

def dhrk_176_historical_max_drawdown_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_176_historical_max_drawdown_zscore_126d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _zscore_rolling(base, 126)

def dhrk_177_historical_max_drawdown_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_177_historical_max_drawdown_rank_126d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rank_pct(base, 126)

def dhrk_178_historical_max_drawdown_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_178_historical_max_drawdown_lvl_252d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rolling_mean(base, 252)

def dhrk_179_historical_max_drawdown_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_179_historical_max_drawdown_zscore_252d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _zscore_rolling(base, 252)

def dhrk_180_historical_max_drawdown_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_180_historical_max_drawdown_rank_252d
    ECONOMIC RATIONALE: Rolling 252-day maximum drawdown.
    """
    base = ((close / close.rolling(252).max() - 1).rolling(252).min())
    return _rank_pct(base, 252)

def dhrk_181_drawdown_exhaustion_proxy_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_181_drawdown_exhaustion_proxy_lvl_5d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dhrk_182_drawdown_exhaustion_proxy_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_182_drawdown_exhaustion_proxy_zscore_5d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dhrk_183_drawdown_exhaustion_proxy_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_183_drawdown_exhaustion_proxy_rank_5d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rank_pct(base, 5)

def dhrk_184_drawdown_exhaustion_proxy_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_184_drawdown_exhaustion_proxy_lvl_21d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dhrk_185_drawdown_exhaustion_proxy_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_185_drawdown_exhaustion_proxy_zscore_21d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dhrk_186_drawdown_exhaustion_proxy_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_186_drawdown_exhaustion_proxy_rank_21d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rank_pct(base, 21)

def dhrk_187_drawdown_exhaustion_proxy_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_187_drawdown_exhaustion_proxy_lvl_63d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dhrk_188_drawdown_exhaustion_proxy_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_188_drawdown_exhaustion_proxy_zscore_63d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dhrk_189_drawdown_exhaustion_proxy_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_189_drawdown_exhaustion_proxy_rank_63d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rank_pct(base, 63)

def dhrk_190_drawdown_exhaustion_proxy_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_190_drawdown_exhaustion_proxy_lvl_126d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dhrk_191_drawdown_exhaustion_proxy_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_191_drawdown_exhaustion_proxy_zscore_126d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dhrk_192_drawdown_exhaustion_proxy_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_192_drawdown_exhaustion_proxy_rank_126d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rank_pct(base, 126)

def dhrk_193_drawdown_exhaustion_proxy_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_193_drawdown_exhaustion_proxy_lvl_252d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def dhrk_194_drawdown_exhaustion_proxy_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_194_drawdown_exhaustion_proxy_zscore_252d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dhrk_195_drawdown_exhaustion_proxy_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_195_drawdown_exhaustion_proxy_rank_252d
    ECONOMIC RATIONALE: Current drawdown relative to recent maximum.
    """
    base = (close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)
    return _rank_pct(base, 252)

def dhrk_196_drawdown_oscillator_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_196_drawdown_oscillator_lvl_5d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dhrk_197_drawdown_oscillator_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_197_drawdown_oscillator_zscore_5d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dhrk_198_drawdown_oscillator_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_198_drawdown_oscillator_rank_5d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def dhrk_199_drawdown_oscillator_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_199_drawdown_oscillator_lvl_21d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dhrk_200_drawdown_oscillator_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_200_drawdown_oscillator_zscore_21d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dhrk_201_drawdown_oscillator_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_201_drawdown_oscillator_rank_21d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def dhrk_202_drawdown_oscillator_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_202_drawdown_oscillator_lvl_63d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dhrk_203_drawdown_oscillator_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_203_drawdown_oscillator_zscore_63d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dhrk_204_drawdown_oscillator_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_204_drawdown_oscillator_rank_63d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def dhrk_205_drawdown_oscillator_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_205_drawdown_oscillator_lvl_126d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dhrk_206_drawdown_oscillator_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_206_drawdown_oscillator_zscore_126d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dhrk_207_drawdown_oscillator_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_207_drawdown_oscillator_rank_126d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def dhrk_208_drawdown_oscillator_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_208_drawdown_oscillator_lvl_252d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def dhrk_209_drawdown_oscillator_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_209_drawdown_oscillator_zscore_252d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dhrk_210_drawdown_oscillator_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_210_drawdown_oscillator_rank_252d
    ECONOMIC RATIONALE: Position within the annual range.
    """
    base = (close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def dhrk_211_drawdown_tail_risk_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_211_drawdown_tail_risk_lvl_5d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rolling_mean(base, 5)

def dhrk_212_drawdown_tail_risk_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_212_drawdown_tail_risk_zscore_5d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _zscore_rolling(base, 5)

def dhrk_213_drawdown_tail_risk_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_213_drawdown_tail_risk_rank_5d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rank_pct(base, 5)

def dhrk_214_drawdown_tail_risk_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_214_drawdown_tail_risk_lvl_21d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rolling_mean(base, 21)

def dhrk_215_drawdown_tail_risk_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_215_drawdown_tail_risk_zscore_21d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _zscore_rolling(base, 21)

def dhrk_216_drawdown_tail_risk_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_216_drawdown_tail_risk_rank_21d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rank_pct(base, 21)

def dhrk_217_drawdown_tail_risk_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_217_drawdown_tail_risk_lvl_63d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rolling_mean(base, 63)

def dhrk_218_drawdown_tail_risk_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_218_drawdown_tail_risk_zscore_63d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _zscore_rolling(base, 63)

def dhrk_219_drawdown_tail_risk_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_219_drawdown_tail_risk_rank_63d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rank_pct(base, 63)

def dhrk_220_drawdown_tail_risk_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_220_drawdown_tail_risk_lvl_126d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rolling_mean(base, 126)

def dhrk_221_drawdown_tail_risk_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_221_drawdown_tail_risk_zscore_126d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _zscore_rolling(base, 126)

def dhrk_222_drawdown_tail_risk_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_222_drawdown_tail_risk_rank_126d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rank_pct(base, 126)

def dhrk_223_drawdown_tail_risk_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_223_drawdown_tail_risk_lvl_252d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rolling_mean(base, 252)

def dhrk_224_drawdown_tail_risk_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_224_drawdown_tail_risk_zscore_252d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _zscore_rolling(base, 252)

def dhrk_225_drawdown_tail_risk_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_225_drawdown_tail_risk_rank_252d
    ECONOMIC RATIONALE: Binary indicator of extreme wealth destruction.
    """
    base = ((close / close.rolling(252).max() - 1) < -0.5).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V108_REGISTRY_2 = {
    "dhrk_121_drawdown_persistence_lvl_5d": {"inputs": ["close"], "func": dhrk_121_drawdown_persistence_lvl_5d},
    "dhrk_122_drawdown_persistence_zscore_5d": {"inputs": ["close"], "func": dhrk_122_drawdown_persistence_zscore_5d},
    "dhrk_123_drawdown_persistence_rank_5d": {"inputs": ["close"], "func": dhrk_123_drawdown_persistence_rank_5d},
    "dhrk_124_drawdown_persistence_lvl_21d": {"inputs": ["close"], "func": dhrk_124_drawdown_persistence_lvl_21d},
    "dhrk_125_drawdown_persistence_zscore_21d": {"inputs": ["close"], "func": dhrk_125_drawdown_persistence_zscore_21d},
    "dhrk_126_drawdown_persistence_rank_21d": {"inputs": ["close"], "func": dhrk_126_drawdown_persistence_rank_21d},
    "dhrk_127_drawdown_persistence_lvl_63d": {"inputs": ["close"], "func": dhrk_127_drawdown_persistence_lvl_63d},
    "dhrk_128_drawdown_persistence_zscore_63d": {"inputs": ["close"], "func": dhrk_128_drawdown_persistence_zscore_63d},
    "dhrk_129_drawdown_persistence_rank_63d": {"inputs": ["close"], "func": dhrk_129_drawdown_persistence_rank_63d},
    "dhrk_130_drawdown_persistence_lvl_126d": {"inputs": ["close"], "func": dhrk_130_drawdown_persistence_lvl_126d},
    "dhrk_131_drawdown_persistence_zscore_126d": {"inputs": ["close"], "func": dhrk_131_drawdown_persistence_zscore_126d},
    "dhrk_132_drawdown_persistence_rank_126d": {"inputs": ["close"], "func": dhrk_132_drawdown_persistence_rank_126d},
    "dhrk_133_drawdown_persistence_lvl_252d": {"inputs": ["close"], "func": dhrk_133_drawdown_persistence_lvl_252d},
    "dhrk_134_drawdown_persistence_zscore_252d": {"inputs": ["close"], "func": dhrk_134_drawdown_persistence_zscore_252d},
    "dhrk_135_drawdown_persistence_rank_252d": {"inputs": ["close"], "func": dhrk_135_drawdown_persistence_rank_252d},
    "dhrk_136_drawdown_regime_lvl_5d": {"inputs": ["close"], "func": dhrk_136_drawdown_regime_lvl_5d},
    "dhrk_137_drawdown_regime_zscore_5d": {"inputs": ["close"], "func": dhrk_137_drawdown_regime_zscore_5d},
    "dhrk_138_drawdown_regime_rank_5d": {"inputs": ["close"], "func": dhrk_138_drawdown_regime_rank_5d},
    "dhrk_139_drawdown_regime_lvl_21d": {"inputs": ["close"], "func": dhrk_139_drawdown_regime_lvl_21d},
    "dhrk_140_drawdown_regime_zscore_21d": {"inputs": ["close"], "func": dhrk_140_drawdown_regime_zscore_21d},
    "dhrk_141_drawdown_regime_rank_21d": {"inputs": ["close"], "func": dhrk_141_drawdown_regime_rank_21d},
    "dhrk_142_drawdown_regime_lvl_63d": {"inputs": ["close"], "func": dhrk_142_drawdown_regime_lvl_63d},
    "dhrk_143_drawdown_regime_zscore_63d": {"inputs": ["close"], "func": dhrk_143_drawdown_regime_zscore_63d},
    "dhrk_144_drawdown_regime_rank_63d": {"inputs": ["close"], "func": dhrk_144_drawdown_regime_rank_63d},
    "dhrk_145_drawdown_regime_lvl_126d": {"inputs": ["close"], "func": dhrk_145_drawdown_regime_lvl_126d},
    "dhrk_146_drawdown_regime_zscore_126d": {"inputs": ["close"], "func": dhrk_146_drawdown_regime_zscore_126d},
    "dhrk_147_drawdown_regime_rank_126d": {"inputs": ["close"], "func": dhrk_147_drawdown_regime_rank_126d},
    "dhrk_148_drawdown_regime_lvl_252d": {"inputs": ["close"], "func": dhrk_148_drawdown_regime_lvl_252d},
    "dhrk_149_drawdown_regime_zscore_252d": {"inputs": ["close"], "func": dhrk_149_drawdown_regime_zscore_252d},
    "dhrk_150_drawdown_regime_rank_252d": {"inputs": ["close"], "func": dhrk_150_drawdown_regime_rank_252d},
    "dhrk_151_drawdown_impact_score_lvl_5d": {"inputs": ["close"], "func": dhrk_151_drawdown_impact_score_lvl_5d},
    "dhrk_152_drawdown_impact_score_zscore_5d": {"inputs": ["close"], "func": dhrk_152_drawdown_impact_score_zscore_5d},
    "dhrk_153_drawdown_impact_score_rank_5d": {"inputs": ["close"], "func": dhrk_153_drawdown_impact_score_rank_5d},
    "dhrk_154_drawdown_impact_score_lvl_21d": {"inputs": ["close"], "func": dhrk_154_drawdown_impact_score_lvl_21d},
    "dhrk_155_drawdown_impact_score_zscore_21d": {"inputs": ["close"], "func": dhrk_155_drawdown_impact_score_zscore_21d},
    "dhrk_156_drawdown_impact_score_rank_21d": {"inputs": ["close"], "func": dhrk_156_drawdown_impact_score_rank_21d},
    "dhrk_157_drawdown_impact_score_lvl_63d": {"inputs": ["close"], "func": dhrk_157_drawdown_impact_score_lvl_63d},
    "dhrk_158_drawdown_impact_score_zscore_63d": {"inputs": ["close"], "func": dhrk_158_drawdown_impact_score_zscore_63d},
    "dhrk_159_drawdown_impact_score_rank_63d": {"inputs": ["close"], "func": dhrk_159_drawdown_impact_score_rank_63d},
    "dhrk_160_drawdown_impact_score_lvl_126d": {"inputs": ["close"], "func": dhrk_160_drawdown_impact_score_lvl_126d},
    "dhrk_161_drawdown_impact_score_zscore_126d": {"inputs": ["close"], "func": dhrk_161_drawdown_impact_score_zscore_126d},
    "dhrk_162_drawdown_impact_score_rank_126d": {"inputs": ["close"], "func": dhrk_162_drawdown_impact_score_rank_126d},
    "dhrk_163_drawdown_impact_score_lvl_252d": {"inputs": ["close"], "func": dhrk_163_drawdown_impact_score_lvl_252d},
    "dhrk_164_drawdown_impact_score_zscore_252d": {"inputs": ["close"], "func": dhrk_164_drawdown_impact_score_zscore_252d},
    "dhrk_165_drawdown_impact_score_rank_252d": {"inputs": ["close"], "func": dhrk_165_drawdown_impact_score_rank_252d},
    "dhrk_166_historical_max_drawdown_lvl_5d": {"inputs": ["close"], "func": dhrk_166_historical_max_drawdown_lvl_5d},
    "dhrk_167_historical_max_drawdown_zscore_5d": {"inputs": ["close"], "func": dhrk_167_historical_max_drawdown_zscore_5d},
    "dhrk_168_historical_max_drawdown_rank_5d": {"inputs": ["close"], "func": dhrk_168_historical_max_drawdown_rank_5d},
    "dhrk_169_historical_max_drawdown_lvl_21d": {"inputs": ["close"], "func": dhrk_169_historical_max_drawdown_lvl_21d},
    "dhrk_170_historical_max_drawdown_zscore_21d": {"inputs": ["close"], "func": dhrk_170_historical_max_drawdown_zscore_21d},
    "dhrk_171_historical_max_drawdown_rank_21d": {"inputs": ["close"], "func": dhrk_171_historical_max_drawdown_rank_21d},
    "dhrk_172_historical_max_drawdown_lvl_63d": {"inputs": ["close"], "func": dhrk_172_historical_max_drawdown_lvl_63d},
    "dhrk_173_historical_max_drawdown_zscore_63d": {"inputs": ["close"], "func": dhrk_173_historical_max_drawdown_zscore_63d},
    "dhrk_174_historical_max_drawdown_rank_63d": {"inputs": ["close"], "func": dhrk_174_historical_max_drawdown_rank_63d},
    "dhrk_175_historical_max_drawdown_lvl_126d": {"inputs": ["close"], "func": dhrk_175_historical_max_drawdown_lvl_126d},
    "dhrk_176_historical_max_drawdown_zscore_126d": {"inputs": ["close"], "func": dhrk_176_historical_max_drawdown_zscore_126d},
    "dhrk_177_historical_max_drawdown_rank_126d": {"inputs": ["close"], "func": dhrk_177_historical_max_drawdown_rank_126d},
    "dhrk_178_historical_max_drawdown_lvl_252d": {"inputs": ["close"], "func": dhrk_178_historical_max_drawdown_lvl_252d},
    "dhrk_179_historical_max_drawdown_zscore_252d": {"inputs": ["close"], "func": dhrk_179_historical_max_drawdown_zscore_252d},
    "dhrk_180_historical_max_drawdown_rank_252d": {"inputs": ["close"], "func": dhrk_180_historical_max_drawdown_rank_252d},
    "dhrk_181_drawdown_exhaustion_proxy_lvl_5d": {"inputs": ["close"], "func": dhrk_181_drawdown_exhaustion_proxy_lvl_5d},
    "dhrk_182_drawdown_exhaustion_proxy_zscore_5d": {"inputs": ["close"], "func": dhrk_182_drawdown_exhaustion_proxy_zscore_5d},
    "dhrk_183_drawdown_exhaustion_proxy_rank_5d": {"inputs": ["close"], "func": dhrk_183_drawdown_exhaustion_proxy_rank_5d},
    "dhrk_184_drawdown_exhaustion_proxy_lvl_21d": {"inputs": ["close"], "func": dhrk_184_drawdown_exhaustion_proxy_lvl_21d},
    "dhrk_185_drawdown_exhaustion_proxy_zscore_21d": {"inputs": ["close"], "func": dhrk_185_drawdown_exhaustion_proxy_zscore_21d},
    "dhrk_186_drawdown_exhaustion_proxy_rank_21d": {"inputs": ["close"], "func": dhrk_186_drawdown_exhaustion_proxy_rank_21d},
    "dhrk_187_drawdown_exhaustion_proxy_lvl_63d": {"inputs": ["close"], "func": dhrk_187_drawdown_exhaustion_proxy_lvl_63d},
    "dhrk_188_drawdown_exhaustion_proxy_zscore_63d": {"inputs": ["close"], "func": dhrk_188_drawdown_exhaustion_proxy_zscore_63d},
    "dhrk_189_drawdown_exhaustion_proxy_rank_63d": {"inputs": ["close"], "func": dhrk_189_drawdown_exhaustion_proxy_rank_63d},
    "dhrk_190_drawdown_exhaustion_proxy_lvl_126d": {"inputs": ["close"], "func": dhrk_190_drawdown_exhaustion_proxy_lvl_126d},
    "dhrk_191_drawdown_exhaustion_proxy_zscore_126d": {"inputs": ["close"], "func": dhrk_191_drawdown_exhaustion_proxy_zscore_126d},
    "dhrk_192_drawdown_exhaustion_proxy_rank_126d": {"inputs": ["close"], "func": dhrk_192_drawdown_exhaustion_proxy_rank_126d},
    "dhrk_193_drawdown_exhaustion_proxy_lvl_252d": {"inputs": ["close"], "func": dhrk_193_drawdown_exhaustion_proxy_lvl_252d},
    "dhrk_194_drawdown_exhaustion_proxy_zscore_252d": {"inputs": ["close"], "func": dhrk_194_drawdown_exhaustion_proxy_zscore_252d},
    "dhrk_195_drawdown_exhaustion_proxy_rank_252d": {"inputs": ["close"], "func": dhrk_195_drawdown_exhaustion_proxy_rank_252d},
    "dhrk_196_drawdown_oscillator_lvl_5d": {"inputs": ["close"], "func": dhrk_196_drawdown_oscillator_lvl_5d},
    "dhrk_197_drawdown_oscillator_zscore_5d": {"inputs": ["close"], "func": dhrk_197_drawdown_oscillator_zscore_5d},
    "dhrk_198_drawdown_oscillator_rank_5d": {"inputs": ["close"], "func": dhrk_198_drawdown_oscillator_rank_5d},
    "dhrk_199_drawdown_oscillator_lvl_21d": {"inputs": ["close"], "func": dhrk_199_drawdown_oscillator_lvl_21d},
    "dhrk_200_drawdown_oscillator_zscore_21d": {"inputs": ["close"], "func": dhrk_200_drawdown_oscillator_zscore_21d},
    "dhrk_201_drawdown_oscillator_rank_21d": {"inputs": ["close"], "func": dhrk_201_drawdown_oscillator_rank_21d},
    "dhrk_202_drawdown_oscillator_lvl_63d": {"inputs": ["close"], "func": dhrk_202_drawdown_oscillator_lvl_63d},
    "dhrk_203_drawdown_oscillator_zscore_63d": {"inputs": ["close"], "func": dhrk_203_drawdown_oscillator_zscore_63d},
    "dhrk_204_drawdown_oscillator_rank_63d": {"inputs": ["close"], "func": dhrk_204_drawdown_oscillator_rank_63d},
    "dhrk_205_drawdown_oscillator_lvl_126d": {"inputs": ["close"], "func": dhrk_205_drawdown_oscillator_lvl_126d},
    "dhrk_206_drawdown_oscillator_zscore_126d": {"inputs": ["close"], "func": dhrk_206_drawdown_oscillator_zscore_126d},
    "dhrk_207_drawdown_oscillator_rank_126d": {"inputs": ["close"], "func": dhrk_207_drawdown_oscillator_rank_126d},
    "dhrk_208_drawdown_oscillator_lvl_252d": {"inputs": ["close"], "func": dhrk_208_drawdown_oscillator_lvl_252d},
    "dhrk_209_drawdown_oscillator_zscore_252d": {"inputs": ["close"], "func": dhrk_209_drawdown_oscillator_zscore_252d},
    "dhrk_210_drawdown_oscillator_rank_252d": {"inputs": ["close"], "func": dhrk_210_drawdown_oscillator_rank_252d},
    "dhrk_211_drawdown_tail_risk_lvl_5d": {"inputs": ["close"], "func": dhrk_211_drawdown_tail_risk_lvl_5d},
    "dhrk_212_drawdown_tail_risk_zscore_5d": {"inputs": ["close"], "func": dhrk_212_drawdown_tail_risk_zscore_5d},
    "dhrk_213_drawdown_tail_risk_rank_5d": {"inputs": ["close"], "func": dhrk_213_drawdown_tail_risk_rank_5d},
    "dhrk_214_drawdown_tail_risk_lvl_21d": {"inputs": ["close"], "func": dhrk_214_drawdown_tail_risk_lvl_21d},
    "dhrk_215_drawdown_tail_risk_zscore_21d": {"inputs": ["close"], "func": dhrk_215_drawdown_tail_risk_zscore_21d},
    "dhrk_216_drawdown_tail_risk_rank_21d": {"inputs": ["close"], "func": dhrk_216_drawdown_tail_risk_rank_21d},
    "dhrk_217_drawdown_tail_risk_lvl_63d": {"inputs": ["close"], "func": dhrk_217_drawdown_tail_risk_lvl_63d},
    "dhrk_218_drawdown_tail_risk_zscore_63d": {"inputs": ["close"], "func": dhrk_218_drawdown_tail_risk_zscore_63d},
    "dhrk_219_drawdown_tail_risk_rank_63d": {"inputs": ["close"], "func": dhrk_219_drawdown_tail_risk_rank_63d},
    "dhrk_220_drawdown_tail_risk_lvl_126d": {"inputs": ["close"], "func": dhrk_220_drawdown_tail_risk_lvl_126d},
    "dhrk_221_drawdown_tail_risk_zscore_126d": {"inputs": ["close"], "func": dhrk_221_drawdown_tail_risk_zscore_126d},
    "dhrk_222_drawdown_tail_risk_rank_126d": {"inputs": ["close"], "func": dhrk_222_drawdown_tail_risk_rank_126d},
    "dhrk_223_drawdown_tail_risk_lvl_252d": {"inputs": ["close"], "func": dhrk_223_drawdown_tail_risk_lvl_252d},
    "dhrk_224_drawdown_tail_risk_zscore_252d": {"inputs": ["close"], "func": dhrk_224_drawdown_tail_risk_zscore_252d},
    "dhrk_225_drawdown_tail_risk_rank_252d": {"inputs": ["close"], "func": dhrk_225_drawdown_tail_risk_rank_252d},
}
