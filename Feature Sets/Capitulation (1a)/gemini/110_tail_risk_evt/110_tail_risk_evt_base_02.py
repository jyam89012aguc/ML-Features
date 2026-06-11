"""
110_tail_risk_evt — Base Features Part 2
Domain: tail_risk_evt
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

def trev_121_gap_down_risk_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_121_gap_down_risk_lvl_5d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_122_gap_down_risk_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_122_gap_down_risk_zscore_5d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_123_gap_down_risk_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_123_gap_down_risk_rank_5d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rank_pct(base, 5)

def trev_124_gap_down_risk_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_124_gap_down_risk_lvl_21d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_125_gap_down_risk_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_125_gap_down_risk_zscore_21d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_126_gap_down_risk_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_126_gap_down_risk_rank_21d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rank_pct(base, 21)

def trev_127_gap_down_risk_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_127_gap_down_risk_lvl_63d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_128_gap_down_risk_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_128_gap_down_risk_zscore_63d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_129_gap_down_risk_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_129_gap_down_risk_rank_63d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rank_pct(base, 63)

def trev_130_gap_down_risk_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_130_gap_down_risk_lvl_126d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_131_gap_down_risk_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_131_gap_down_risk_zscore_126d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_132_gap_down_risk_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_132_gap_down_risk_rank_126d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rank_pct(base, 126)

def trev_133_gap_down_risk_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_133_gap_down_risk_lvl_252d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_134_gap_down_risk_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_134_gap_down_risk_zscore_252d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_135_gap_down_risk_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_135_gap_down_risk_rank_252d
    ECONOMIC RATIONALE: 1st percentile of overnight gaps.
    """
    base = (open / close.shift(1) - 1).rolling(252).quantile(0.01)
    return _rank_pct(base, 252)

def trev_136_tail_persistence_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_136_tail_persistence_lvl_5d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rolling_mean(base, 5)

def trev_137_tail_persistence_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_137_tail_persistence_zscore_5d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _zscore_rolling(base, 5)

def trev_138_tail_persistence_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_138_tail_persistence_rank_5d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rank_pct(base, 5)

def trev_139_tail_persistence_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_139_tail_persistence_lvl_21d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rolling_mean(base, 21)

def trev_140_tail_persistence_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_140_tail_persistence_zscore_21d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _zscore_rolling(base, 21)

def trev_141_tail_persistence_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_141_tail_persistence_rank_21d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rank_pct(base, 21)

def trev_142_tail_persistence_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_142_tail_persistence_lvl_63d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rolling_mean(base, 63)

def trev_143_tail_persistence_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_143_tail_persistence_zscore_63d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _zscore_rolling(base, 63)

def trev_144_tail_persistence_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_144_tail_persistence_rank_63d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rank_pct(base, 63)

def trev_145_tail_persistence_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_145_tail_persistence_lvl_126d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rolling_mean(base, 126)

def trev_146_tail_persistence_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_146_tail_persistence_zscore_126d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _zscore_rolling(base, 126)

def trev_147_tail_persistence_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_147_tail_persistence_rank_126d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rank_pct(base, 126)

def trev_148_tail_persistence_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_148_tail_persistence_lvl_252d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rolling_mean(base, 252)

def trev_149_tail_persistence_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_149_tail_persistence_zscore_252d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _zscore_rolling(base, 252)

def trev_150_tail_persistence_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_150_tail_persistence_rank_252d
    ECONOMIC RATIONALE: Sequential tail events.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)
    return _rank_pct(base, 252)

def trev_151_tail_volatility_spread_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_151_tail_volatility_spread_lvl_5d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 5)

def trev_152_tail_volatility_spread_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_152_tail_volatility_spread_zscore_5d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 5)

def trev_153_tail_volatility_spread_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_153_tail_volatility_spread_rank_5d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 5)

def trev_154_tail_volatility_spread_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_154_tail_volatility_spread_lvl_21d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 21)

