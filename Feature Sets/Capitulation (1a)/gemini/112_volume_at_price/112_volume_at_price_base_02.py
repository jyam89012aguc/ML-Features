"""
112_volume_at_price — Base Features Part 2
Domain: volume_at_price
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

def vapr_121_price_volume_overlap_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_121_price_volume_overlap_lvl_5d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rolling_mean(base, 5)

def vapr_122_price_volume_overlap_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_122_price_volume_overlap_zscore_5d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _zscore_rolling(base, 5)

def vapr_123_price_volume_overlap_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_123_price_volume_overlap_rank_5d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rank_pct(base, 5)

def vapr_124_price_volume_overlap_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_124_price_volume_overlap_lvl_21d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rolling_mean(base, 21)

def vapr_125_price_volume_overlap_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_125_price_volume_overlap_zscore_21d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _zscore_rolling(base, 21)

def vapr_126_price_volume_overlap_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_126_price_volume_overlap_rank_21d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rank_pct(base, 21)

def vapr_127_price_volume_overlap_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_127_price_volume_overlap_lvl_63d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rolling_mean(base, 63)

def vapr_128_price_volume_overlap_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_128_price_volume_overlap_zscore_63d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _zscore_rolling(base, 63)

def vapr_129_price_volume_overlap_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_129_price_volume_overlap_rank_63d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rank_pct(base, 63)

def vapr_130_price_volume_overlap_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_130_price_volume_overlap_lvl_126d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rolling_mean(base, 126)

def vapr_131_price_volume_overlap_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_131_price_volume_overlap_zscore_126d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _zscore_rolling(base, 126)

def vapr_132_price_volume_overlap_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_132_price_volume_overlap_rank_126d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rank_pct(base, 126)

def vapr_133_price_volume_overlap_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_133_price_volume_overlap_lvl_252d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rolling_mean(base, 252)

def vapr_134_price_volume_overlap_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_134_price_volume_overlap_zscore_252d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _zscore_rolling(base, 252)

def vapr_135_price_volume_overlap_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_135_price_volume_overlap_rank_252d
    ECONOMIC RATIONALE: Diversity of price levels traded recently.
    """
    base = close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))
    return _rank_pct(base, 252)

def vapr_136_vapr_momentum_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_136_vapr_momentum_lvl_5d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rolling_mean(base, 5)

def vapr_137_vapr_momentum_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_137_vapr_momentum_zscore_5d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _zscore_rolling(base, 5)

def vapr_138_vapr_momentum_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_138_vapr_momentum_rank_5d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rank_pct(base, 5)

def vapr_139_vapr_momentum_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_139_vapr_momentum_lvl_21d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rolling_mean(base, 21)

def vapr_140_vapr_momentum_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_140_vapr_momentum_zscore_21d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _zscore_rolling(base, 21)

def vapr_141_vapr_momentum_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_141_vapr_momentum_rank_21d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rank_pct(base, 21)

def vapr_142_vapr_momentum_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_142_vapr_momentum_lvl_63d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rolling_mean(base, 63)

def vapr_143_vapr_momentum_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_143_vapr_momentum_zscore_63d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _zscore_rolling(base, 63)

def vapr_144_vapr_momentum_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_144_vapr_momentum_rank_63d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rank_pct(base, 63)

def vapr_145_vapr_momentum_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_145_vapr_momentum_lvl_126d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rolling_mean(base, 126)

def vapr_146_vapr_momentum_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_146_vapr_momentum_zscore_126d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _zscore_rolling(base, 126)

def vapr_147_vapr_momentum_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_147_vapr_momentum_rank_126d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rank_pct(base, 126)

def vapr_148_vapr_momentum_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_148_vapr_momentum_lvl_252d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rolling_mean(base, 252)

def vapr_149_vapr_momentum_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_149_vapr_momentum_zscore_252d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _zscore_rolling(base, 252)

