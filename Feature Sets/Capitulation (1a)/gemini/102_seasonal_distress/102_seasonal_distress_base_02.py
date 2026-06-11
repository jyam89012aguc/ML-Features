"""
102_seasonal_distress — Base Features Part 2
Domain: seasonal_distress
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

def seas_121_may_sell_signal_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_121_may_sell_signal_lvl_5d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rolling_mean(base, 5)

def seas_122_may_sell_signal_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_122_may_sell_signal_zscore_5d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _zscore_rolling(base, 5)

def seas_123_may_sell_signal_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_123_may_sell_signal_rank_5d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rank_pct(base, 5)

def seas_124_may_sell_signal_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_124_may_sell_signal_lvl_21d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rolling_mean(base, 21)

def seas_125_may_sell_signal_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_125_may_sell_signal_zscore_21d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _zscore_rolling(base, 21)

def seas_126_may_sell_signal_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_126_may_sell_signal_rank_21d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rank_pct(base, 21)

def seas_127_may_sell_signal_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_127_may_sell_signal_lvl_63d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rolling_mean(base, 63)

def seas_128_may_sell_signal_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_128_may_sell_signal_zscore_63d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _zscore_rolling(base, 63)

def seas_129_may_sell_signal_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_129_may_sell_signal_rank_63d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rank_pct(base, 63)

def seas_130_may_sell_signal_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_130_may_sell_signal_lvl_126d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rolling_mean(base, 126)

def seas_131_may_sell_signal_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_131_may_sell_signal_zscore_126d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _zscore_rolling(base, 126)

def seas_132_may_sell_signal_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_132_may_sell_signal_rank_126d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rank_pct(base, 126)

def seas_133_may_sell_signal_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_133_may_sell_signal_lvl_252d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rolling_mean(base, 252)

def seas_134_may_sell_signal_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_134_may_sell_signal_zscore_252d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _zscore_rolling(base, 252)

def seas_135_may_sell_signal_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_135_may_sell_signal_rank_252d
    ECONOMIC RATIONALE: Seasonal 'sell in May' effect.
    """
    base = close.pct_change(21) * (close.index.month == 5).astype(float)
    return _rank_pct(base, 252)

def seas_136_quarterly_seasonality_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_136_quarterly_seasonality_lvl_5d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rolling_mean(base, 5)

def seas_137_quarterly_seasonality_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_137_quarterly_seasonality_zscore_5d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _zscore_rolling(base, 5)

def seas_138_quarterly_seasonality_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_138_quarterly_seasonality_rank_5d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rank_pct(base, 5)

def seas_139_quarterly_seasonality_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_139_quarterly_seasonality_lvl_21d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rolling_mean(base, 21)

def seas_140_quarterly_seasonality_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_140_quarterly_seasonality_zscore_21d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _zscore_rolling(base, 21)

def seas_141_quarterly_seasonality_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_141_quarterly_seasonality_rank_21d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rank_pct(base, 21)

def seas_142_quarterly_seasonality_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_142_quarterly_seasonality_lvl_63d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rolling_mean(base, 63)

def seas_143_quarterly_seasonality_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_143_quarterly_seasonality_zscore_63d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _zscore_rolling(base, 63)

def seas_144_quarterly_seasonality_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_144_quarterly_seasonality_rank_63d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rank_pct(base, 63)

def seas_145_quarterly_seasonality_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_145_quarterly_seasonality_lvl_126d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rolling_mean(base, 126)

def seas_146_quarterly_seasonality_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_146_quarterly_seasonality_zscore_126d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _zscore_rolling(base, 126)

def seas_147_quarterly_seasonality_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_147_quarterly_seasonality_rank_126d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rank_pct(base, 126)

def seas_148_quarterly_seasonality_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_148_quarterly_seasonality_lvl_252d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rolling_mean(base, 252)

def seas_149_quarterly_seasonality_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_149_quarterly_seasonality_zscore_252d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _zscore_rolling(base, 252)

