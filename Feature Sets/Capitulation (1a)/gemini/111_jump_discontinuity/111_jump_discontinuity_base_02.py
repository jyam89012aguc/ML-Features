"""
111_jump_discontinuity — Base Features Part 2
Domain: jump_discontinuity
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

def jump_121_jump_decay_rate_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_121_jump_decay_rate_lvl_5d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rolling_mean(base, 5)

def jump_122_jump_decay_rate_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_122_jump_decay_rate_zscore_5d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _zscore_rolling(base, 5)

def jump_123_jump_decay_rate_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_123_jump_decay_rate_rank_5d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rank_pct(base, 5)

def jump_124_jump_decay_rate_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_124_jump_decay_rate_lvl_21d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rolling_mean(base, 21)

def jump_125_jump_decay_rate_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_125_jump_decay_rate_zscore_21d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _zscore_rolling(base, 21)

def jump_126_jump_decay_rate_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_126_jump_decay_rate_rank_21d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rank_pct(base, 21)

def jump_127_jump_decay_rate_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_127_jump_decay_rate_lvl_63d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rolling_mean(base, 63)

def jump_128_jump_decay_rate_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_128_jump_decay_rate_zscore_63d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _zscore_rolling(base, 63)

def jump_129_jump_decay_rate_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_129_jump_decay_rate_rank_63d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rank_pct(base, 63)

def jump_130_jump_decay_rate_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_130_jump_decay_rate_lvl_126d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rolling_mean(base, 126)

def jump_131_jump_decay_rate_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_131_jump_decay_rate_zscore_126d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _zscore_rolling(base, 126)

def jump_132_jump_decay_rate_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_132_jump_decay_rate_rank_126d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rank_pct(base, 126)

def jump_133_jump_decay_rate_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_133_jump_decay_rate_lvl_252d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rolling_mean(base, 252)

def jump_134_jump_decay_rate_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_134_jump_decay_rate_zscore_252d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _zscore_rolling(base, 252)

def jump_135_jump_decay_rate_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_135_jump_decay_rate_rank_252d
    ECONOMIC RATIONALE: Decay of impact from recent jumps.
    """
    base = close.diff(1).abs().ewm(span=5).mean()
    return _rank_pct(base, 252)

def jump_136_jump_clustering_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_136_jump_clustering_lvl_5d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rolling_mean(base, 5)

def jump_137_jump_clustering_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_137_jump_clustering_zscore_5d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _zscore_rolling(base, 5)

def jump_138_jump_clustering_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_138_jump_clustering_rank_5d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rank_pct(base, 5)

def jump_139_jump_clustering_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_139_jump_clustering_lvl_21d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rolling_mean(base, 21)

def jump_140_jump_clustering_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_140_jump_clustering_zscore_21d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _zscore_rolling(base, 21)

def jump_141_jump_clustering_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_141_jump_clustering_rank_21d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rank_pct(base, 21)

def jump_142_jump_clustering_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_142_jump_clustering_lvl_63d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rolling_mean(base, 63)

def jump_143_jump_clustering_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_143_jump_clustering_zscore_63d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _zscore_rolling(base, 63)

def jump_144_jump_clustering_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_144_jump_clustering_rank_63d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rank_pct(base, 63)

def jump_145_jump_clustering_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_145_jump_clustering_lvl_126d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rolling_mean(base, 126)

def jump_146_jump_clustering_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_146_jump_clustering_zscore_126d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _zscore_rolling(base, 126)

def jump_147_jump_clustering_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_147_jump_clustering_rank_126d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rank_pct(base, 126)

def jump_148_jump_clustering_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_148_jump_clustering_lvl_252d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rolling_mean(base, 252)

def jump_149_jump_clustering_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_149_jump_clustering_zscore_252d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _zscore_rolling(base, 252)

