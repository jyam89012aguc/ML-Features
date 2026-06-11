"""
114_overnight_intraday_split — Base Features Part 2
Domain: overnight_intraday_split
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

def onid_121_gap_fade_potential_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_121_gap_fade_potential_lvl_5d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rolling_mean(base, 5)

def onid_122_gap_fade_potential_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_122_gap_fade_potential_zscore_5d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _zscore_rolling(base, 5)

def onid_123_gap_fade_potential_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_123_gap_fade_potential_rank_5d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rank_pct(base, 5)

def onid_124_gap_fade_potential_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_124_gap_fade_potential_lvl_21d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rolling_mean(base, 21)

def onid_125_gap_fade_potential_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_125_gap_fade_potential_zscore_21d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _zscore_rolling(base, 21)

def onid_126_gap_fade_potential_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_126_gap_fade_potential_rank_21d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rank_pct(base, 21)

def onid_127_gap_fade_potential_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_127_gap_fade_potential_lvl_63d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rolling_mean(base, 63)

def onid_128_gap_fade_potential_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_128_gap_fade_potential_zscore_63d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _zscore_rolling(base, 63)

def onid_129_gap_fade_potential_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_129_gap_fade_potential_rank_63d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rank_pct(base, 63)

def onid_130_gap_fade_potential_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_130_gap_fade_potential_lvl_126d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rolling_mean(base, 126)

def onid_131_gap_fade_potential_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_131_gap_fade_potential_zscore_126d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _zscore_rolling(base, 126)

def onid_132_gap_fade_potential_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_132_gap_fade_potential_rank_126d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rank_pct(base, 126)

def onid_133_gap_fade_potential_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_133_gap_fade_potential_lvl_252d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rolling_mean(base, 252)

def onid_134_gap_fade_potential_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_134_gap_fade_potential_zscore_252d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _zscore_rolling(base, 252)

def onid_135_gap_fade_potential_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_135_gap_fade_potential_rank_252d
    ECONOMIC RATIONALE: Potential for intraday fading of overnight gaps.
    """
    base = (open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)
    return _rank_pct(base, 252)

def onid_136_overnight_gap_z_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_136_overnight_gap_z_lvl_5d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rolling_mean(base, 5)

def onid_137_overnight_gap_z_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_137_overnight_gap_z_zscore_5d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _zscore_rolling(base, 5)

def onid_138_overnight_gap_z_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_138_overnight_gap_z_rank_5d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rank_pct(base, 5)

def onid_139_overnight_gap_z_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_139_overnight_gap_z_lvl_21d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rolling_mean(base, 21)

def onid_140_overnight_gap_z_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_140_overnight_gap_z_zscore_21d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _zscore_rolling(base, 21)

def onid_141_overnight_gap_z_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_141_overnight_gap_z_rank_21d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rank_pct(base, 21)

def onid_142_overnight_gap_z_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_142_overnight_gap_z_lvl_63d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rolling_mean(base, 63)

def onid_143_overnight_gap_z_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_143_overnight_gap_z_zscore_63d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _zscore_rolling(base, 63)

def onid_144_overnight_gap_z_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_144_overnight_gap_z_rank_63d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rank_pct(base, 63)

def onid_145_overnight_gap_z_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_145_overnight_gap_z_lvl_126d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rolling_mean(base, 126)

def onid_146_overnight_gap_z_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_146_overnight_gap_z_zscore_126d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _zscore_rolling(base, 126)

def onid_147_overnight_gap_z_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_147_overnight_gap_z_rank_126d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rank_pct(base, 126)

def onid_148_overnight_gap_z_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_148_overnight_gap_z_lvl_252d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rolling_mean(base, 252)

def onid_149_overnight_gap_z_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_149_overnight_gap_z_zscore_252d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _zscore_rolling(base, 252)

