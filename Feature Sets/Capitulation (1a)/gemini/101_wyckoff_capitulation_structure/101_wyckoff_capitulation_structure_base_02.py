"""
101_wyckoff_capitulation_structure — Base Features Part 2
Domain: wyckoff_capitulation_structure
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

def wyck_121_upthrust_detection_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_121_upthrust_detection_lvl_5d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rolling_mean(base, 5)

def wyck_122_upthrust_detection_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_122_upthrust_detection_zscore_5d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _zscore_rolling(base, 5)

def wyck_123_upthrust_detection_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_123_upthrust_detection_rank_5d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rank_pct(base, 5)

def wyck_124_upthrust_detection_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_124_upthrust_detection_lvl_21d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rolling_mean(base, 21)

def wyck_125_upthrust_detection_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_125_upthrust_detection_zscore_21d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _zscore_rolling(base, 21)

def wyck_126_upthrust_detection_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_126_upthrust_detection_rank_21d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rank_pct(base, 21)

def wyck_127_upthrust_detection_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_127_upthrust_detection_lvl_63d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rolling_mean(base, 63)

def wyck_128_upthrust_detection_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_128_upthrust_detection_zscore_63d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _zscore_rolling(base, 63)

def wyck_129_upthrust_detection_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_129_upthrust_detection_rank_63d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rank_pct(base, 63)

def wyck_130_upthrust_detection_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_130_upthrust_detection_lvl_126d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rolling_mean(base, 126)

def wyck_131_upthrust_detection_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_131_upthrust_detection_zscore_126d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _zscore_rolling(base, 126)

def wyck_132_upthrust_detection_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_132_upthrust_detection_rank_126d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rank_pct(base, 126)

def wyck_133_upthrust_detection_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_133_upthrust_detection_lvl_252d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rolling_mean(base, 252)

def wyck_134_upthrust_detection_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_134_upthrust_detection_zscore_252d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _zscore_rolling(base, 252)

def wyck_135_upthrust_detection_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_135_upthrust_detection_rank_252d
    ECONOMIC RATIONALE: False breakout above resistance.
    """
    base = (high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))
    return _rank_pct(base, 252)

def wyck_136_preliminary_support_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_136_preliminary_support_lvl_5d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rolling_mean(base, 5)

def wyck_137_preliminary_support_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_137_preliminary_support_zscore_5d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _zscore_rolling(base, 5)

def wyck_138_preliminary_support_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_138_preliminary_support_rank_5d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rank_pct(base, 5)

def wyck_139_preliminary_support_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_139_preliminary_support_lvl_21d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rolling_mean(base, 21)

def wyck_140_preliminary_support_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_140_preliminary_support_zscore_21d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _zscore_rolling(base, 21)

def wyck_141_preliminary_support_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_141_preliminary_support_rank_21d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rank_pct(base, 21)

def wyck_142_preliminary_support_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_142_preliminary_support_lvl_63d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rolling_mean(base, 63)

def wyck_143_preliminary_support_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_143_preliminary_support_zscore_63d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _zscore_rolling(base, 63)

def wyck_144_preliminary_support_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_144_preliminary_support_rank_63d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rank_pct(base, 63)

def wyck_145_preliminary_support_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_145_preliminary_support_lvl_126d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rolling_mean(base, 126)

def wyck_146_preliminary_support_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_146_preliminary_support_zscore_126d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _zscore_rolling(base, 126)

def wyck_147_preliminary_support_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_147_preliminary_support_rank_126d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rank_pct(base, 126)

def wyck_148_preliminary_support_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_148_preliminary_support_lvl_252d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rolling_mean(base, 252)

def wyck_149_preliminary_support_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_149_preliminary_support_zscore_252d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _zscore_rolling(base, 252)