def trev_155_tail_volatility_spread_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_155_tail_volatility_spread_zscore_21d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 21)

def trev_156_tail_volatility_spread_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_156_tail_volatility_spread_rank_21d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 21)

def trev_157_tail_volatility_spread_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_157_tail_volatility_spread_lvl_63d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 63)

def trev_158_tail_volatility_spread_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_158_tail_volatility_spread_zscore_63d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 63)

def trev_159_tail_volatility_spread_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_159_tail_volatility_spread_rank_63d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 63)

def trev_160_tail_volatility_spread_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_160_tail_volatility_spread_lvl_126d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 126)

def trev_161_tail_volatility_spread_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_161_tail_volatility_spread_zscore_126d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 126)

def trev_162_tail_volatility_spread_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_162_tail_volatility_spread_rank_126d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 126)

def trev_163_tail_volatility_spread_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_163_tail_volatility_spread_lvl_252d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 252)

def trev_164_tail_volatility_spread_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_164_tail_volatility_spread_zscore_252d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 252)

def trev_165_tail_volatility_spread_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_165_tail_volatility_spread_rank_252d
    ECONOMIC RATIONALE: Short-term vs long-term volatility expansion.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 252)

def trev_166_downside_deviation_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_166_downside_deviation_lvl_5d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rolling_mean(base, 5)

def trev_167_downside_deviation_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_167_downside_deviation_zscore_5d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _zscore_rolling(base, 5)

def trev_168_downside_deviation_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_168_downside_deviation_rank_5d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rank_pct(base, 5)

def trev_169_downside_deviation_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_169_downside_deviation_lvl_21d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rolling_mean(base, 21)

def trev_170_downside_deviation_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_170_downside_deviation_zscore_21d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _zscore_rolling(base, 21)

def trev_171_downside_deviation_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_171_downside_deviation_rank_21d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rank_pct(base, 21)

def trev_172_downside_deviation_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_172_downside_deviation_lvl_63d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rolling_mean(base, 63)

def trev_173_downside_deviation_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_173_downside_deviation_zscore_63d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _zscore_rolling(base, 63)

def trev_174_downside_deviation_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_174_downside_deviation_rank_63d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rank_pct(base, 63)

def trev_175_downside_deviation_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_175_downside_deviation_lvl_126d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rolling_mean(base, 126)

def trev_176_downside_deviation_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_176_downside_deviation_zscore_126d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _zscore_rolling(base, 126)

def trev_177_downside_deviation_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_177_downside_deviation_rank_126d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rank_pct(base, 126)

def trev_178_downside_deviation_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_178_downside_deviation_lvl_252d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rolling_mean(base, 252)

def trev_179_downside_deviation_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_179_downside_deviation_zscore_252d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _zscore_rolling(base, 252)