def onid_150_overnight_gap_z_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_150_overnight_gap_z_rank_252d
    ECONOMIC RATIONALE: Z-score of current overnight gap.
    """
    base = _zscore_rolling(open / close.shift(1) - 1, 252)
    return _rank_pct(base, 252)

def onid_151_intraday_range_pos_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_151_intraday_range_pos_lvl_5d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def onid_152_intraday_range_pos_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_152_intraday_range_pos_zscore_5d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def onid_153_intraday_range_pos_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_153_intraday_range_pos_rank_5d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 5)

def onid_154_intraday_range_pos_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_154_intraday_range_pos_lvl_21d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def onid_155_intraday_range_pos_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_155_intraday_range_pos_zscore_21d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def onid_156_intraday_range_pos_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_156_intraday_range_pos_rank_21d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 21)

def onid_157_intraday_range_pos_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_157_intraday_range_pos_lvl_63d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def onid_158_intraday_range_pos_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_158_intraday_range_pos_zscore_63d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def onid_159_intraday_range_pos_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_159_intraday_range_pos_rank_63d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 63)

def onid_160_intraday_range_pos_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_160_intraday_range_pos_lvl_126d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def onid_161_intraday_range_pos_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_161_intraday_range_pos_zscore_126d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def onid_162_intraday_range_pos_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_162_intraday_range_pos_rank_126d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 126)

def onid_163_intraday_range_pos_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_163_intraday_range_pos_lvl_252d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def onid_164_intraday_range_pos_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_164_intraday_range_pos_zscore_252d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def onid_165_intraday_range_pos_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_165_intraday_range_pos_rank_252d
    ECONOMIC RATIONALE: Closing position within the intraday range.
    """
    base = (close - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 252)

def onid_166_overnight_momentum_lead_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_166_overnight_momentum_lead_lvl_5d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def onid_167_overnight_momentum_lead_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_167_overnight_momentum_lead_zscore_5d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def onid_168_overnight_momentum_lead_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_168_overnight_momentum_lead_rank_5d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rank_pct(base, 5)

def onid_169_overnight_momentum_lead_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_169_overnight_momentum_lead_lvl_21d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def onid_170_overnight_momentum_lead_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_170_overnight_momentum_lead_zscore_21d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def onid_171_overnight_momentum_lead_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_171_overnight_momentum_lead_rank_21d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rank_pct(base, 21)

def onid_172_overnight_momentum_lead_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_172_overnight_momentum_lead_lvl_63d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def onid_173_overnight_momentum_lead_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_173_overnight_momentum_lead_zscore_63d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def onid_174_overnight_momentum_lead_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_174_overnight_momentum_lead_rank_63d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rank_pct(base, 63)

def onid_175_overnight_momentum_lead_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_175_overnight_momentum_lead_lvl_126d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def onid_176_overnight_momentum_lead_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_176_overnight_momentum_lead_zscore_126d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def onid_177_overnight_momentum_lead_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_177_overnight_momentum_lead_rank_126d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rank_pct(base, 126)