def wyck_150_preliminary_support_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_150_preliminary_support_rank_252d
    ECONOMIC RATIONALE: Identification of early support levels.
    """
    base = low.rolling(10).min() < low.rolling(63).min()
    return _rank_pct(base, 252)

def wyck_151_jump_across_creek_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_151_jump_across_creek_lvl_5d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rolling_mean(base, 5)

def wyck_152_jump_across_creek_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_152_jump_across_creek_zscore_5d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _zscore_rolling(base, 5)

def wyck_153_jump_across_creek_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_153_jump_across_creek_rank_5d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rank_pct(base, 5)

def wyck_154_jump_across_creek_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_154_jump_across_creek_lvl_21d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rolling_mean(base, 21)

def wyck_155_jump_across_creek_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_155_jump_across_creek_zscore_21d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _zscore_rolling(base, 21)

def wyck_156_jump_across_creek_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_156_jump_across_creek_rank_21d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rank_pct(base, 21)

def wyck_157_jump_across_creek_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_157_jump_across_creek_lvl_63d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rolling_mean(base, 63)

def wyck_158_jump_across_creek_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_158_jump_across_creek_zscore_63d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _zscore_rolling(base, 63)

def wyck_159_jump_across_creek_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_159_jump_across_creek_rank_63d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rank_pct(base, 63)

def wyck_160_jump_across_creek_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_160_jump_across_creek_lvl_126d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rolling_mean(base, 126)

def wyck_161_jump_across_creek_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_161_jump_across_creek_zscore_126d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _zscore_rolling(base, 126)

def wyck_162_jump_across_creek_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_162_jump_across_creek_rank_126d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rank_pct(base, 126)

def wyck_163_jump_across_creek_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_163_jump_across_creek_lvl_252d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rolling_mean(base, 252)

def wyck_164_jump_across_creek_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_164_jump_across_creek_zscore_252d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _zscore_rolling(base, 252)

def wyck_165_jump_across_creek_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_165_jump_across_creek_rank_252d
    ECONOMIC RATIONALE: Strong breakout indicating change of trend.
    """
    base = close > high.rolling(63).max()
    return _rank_pct(base, 252)

def wyck_166_last_point_of_supply_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_166_last_point_of_supply_lvl_5d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rolling_mean(base, 5)

def wyck_167_last_point_of_supply_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_167_last_point_of_supply_zscore_5d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _zscore_rolling(base, 5)

def wyck_168_last_point_of_supply_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_168_last_point_of_supply_rank_5d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rank_pct(base, 5)

def wyck_169_last_point_of_supply_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_169_last_point_of_supply_lvl_21d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rolling_mean(base, 21)

def wyck_170_last_point_of_supply_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_170_last_point_of_supply_zscore_21d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _zscore_rolling(base, 21)

def wyck_171_last_point_of_supply_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_171_last_point_of_supply_rank_21d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rank_pct(base, 21)

def wyck_172_last_point_of_supply_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_172_last_point_of_supply_lvl_63d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rolling_mean(base, 63)

def wyck_173_last_point_of_supply_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_173_last_point_of_supply_zscore_63d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _zscore_rolling(base, 63)

def wyck_174_last_point_of_supply_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_174_last_point_of_supply_rank_63d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rank_pct(base, 63)

def wyck_175_last_point_of_supply_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_175_last_point_of_supply_lvl_126d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rolling_mean(base, 126)

def wyck_176_last_point_of_supply_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_176_last_point_of_supply_zscore_126d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _zscore_rolling(base, 126)

def wyck_177_last_point_of_supply_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_177_last_point_of_supply_rank_126d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rank_pct(base, 126)

def wyck_178_last_point_of_supply_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_178_last_point_of_supply_lvl_252d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rolling_mean(base, 252)

def wyck_179_last_point_of_supply_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_179_last_point_of_supply_zscore_252d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _zscore_rolling(base, 252)

def wyck_180_last_point_of_supply_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_180_last_point_of_supply_rank_252d
    ECONOMIC RATIONALE: Lower highs during a distributive phase.
    """
    base = high < high.rolling(21).max()
    return _rank_pct(base, 252)

def wyck_181_volume_price_divergence_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_181_volume_price_divergence_lvl_5d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rolling_mean(base, 5)

def wyck_182_volume_price_divergence_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_182_volume_price_divergence_zscore_5d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 5)

def wyck_183_volume_price_divergence_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_183_volume_price_divergence_rank_5d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rank_pct(base, 5)

def wyck_184_volume_price_divergence_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_184_volume_price_divergence_lvl_21d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rolling_mean(base, 21)

def wyck_185_volume_price_divergence_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_185_volume_price_divergence_zscore_21d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 21)

def wyck_186_volume_price_divergence_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_186_volume_price_divergence_rank_21d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rank_pct(base, 21)

def wyck_187_volume_price_divergence_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_187_volume_price_divergence_lvl_63d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rolling_mean(base, 63)

def wyck_188_volume_price_divergence_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_188_volume_price_divergence_zscore_63d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 63)

def wyck_189_volume_price_divergence_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_189_volume_price_divergence_rank_63d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rank_pct(base, 63)

def wyck_190_volume_price_divergence_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_190_volume_price_divergence_lvl_126d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rolling_mean(base, 126)

def wyck_191_volume_price_divergence_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_191_volume_price_divergence_zscore_126d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 126)

def wyck_192_volume_price_divergence_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_192_volume_price_divergence_rank_126d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rank_pct(base, 126)

def wyck_193_volume_price_divergence_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_193_volume_price_divergence_lvl_252d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rolling_mean(base, 252)

def wyck_194_volume_price_divergence_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_194_volume_price_divergence_zscore_252d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 252)

def wyck_195_volume_price_divergence_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_195_volume_price_divergence_rank_252d
    ECONOMIC RATIONALE: Efficiency of volume in moving price.
    """
    base = close.pct_change(21).abs() / volume.pct_change(21).abs()
    return _rank_pct(base, 252)