def jump_150_jump_clustering_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_150_jump_clustering_rank_252d
    ECONOMIC RATIONALE: Recent clusters of price jumps.
    """
    base = (close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()
    return _rank_pct(base, 252)

def jump_151_intraday_jump_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_151_intraday_jump_lvl_5d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rolling_mean(base, 5)

def jump_152_intraday_jump_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_152_intraday_jump_zscore_5d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _zscore_rolling(base, 5)

def jump_153_intraday_jump_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_153_intraday_jump_rank_5d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rank_pct(base, 5)

def jump_154_intraday_jump_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_154_intraday_jump_lvl_21d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rolling_mean(base, 21)

def jump_155_intraday_jump_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_155_intraday_jump_zscore_21d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _zscore_rolling(base, 21)

def jump_156_intraday_jump_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_156_intraday_jump_rank_21d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rank_pct(base, 21)

def jump_157_intraday_jump_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_157_intraday_jump_lvl_63d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rolling_mean(base, 63)

def jump_158_intraday_jump_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_158_intraday_jump_zscore_63d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _zscore_rolling(base, 63)

def jump_159_intraday_jump_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_159_intraday_jump_rank_63d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rank_pct(base, 63)

def jump_160_intraday_jump_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_160_intraday_jump_lvl_126d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rolling_mean(base, 126)

def jump_161_intraday_jump_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_161_intraday_jump_zscore_126d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _zscore_rolling(base, 126)

def jump_162_intraday_jump_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_162_intraday_jump_rank_126d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rank_pct(base, 126)

def jump_163_intraday_jump_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_163_intraday_jump_lvl_252d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rolling_mean(base, 252)

def jump_164_intraday_jump_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_164_intraday_jump_zscore_252d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _zscore_rolling(base, 252)

def jump_165_intraday_jump_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_165_intraday_jump_rank_252d
    ECONOMIC RATIONALE: Intraday range as a proxy for jump potential.
    """
    base = (high - low) / close.rolling(21).std()
    return _rank_pct(base, 252)

def jump_166_jump_regime_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_166_jump_regime_lvl_5d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 5)

def jump_167_jump_regime_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_167_jump_regime_zscore_5d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 5)

def jump_168_jump_regime_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_168_jump_regime_rank_5d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 5)

def jump_169_jump_regime_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_169_jump_regime_lvl_21d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 21)

def jump_170_jump_regime_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_170_jump_regime_zscore_21d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 21)

def jump_171_jump_regime_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_171_jump_regime_rank_21d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 21)

def jump_172_jump_regime_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_172_jump_regime_lvl_63d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 63)

def jump_173_jump_regime_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_173_jump_regime_zscore_63d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 63)

def jump_174_jump_regime_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_174_jump_regime_rank_63d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 63)

def jump_175_jump_regime_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_175_jump_regime_lvl_126d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 126)

def jump_176_jump_regime_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_176_jump_regime_zscore_126d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 126)

def jump_177_jump_regime_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_177_jump_regime_rank_126d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 126)

def jump_178_jump_regime_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_178_jump_regime_lvl_252d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rolling_mean(base, 252)

def jump_179_jump_regime_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_179_jump_regime_zscore_252d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _zscore_rolling(base, 252)

def jump_180_jump_regime_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_180_jump_regime_rank_252d
    ECONOMIC RATIONALE: Ratio of recent to long-term jumpiness.
    """
    base = close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()
    return _rank_pct(base, 252)

def jump_181_jump_impact_on_drawdown_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_181_jump_impact_on_drawdown_lvl_5d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rolling_mean(base, 5)

def jump_182_jump_impact_on_drawdown_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_182_jump_impact_on_drawdown_zscore_5d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _zscore_rolling(base, 5)

def jump_183_jump_impact_on_drawdown_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_183_jump_impact_on_drawdown_rank_5d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rank_pct(base, 5)

def jump_184_jump_impact_on_drawdown_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_184_jump_impact_on_drawdown_lvl_21d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rolling_mean(base, 21)

def jump_185_jump_impact_on_drawdown_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_185_jump_impact_on_drawdown_zscore_21d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _zscore_rolling(base, 21)

def jump_186_jump_impact_on_drawdown_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_186_jump_impact_on_drawdown_rank_21d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rank_pct(base, 21)

def jump_187_jump_impact_on_drawdown_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_187_jump_impact_on_drawdown_lvl_63d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rolling_mean(base, 63)

def jump_188_jump_impact_on_drawdown_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_188_jump_impact_on_drawdown_zscore_63d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _zscore_rolling(base, 63)

def jump_189_jump_impact_on_drawdown_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_189_jump_impact_on_drawdown_rank_63d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rank_pct(base, 63)

def jump_190_jump_impact_on_drawdown_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_190_jump_impact_on_drawdown_lvl_126d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rolling_mean(base, 126)

def jump_191_jump_impact_on_drawdown_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_191_jump_impact_on_drawdown_zscore_126d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _zscore_rolling(base, 126)

def jump_192_jump_impact_on_drawdown_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_192_jump_impact_on_drawdown_rank_126d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rank_pct(base, 126)

def jump_193_jump_impact_on_drawdown_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_193_jump_impact_on_drawdown_lvl_252d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rolling_mean(base, 252)

def jump_194_jump_impact_on_drawdown_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_194_jump_impact_on_drawdown_zscore_252d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _zscore_rolling(base, 252)

def jump_195_jump_impact_on_drawdown_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_195_jump_impact_on_drawdown_rank_252d
    ECONOMIC RATIONALE: Jumps occurring within established drawdowns.
    """
    base = close.diff(1) * (close < close.rolling(63).max())
    return _rank_pct(base, 252)