def vapr_150_vapr_momentum_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_150_vapr_momentum_rank_252d
    ECONOMIC RATIONALE: Volume-weighted price momentum.
    """
    base = volume.rolling(21).mean() * close.pct_change(21)
    return _rank_pct(base, 252)

def vapr_151_vapr_exhaustion_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_151_vapr_exhaustion_lvl_5d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 5)

def vapr_152_vapr_exhaustion_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_152_vapr_exhaustion_zscore_5d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 5)

def vapr_153_vapr_exhaustion_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_153_vapr_exhaustion_rank_5d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 5)

def vapr_154_vapr_exhaustion_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_154_vapr_exhaustion_lvl_21d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 21)

def vapr_155_vapr_exhaustion_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_155_vapr_exhaustion_zscore_21d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 21)

def vapr_156_vapr_exhaustion_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_156_vapr_exhaustion_rank_21d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 21)

def vapr_157_vapr_exhaustion_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_157_vapr_exhaustion_lvl_63d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 63)

def vapr_158_vapr_exhaustion_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_158_vapr_exhaustion_zscore_63d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 63)

def vapr_159_vapr_exhaustion_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_159_vapr_exhaustion_rank_63d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 63)

def vapr_160_vapr_exhaustion_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_160_vapr_exhaustion_lvl_126d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 126)

def vapr_161_vapr_exhaustion_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_161_vapr_exhaustion_zscore_126d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 126)

def vapr_162_vapr_exhaustion_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_162_vapr_exhaustion_rank_126d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 126)

def vapr_163_vapr_exhaustion_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_163_vapr_exhaustion_lvl_252d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rolling_mean(base, 252)

def vapr_164_vapr_exhaustion_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_164_vapr_exhaustion_zscore_252d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _zscore_rolling(base, 252)

def vapr_165_vapr_exhaustion_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_165_vapr_exhaustion_rank_252d
    ECONOMIC RATIONALE: High volume with little price movement (churn).
    """
    base = (volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)
    return _rank_pct(base, 252)

def vapr_166_support_volume_strength_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_166_support_volume_strength_lvl_5d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rolling_mean(base, 5)

def vapr_167_support_volume_strength_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_167_support_volume_strength_zscore_5d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _zscore_rolling(base, 5)

def vapr_168_support_volume_strength_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_168_support_volume_strength_rank_5d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rank_pct(base, 5)

def vapr_169_support_volume_strength_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_169_support_volume_strength_lvl_21d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rolling_mean(base, 21)

def vapr_170_support_volume_strength_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_170_support_volume_strength_zscore_21d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _zscore_rolling(base, 21)

def vapr_171_support_volume_strength_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_171_support_volume_strength_rank_21d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rank_pct(base, 21)

def vapr_172_support_volume_strength_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_172_support_volume_strength_lvl_63d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rolling_mean(base, 63)

def vapr_173_support_volume_strength_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_173_support_volume_strength_zscore_63d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _zscore_rolling(base, 63)

def vapr_174_support_volume_strength_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_174_support_volume_strength_rank_63d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rank_pct(base, 63)

def vapr_175_support_volume_strength_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_175_support_volume_strength_lvl_126d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rolling_mean(base, 126)

def vapr_176_support_volume_strength_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_176_support_volume_strength_zscore_126d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _zscore_rolling(base, 126)

def vapr_177_support_volume_strength_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_177_support_volume_strength_rank_126d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rank_pct(base, 126)

def vapr_178_support_volume_strength_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_178_support_volume_strength_lvl_252d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rolling_mean(base, 252)

def vapr_179_support_volume_strength_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_179_support_volume_strength_zscore_252d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _zscore_rolling(base, 252)