def onid_178_overnight_momentum_lead_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_178_overnight_momentum_lead_lvl_252d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def onid_179_overnight_momentum_lead_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_179_overnight_momentum_lead_zscore_252d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def onid_180_overnight_momentum_lead_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_180_overnight_momentum_lead_rank_252d
    ECONOMIC RATIONALE: Lead of overnight momentum over intraday.
    """
    base = (open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)
    return _rank_pct(base, 252)

def onid_181_id_reversal_strength_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_181_id_reversal_strength_lvl_5d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rolling_mean(base, 5)

def onid_182_id_reversal_strength_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_182_id_reversal_strength_zscore_5d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _zscore_rolling(base, 5)

def onid_183_id_reversal_strength_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_183_id_reversal_strength_rank_5d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rank_pct(base, 5)

def onid_184_id_reversal_strength_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_184_id_reversal_strength_lvl_21d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rolling_mean(base, 21)

def onid_185_id_reversal_strength_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_185_id_reversal_strength_zscore_21d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _zscore_rolling(base, 21)

def onid_186_id_reversal_strength_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_186_id_reversal_strength_rank_21d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rank_pct(base, 21)

def onid_187_id_reversal_strength_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_187_id_reversal_strength_lvl_63d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rolling_mean(base, 63)

def onid_188_id_reversal_strength_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_188_id_reversal_strength_zscore_63d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _zscore_rolling(base, 63)

def onid_189_id_reversal_strength_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_189_id_reversal_strength_rank_63d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rank_pct(base, 63)

def onid_190_id_reversal_strength_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_190_id_reversal_strength_lvl_126d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rolling_mean(base, 126)

def onid_191_id_reversal_strength_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_191_id_reversal_strength_zscore_126d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _zscore_rolling(base, 126)

def onid_192_id_reversal_strength_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_192_id_reversal_strength_rank_126d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rank_pct(base, 126)

def onid_193_id_reversal_strength_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_193_id_reversal_strength_lvl_252d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rolling_mean(base, 252)

def onid_194_id_reversal_strength_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_194_id_reversal_strength_zscore_252d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _zscore_rolling(base, 252)

def onid_195_id_reversal_strength_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_195_id_reversal_strength_rank_252d
    ECONOMIC RATIONALE: Frequency of intraday reversals of overnight moves.
    """
    base = ((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()
    return _rank_pct(base, 252)

def onid_196_on_id_correlation_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_196_on_id_correlation_lvl_5d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rolling_mean(base, 5)

def onid_197_on_id_correlation_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_197_on_id_correlation_zscore_5d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _zscore_rolling(base, 5)

def onid_198_on_id_correlation_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_198_on_id_correlation_rank_5d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rank_pct(base, 5)

def onid_199_on_id_correlation_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_199_on_id_correlation_lvl_21d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rolling_mean(base, 21)

def onid_200_on_id_correlation_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_200_on_id_correlation_zscore_21d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _zscore_rolling(base, 21)

def onid_201_on_id_correlation_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_201_on_id_correlation_rank_21d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rank_pct(base, 21)

def onid_202_on_id_correlation_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_202_on_id_correlation_lvl_63d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rolling_mean(base, 63)

def onid_203_on_id_correlation_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_203_on_id_correlation_zscore_63d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _zscore_rolling(base, 63)

def onid_204_on_id_correlation_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_204_on_id_correlation_rank_63d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rank_pct(base, 63)

def onid_205_on_id_correlation_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_205_on_id_correlation_lvl_126d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rolling_mean(base, 126)

def onid_206_on_id_correlation_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_206_on_id_correlation_zscore_126d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _zscore_rolling(base, 126)

def onid_207_on_id_correlation_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_207_on_id_correlation_rank_126d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rank_pct(base, 126)

def onid_208_on_id_correlation_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_208_on_id_correlation_lvl_252d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rolling_mean(base, 252)

def onid_209_on_id_correlation_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_209_on_id_correlation_zscore_252d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _zscore_rolling(base, 252)

def onid_210_on_id_correlation_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_210_on_id_correlation_rank_252d
    ECONOMIC RATIONALE: Correlation between overnight and intraday returns.
    """
    base = (open / close.shift(1) - 1).rolling(63).corr(close / open - 1)
    return _rank_pct(base, 252)

def onid_211_overnight_shock_flag_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_211_overnight_shock_flag_lvl_5d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 5)

def onid_212_overnight_shock_flag_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_212_overnight_shock_flag_zscore_5d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 5)

def onid_213_overnight_shock_flag_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_213_overnight_shock_flag_rank_5d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rank_pct(base, 5)

def onid_214_overnight_shock_flag_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_214_overnight_shock_flag_lvl_21d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 21)

def onid_215_overnight_shock_flag_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_215_overnight_shock_flag_zscore_21d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 21)

def onid_216_overnight_shock_flag_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_216_overnight_shock_flag_rank_21d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rank_pct(base, 21)

def onid_217_overnight_shock_flag_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_217_overnight_shock_flag_lvl_63d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 63)

def onid_218_overnight_shock_flag_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_218_overnight_shock_flag_zscore_63d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 63)

def onid_219_overnight_shock_flag_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_219_overnight_shock_flag_rank_63d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rank_pct(base, 63)

def onid_220_overnight_shock_flag_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_220_overnight_shock_flag_lvl_126d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 126)

def onid_221_overnight_shock_flag_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_221_overnight_shock_flag_zscore_126d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 126)

def onid_222_overnight_shock_flag_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_222_overnight_shock_flag_rank_126d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rank_pct(base, 126)

def onid_223_overnight_shock_flag_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_223_overnight_shock_flag_lvl_252d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 252)

def onid_224_overnight_shock_flag_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_224_overnight_shock_flag_zscore_252d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 252)

def onid_225_overnight_shock_flag_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_225_overnight_shock_flag_rank_252d
    ECONOMIC RATIONALE: Binary indicator of extreme overnight price shocks.
    """
    base = (abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V114_REGISTRY_2 = {
    "onid_121_gap_fade_potential_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_121_gap_fade_potential_lvl_5d},
    "onid_122_gap_fade_potential_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_122_gap_fade_potential_zscore_5d},
    "onid_123_gap_fade_potential_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_123_gap_fade_potential_rank_5d},
    "onid_124_gap_fade_potential_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_124_gap_fade_potential_lvl_21d},
    "onid_125_gap_fade_potential_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_125_gap_fade_potential_zscore_21d},
    "onid_126_gap_fade_potential_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_126_gap_fade_potential_rank_21d},
    "onid_127_gap_fade_potential_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_127_gap_fade_potential_lvl_63d},
    "onid_128_gap_fade_potential_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_128_gap_fade_potential_zscore_63d},
    "onid_129_gap_fade_potential_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_129_gap_fade_potential_rank_63d},
    "onid_130_gap_fade_potential_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_130_gap_fade_potential_lvl_126d},
    "onid_131_gap_fade_potential_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_131_gap_fade_potential_zscore_126d},
    "onid_132_gap_fade_potential_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_132_gap_fade_potential_rank_126d},
    "onid_133_gap_fade_potential_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_133_gap_fade_potential_lvl_252d},
    "onid_134_gap_fade_potential_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_134_gap_fade_potential_zscore_252d},
    "onid_135_gap_fade_potential_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_135_gap_fade_potential_rank_252d},
    "onid_136_overnight_gap_z_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_136_overnight_gap_z_lvl_5d},
    "onid_137_overnight_gap_z_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_137_overnight_gap_z_zscore_5d},
    "onid_138_overnight_gap_z_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_138_overnight_gap_z_rank_5d},
    "onid_139_overnight_gap_z_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_139_overnight_gap_z_lvl_21d},
    "onid_140_overnight_gap_z_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_140_overnight_gap_z_zscore_21d},
    "onid_141_overnight_gap_z_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_141_overnight_gap_z_rank_21d},
    "onid_142_overnight_gap_z_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_142_overnight_gap_z_lvl_63d},
    "onid_143_overnight_gap_z_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_143_overnight_gap_z_zscore_63d},
    "onid_144_overnight_gap_z_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_144_overnight_gap_z_rank_63d},
    "onid_145_overnight_gap_z_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_145_overnight_gap_z_lvl_126d},
    "onid_146_overnight_gap_z_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_146_overnight_gap_z_zscore_126d},
    "onid_147_overnight_gap_z_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_147_overnight_gap_z_rank_126d},
    "onid_148_overnight_gap_z_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_148_overnight_gap_z_lvl_252d},
    "onid_149_overnight_gap_z_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_149_overnight_gap_z_zscore_252d},
    "onid_150_overnight_gap_z_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_150_overnight_gap_z_rank_252d},
    "onid_151_intraday_range_pos_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_151_intraday_range_pos_lvl_5d},
    "onid_152_intraday_range_pos_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_152_intraday_range_pos_zscore_5d},
    "onid_153_intraday_range_pos_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_153_intraday_range_pos_rank_5d},
    "onid_154_intraday_range_pos_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_154_intraday_range_pos_lvl_21d},
    "onid_155_intraday_range_pos_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_155_intraday_range_pos_zscore_21d},
    "onid_156_intraday_range_pos_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_156_intraday_range_pos_rank_21d},
    "onid_157_intraday_range_pos_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_157_intraday_range_pos_lvl_63d},
    "onid_158_intraday_range_pos_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_158_intraday_range_pos_zscore_63d},
    "onid_159_intraday_range_pos_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_159_intraday_range_pos_rank_63d},
    "onid_160_intraday_range_pos_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_160_intraday_range_pos_lvl_126d},
    "onid_161_intraday_range_pos_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_161_intraday_range_pos_zscore_126d},
    "onid_162_intraday_range_pos_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_162_intraday_range_pos_rank_126d},
    "onid_163_intraday_range_pos_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_163_intraday_range_pos_lvl_252d},
    "onid_164_intraday_range_pos_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_164_intraday_range_pos_zscore_252d},
    "onid_165_intraday_range_pos_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_165_intraday_range_pos_rank_252d},
    "onid_166_overnight_momentum_lead_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_166_overnight_momentum_lead_lvl_5d},
    "onid_167_overnight_momentum_lead_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_167_overnight_momentum_lead_zscore_5d},
    "onid_168_overnight_momentum_lead_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_168_overnight_momentum_lead_rank_5d},
    "onid_169_overnight_momentum_lead_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_169_overnight_momentum_lead_lvl_21d},
    "onid_170_overnight_momentum_lead_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_170_overnight_momentum_lead_zscore_21d},
    "onid_171_overnight_momentum_lead_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_171_overnight_momentum_lead_rank_21d},
    "onid_172_overnight_momentum_lead_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_172_overnight_momentum_lead_lvl_63d},
    "onid_173_overnight_momentum_lead_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_173_overnight_momentum_lead_zscore_63d},
    "onid_174_overnight_momentum_lead_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_174_overnight_momentum_lead_rank_63d},
    "onid_175_overnight_momentum_lead_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_175_overnight_momentum_lead_lvl_126d},
    "onid_176_overnight_momentum_lead_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_176_overnight_momentum_lead_zscore_126d},
    "onid_177_overnight_momentum_lead_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_177_overnight_momentum_lead_rank_126d},
    "onid_178_overnight_momentum_lead_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_178_overnight_momentum_lead_lvl_252d},
    "onid_179_overnight_momentum_lead_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_179_overnight_momentum_lead_zscore_252d},
    "onid_180_overnight_momentum_lead_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_180_overnight_momentum_lead_rank_252d},
    "onid_181_id_reversal_strength_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_181_id_reversal_strength_lvl_5d},
    "onid_182_id_reversal_strength_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_182_id_reversal_strength_zscore_5d},
    "onid_183_id_reversal_strength_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_183_id_reversal_strength_rank_5d},
    "onid_184_id_reversal_strength_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_184_id_reversal_strength_lvl_21d},
    "onid_185_id_reversal_strength_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_185_id_reversal_strength_zscore_21d},
    "onid_186_id_reversal_strength_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_186_id_reversal_strength_rank_21d},
    "onid_187_id_reversal_strength_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_187_id_reversal_strength_lvl_63d},
    "onid_188_id_reversal_strength_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_188_id_reversal_strength_zscore_63d},
    "onid_189_id_reversal_strength_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_189_id_reversal_strength_rank_63d},
    "onid_190_id_reversal_strength_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_190_id_reversal_strength_lvl_126d},
    "onid_191_id_reversal_strength_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_191_id_reversal_strength_zscore_126d},
    "onid_192_id_reversal_strength_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_192_id_reversal_strength_rank_126d},
    "onid_193_id_reversal_strength_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_193_id_reversal_strength_lvl_252d},
    "onid_194_id_reversal_strength_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_194_id_reversal_strength_zscore_252d},
    "onid_195_id_reversal_strength_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_195_id_reversal_strength_rank_252d},
    "onid_196_on_id_correlation_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_196_on_id_correlation_lvl_5d},
    "onid_197_on_id_correlation_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_197_on_id_correlation_zscore_5d},
    "onid_198_on_id_correlation_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_198_on_id_correlation_rank_5d},
    "onid_199_on_id_correlation_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_199_on_id_correlation_lvl_21d},
    "onid_200_on_id_correlation_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_200_on_id_correlation_zscore_21d},
    "onid_201_on_id_correlation_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_201_on_id_correlation_rank_21d},
    "onid_202_on_id_correlation_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_202_on_id_correlation_lvl_63d},
    "onid_203_on_id_correlation_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_203_on_id_correlation_zscore_63d},
    "onid_204_on_id_correlation_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_204_on_id_correlation_rank_63d},
    "onid_205_on_id_correlation_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_205_on_id_correlation_lvl_126d},
    "onid_206_on_id_correlation_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_206_on_id_correlation_zscore_126d},
    "onid_207_on_id_correlation_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_207_on_id_correlation_rank_126d},
    "onid_208_on_id_correlation_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_208_on_id_correlation_lvl_252d},
    "onid_209_on_id_correlation_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_209_on_id_correlation_zscore_252d},
    "onid_210_on_id_correlation_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_210_on_id_correlation_rank_252d},
    "onid_211_overnight_shock_flag_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_211_overnight_shock_flag_lvl_5d},
    "onid_212_overnight_shock_flag_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_212_overnight_shock_flag_zscore_5d},
    "onid_213_overnight_shock_flag_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_213_overnight_shock_flag_rank_5d},
    "onid_214_overnight_shock_flag_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_214_overnight_shock_flag_lvl_21d},
    "onid_215_overnight_shock_flag_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_215_overnight_shock_flag_zscore_21d},
    "onid_216_overnight_shock_flag_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_216_overnight_shock_flag_rank_21d},
    "onid_217_overnight_shock_flag_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_217_overnight_shock_flag_lvl_63d},
    "onid_218_overnight_shock_flag_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_218_overnight_shock_flag_zscore_63d},
    "onid_219_overnight_shock_flag_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_219_overnight_shock_flag_rank_63d},
    "onid_220_overnight_shock_flag_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_220_overnight_shock_flag_lvl_126d},
    "onid_221_overnight_shock_flag_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_221_overnight_shock_flag_zscore_126d},
    "onid_222_overnight_shock_flag_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_222_overnight_shock_flag_rank_126d},
    "onid_223_overnight_shock_flag_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_223_overnight_shock_flag_lvl_252d},
    "onid_224_overnight_shock_flag_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_224_overnight_shock_flag_zscore_252d},
    "onid_225_overnight_shock_flag_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_225_overnight_shock_flag_rank_252d},
}