def seas_150_quarterly_seasonality_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_150_quarterly_seasonality_rank_252d
    ECONOMIC RATIONALE: Average returns by fiscal quarter.
    """
    base = close.pct_change(63).groupby(close.index.quarter).transform('mean')
    return _rank_pct(base, 252)

def seas_151_seasonal_zscore_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_151_seasonal_zscore_lvl_5d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 5)

def seas_152_seasonal_zscore_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_152_seasonal_zscore_zscore_5d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 5)

def seas_153_seasonal_zscore_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_153_seasonal_zscore_rank_5d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 5)

def seas_154_seasonal_zscore_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_154_seasonal_zscore_lvl_21d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 21)

def seas_155_seasonal_zscore_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_155_seasonal_zscore_zscore_21d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 21)

def seas_156_seasonal_zscore_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_156_seasonal_zscore_rank_21d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 21)

def seas_157_seasonal_zscore_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_157_seasonal_zscore_lvl_63d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 63)

def seas_158_seasonal_zscore_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_158_seasonal_zscore_zscore_63d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 63)

def seas_159_seasonal_zscore_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_159_seasonal_zscore_rank_63d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 63)

def seas_160_seasonal_zscore_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_160_seasonal_zscore_lvl_126d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 126)

def seas_161_seasonal_zscore_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_161_seasonal_zscore_zscore_126d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 126)

def seas_162_seasonal_zscore_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_162_seasonal_zscore_rank_126d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 126)

def seas_163_seasonal_zscore_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_163_seasonal_zscore_lvl_252d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rolling_mean(base, 252)

def seas_164_seasonal_zscore_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_164_seasonal_zscore_zscore_252d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _zscore_rolling(base, 252)

def seas_165_seasonal_zscore_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_165_seasonal_zscore_rank_252d
    ECONOMIC RATIONALE: Returns relative to the rolling annual distribution.
    """
    base = _zscore_rolling(close.pct_change(21), 252)
    return _rank_pct(base, 252)

def seas_166_holiday_liquidity_drain_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_166_holiday_liquidity_drain_lvl_5d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 5)

def seas_167_holiday_liquidity_drain_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_167_holiday_liquidity_drain_zscore_5d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 5)

def seas_168_holiday_liquidity_drain_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_168_holiday_liquidity_drain_rank_5d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 5)

def seas_169_holiday_liquidity_drain_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_169_holiday_liquidity_drain_lvl_21d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 21)

def seas_170_holiday_liquidity_drain_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_170_holiday_liquidity_drain_zscore_21d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 21)

def seas_171_holiday_liquidity_drain_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_171_holiday_liquidity_drain_rank_21d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 21)

def seas_172_holiday_liquidity_drain_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_172_holiday_liquidity_drain_lvl_63d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 63)

def seas_173_holiday_liquidity_drain_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_173_holiday_liquidity_drain_zscore_63d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 63)

def seas_174_holiday_liquidity_drain_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_174_holiday_liquidity_drain_rank_63d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 63)

def seas_175_holiday_liquidity_drain_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_175_holiday_liquidity_drain_lvl_126d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 126)

def seas_176_holiday_liquidity_drain_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_176_holiday_liquidity_drain_zscore_126d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 126)

def seas_177_holiday_liquidity_drain_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_177_holiday_liquidity_drain_rank_126d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 126)

def seas_178_holiday_liquidity_drain_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_178_holiday_liquidity_drain_lvl_252d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 252)

def seas_179_holiday_liquidity_drain_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_179_holiday_liquidity_drain_zscore_252d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 252)

def seas_180_holiday_liquidity_drain_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_180_holiday_liquidity_drain_rank_252d
    ECONOMIC RATIONALE: Volume drops around holiday periods.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 252)

def seas_181_seasonal_trend_strength_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_181_seasonal_trend_strength_lvl_5d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rolling_mean(base, 5)

def seas_182_seasonal_trend_strength_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_182_seasonal_trend_strength_zscore_5d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _zscore_rolling(base, 5)

def seas_183_seasonal_trend_strength_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_183_seasonal_trend_strength_rank_5d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rank_pct(base, 5)

def seas_184_seasonal_trend_strength_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_184_seasonal_trend_strength_lvl_21d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rolling_mean(base, 21)

def seas_185_seasonal_trend_strength_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_185_seasonal_trend_strength_zscore_21d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _zscore_rolling(base, 21)

def seas_186_seasonal_trend_strength_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_186_seasonal_trend_strength_rank_21d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rank_pct(base, 21)

def seas_187_seasonal_trend_strength_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_187_seasonal_trend_strength_lvl_63d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rolling_mean(base, 63)