def vapr_180_support_volume_strength_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_180_support_volume_strength_rank_252d
    ECONOMIC RATIONALE: Volume traded near structural support.
    """
    base = volume * (close < low.rolling(63).min()*1.05)
    return _rank_pct(base, 252)

def vapr_181_resistance_volume_strength_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_181_resistance_volume_strength_lvl_5d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rolling_mean(base, 5)

def vapr_182_resistance_volume_strength_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_182_resistance_volume_strength_zscore_5d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _zscore_rolling(base, 5)

def vapr_183_resistance_volume_strength_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_183_resistance_volume_strength_rank_5d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rank_pct(base, 5)

def vapr_184_resistance_volume_strength_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_184_resistance_volume_strength_lvl_21d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rolling_mean(base, 21)

def vapr_185_resistance_volume_strength_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_185_resistance_volume_strength_zscore_21d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _zscore_rolling(base, 21)

def vapr_186_resistance_volume_strength_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_186_resistance_volume_strength_rank_21d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rank_pct(base, 21)

def vapr_187_resistance_volume_strength_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_187_resistance_volume_strength_lvl_63d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rolling_mean(base, 63)

def vapr_188_resistance_volume_strength_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_188_resistance_volume_strength_zscore_63d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _zscore_rolling(base, 63)

def vapr_189_resistance_volume_strength_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_189_resistance_volume_strength_rank_63d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rank_pct(base, 63)

def vapr_190_resistance_volume_strength_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_190_resistance_volume_strength_lvl_126d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rolling_mean(base, 126)

def vapr_191_resistance_volume_strength_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_191_resistance_volume_strength_zscore_126d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _zscore_rolling(base, 126)

def vapr_192_resistance_volume_strength_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_192_resistance_volume_strength_rank_126d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rank_pct(base, 126)

def vapr_193_resistance_volume_strength_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_193_resistance_volume_strength_lvl_252d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rolling_mean(base, 252)

def vapr_194_resistance_volume_strength_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_194_resistance_volume_strength_zscore_252d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _zscore_rolling(base, 252)

def vapr_195_resistance_volume_strength_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_195_resistance_volume_strength_rank_252d
    ECONOMIC RATIONALE: Volume traded near structural resistance.
    """
    base = volume * (close > high.rolling(63).max()*0.95)
    return _rank_pct(base, 252)

def vapr_196_vapr_regime_shift_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_196_vapr_regime_shift_lvl_5d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rolling_mean(base, 5)

def vapr_197_vapr_regime_shift_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_197_vapr_regime_shift_zscore_5d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _zscore_rolling(base, 5)

def vapr_198_vapr_regime_shift_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_198_vapr_regime_shift_rank_5d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rank_pct(base, 5)

def vapr_199_vapr_regime_shift_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_199_vapr_regime_shift_lvl_21d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rolling_mean(base, 21)

def vapr_200_vapr_regime_shift_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_200_vapr_regime_shift_zscore_21d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _zscore_rolling(base, 21)

def vapr_201_vapr_regime_shift_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_201_vapr_regime_shift_rank_21d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rank_pct(base, 21)

def vapr_202_vapr_regime_shift_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_202_vapr_regime_shift_lvl_63d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rolling_mean(base, 63)

def vapr_203_vapr_regime_shift_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_203_vapr_regime_shift_zscore_63d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _zscore_rolling(base, 63)

def vapr_204_vapr_regime_shift_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_204_vapr_regime_shift_rank_63d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rank_pct(base, 63)

def vapr_205_vapr_regime_shift_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_205_vapr_regime_shift_lvl_126d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rolling_mean(base, 126)

def vapr_206_vapr_regime_shift_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_206_vapr_regime_shift_zscore_126d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _zscore_rolling(base, 126)

def vapr_207_vapr_regime_shift_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_207_vapr_regime_shift_rank_126d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rank_pct(base, 126)

def vapr_208_vapr_regime_shift_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_208_vapr_regime_shift_lvl_252d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rolling_mean(base, 252)

def vapr_209_vapr_regime_shift_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_209_vapr_regime_shift_zscore_252d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _zscore_rolling(base, 252)