def jump_196_jump_entropy_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_196_jump_entropy_lvl_5d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 5)

def jump_197_jump_entropy_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_197_jump_entropy_zscore_5d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 5)

def jump_198_jump_entropy_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_198_jump_entropy_rank_5d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 5)

def jump_199_jump_entropy_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_199_jump_entropy_lvl_21d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 21)

def jump_200_jump_entropy_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_200_jump_entropy_zscore_21d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 21)

def jump_201_jump_entropy_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_201_jump_entropy_rank_21d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 21)

def jump_202_jump_entropy_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_202_jump_entropy_lvl_63d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 63)

def jump_203_jump_entropy_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_203_jump_entropy_zscore_63d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 63)

def jump_204_jump_entropy_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_204_jump_entropy_rank_63d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 63)

def jump_205_jump_entropy_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_205_jump_entropy_lvl_126d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 126)

def jump_206_jump_entropy_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_206_jump_entropy_zscore_126d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 126)

def jump_207_jump_entropy_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_207_jump_entropy_rank_126d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 126)

def jump_208_jump_entropy_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_208_jump_entropy_lvl_252d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rolling_mean(base, 252)

def jump_209_jump_entropy_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_209_jump_entropy_zscore_252d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _zscore_rolling(base, 252)

def jump_210_jump_entropy_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_210_jump_entropy_rank_252d
    ECONOMIC RATIONALE: Unpredictability of price jump magnitudes.
    """
    base = close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))
    return _rank_pct(base, 252)

def jump_211_jump_tail_risk_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_211_jump_tail_risk_lvl_5d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 5)

def jump_212_jump_tail_risk_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_212_jump_tail_risk_zscore_5d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 5)

def jump_213_jump_tail_risk_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_213_jump_tail_risk_rank_5d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 5)

def jump_214_jump_tail_risk_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_214_jump_tail_risk_lvl_21d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 21)

def jump_215_jump_tail_risk_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_215_jump_tail_risk_zscore_21d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 21)

def jump_216_jump_tail_risk_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_216_jump_tail_risk_rank_21d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 21)

def jump_217_jump_tail_risk_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_217_jump_tail_risk_lvl_63d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 63)

def jump_218_jump_tail_risk_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_218_jump_tail_risk_zscore_63d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 63)

def jump_219_jump_tail_risk_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_219_jump_tail_risk_rank_63d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 63)

def jump_220_jump_tail_risk_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_220_jump_tail_risk_lvl_126d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 126)

def jump_221_jump_tail_risk_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_221_jump_tail_risk_zscore_126d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 126)

def jump_222_jump_tail_risk_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_222_jump_tail_risk_rank_126d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 126)

def jump_223_jump_tail_risk_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_223_jump_tail_risk_lvl_252d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rolling_mean(base, 252)

def jump_224_jump_tail_risk_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_224_jump_tail_risk_zscore_252d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _zscore_rolling(base, 252)

def jump_225_jump_tail_risk_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_225_jump_tail_risk_rank_252d
    ECONOMIC RATIONALE: Binary indicator of severe negative jumps.
    """
    base = (close.diff(1) < -3*close.rolling(252).std()).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V111_REGISTRY_2 = {
    "jump_121_jump_decay_rate_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_121_jump_decay_rate_lvl_5d},
    "jump_122_jump_decay_rate_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_122_jump_decay_rate_zscore_5d},
    "jump_123_jump_decay_rate_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_123_jump_decay_rate_rank_5d},
    "jump_124_jump_decay_rate_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_124_jump_decay_rate_lvl_21d},
    "jump_125_jump_decay_rate_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_125_jump_decay_rate_zscore_21d},
    "jump_126_jump_decay_rate_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_126_jump_decay_rate_rank_21d},
    "jump_127_jump_decay_rate_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_127_jump_decay_rate_lvl_63d},
    "jump_128_jump_decay_rate_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_128_jump_decay_rate_zscore_63d},
    "jump_129_jump_decay_rate_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_129_jump_decay_rate_rank_63d},
    "jump_130_jump_decay_rate_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_130_jump_decay_rate_lvl_126d},
    "jump_131_jump_decay_rate_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_131_jump_decay_rate_zscore_126d},
    "jump_132_jump_decay_rate_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_132_jump_decay_rate_rank_126d},
    "jump_133_jump_decay_rate_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_133_jump_decay_rate_lvl_252d},
    "jump_134_jump_decay_rate_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_134_jump_decay_rate_zscore_252d},
    "jump_135_jump_decay_rate_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_135_jump_decay_rate_rank_252d},
    "jump_136_jump_clustering_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_136_jump_clustering_lvl_5d},
    "jump_137_jump_clustering_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_137_jump_clustering_zscore_5d},
    "jump_138_jump_clustering_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_138_jump_clustering_rank_5d},
    "jump_139_jump_clustering_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_139_jump_clustering_lvl_21d},
    "jump_140_jump_clustering_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_140_jump_clustering_zscore_21d},
    "jump_141_jump_clustering_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_141_jump_clustering_rank_21d},
    "jump_142_jump_clustering_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_142_jump_clustering_lvl_63d},
    "jump_143_jump_clustering_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_143_jump_clustering_zscore_63d},
    "jump_144_jump_clustering_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_144_jump_clustering_rank_63d},
    "jump_145_jump_clustering_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_145_jump_clustering_lvl_126d},
    "jump_146_jump_clustering_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_146_jump_clustering_zscore_126d},
    "jump_147_jump_clustering_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_147_jump_clustering_rank_126d},
    "jump_148_jump_clustering_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_148_jump_clustering_lvl_252d},
    "jump_149_jump_clustering_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_149_jump_clustering_zscore_252d},
    "jump_150_jump_clustering_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_150_jump_clustering_rank_252d},
    "jump_151_intraday_jump_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_151_intraday_jump_lvl_5d},
    "jump_152_intraday_jump_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_152_intraday_jump_zscore_5d},
    "jump_153_intraday_jump_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_153_intraday_jump_rank_5d},
    "jump_154_intraday_jump_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_154_intraday_jump_lvl_21d},
    "jump_155_intraday_jump_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_155_intraday_jump_zscore_21d},
    "jump_156_intraday_jump_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_156_intraday_jump_rank_21d},
    "jump_157_intraday_jump_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_157_intraday_jump_lvl_63d},
    "jump_158_intraday_jump_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_158_intraday_jump_zscore_63d},
    "jump_159_intraday_jump_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_159_intraday_jump_rank_63d},
    "jump_160_intraday_jump_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_160_intraday_jump_lvl_126d},
    "jump_161_intraday_jump_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_161_intraday_jump_zscore_126d},
    "jump_162_intraday_jump_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_162_intraday_jump_rank_126d},
    "jump_163_intraday_jump_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_163_intraday_jump_lvl_252d},
    "jump_164_intraday_jump_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_164_intraday_jump_zscore_252d},
    "jump_165_intraday_jump_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_165_intraday_jump_rank_252d},
    "jump_166_jump_regime_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_166_jump_regime_lvl_5d},
    "jump_167_jump_regime_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_167_jump_regime_zscore_5d},
    "jump_168_jump_regime_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_168_jump_regime_rank_5d},
    "jump_169_jump_regime_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_169_jump_regime_lvl_21d},
    "jump_170_jump_regime_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_170_jump_regime_zscore_21d},
    "jump_171_jump_regime_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_171_jump_regime_rank_21d},
    "jump_172_jump_regime_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_172_jump_regime_lvl_63d},
    "jump_173_jump_regime_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_173_jump_regime_zscore_63d},
    "jump_174_jump_regime_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_174_jump_regime_rank_63d},
    "jump_175_jump_regime_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_175_jump_regime_lvl_126d},
    "jump_176_jump_regime_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_176_jump_regime_zscore_126d},
    "jump_177_jump_regime_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_177_jump_regime_rank_126d},
    "jump_178_jump_regime_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_178_jump_regime_lvl_252d},
    "jump_179_jump_regime_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_179_jump_regime_zscore_252d},
    "jump_180_jump_regime_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_180_jump_regime_rank_252d},
    "jump_181_jump_impact_on_drawdown_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_181_jump_impact_on_drawdown_lvl_5d},
    "jump_182_jump_impact_on_drawdown_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_182_jump_impact_on_drawdown_zscore_5d},
    "jump_183_jump_impact_on_drawdown_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_183_jump_impact_on_drawdown_rank_5d},
    "jump_184_jump_impact_on_drawdown_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_184_jump_impact_on_drawdown_lvl_21d},
    "jump_185_jump_impact_on_drawdown_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_185_jump_impact_on_drawdown_zscore_21d},
    "jump_186_jump_impact_on_drawdown_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_186_jump_impact_on_drawdown_rank_21d},
    "jump_187_jump_impact_on_drawdown_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_187_jump_impact_on_drawdown_lvl_63d},
    "jump_188_jump_impact_on_drawdown_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_188_jump_impact_on_drawdown_zscore_63d},
    "jump_189_jump_impact_on_drawdown_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_189_jump_impact_on_drawdown_rank_63d},
    "jump_190_jump_impact_on_drawdown_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_190_jump_impact_on_drawdown_lvl_126d},
    "jump_191_jump_impact_on_drawdown_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_191_jump_impact_on_drawdown_zscore_126d},
    "jump_192_jump_impact_on_drawdown_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_192_jump_impact_on_drawdown_rank_126d},
    "jump_193_jump_impact_on_drawdown_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_193_jump_impact_on_drawdown_lvl_252d},
    "jump_194_jump_impact_on_drawdown_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_194_jump_impact_on_drawdown_zscore_252d},
    "jump_195_jump_impact_on_drawdown_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_195_jump_impact_on_drawdown_rank_252d},
    "jump_196_jump_entropy_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_196_jump_entropy_lvl_5d},
    "jump_197_jump_entropy_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_197_jump_entropy_zscore_5d},
    "jump_198_jump_entropy_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_198_jump_entropy_rank_5d},
    "jump_199_jump_entropy_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_199_jump_entropy_lvl_21d},
    "jump_200_jump_entropy_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_200_jump_entropy_zscore_21d},
    "jump_201_jump_entropy_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_201_jump_entropy_rank_21d},
    "jump_202_jump_entropy_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_202_jump_entropy_lvl_63d},
    "jump_203_jump_entropy_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_203_jump_entropy_zscore_63d},
    "jump_204_jump_entropy_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_204_jump_entropy_rank_63d},
    "jump_205_jump_entropy_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_205_jump_entropy_lvl_126d},
    "jump_206_jump_entropy_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_206_jump_entropy_zscore_126d},
    "jump_207_jump_entropy_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_207_jump_entropy_rank_126d},
    "jump_208_jump_entropy_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_208_jump_entropy_lvl_252d},
    "jump_209_jump_entropy_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_209_jump_entropy_zscore_252d},
    "jump_210_jump_entropy_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_210_jump_entropy_rank_252d},
    "jump_211_jump_tail_risk_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_211_jump_tail_risk_lvl_5d},
    "jump_212_jump_tail_risk_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_212_jump_tail_risk_zscore_5d},
    "jump_213_jump_tail_risk_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_213_jump_tail_risk_rank_5d},
    "jump_214_jump_tail_risk_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_214_jump_tail_risk_lvl_21d},
    "jump_215_jump_tail_risk_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_215_jump_tail_risk_zscore_21d},
    "jump_216_jump_tail_risk_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_216_jump_tail_risk_rank_21d},
    "jump_217_jump_tail_risk_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_217_jump_tail_risk_lvl_63d},
    "jump_218_jump_tail_risk_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_218_jump_tail_risk_zscore_63d},
    "jump_219_jump_tail_risk_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_219_jump_tail_risk_rank_63d},
    "jump_220_jump_tail_risk_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_220_jump_tail_risk_lvl_126d},
    "jump_221_jump_tail_risk_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_221_jump_tail_risk_zscore_126d},
    "jump_222_jump_tail_risk_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_222_jump_tail_risk_rank_126d},
    "jump_223_jump_tail_risk_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_223_jump_tail_risk_lvl_252d},
    "jump_224_jump_tail_risk_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_224_jump_tail_risk_zscore_252d},
    "jump_225_jump_tail_risk_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_225_jump_tail_risk_rank_252d},
}