def wyck_196_effort_vs_result_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_196_effort_vs_result_lvl_5d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def wyck_197_effort_vs_result_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_197_effort_vs_result_zscore_5d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def wyck_198_effort_vs_result_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_198_effort_vs_result_rank_5d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 5)

def wyck_199_effort_vs_result_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_199_effort_vs_result_lvl_21d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def wyck_200_effort_vs_result_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_200_effort_vs_result_zscore_21d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def wyck_201_effort_vs_result_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_201_effort_vs_result_rank_21d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 21)

def wyck_202_effort_vs_result_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_202_effort_vs_result_lvl_63d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def wyck_203_effort_vs_result_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_203_effort_vs_result_zscore_63d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def wyck_204_effort_vs_result_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_204_effort_vs_result_rank_63d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 63)

def wyck_205_effort_vs_result_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_205_effort_vs_result_lvl_126d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def wyck_206_effort_vs_result_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_206_effort_vs_result_zscore_126d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def wyck_207_effort_vs_result_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_207_effort_vs_result_rank_126d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 126)

def wyck_208_effort_vs_result_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_208_effort_vs_result_lvl_252d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def wyck_209_effort_vs_result_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_209_effort_vs_result_zscore_252d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def wyck_210_effort_vs_result_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_210_effort_vs_result_rank_252d
    ECONOMIC RATIONALE: Volume expended relative to the price range achieved.
    """
    base = volume / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 252)

def wyck_211_trend_channel_violation_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_211_trend_channel_violation_lvl_5d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rolling_mean(base, 5)

def wyck_212_trend_channel_violation_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_212_trend_channel_violation_zscore_5d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _zscore_rolling(base, 5)

def wyck_213_trend_channel_violation_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_213_trend_channel_violation_rank_5d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rank_pct(base, 5)

def wyck_214_trend_channel_violation_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_214_trend_channel_violation_lvl_21d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rolling_mean(base, 21)

def wyck_215_trend_channel_violation_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_215_trend_channel_violation_zscore_21d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _zscore_rolling(base, 21)

def wyck_216_trend_channel_violation_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_216_trend_channel_violation_rank_21d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rank_pct(base, 21)

def wyck_217_trend_channel_violation_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_217_trend_channel_violation_lvl_63d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rolling_mean(base, 63)

def wyck_218_trend_channel_violation_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_218_trend_channel_violation_zscore_63d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _zscore_rolling(base, 63)

def wyck_219_trend_channel_violation_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_219_trend_channel_violation_rank_63d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rank_pct(base, 63)

def wyck_220_trend_channel_violation_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_220_trend_channel_violation_lvl_126d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rolling_mean(base, 126)

def wyck_221_trend_channel_violation_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_221_trend_channel_violation_zscore_126d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _zscore_rolling(base, 126)

def wyck_222_trend_channel_violation_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_222_trend_channel_violation_rank_126d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rank_pct(base, 126)

def wyck_223_trend_channel_violation_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_223_trend_channel_violation_lvl_252d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rolling_mean(base, 252)

def wyck_224_trend_channel_violation_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_224_trend_channel_violation_zscore_252d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _zscore_rolling(base, 252)

def wyck_225_trend_channel_violation_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_225_trend_channel_violation_rank_252d
    ECONOMIC RATIONALE: Breakdown below trend channels.
    """
    base = low < low.rolling(63).mean() - 2*low.rolling(63).std()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V101_REGISTRY_2 = {
    "wyck_121_upthrust_detection_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_121_upthrust_detection_lvl_5d},
    "wyck_122_upthrust_detection_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_122_upthrust_detection_zscore_5d},
    "wyck_123_upthrust_detection_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_123_upthrust_detection_rank_5d},
    "wyck_124_upthrust_detection_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_124_upthrust_detection_lvl_21d},
    "wyck_125_upthrust_detection_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_125_upthrust_detection_zscore_21d},
    "wyck_126_upthrust_detection_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_126_upthrust_detection_rank_21d},
    "wyck_127_upthrust_detection_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_127_upthrust_detection_lvl_63d},
    "wyck_128_upthrust_detection_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_128_upthrust_detection_zscore_63d},
    "wyck_129_upthrust_detection_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_129_upthrust_detection_rank_63d},
    "wyck_130_upthrust_detection_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_130_upthrust_detection_lvl_126d},
    "wyck_131_upthrust_detection_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_131_upthrust_detection_zscore_126d},
    "wyck_132_upthrust_detection_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_132_upthrust_detection_rank_126d},
    "wyck_133_upthrust_detection_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_133_upthrust_detection_lvl_252d},
    "wyck_134_upthrust_detection_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_134_upthrust_detection_zscore_252d},
    "wyck_135_upthrust_detection_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_135_upthrust_detection_rank_252d},
    "wyck_136_preliminary_support_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_136_preliminary_support_lvl_5d},
    "wyck_137_preliminary_support_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_137_preliminary_support_zscore_5d},
    "wyck_138_preliminary_support_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_138_preliminary_support_rank_5d},
    "wyck_139_preliminary_support_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_139_preliminary_support_lvl_21d},
    "wyck_140_preliminary_support_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_140_preliminary_support_zscore_21d},
    "wyck_141_preliminary_support_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_141_preliminary_support_rank_21d},
    "wyck_142_preliminary_support_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_142_preliminary_support_lvl_63d},
    "wyck_143_preliminary_support_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_143_preliminary_support_zscore_63d},
    "wyck_144_preliminary_support_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_144_preliminary_support_rank_63d},
    "wyck_145_preliminary_support_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_145_preliminary_support_lvl_126d},
    "wyck_146_preliminary_support_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_146_preliminary_support_zscore_126d},
    "wyck_147_preliminary_support_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_147_preliminary_support_rank_126d},
    "wyck_148_preliminary_support_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_148_preliminary_support_lvl_252d},
    "wyck_149_preliminary_support_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_149_preliminary_support_zscore_252d},
    "wyck_150_preliminary_support_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_150_preliminary_support_rank_252d},
    "wyck_151_jump_across_creek_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_151_jump_across_creek_lvl_5d},
    "wyck_152_jump_across_creek_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_152_jump_across_creek_zscore_5d},
    "wyck_153_jump_across_creek_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_153_jump_across_creek_rank_5d},
    "wyck_154_jump_across_creek_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_154_jump_across_creek_lvl_21d},
    "wyck_155_jump_across_creek_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_155_jump_across_creek_zscore_21d},
    "wyck_156_jump_across_creek_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_156_jump_across_creek_rank_21d},
    "wyck_157_jump_across_creek_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_157_jump_across_creek_lvl_63d},
    "wyck_158_jump_across_creek_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_158_jump_across_creek_zscore_63d},
    "wyck_159_jump_across_creek_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_159_jump_across_creek_rank_63d},
    "wyck_160_jump_across_creek_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_160_jump_across_creek_lvl_126d},
    "wyck_161_jump_across_creek_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_161_jump_across_creek_zscore_126d},
    "wyck_162_jump_across_creek_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_162_jump_across_creek_rank_126d},
    "wyck_163_jump_across_creek_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_163_jump_across_creek_lvl_252d},
    "wyck_164_jump_across_creek_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_164_jump_across_creek_zscore_252d},
    "wyck_165_jump_across_creek_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_165_jump_across_creek_rank_252d},
    "wyck_166_last_point_of_supply_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_166_last_point_of_supply_lvl_5d},
    "wyck_167_last_point_of_supply_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_167_last_point_of_supply_zscore_5d},
    "wyck_168_last_point_of_supply_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_168_last_point_of_supply_rank_5d},
    "wyck_169_last_point_of_supply_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_169_last_point_of_supply_lvl_21d},
    "wyck_170_last_point_of_supply_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_170_last_point_of_supply_zscore_21d},
    "wyck_171_last_point_of_supply_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_171_last_point_of_supply_rank_21d},
    "wyck_172_last_point_of_supply_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_172_last_point_of_supply_lvl_63d},
    "wyck_173_last_point_of_supply_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_173_last_point_of_supply_zscore_63d},
    "wyck_174_last_point_of_supply_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_174_last_point_of_supply_rank_63d},
    "wyck_175_last_point_of_supply_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_175_last_point_of_supply_lvl_126d},
    "wyck_176_last_point_of_supply_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_176_last_point_of_supply_zscore_126d},
    "wyck_177_last_point_of_supply_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_177_last_point_of_supply_rank_126d},
    "wyck_178_last_point_of_supply_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_178_last_point_of_supply_lvl_252d},
    "wyck_179_last_point_of_supply_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_179_last_point_of_supply_zscore_252d},
    "wyck_180_last_point_of_supply_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_180_last_point_of_supply_rank_252d},
    "wyck_181_volume_price_divergence_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_181_volume_price_divergence_lvl_5d},
    "wyck_182_volume_price_divergence_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_182_volume_price_divergence_zscore_5d},
    "wyck_183_volume_price_divergence_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_183_volume_price_divergence_rank_5d},
    "wyck_184_volume_price_divergence_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_184_volume_price_divergence_lvl_21d},
    "wyck_185_volume_price_divergence_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_185_volume_price_divergence_zscore_21d},
    "wyck_186_volume_price_divergence_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_186_volume_price_divergence_rank_21d},
    "wyck_187_volume_price_divergence_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_187_volume_price_divergence_lvl_63d},
    "wyck_188_volume_price_divergence_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_188_volume_price_divergence_zscore_63d},
    "wyck_189_volume_price_divergence_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_189_volume_price_divergence_rank_63d},
    "wyck_190_volume_price_divergence_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_190_volume_price_divergence_lvl_126d},
    "wyck_191_volume_price_divergence_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_191_volume_price_divergence_zscore_126d},
    "wyck_192_volume_price_divergence_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_192_volume_price_divergence_rank_126d},
    "wyck_193_volume_price_divergence_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_193_volume_price_divergence_lvl_252d},
    "wyck_194_volume_price_divergence_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_194_volume_price_divergence_zscore_252d},
    "wyck_195_volume_price_divergence_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_195_volume_price_divergence_rank_252d},
    "wyck_196_effort_vs_result_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_196_effort_vs_result_lvl_5d},
    "wyck_197_effort_vs_result_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_197_effort_vs_result_zscore_5d},
    "wyck_198_effort_vs_result_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_198_effort_vs_result_rank_5d},
    "wyck_199_effort_vs_result_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_199_effort_vs_result_lvl_21d},
    "wyck_200_effort_vs_result_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_200_effort_vs_result_zscore_21d},
    "wyck_201_effort_vs_result_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_201_effort_vs_result_rank_21d},
    "wyck_202_effort_vs_result_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_202_effort_vs_result_lvl_63d},
    "wyck_203_effort_vs_result_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_203_effort_vs_result_zscore_63d},
    "wyck_204_effort_vs_result_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_204_effort_vs_result_rank_63d},
    "wyck_205_effort_vs_result_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_205_effort_vs_result_lvl_126d},
    "wyck_206_effort_vs_result_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_206_effort_vs_result_zscore_126d},
    "wyck_207_effort_vs_result_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_207_effort_vs_result_rank_126d},
    "wyck_208_effort_vs_result_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_208_effort_vs_result_lvl_252d},
    "wyck_209_effort_vs_result_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_209_effort_vs_result_zscore_252d},
    "wyck_210_effort_vs_result_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_210_effort_vs_result_rank_252d},
    "wyck_211_trend_channel_violation_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_211_trend_channel_violation_lvl_5d},
    "wyck_212_trend_channel_violation_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_212_trend_channel_violation_zscore_5d},
    "wyck_213_trend_channel_violation_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_213_trend_channel_violation_rank_5d},
    "wyck_214_trend_channel_violation_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_214_trend_channel_violation_lvl_21d},
    "wyck_215_trend_channel_violation_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_215_trend_channel_violation_zscore_21d},
    "wyck_216_trend_channel_violation_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_216_trend_channel_violation_rank_21d},
    "wyck_217_trend_channel_violation_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_217_trend_channel_violation_lvl_63d},
    "wyck_218_trend_channel_violation_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_218_trend_channel_violation_zscore_63d},
    "wyck_219_trend_channel_violation_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_219_trend_channel_violation_rank_63d},
    "wyck_220_trend_channel_violation_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_220_trend_channel_violation_lvl_126d},
    "wyck_221_trend_channel_violation_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_221_trend_channel_violation_zscore_126d},
    "wyck_222_trend_channel_violation_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_222_trend_channel_violation_rank_126d},
    "wyck_223_trend_channel_violation_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_223_trend_channel_violation_lvl_252d},
    "wyck_224_trend_channel_violation_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_224_trend_channel_violation_zscore_252d},
    "wyck_225_trend_channel_violation_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_225_trend_channel_violation_rank_252d},
}