def trev_180_downside_deviation_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_180_downside_deviation_rank_252d
    ECONOMIC RATIONALE: Standard deviation of negative returns only.
    """
    base = close.pct_change(1).clip(upper=0).rolling(252).std()
    return _rank_pct(base, 252)

def trev_181_tail_event_cluster_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_181_tail_event_cluster_lvl_5d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rolling_mean(base, 5)

def trev_182_tail_event_cluster_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_182_tail_event_cluster_zscore_5d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _zscore_rolling(base, 5)

def trev_183_tail_event_cluster_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_183_tail_event_cluster_rank_5d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rank_pct(base, 5)

def trev_184_tail_event_cluster_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_184_tail_event_cluster_lvl_21d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rolling_mean(base, 21)

def trev_185_tail_event_cluster_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_185_tail_event_cluster_zscore_21d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _zscore_rolling(base, 21)

def trev_186_tail_event_cluster_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_186_tail_event_cluster_rank_21d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rank_pct(base, 21)

def trev_187_tail_event_cluster_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_187_tail_event_cluster_lvl_63d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rolling_mean(base, 63)

def trev_188_tail_event_cluster_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_188_tail_event_cluster_zscore_63d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _zscore_rolling(base, 63)

def trev_189_tail_event_cluster_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_189_tail_event_cluster_rank_63d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rank_pct(base, 63)

def trev_190_tail_event_cluster_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_190_tail_event_cluster_lvl_126d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rolling_mean(base, 126)

def trev_191_tail_event_cluster_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_191_tail_event_cluster_zscore_126d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _zscore_rolling(base, 126)

def trev_192_tail_event_cluster_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_192_tail_event_cluster_rank_126d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rank_pct(base, 126)

def trev_193_tail_event_cluster_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_193_tail_event_cluster_lvl_252d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rolling_mean(base, 252)

def trev_194_tail_event_cluster_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_194_tail_event_cluster_zscore_252d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _zscore_rolling(base, 252)

def trev_195_tail_event_cluster_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_195_tail_event_cluster_rank_252d
    ECONOMIC RATIONALE: Clustering of extreme negative returns.
    """
    base = ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())
    return _rank_pct(base, 252)

def trev_196_tail_drawdown_corr_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_196_tail_drawdown_corr_lvl_5d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rolling_mean(base, 5)

def trev_197_tail_drawdown_corr_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_197_tail_drawdown_corr_zscore_5d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _zscore_rolling(base, 5)

def trev_198_tail_drawdown_corr_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_198_tail_drawdown_corr_rank_5d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rank_pct(base, 5)

def trev_199_tail_drawdown_corr_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_199_tail_drawdown_corr_lvl_21d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rolling_mean(base, 21)

def trev_200_tail_drawdown_corr_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_200_tail_drawdown_corr_zscore_21d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _zscore_rolling(base, 21)

def trev_201_tail_drawdown_corr_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_201_tail_drawdown_corr_rank_21d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rank_pct(base, 21)

def trev_202_tail_drawdown_corr_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_202_tail_drawdown_corr_lvl_63d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rolling_mean(base, 63)

def trev_203_tail_drawdown_corr_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_203_tail_drawdown_corr_zscore_63d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _zscore_rolling(base, 63)

def trev_204_tail_drawdown_corr_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_204_tail_drawdown_corr_rank_63d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rank_pct(base, 63)

def trev_205_tail_drawdown_corr_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_205_tail_drawdown_corr_lvl_126d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rolling_mean(base, 126)

def trev_206_tail_drawdown_corr_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_206_tail_drawdown_corr_zscore_126d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _zscore_rolling(base, 126)

def trev_207_tail_drawdown_corr_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_207_tail_drawdown_corr_rank_126d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rank_pct(base, 126)

def trev_208_tail_drawdown_corr_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_208_tail_drawdown_corr_lvl_252d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rolling_mean(base, 252)

def trev_209_tail_drawdown_corr_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_209_tail_drawdown_corr_zscore_252d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _zscore_rolling(base, 252)