def seas_188_seasonal_trend_strength_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_188_seasonal_trend_strength_zscore_63d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _zscore_rolling(base, 63)

def seas_189_seasonal_trend_strength_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_189_seasonal_trend_strength_rank_63d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rank_pct(base, 63)

def seas_190_seasonal_trend_strength_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_190_seasonal_trend_strength_lvl_126d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rolling_mean(base, 126)

def seas_191_seasonal_trend_strength_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_191_seasonal_trend_strength_zscore_126d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _zscore_rolling(base, 126)

def seas_192_seasonal_trend_strength_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_192_seasonal_trend_strength_rank_126d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rank_pct(base, 126)

def seas_193_seasonal_trend_strength_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_193_seasonal_trend_strength_lvl_252d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rolling_mean(base, 252)

def seas_194_seasonal_trend_strength_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_194_seasonal_trend_strength_zscore_252d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _zscore_rolling(base, 252)

def seas_195_seasonal_trend_strength_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_195_seasonal_trend_strength_rank_252d
    ECONOMIC RATIONALE: Medium vs long term structural trend.
    """
    base = close.rolling(63).mean() / close.rolling(252).mean()
    return _rank_pct(base, 252)

def seas_196_periodic_reversal_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_196_periodic_reversal_lvl_5d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rolling_mean(base, 5)

def seas_197_periodic_reversal_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_197_periodic_reversal_zscore_5d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _zscore_rolling(base, 5)

def seas_198_periodic_reversal_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_198_periodic_reversal_rank_5d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rank_pct(base, 5)

def seas_199_periodic_reversal_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_199_periodic_reversal_lvl_21d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rolling_mean(base, 21)

def seas_200_periodic_reversal_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_200_periodic_reversal_zscore_21d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _zscore_rolling(base, 21)

def seas_201_periodic_reversal_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_201_periodic_reversal_rank_21d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rank_pct(base, 21)

def seas_202_periodic_reversal_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_202_periodic_reversal_lvl_63d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rolling_mean(base, 63)

def seas_203_periodic_reversal_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_203_periodic_reversal_zscore_63d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _zscore_rolling(base, 63)

def seas_204_periodic_reversal_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_204_periodic_reversal_rank_63d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rank_pct(base, 63)

def seas_205_periodic_reversal_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_205_periodic_reversal_lvl_126d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rolling_mean(base, 126)

def seas_206_periodic_reversal_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_206_periodic_reversal_zscore_126d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _zscore_rolling(base, 126)

def seas_207_periodic_reversal_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_207_periodic_reversal_rank_126d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rank_pct(base, 126)

def seas_208_periodic_reversal_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_208_periodic_reversal_lvl_252d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rolling_mean(base, 252)

def seas_209_periodic_reversal_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_209_periodic_reversal_zscore_252d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _zscore_rolling(base, 252)

def seas_210_periodic_reversal_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_210_periodic_reversal_rank_252d
    ECONOMIC RATIONALE: Short-term reaction vs long-term cycle.
    """
    base = close.pct_change(5) / close.pct_change(252)
    return _rank_pct(base, 252)

def seas_211_cycle_position_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_211_cycle_position_lvl_5d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rolling_mean(base, 5)

def seas_212_cycle_position_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_212_cycle_position_zscore_5d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _zscore_rolling(base, 5)

def seas_213_cycle_position_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_213_cycle_position_rank_5d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rank_pct(base, 5)

def seas_214_cycle_position_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_214_cycle_position_lvl_21d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rolling_mean(base, 21)

def seas_215_cycle_position_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_215_cycle_position_zscore_21d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _zscore_rolling(base, 21)

def seas_216_cycle_position_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_216_cycle_position_rank_21d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rank_pct(base, 21)

def seas_217_cycle_position_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_217_cycle_position_lvl_63d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rolling_mean(base, 63)

def seas_218_cycle_position_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_218_cycle_position_zscore_63d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _zscore_rolling(base, 63)

def seas_219_cycle_position_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_219_cycle_position_rank_63d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rank_pct(base, 63)

def seas_220_cycle_position_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_220_cycle_position_lvl_126d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rolling_mean(base, 126)

def seas_221_cycle_position_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_221_cycle_position_zscore_126d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _zscore_rolling(base, 126)