def vapr_210_vapr_regime_shift_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_210_vapr_regime_shift_rank_252d
    ECONOMIC RATIONALE: Shift in the price-volume correlation regime.
    """
    base = volume.rolling(21).corr(close).diff(21)
    return _rank_pct(base, 252)

def vapr_211_vapr_tail_volume_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_211_vapr_tail_volume_lvl_5d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rolling_mean(base, 5)

def vapr_212_vapr_tail_volume_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_212_vapr_tail_volume_zscore_5d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _zscore_rolling(base, 5)

def vapr_213_vapr_tail_volume_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_213_vapr_tail_volume_rank_5d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rank_pct(base, 5)

def vapr_214_vapr_tail_volume_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_214_vapr_tail_volume_lvl_21d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rolling_mean(base, 21)

def vapr_215_vapr_tail_volume_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_215_vapr_tail_volume_zscore_21d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _zscore_rolling(base, 21)

def vapr_216_vapr_tail_volume_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_216_vapr_tail_volume_rank_21d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rank_pct(base, 21)

def vapr_217_vapr_tail_volume_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_217_vapr_tail_volume_lvl_63d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rolling_mean(base, 63)

def vapr_218_vapr_tail_volume_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_218_vapr_tail_volume_zscore_63d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _zscore_rolling(base, 63)

def vapr_219_vapr_tail_volume_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_219_vapr_tail_volume_rank_63d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rank_pct(base, 63)

def vapr_220_vapr_tail_volume_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_220_vapr_tail_volume_lvl_126d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rolling_mean(base, 126)

def vapr_221_vapr_tail_volume_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_221_vapr_tail_volume_zscore_126d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _zscore_rolling(base, 126)

def vapr_222_vapr_tail_volume_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_222_vapr_tail_volume_rank_126d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rank_pct(base, 126)

def vapr_223_vapr_tail_volume_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_223_vapr_tail_volume_lvl_252d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rolling_mean(base, 252)

def vapr_224_vapr_tail_volume_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_224_vapr_tail_volume_zscore_252d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _zscore_rolling(base, 252)

def vapr_225_vapr_tail_volume_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_225_vapr_tail_volume_rank_252d
    ECONOMIC RATIONALE: Volume associated with extreme low prices.
    """
    base = volume * (close < close.rolling(252).quantile(0.05))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V112_REGISTRY_2 = {
    "vapr_121_price_volume_overlap_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_121_price_volume_overlap_lvl_5d},
    "vapr_122_price_volume_overlap_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_122_price_volume_overlap_zscore_5d},
    "vapr_123_price_volume_overlap_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_123_price_volume_overlap_rank_5d},
    "vapr_124_price_volume_overlap_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_124_price_volume_overlap_lvl_21d},
    "vapr_125_price_volume_overlap_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_125_price_volume_overlap_zscore_21d},
    "vapr_126_price_volume_overlap_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_126_price_volume_overlap_rank_21d},
    "vapr_127_price_volume_overlap_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_127_price_volume_overlap_lvl_63d},
    "vapr_128_price_volume_overlap_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_128_price_volume_overlap_zscore_63d},
    "vapr_129_price_volume_overlap_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_129_price_volume_overlap_rank_63d},
    "vapr_130_price_volume_overlap_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_130_price_volume_overlap_lvl_126d},
    "vapr_131_price_volume_overlap_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_131_price_volume_overlap_zscore_126d},
    "vapr_132_price_volume_overlap_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_132_price_volume_overlap_rank_126d},
    "vapr_133_price_volume_overlap_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_133_price_volume_overlap_lvl_252d},
    "vapr_134_price_volume_overlap_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_134_price_volume_overlap_zscore_252d},
    "vapr_135_price_volume_overlap_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_135_price_volume_overlap_rank_252d},
    "vapr_136_vapr_momentum_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_136_vapr_momentum_lvl_5d},
    "vapr_137_vapr_momentum_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_137_vapr_momentum_zscore_5d},
    "vapr_138_vapr_momentum_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_138_vapr_momentum_rank_5d},
    "vapr_139_vapr_momentum_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_139_vapr_momentum_lvl_21d},
    "vapr_140_vapr_momentum_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_140_vapr_momentum_zscore_21d},
    "vapr_141_vapr_momentum_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_141_vapr_momentum_rank_21d},
    "vapr_142_vapr_momentum_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_142_vapr_momentum_lvl_63d},
    "vapr_143_vapr_momentum_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_143_vapr_momentum_zscore_63d},
    "vapr_144_vapr_momentum_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_144_vapr_momentum_rank_63d},
    "vapr_145_vapr_momentum_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_145_vapr_momentum_lvl_126d},
    "vapr_146_vapr_momentum_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_146_vapr_momentum_zscore_126d},
    "vapr_147_vapr_momentum_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_147_vapr_momentum_rank_126d},
    "vapr_148_vapr_momentum_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_148_vapr_momentum_lvl_252d},
    "vapr_149_vapr_momentum_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_149_vapr_momentum_zscore_252d},
    "vapr_150_vapr_momentum_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_150_vapr_momentum_rank_252d},
    "vapr_151_vapr_exhaustion_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_151_vapr_exhaustion_lvl_5d},
    "vapr_152_vapr_exhaustion_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_152_vapr_exhaustion_zscore_5d},
    "vapr_153_vapr_exhaustion_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_153_vapr_exhaustion_rank_5d},
    "vapr_154_vapr_exhaustion_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_154_vapr_exhaustion_lvl_21d},
    "vapr_155_vapr_exhaustion_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_155_vapr_exhaustion_zscore_21d},
    "vapr_156_vapr_exhaustion_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_156_vapr_exhaustion_rank_21d},
    "vapr_157_vapr_exhaustion_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_157_vapr_exhaustion_lvl_63d},
    "vapr_158_vapr_exhaustion_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_158_vapr_exhaustion_zscore_63d},
    "vapr_159_vapr_exhaustion_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_159_vapr_exhaustion_rank_63d},
    "vapr_160_vapr_exhaustion_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_160_vapr_exhaustion_lvl_126d},
    "vapr_161_vapr_exhaustion_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_161_vapr_exhaustion_zscore_126d},
    "vapr_162_vapr_exhaustion_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_162_vapr_exhaustion_rank_126d},
    "vapr_163_vapr_exhaustion_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_163_vapr_exhaustion_lvl_252d},
    "vapr_164_vapr_exhaustion_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_164_vapr_exhaustion_zscore_252d},
    "vapr_165_vapr_exhaustion_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_165_vapr_exhaustion_rank_252d},
    "vapr_166_support_volume_strength_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_166_support_volume_strength_lvl_5d},
    "vapr_167_support_volume_strength_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_167_support_volume_strength_zscore_5d},
    "vapr_168_support_volume_strength_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_168_support_volume_strength_rank_5d},
    "vapr_169_support_volume_strength_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_169_support_volume_strength_lvl_21d},
    "vapr_170_support_volume_strength_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_170_support_volume_strength_zscore_21d},
    "vapr_171_support_volume_strength_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_171_support_volume_strength_rank_21d},
    "vapr_172_support_volume_strength_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_172_support_volume_strength_lvl_63d},
    "vapr_173_support_volume_strength_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_173_support_volume_strength_zscore_63d},
    "vapr_174_support_volume_strength_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_174_support_volume_strength_rank_63d},
    "vapr_175_support_volume_strength_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_175_support_volume_strength_lvl_126d},
    "vapr_176_support_volume_strength_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_176_support_volume_strength_zscore_126d},
    "vapr_177_support_volume_strength_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_177_support_volume_strength_rank_126d},
    "vapr_178_support_volume_strength_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_178_support_volume_strength_lvl_252d},
    "vapr_179_support_volume_strength_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_179_support_volume_strength_zscore_252d},
    "vapr_180_support_volume_strength_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_180_support_volume_strength_rank_252d},
    "vapr_181_resistance_volume_strength_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_181_resistance_volume_strength_lvl_5d},
    "vapr_182_resistance_volume_strength_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_182_resistance_volume_strength_zscore_5d},
    "vapr_183_resistance_volume_strength_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_183_resistance_volume_strength_rank_5d},
    "vapr_184_resistance_volume_strength_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_184_resistance_volume_strength_lvl_21d},
    "vapr_185_resistance_volume_strength_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_185_resistance_volume_strength_zscore_21d},
    "vapr_186_resistance_volume_strength_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_186_resistance_volume_strength_rank_21d},
    "vapr_187_resistance_volume_strength_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_187_resistance_volume_strength_lvl_63d},
    "vapr_188_resistance_volume_strength_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_188_resistance_volume_strength_zscore_63d},
    "vapr_189_resistance_volume_strength_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_189_resistance_volume_strength_rank_63d},
    "vapr_190_resistance_volume_strength_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_190_resistance_volume_strength_lvl_126d},
    "vapr_191_resistance_volume_strength_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_191_resistance_volume_strength_zscore_126d},
    "vapr_192_resistance_volume_strength_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_192_resistance_volume_strength_rank_126d},
    "vapr_193_resistance_volume_strength_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_193_resistance_volume_strength_lvl_252d},
    "vapr_194_resistance_volume_strength_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_194_resistance_volume_strength_zscore_252d},
    "vapr_195_resistance_volume_strength_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_195_resistance_volume_strength_rank_252d},
    "vapr_196_vapr_regime_shift_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_196_vapr_regime_shift_lvl_5d},
    "vapr_197_vapr_regime_shift_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_197_vapr_regime_shift_zscore_5d},
    "vapr_198_vapr_regime_shift_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_198_vapr_regime_shift_rank_5d},
    "vapr_199_vapr_regime_shift_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_199_vapr_regime_shift_lvl_21d},
    "vapr_200_vapr_regime_shift_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_200_vapr_regime_shift_zscore_21d},
    "vapr_201_vapr_regime_shift_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_201_vapr_regime_shift_rank_21d},
    "vapr_202_vapr_regime_shift_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_202_vapr_regime_shift_lvl_63d},
    "vapr_203_vapr_regime_shift_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_203_vapr_regime_shift_zscore_63d},
    "vapr_204_vapr_regime_shift_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_204_vapr_regime_shift_rank_63d},
    "vapr_205_vapr_regime_shift_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_205_vapr_regime_shift_lvl_126d},
    "vapr_206_vapr_regime_shift_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_206_vapr_regime_shift_zscore_126d},
    "vapr_207_vapr_regime_shift_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_207_vapr_regime_shift_rank_126d},
    "vapr_208_vapr_regime_shift_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_208_vapr_regime_shift_lvl_252d},
    "vapr_209_vapr_regime_shift_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_209_vapr_regime_shift_zscore_252d},
    "vapr_210_vapr_regime_shift_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_210_vapr_regime_shift_rank_252d},
    "vapr_211_vapr_tail_volume_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_211_vapr_tail_volume_lvl_5d},
    "vapr_212_vapr_tail_volume_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_212_vapr_tail_volume_zscore_5d},
    "vapr_213_vapr_tail_volume_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_213_vapr_tail_volume_rank_5d},
    "vapr_214_vapr_tail_volume_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_214_vapr_tail_volume_lvl_21d},
    "vapr_215_vapr_tail_volume_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_215_vapr_tail_volume_zscore_21d},
    "vapr_216_vapr_tail_volume_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_216_vapr_tail_volume_rank_21d},
    "vapr_217_vapr_tail_volume_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_217_vapr_tail_volume_lvl_63d},
    "vapr_218_vapr_tail_volume_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_218_vapr_tail_volume_zscore_63d},
    "vapr_219_vapr_tail_volume_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_219_vapr_tail_volume_rank_63d},
    "vapr_220_vapr_tail_volume_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_220_vapr_tail_volume_lvl_126d},
    "vapr_221_vapr_tail_volume_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_221_vapr_tail_volume_zscore_126d},
    "vapr_222_vapr_tail_volume_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_222_vapr_tail_volume_rank_126d},
    "vapr_223_vapr_tail_volume_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_223_vapr_tail_volume_lvl_252d},
    "vapr_224_vapr_tail_volume_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_224_vapr_tail_volume_zscore_252d},
    "vapr_225_vapr_tail_volume_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_225_vapr_tail_volume_rank_252d},
}