def trev_210_tail_drawdown_corr_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_210_tail_drawdown_corr_rank_252d
    ECONOMIC RATIONALE: Correlation between tail risk and drawdown depth.
    """
    base = close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)
    return _rank_pct(base, 252)

def trev_211_black_swan_proxy_lvl_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_211_black_swan_proxy_lvl_5d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 5)

def trev_212_black_swan_proxy_zscore_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_212_black_swan_proxy_zscore_5d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 5)

def trev_213_black_swan_proxy_rank_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_213_black_swan_proxy_rank_5d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 5)

def trev_214_black_swan_proxy_lvl_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_214_black_swan_proxy_lvl_21d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 21)

def trev_215_black_swan_proxy_zscore_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_215_black_swan_proxy_zscore_21d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 21)

def trev_216_black_swan_proxy_rank_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_216_black_swan_proxy_rank_21d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 21)

def trev_217_black_swan_proxy_lvl_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_217_black_swan_proxy_lvl_63d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 63)

def trev_218_black_swan_proxy_zscore_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_218_black_swan_proxy_zscore_63d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 63)

def trev_219_black_swan_proxy_rank_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_219_black_swan_proxy_rank_63d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 63)

def trev_220_black_swan_proxy_lvl_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_220_black_swan_proxy_lvl_126d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 126)

def trev_221_black_swan_proxy_zscore_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_221_black_swan_proxy_zscore_126d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 126)

def trev_222_black_swan_proxy_rank_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_222_black_swan_proxy_rank_126d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 126)

def trev_223_black_swan_proxy_lvl_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_223_black_swan_proxy_lvl_252d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 252)

def trev_224_black_swan_proxy_zscore_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_224_black_swan_proxy_zscore_252d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 252)

def trev_225_black_swan_proxy_rank_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_225_black_swan_proxy_rank_252d
    ECONOMIC RATIONALE: Occurrence of 4-sigma negative events.
    """
    base = (close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V110_REGISTRY_2 = {
    "trev_121_gap_down_risk_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_121_gap_down_risk_lvl_5d},
    "trev_122_gap_down_risk_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_122_gap_down_risk_zscore_5d},
    "trev_123_gap_down_risk_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_123_gap_down_risk_rank_5d},
    "trev_124_gap_down_risk_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_124_gap_down_risk_lvl_21d},
    "trev_125_gap_down_risk_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_125_gap_down_risk_zscore_21d},
    "trev_126_gap_down_risk_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_126_gap_down_risk_rank_21d},
    "trev_127_gap_down_risk_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_127_gap_down_risk_lvl_63d},
    "trev_128_gap_down_risk_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_128_gap_down_risk_zscore_63d},
    "trev_129_gap_down_risk_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_129_gap_down_risk_rank_63d},
    "trev_130_gap_down_risk_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_130_gap_down_risk_lvl_126d},
    "trev_131_gap_down_risk_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_131_gap_down_risk_zscore_126d},
    "trev_132_gap_down_risk_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_132_gap_down_risk_rank_126d},
    "trev_133_gap_down_risk_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_133_gap_down_risk_lvl_252d},
    "trev_134_gap_down_risk_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_134_gap_down_risk_zscore_252d},
    "trev_135_gap_down_risk_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_135_gap_down_risk_rank_252d},
    "trev_136_tail_persistence_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_136_tail_persistence_lvl_5d},
    "trev_137_tail_persistence_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_137_tail_persistence_zscore_5d},
    "trev_138_tail_persistence_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_138_tail_persistence_rank_5d},
    "trev_139_tail_persistence_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_139_tail_persistence_lvl_21d},
    "trev_140_tail_persistence_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_140_tail_persistence_zscore_21d},
    "trev_141_tail_persistence_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_141_tail_persistence_rank_21d},
    "trev_142_tail_persistence_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_142_tail_persistence_lvl_63d},
    "trev_143_tail_persistence_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_143_tail_persistence_zscore_63d},
    "trev_144_tail_persistence_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_144_tail_persistence_rank_63d},
    "trev_145_tail_persistence_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_145_tail_persistence_lvl_126d},
    "trev_146_tail_persistence_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_146_tail_persistence_zscore_126d},
    "trev_147_tail_persistence_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_147_tail_persistence_rank_126d},
    "trev_148_tail_persistence_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_148_tail_persistence_lvl_252d},
    "trev_149_tail_persistence_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_149_tail_persistence_zscore_252d},
    "trev_150_tail_persistence_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_150_tail_persistence_rank_252d},
    "trev_151_tail_volatility_spread_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_151_tail_volatility_spread_lvl_5d},
    "trev_152_tail_volatility_spread_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_152_tail_volatility_spread_zscore_5d},
    "trev_153_tail_volatility_spread_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_153_tail_volatility_spread_rank_5d},
    "trev_154_tail_volatility_spread_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_154_tail_volatility_spread_lvl_21d},
    "trev_155_tail_volatility_spread_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_155_tail_volatility_spread_zscore_21d},
    "trev_156_tail_volatility_spread_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_156_tail_volatility_spread_rank_21d},
    "trev_157_tail_volatility_spread_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_157_tail_volatility_spread_lvl_63d},
    "trev_158_tail_volatility_spread_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_158_tail_volatility_spread_zscore_63d},
    "trev_159_tail_volatility_spread_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_159_tail_volatility_spread_rank_63d},
    "trev_160_tail_volatility_spread_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_160_tail_volatility_spread_lvl_126d},
    "trev_161_tail_volatility_spread_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_161_tail_volatility_spread_zscore_126d},
    "trev_162_tail_volatility_spread_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_162_tail_volatility_spread_rank_126d},
    "trev_163_tail_volatility_spread_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_163_tail_volatility_spread_lvl_252d},
    "trev_164_tail_volatility_spread_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_164_tail_volatility_spread_zscore_252d},
    "trev_165_tail_volatility_spread_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_165_tail_volatility_spread_rank_252d},
    "trev_166_downside_deviation_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_166_downside_deviation_lvl_5d},
    "trev_167_downside_deviation_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_167_downside_deviation_zscore_5d},
    "trev_168_downside_deviation_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_168_downside_deviation_rank_5d},
    "trev_169_downside_deviation_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_169_downside_deviation_lvl_21d},
    "trev_170_downside_deviation_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_170_downside_deviation_zscore_21d},
    "trev_171_downside_deviation_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_171_downside_deviation_rank_21d},
    "trev_172_downside_deviation_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_172_downside_deviation_lvl_63d},
    "trev_173_downside_deviation_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_173_downside_deviation_zscore_63d},
    "trev_174_downside_deviation_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_174_downside_deviation_rank_63d},
    "trev_175_downside_deviation_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_175_downside_deviation_lvl_126d},
    "trev_176_downside_deviation_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_176_downside_deviation_zscore_126d},
    "trev_177_downside_deviation_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_177_downside_deviation_rank_126d},
    "trev_178_downside_deviation_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_178_downside_deviation_lvl_252d},
    "trev_179_downside_deviation_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_179_downside_deviation_zscore_252d},
    "trev_180_downside_deviation_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_180_downside_deviation_rank_252d},
    "trev_181_tail_event_cluster_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_181_tail_event_cluster_lvl_5d},
    "trev_182_tail_event_cluster_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_182_tail_event_cluster_zscore_5d},
    "trev_183_tail_event_cluster_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_183_tail_event_cluster_rank_5d},
    "trev_184_tail_event_cluster_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_184_tail_event_cluster_lvl_21d},
    "trev_185_tail_event_cluster_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_185_tail_event_cluster_zscore_21d},
    "trev_186_tail_event_cluster_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_186_tail_event_cluster_rank_21d},
    "trev_187_tail_event_cluster_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_187_tail_event_cluster_lvl_63d},
    "trev_188_tail_event_cluster_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_188_tail_event_cluster_zscore_63d},
    "trev_189_tail_event_cluster_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_189_tail_event_cluster_rank_63d},
    "trev_190_tail_event_cluster_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_190_tail_event_cluster_lvl_126d},
    "trev_191_tail_event_cluster_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_191_tail_event_cluster_zscore_126d},
    "trev_192_tail_event_cluster_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_192_tail_event_cluster_rank_126d},
    "trev_193_tail_event_cluster_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_193_tail_event_cluster_lvl_252d},
    "trev_194_tail_event_cluster_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_194_tail_event_cluster_zscore_252d},
    "trev_195_tail_event_cluster_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_195_tail_event_cluster_rank_252d},
    "trev_196_tail_drawdown_corr_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_196_tail_drawdown_corr_lvl_5d},
    "trev_197_tail_drawdown_corr_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_197_tail_drawdown_corr_zscore_5d},
    "trev_198_tail_drawdown_corr_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_198_tail_drawdown_corr_rank_5d},
    "trev_199_tail_drawdown_corr_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_199_tail_drawdown_corr_lvl_21d},
    "trev_200_tail_drawdown_corr_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_200_tail_drawdown_corr_zscore_21d},
    "trev_201_tail_drawdown_corr_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_201_tail_drawdown_corr_rank_21d},
    "trev_202_tail_drawdown_corr_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_202_tail_drawdown_corr_lvl_63d},
    "trev_203_tail_drawdown_corr_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_203_tail_drawdown_corr_zscore_63d},
    "trev_204_tail_drawdown_corr_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_204_tail_drawdown_corr_rank_63d},
    "trev_205_tail_drawdown_corr_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_205_tail_drawdown_corr_lvl_126d},
    "trev_206_tail_drawdown_corr_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_206_tail_drawdown_corr_zscore_126d},
    "trev_207_tail_drawdown_corr_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_207_tail_drawdown_corr_rank_126d},
    "trev_208_tail_drawdown_corr_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_208_tail_drawdown_corr_lvl_252d},
    "trev_209_tail_drawdown_corr_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_209_tail_drawdown_corr_zscore_252d},
    "trev_210_tail_drawdown_corr_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_210_tail_drawdown_corr_rank_252d},
    "trev_211_black_swan_proxy_lvl_5d": {"inputs": ["close", "low", "open"], "func": trev_211_black_swan_proxy_lvl_5d},
    "trev_212_black_swan_proxy_zscore_5d": {"inputs": ["close", "low", "open"], "func": trev_212_black_swan_proxy_zscore_5d},
    "trev_213_black_swan_proxy_rank_5d": {"inputs": ["close", "low", "open"], "func": trev_213_black_swan_proxy_rank_5d},
    "trev_214_black_swan_proxy_lvl_21d": {"inputs": ["close", "low", "open"], "func": trev_214_black_swan_proxy_lvl_21d},
    "trev_215_black_swan_proxy_zscore_21d": {"inputs": ["close", "low", "open"], "func": trev_215_black_swan_proxy_zscore_21d},
    "trev_216_black_swan_proxy_rank_21d": {"inputs": ["close", "low", "open"], "func": trev_216_black_swan_proxy_rank_21d},
    "trev_217_black_swan_proxy_lvl_63d": {"inputs": ["close", "low", "open"], "func": trev_217_black_swan_proxy_lvl_63d},
    "trev_218_black_swan_proxy_zscore_63d": {"inputs": ["close", "low", "open"], "func": trev_218_black_swan_proxy_zscore_63d},
    "trev_219_black_swan_proxy_rank_63d": {"inputs": ["close", "low", "open"], "func": trev_219_black_swan_proxy_rank_63d},
    "trev_220_black_swan_proxy_lvl_126d": {"inputs": ["close", "low", "open"], "func": trev_220_black_swan_proxy_lvl_126d},
    "trev_221_black_swan_proxy_zscore_126d": {"inputs": ["close", "low", "open"], "func": trev_221_black_swan_proxy_zscore_126d},
    "trev_222_black_swan_proxy_rank_126d": {"inputs": ["close", "low", "open"], "func": trev_222_black_swan_proxy_rank_126d},
    "trev_223_black_swan_proxy_lvl_252d": {"inputs": ["close", "low", "open"], "func": trev_223_black_swan_proxy_lvl_252d},
    "trev_224_black_swan_proxy_zscore_252d": {"inputs": ["close", "low", "open"], "func": trev_224_black_swan_proxy_zscore_252d},
    "trev_225_black_swan_proxy_rank_252d": {"inputs": ["close", "low", "open"], "func": trev_225_black_swan_proxy_rank_252d},
}