def seas_222_cycle_position_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_222_cycle_position_rank_126d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rank_pct(base, 126)

def seas_223_cycle_position_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_223_cycle_position_lvl_252d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rolling_mean(base, 252)

def seas_224_cycle_position_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_224_cycle_position_zscore_252d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _zscore_rolling(base, 252)

def seas_225_cycle_position_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_225_cycle_position_rank_252d
    ECONOMIC RATIONALE: Sinusoidal representation of the annual cycle.
    """
    base = np.sin(2 * np.pi * close.index.dayofyear / 365.25)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V102_REGISTRY_2 = {
    "seas_121_may_sell_signal_lvl_5d": {"inputs": ["close", "volume"], "func": seas_121_may_sell_signal_lvl_5d},
    "seas_122_may_sell_signal_zscore_5d": {"inputs": ["close", "volume"], "func": seas_122_may_sell_signal_zscore_5d},
    "seas_123_may_sell_signal_rank_5d": {"inputs": ["close", "volume"], "func": seas_123_may_sell_signal_rank_5d},
    "seas_124_may_sell_signal_lvl_21d": {"inputs": ["close", "volume"], "func": seas_124_may_sell_signal_lvl_21d},
    "seas_125_may_sell_signal_zscore_21d": {"inputs": ["close", "volume"], "func": seas_125_may_sell_signal_zscore_21d},
    "seas_126_may_sell_signal_rank_21d": {"inputs": ["close", "volume"], "func": seas_126_may_sell_signal_rank_21d},
    "seas_127_may_sell_signal_lvl_63d": {"inputs": ["close", "volume"], "func": seas_127_may_sell_signal_lvl_63d},
    "seas_128_may_sell_signal_zscore_63d": {"inputs": ["close", "volume"], "func": seas_128_may_sell_signal_zscore_63d},
    "seas_129_may_sell_signal_rank_63d": {"inputs": ["close", "volume"], "func": seas_129_may_sell_signal_rank_63d},
    "seas_130_may_sell_signal_lvl_126d": {"inputs": ["close", "volume"], "func": seas_130_may_sell_signal_lvl_126d},
    "seas_131_may_sell_signal_zscore_126d": {"inputs": ["close", "volume"], "func": seas_131_may_sell_signal_zscore_126d},
    "seas_132_may_sell_signal_rank_126d": {"inputs": ["close", "volume"], "func": seas_132_may_sell_signal_rank_126d},
    "seas_133_may_sell_signal_lvl_252d": {"inputs": ["close", "volume"], "func": seas_133_may_sell_signal_lvl_252d},
    "seas_134_may_sell_signal_zscore_252d": {"inputs": ["close", "volume"], "func": seas_134_may_sell_signal_zscore_252d},
    "seas_135_may_sell_signal_rank_252d": {"inputs": ["close", "volume"], "func": seas_135_may_sell_signal_rank_252d},
    "seas_136_quarterly_seasonality_lvl_5d": {"inputs": ["close", "volume"], "func": seas_136_quarterly_seasonality_lvl_5d},
    "seas_137_quarterly_seasonality_zscore_5d": {"inputs": ["close", "volume"], "func": seas_137_quarterly_seasonality_zscore_5d},
    "seas_138_quarterly_seasonality_rank_5d": {"inputs": ["close", "volume"], "func": seas_138_quarterly_seasonality_rank_5d},
    "seas_139_quarterly_seasonality_lvl_21d": {"inputs": ["close", "volume"], "func": seas_139_quarterly_seasonality_lvl_21d},
    "seas_140_quarterly_seasonality_zscore_21d": {"inputs": ["close", "volume"], "func": seas_140_quarterly_seasonality_zscore_21d},
    "seas_141_quarterly_seasonality_rank_21d": {"inputs": ["close", "volume"], "func": seas_141_quarterly_seasonality_rank_21d},
    "seas_142_quarterly_seasonality_lvl_63d": {"inputs": ["close", "volume"], "func": seas_142_quarterly_seasonality_lvl_63d},
    "seas_143_quarterly_seasonality_zscore_63d": {"inputs": ["close", "volume"], "func": seas_143_quarterly_seasonality_zscore_63d},
    "seas_144_quarterly_seasonality_rank_63d": {"inputs": ["close", "volume"], "func": seas_144_quarterly_seasonality_rank_63d},
    "seas_145_quarterly_seasonality_lvl_126d": {"inputs": ["close", "volume"], "func": seas_145_quarterly_seasonality_lvl_126d},
    "seas_146_quarterly_seasonality_zscore_126d": {"inputs": ["close", "volume"], "func": seas_146_quarterly_seasonality_zscore_126d},
    "seas_147_quarterly_seasonality_rank_126d": {"inputs": ["close", "volume"], "func": seas_147_quarterly_seasonality_rank_126d},
    "seas_148_quarterly_seasonality_lvl_252d": {"inputs": ["close", "volume"], "func": seas_148_quarterly_seasonality_lvl_252d},
    "seas_149_quarterly_seasonality_zscore_252d": {"inputs": ["close", "volume"], "func": seas_149_quarterly_seasonality_zscore_252d},
    "seas_150_quarterly_seasonality_rank_252d": {"inputs": ["close", "volume"], "func": seas_150_quarterly_seasonality_rank_252d},
    "seas_151_seasonal_zscore_lvl_5d": {"inputs": ["close", "volume"], "func": seas_151_seasonal_zscore_lvl_5d},
    "seas_152_seasonal_zscore_zscore_5d": {"inputs": ["close", "volume"], "func": seas_152_seasonal_zscore_zscore_5d},
    "seas_153_seasonal_zscore_rank_5d": {"inputs": ["close", "volume"], "func": seas_153_seasonal_zscore_rank_5d},
    "seas_154_seasonal_zscore_lvl_21d": {"inputs": ["close", "volume"], "func": seas_154_seasonal_zscore_lvl_21d},
    "seas_155_seasonal_zscore_zscore_21d": {"inputs": ["close", "volume"], "func": seas_155_seasonal_zscore_zscore_21d},
    "seas_156_seasonal_zscore_rank_21d": {"inputs": ["close", "volume"], "func": seas_156_seasonal_zscore_rank_21d},
    "seas_157_seasonal_zscore_lvl_63d": {"inputs": ["close", "volume"], "func": seas_157_seasonal_zscore_lvl_63d},
    "seas_158_seasonal_zscore_zscore_63d": {"inputs": ["close", "volume"], "func": seas_158_seasonal_zscore_zscore_63d},
    "seas_159_seasonal_zscore_rank_63d": {"inputs": ["close", "volume"], "func": seas_159_seasonal_zscore_rank_63d},
    "seas_160_seasonal_zscore_lvl_126d": {"inputs": ["close", "volume"], "func": seas_160_seasonal_zscore_lvl_126d},
    "seas_161_seasonal_zscore_zscore_126d": {"inputs": ["close", "volume"], "func": seas_161_seasonal_zscore_zscore_126d},
    "seas_162_seasonal_zscore_rank_126d": {"inputs": ["close", "volume"], "func": seas_162_seasonal_zscore_rank_126d},
    "seas_163_seasonal_zscore_lvl_252d": {"inputs": ["close", "volume"], "func": seas_163_seasonal_zscore_lvl_252d},
    "seas_164_seasonal_zscore_zscore_252d": {"inputs": ["close", "volume"], "func": seas_164_seasonal_zscore_zscore_252d},
    "seas_165_seasonal_zscore_rank_252d": {"inputs": ["close", "volume"], "func": seas_165_seasonal_zscore_rank_252d},
    "seas_166_holiday_liquidity_drain_lvl_5d": {"inputs": ["close", "volume"], "func": seas_166_holiday_liquidity_drain_lvl_5d},
    "seas_167_holiday_liquidity_drain_zscore_5d": {"inputs": ["close", "volume"], "func": seas_167_holiday_liquidity_drain_zscore_5d},
    "seas_168_holiday_liquidity_drain_rank_5d": {"inputs": ["close", "volume"], "func": seas_168_holiday_liquidity_drain_rank_5d},
    "seas_169_holiday_liquidity_drain_lvl_21d": {"inputs": ["close", "volume"], "func": seas_169_holiday_liquidity_drain_lvl_21d},
    "seas_170_holiday_liquidity_drain_zscore_21d": {"inputs": ["close", "volume"], "func": seas_170_holiday_liquidity_drain_zscore_21d},
    "seas_171_holiday_liquidity_drain_rank_21d": {"inputs": ["close", "volume"], "func": seas_171_holiday_liquidity_drain_rank_21d},
    "seas_172_holiday_liquidity_drain_lvl_63d": {"inputs": ["close", "volume"], "func": seas_172_holiday_liquidity_drain_lvl_63d},
    "seas_173_holiday_liquidity_drain_zscore_63d": {"inputs": ["close", "volume"], "func": seas_173_holiday_liquidity_drain_zscore_63d},
    "seas_174_holiday_liquidity_drain_rank_63d": {"inputs": ["close", "volume"], "func": seas_174_holiday_liquidity_drain_rank_63d},
    "seas_175_holiday_liquidity_drain_lvl_126d": {"inputs": ["close", "volume"], "func": seas_175_holiday_liquidity_drain_lvl_126d},
    "seas_176_holiday_liquidity_drain_zscore_126d": {"inputs": ["close", "volume"], "func": seas_176_holiday_liquidity_drain_zscore_126d},
    "seas_177_holiday_liquidity_drain_rank_126d": {"inputs": ["close", "volume"], "func": seas_177_holiday_liquidity_drain_rank_126d},
    "seas_178_holiday_liquidity_drain_lvl_252d": {"inputs": ["close", "volume"], "func": seas_178_holiday_liquidity_drain_lvl_252d},
    "seas_179_holiday_liquidity_drain_zscore_252d": {"inputs": ["close", "volume"], "func": seas_179_holiday_liquidity_drain_zscore_252d},
    "seas_180_holiday_liquidity_drain_rank_252d": {"inputs": ["close", "volume"], "func": seas_180_holiday_liquidity_drain_rank_252d},
    "seas_181_seasonal_trend_strength_lvl_5d": {"inputs": ["close", "volume"], "func": seas_181_seasonal_trend_strength_lvl_5d},
    "seas_182_seasonal_trend_strength_zscore_5d": {"inputs": ["close", "volume"], "func": seas_182_seasonal_trend_strength_zscore_5d},
    "seas_183_seasonal_trend_strength_rank_5d": {"inputs": ["close", "volume"], "func": seas_183_seasonal_trend_strength_rank_5d},
    "seas_184_seasonal_trend_strength_lvl_21d": {"inputs": ["close", "volume"], "func": seas_184_seasonal_trend_strength_lvl_21d},
    "seas_185_seasonal_trend_strength_zscore_21d": {"inputs": ["close", "volume"], "func": seas_185_seasonal_trend_strength_zscore_21d},
    "seas_186_seasonal_trend_strength_rank_21d": {"inputs": ["close", "volume"], "func": seas_186_seasonal_trend_strength_rank_21d},
    "seas_187_seasonal_trend_strength_lvl_63d": {"inputs": ["close", "volume"], "func": seas_187_seasonal_trend_strength_lvl_63d},
    "seas_188_seasonal_trend_strength_zscore_63d": {"inputs": ["close", "volume"], "func": seas_188_seasonal_trend_strength_zscore_63d},
    "seas_189_seasonal_trend_strength_rank_63d": {"inputs": ["close", "volume"], "func": seas_189_seasonal_trend_strength_rank_63d},
    "seas_190_seasonal_trend_strength_lvl_126d": {"inputs": ["close", "volume"], "func": seas_190_seasonal_trend_strength_lvl_126d},
    "seas_191_seasonal_trend_strength_zscore_126d": {"inputs": ["close", "volume"], "func": seas_191_seasonal_trend_strength_zscore_126d},
    "seas_192_seasonal_trend_strength_rank_126d": {"inputs": ["close", "volume"], "func": seas_192_seasonal_trend_strength_rank_126d},
    "seas_193_seasonal_trend_strength_lvl_252d": {"inputs": ["close", "volume"], "func": seas_193_seasonal_trend_strength_lvl_252d},
    "seas_194_seasonal_trend_strength_zscore_252d": {"inputs": ["close", "volume"], "func": seas_194_seasonal_trend_strength_zscore_252d},
    "seas_195_seasonal_trend_strength_rank_252d": {"inputs": ["close", "volume"], "func": seas_195_seasonal_trend_strength_rank_252d},
    "seas_196_periodic_reversal_lvl_5d": {"inputs": ["close", "volume"], "func": seas_196_periodic_reversal_lvl_5d},
    "seas_197_periodic_reversal_zscore_5d": {"inputs": ["close", "volume"], "func": seas_197_periodic_reversal_zscore_5d},
    "seas_198_periodic_reversal_rank_5d": {"inputs": ["close", "volume"], "func": seas_198_periodic_reversal_rank_5d},
    "seas_199_periodic_reversal_lvl_21d": {"inputs": ["close", "volume"], "func": seas_199_periodic_reversal_lvl_21d},
    "seas_200_periodic_reversal_zscore_21d": {"inputs": ["close", "volume"], "func": seas_200_periodic_reversal_zscore_21d},
    "seas_201_periodic_reversal_rank_21d": {"inputs": ["close", "volume"], "func": seas_201_periodic_reversal_rank_21d},
    "seas_202_periodic_reversal_lvl_63d": {"inputs": ["close", "volume"], "func": seas_202_periodic_reversal_lvl_63d},
    "seas_203_periodic_reversal_zscore_63d": {"inputs": ["close", "volume"], "func": seas_203_periodic_reversal_zscore_63d},
    "seas_204_periodic_reversal_rank_63d": {"inputs": ["close", "volume"], "func": seas_204_periodic_reversal_rank_63d},
    "seas_205_periodic_reversal_lvl_126d": {"inputs": ["close", "volume"], "func": seas_205_periodic_reversal_lvl_126d},
    "seas_206_periodic_reversal_zscore_126d": {"inputs": ["close", "volume"], "func": seas_206_periodic_reversal_zscore_126d},
    "seas_207_periodic_reversal_rank_126d": {"inputs": ["close", "volume"], "func": seas_207_periodic_reversal_rank_126d},
    "seas_208_periodic_reversal_lvl_252d": {"inputs": ["close", "volume"], "func": seas_208_periodic_reversal_lvl_252d},
    "seas_209_periodic_reversal_zscore_252d": {"inputs": ["close", "volume"], "func": seas_209_periodic_reversal_zscore_252d},
    "seas_210_periodic_reversal_rank_252d": {"inputs": ["close", "volume"], "func": seas_210_periodic_reversal_rank_252d},
    "seas_211_cycle_position_lvl_5d": {"inputs": ["close", "volume"], "func": seas_211_cycle_position_lvl_5d},
    "seas_212_cycle_position_zscore_5d": {"inputs": ["close", "volume"], "func": seas_212_cycle_position_zscore_5d},
    "seas_213_cycle_position_rank_5d": {"inputs": ["close", "volume"], "func": seas_213_cycle_position_rank_5d},
    "seas_214_cycle_position_lvl_21d": {"inputs": ["close", "volume"], "func": seas_214_cycle_position_lvl_21d},
    "seas_215_cycle_position_zscore_21d": {"inputs": ["close", "volume"], "func": seas_215_cycle_position_zscore_21d},
    "seas_216_cycle_position_rank_21d": {"inputs": ["close", "volume"], "func": seas_216_cycle_position_rank_21d},
    "seas_217_cycle_position_lvl_63d": {"inputs": ["close", "volume"], "func": seas_217_cycle_position_lvl_63d},
    "seas_218_cycle_position_zscore_63d": {"inputs": ["close", "volume"], "func": seas_218_cycle_position_zscore_63d},
    "seas_219_cycle_position_rank_63d": {"inputs": ["close", "volume"], "func": seas_219_cycle_position_rank_63d},
    "seas_220_cycle_position_lvl_126d": {"inputs": ["close", "volume"], "func": seas_220_cycle_position_lvl_126d},
    "seas_221_cycle_position_zscore_126d": {"inputs": ["close", "volume"], "func": seas_221_cycle_position_zscore_126d},
    "seas_222_cycle_position_rank_126d": {"inputs": ["close", "volume"], "func": seas_222_cycle_position_rank_126d},
    "seas_223_cycle_position_lvl_252d": {"inputs": ["close", "volume"], "func": seas_223_cycle_position_lvl_252d},
    "seas_224_cycle_position_zscore_252d": {"inputs": ["close", "volume"], "func": seas_224_cycle_position_zscore_252d},
    "seas_225_cycle_position_rank_252d": {"inputs": ["close", "volume"], "func": seas_225_cycle_position_rank_252d},
}
