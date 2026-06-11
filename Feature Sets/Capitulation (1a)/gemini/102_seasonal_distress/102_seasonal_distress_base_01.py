"""
102_seasonal_distress — Base Features Part 1
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

def seas_001_tax_loss_selling_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_001_tax_loss_selling_lvl_5d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rolling_mean(base, 5)

def seas_002_tax_loss_selling_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_002_tax_loss_selling_zscore_5d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _zscore_rolling(base, 5)

def seas_003_tax_loss_selling_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_003_tax_loss_selling_rank_5d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rank_pct(base, 5)

def seas_004_tax_loss_selling_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_004_tax_loss_selling_lvl_21d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rolling_mean(base, 21)

def seas_005_tax_loss_selling_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_005_tax_loss_selling_zscore_21d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _zscore_rolling(base, 21)

def seas_006_tax_loss_selling_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_006_tax_loss_selling_rank_21d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rank_pct(base, 21)

def seas_007_tax_loss_selling_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_007_tax_loss_selling_lvl_63d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rolling_mean(base, 63)

def seas_008_tax_loss_selling_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_008_tax_loss_selling_zscore_63d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _zscore_rolling(base, 63)

def seas_009_tax_loss_selling_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_009_tax_loss_selling_rank_63d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rank_pct(base, 63)

def seas_010_tax_loss_selling_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_010_tax_loss_selling_lvl_126d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rolling_mean(base, 126)

def seas_011_tax_loss_selling_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_011_tax_loss_selling_zscore_126d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _zscore_rolling(base, 126)

def seas_012_tax_loss_selling_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_012_tax_loss_selling_rank_126d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rank_pct(base, 126)

def seas_013_tax_loss_selling_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_013_tax_loss_selling_lvl_252d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rolling_mean(base, 252)

def seas_014_tax_loss_selling_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_014_tax_loss_selling_zscore_252d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _zscore_rolling(base, 252)

def seas_015_tax_loss_selling_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_015_tax_loss_selling_rank_252d
    ECONOMIC RATIONALE: Deeply negative annual returns increase year-end selling pressure.
    """
    base = close.pct_change(252) < -0.3
    return _rank_pct(base, 252)

def seas_016_january_effect_reversal_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_016_january_effect_reversal_lvl_5d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rolling_mean(base, 5)

def seas_017_january_effect_reversal_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_017_january_effect_reversal_zscore_5d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _zscore_rolling(base, 5)

def seas_018_january_effect_reversal_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_018_january_effect_reversal_rank_5d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rank_pct(base, 5)

def seas_019_january_effect_reversal_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_019_january_effect_reversal_lvl_21d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rolling_mean(base, 21)

def seas_020_january_effect_reversal_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_020_january_effect_reversal_zscore_21d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _zscore_rolling(base, 21)

def seas_021_january_effect_reversal_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_021_january_effect_reversal_rank_21d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rank_pct(base, 21)

def seas_022_january_effect_reversal_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_022_january_effect_reversal_lvl_63d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rolling_mean(base, 63)

def seas_023_january_effect_reversal_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_023_january_effect_reversal_zscore_63d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _zscore_rolling(base, 63)

def seas_024_january_effect_reversal_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_024_january_effect_reversal_rank_63d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rank_pct(base, 63)

def seas_025_january_effect_reversal_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_025_january_effect_reversal_lvl_126d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rolling_mean(base, 126)

def seas_026_january_effect_reversal_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_026_january_effect_reversal_zscore_126d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _zscore_rolling(base, 126)

def seas_027_january_effect_reversal_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_027_january_effect_reversal_rank_126d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rank_pct(base, 126)

def seas_028_january_effect_reversal_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_028_january_effect_reversal_lvl_252d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rolling_mean(base, 252)

def seas_029_january_effect_reversal_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_029_january_effect_reversal_zscore_252d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _zscore_rolling(base, 252)

def seas_030_january_effect_reversal_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_030_january_effect_reversal_rank_252d
    ECONOMIC RATIONALE: Mean reversion potential in January for oversold stocks.
    """
    base = close.pct_change(21)
    return _rank_pct(base, 252)

def seas_031_quarter_end_window_dressing_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_031_quarter_end_window_dressing_lvl_5d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 5)

def seas_032_quarter_end_window_dressing_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_032_quarter_end_window_dressing_zscore_5d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 5)

def seas_033_quarter_end_window_dressing_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_033_quarter_end_window_dressing_rank_5d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 5)

def seas_034_quarter_end_window_dressing_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_034_quarter_end_window_dressing_lvl_21d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 21)

def seas_035_quarter_end_window_dressing_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_035_quarter_end_window_dressing_zscore_21d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 21)

def seas_036_quarter_end_window_dressing_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_036_quarter_end_window_dressing_rank_21d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 21)

def seas_037_quarter_end_window_dressing_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_037_quarter_end_window_dressing_lvl_63d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 63)

def seas_038_quarter_end_window_dressing_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_038_quarter_end_window_dressing_zscore_63d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 63)

def seas_039_quarter_end_window_dressing_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_039_quarter_end_window_dressing_rank_63d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 63)

def seas_040_quarter_end_window_dressing_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_040_quarter_end_window_dressing_lvl_126d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 126)

def seas_041_quarter_end_window_dressing_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_041_quarter_end_window_dressing_zscore_126d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 126)

def seas_042_quarter_end_window_dressing_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_042_quarter_end_window_dressing_rank_126d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 126)

def seas_043_quarter_end_window_dressing_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_043_quarter_end_window_dressing_lvl_252d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 252)

def seas_044_quarter_end_window_dressing_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_044_quarter_end_window_dressing_zscore_252d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 252)

def seas_045_quarter_end_window_dressing_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_045_quarter_end_window_dressing_rank_252d
    ECONOMIC RATIONALE: Performance during quarter-end reporting periods.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 252)

def seas_046_seasonal_volatility_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_046_seasonal_volatility_lvl_5d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 5)

def seas_047_seasonal_volatility_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_047_seasonal_volatility_zscore_5d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 5)

def seas_048_seasonal_volatility_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_048_seasonal_volatility_rank_5d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rank_pct(base, 5)

def seas_049_seasonal_volatility_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_049_seasonal_volatility_lvl_21d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 21)

def seas_050_seasonal_volatility_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_050_seasonal_volatility_zscore_21d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 21)

def seas_051_seasonal_volatility_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_051_seasonal_volatility_rank_21d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rank_pct(base, 21)

def seas_052_seasonal_volatility_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_052_seasonal_volatility_lvl_63d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 63)

def seas_053_seasonal_volatility_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_053_seasonal_volatility_zscore_63d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 63)

def seas_054_seasonal_volatility_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_054_seasonal_volatility_rank_63d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rank_pct(base, 63)

def seas_055_seasonal_volatility_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_055_seasonal_volatility_lvl_126d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 126)

def seas_056_seasonal_volatility_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_056_seasonal_volatility_zscore_126d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 126)

def seas_057_seasonal_volatility_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_057_seasonal_volatility_rank_126d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rank_pct(base, 126)

def seas_058_seasonal_volatility_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_058_seasonal_volatility_lvl_252d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 252)

def seas_059_seasonal_volatility_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_059_seasonal_volatility_zscore_252d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 252)

def seas_060_seasonal_volatility_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_060_seasonal_volatility_rank_252d
    ECONOMIC RATIONALE: Historical average volatility for the current month.
    """
    base = close.rolling(21).std().groupby(close.index.month).transform('mean')
    return _rank_pct(base, 252)

def seas_061_month_of_year_returns_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_061_month_of_year_returns_lvl_5d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 5)

def seas_062_month_of_year_returns_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_062_month_of_year_returns_zscore_5d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 5)

def seas_063_month_of_year_returns_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_063_month_of_year_returns_rank_5d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rank_pct(base, 5)

def seas_064_month_of_year_returns_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_064_month_of_year_returns_lvl_21d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 21)

def seas_065_month_of_year_returns_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_065_month_of_year_returns_zscore_21d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 21)

def seas_066_month_of_year_returns_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_066_month_of_year_returns_rank_21d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rank_pct(base, 21)

def seas_067_month_of_year_returns_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_067_month_of_year_returns_lvl_63d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 63)

def seas_068_month_of_year_returns_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_068_month_of_year_returns_zscore_63d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 63)

def seas_069_month_of_year_returns_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_069_month_of_year_returns_rank_63d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rank_pct(base, 63)

def seas_070_month_of_year_returns_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_070_month_of_year_returns_lvl_126d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 126)

def seas_071_month_of_year_returns_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_071_month_of_year_returns_zscore_126d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 126)

def seas_072_month_of_year_returns_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_072_month_of_year_returns_rank_126d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rank_pct(base, 126)

def seas_073_month_of_year_returns_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_073_month_of_year_returns_lvl_252d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rolling_mean(base, 252)

def seas_074_month_of_year_returns_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_074_month_of_year_returns_zscore_252d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _zscore_rolling(base, 252)

def seas_075_month_of_year_returns_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_075_month_of_year_returns_rank_252d
    ECONOMIC RATIONALE: Historical average return for the current month.
    """
    base = close.pct_change(21).groupby(close.index.month).transform('mean')
    return _rank_pct(base, 252)

def seas_076_seasonal_drawdown_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_076_seasonal_drawdown_lvl_5d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 5)

def seas_077_seasonal_drawdown_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_077_seasonal_drawdown_zscore_5d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 5)

def seas_078_seasonal_drawdown_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_078_seasonal_drawdown_rank_5d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 5)

def seas_079_seasonal_drawdown_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_079_seasonal_drawdown_lvl_21d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 21)

def seas_080_seasonal_drawdown_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_080_seasonal_drawdown_zscore_21d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 21)

def seas_081_seasonal_drawdown_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_081_seasonal_drawdown_rank_21d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 21)

def seas_082_seasonal_drawdown_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_082_seasonal_drawdown_lvl_63d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 63)

def seas_083_seasonal_drawdown_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_083_seasonal_drawdown_zscore_63d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 63)

def seas_084_seasonal_drawdown_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_084_seasonal_drawdown_rank_63d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 63)

def seas_085_seasonal_drawdown_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_085_seasonal_drawdown_lvl_126d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 126)

def seas_086_seasonal_drawdown_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_086_seasonal_drawdown_zscore_126d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 126)

def seas_087_seasonal_drawdown_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_087_seasonal_drawdown_rank_126d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 126)

def seas_088_seasonal_drawdown_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_088_seasonal_drawdown_lvl_252d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 252)

def seas_089_seasonal_drawdown_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_089_seasonal_drawdown_zscore_252d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 252)

def seas_090_seasonal_drawdown_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_090_seasonal_drawdown_rank_252d
    ECONOMIC RATIONALE: Drawdown state relative to seasonal cycles.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 252)

def seas_091_monthly_momentum_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_091_monthly_momentum_lvl_5d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rolling_mean(base, 5)

def seas_092_monthly_momentum_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_092_monthly_momentum_zscore_5d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _zscore_rolling(base, 5)

def seas_093_monthly_momentum_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_093_monthly_momentum_rank_5d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rank_pct(base, 5)

def seas_094_monthly_momentum_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_094_monthly_momentum_lvl_21d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rolling_mean(base, 21)

def seas_095_monthly_momentum_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_095_monthly_momentum_zscore_21d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _zscore_rolling(base, 21)

def seas_096_monthly_momentum_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_096_monthly_momentum_rank_21d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rank_pct(base, 21)

def seas_097_monthly_momentum_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_097_monthly_momentum_lvl_63d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rolling_mean(base, 63)

def seas_098_monthly_momentum_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_098_monthly_momentum_zscore_63d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _zscore_rolling(base, 63)

def seas_099_monthly_momentum_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_099_monthly_momentum_rank_63d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rank_pct(base, 63)

def seas_100_monthly_momentum_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_100_monthly_momentum_lvl_126d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rolling_mean(base, 126)

def seas_101_monthly_momentum_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_101_monthly_momentum_zscore_126d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _zscore_rolling(base, 126)

def seas_102_monthly_momentum_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_102_monthly_momentum_rank_126d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rank_pct(base, 126)

def seas_103_monthly_momentum_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_103_monthly_momentum_lvl_252d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rolling_mean(base, 252)

def seas_104_monthly_momentum_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_104_monthly_momentum_zscore_252d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _zscore_rolling(base, 252)

def seas_105_monthly_momentum_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_105_monthly_momentum_rank_252d
    ECONOMIC RATIONALE: Deviation from typical seasonal momentum.
    """
    base = close.pct_change(21) - close.pct_change(126).rolling(21).mean()
    return _rank_pct(base, 252)

def seas_106_september_distress_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_106_september_distress_lvl_5d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rolling_mean(base, 5)

def seas_107_september_distress_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_107_september_distress_zscore_5d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _zscore_rolling(base, 5)

def seas_108_september_distress_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_108_september_distress_rank_5d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rank_pct(base, 5)

def seas_109_september_distress_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_109_september_distress_lvl_21d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rolling_mean(base, 21)

def seas_110_september_distress_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_110_september_distress_zscore_21d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _zscore_rolling(base, 21)

def seas_111_september_distress_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_111_september_distress_rank_21d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rank_pct(base, 21)

def seas_112_september_distress_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_112_september_distress_lvl_63d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rolling_mean(base, 63)

def seas_113_september_distress_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_113_september_distress_zscore_63d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _zscore_rolling(base, 63)

def seas_114_september_distress_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_114_september_distress_rank_63d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rank_pct(base, 63)

def seas_115_september_distress_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_115_september_distress_lvl_126d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rolling_mean(base, 126)

def seas_116_september_distress_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_116_september_distress_zscore_126d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _zscore_rolling(base, 126)

def seas_117_september_distress_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_117_september_distress_rank_126d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rank_pct(base, 126)

def seas_118_september_distress_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_118_september_distress_lvl_252d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rolling_mean(base, 252)

def seas_119_september_distress_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_119_september_distress_zscore_252d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _zscore_rolling(base, 252)

def seas_120_september_distress_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_120_september_distress_rank_252d
    ECONOMIC RATIONALE: Historical weakness in September applied to current price.
    """
    base = close.pct_change(21) * (close.index.month == 9).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V102_REGISTRY_1 = {
    "seas_001_tax_loss_selling_lvl_5d": {"inputs": ["close", "volume"], "func": seas_001_tax_loss_selling_lvl_5d},
    "seas_002_tax_loss_selling_zscore_5d": {"inputs": ["close", "volume"], "func": seas_002_tax_loss_selling_zscore_5d},
    "seas_003_tax_loss_selling_rank_5d": {"inputs": ["close", "volume"], "func": seas_003_tax_loss_selling_rank_5d},
    "seas_004_tax_loss_selling_lvl_21d": {"inputs": ["close", "volume"], "func": seas_004_tax_loss_selling_lvl_21d},
    "seas_005_tax_loss_selling_zscore_21d": {"inputs": ["close", "volume"], "func": seas_005_tax_loss_selling_zscore_21d},
    "seas_006_tax_loss_selling_rank_21d": {"inputs": ["close", "volume"], "func": seas_006_tax_loss_selling_rank_21d},
    "seas_007_tax_loss_selling_lvl_63d": {"inputs": ["close", "volume"], "func": seas_007_tax_loss_selling_lvl_63d},
    "seas_008_tax_loss_selling_zscore_63d": {"inputs": ["close", "volume"], "func": seas_008_tax_loss_selling_zscore_63d},
    "seas_009_tax_loss_selling_rank_63d": {"inputs": ["close", "volume"], "func": seas_009_tax_loss_selling_rank_63d},
    "seas_010_tax_loss_selling_lvl_126d": {"inputs": ["close", "volume"], "func": seas_010_tax_loss_selling_lvl_126d},
    "seas_011_tax_loss_selling_zscore_126d": {"inputs": ["close", "volume"], "func": seas_011_tax_loss_selling_zscore_126d},
    "seas_012_tax_loss_selling_rank_126d": {"inputs": ["close", "volume"], "func": seas_012_tax_loss_selling_rank_126d},
    "seas_013_tax_loss_selling_lvl_252d": {"inputs": ["close", "volume"], "func": seas_013_tax_loss_selling_lvl_252d},
    "seas_014_tax_loss_selling_zscore_252d": {"inputs": ["close", "volume"], "func": seas_014_tax_loss_selling_zscore_252d},
    "seas_015_tax_loss_selling_rank_252d": {"inputs": ["close", "volume"], "func": seas_015_tax_loss_selling_rank_252d},
    "seas_016_january_effect_reversal_lvl_5d": {"inputs": ["close", "volume"], "func": seas_016_january_effect_reversal_lvl_5d},
    "seas_017_january_effect_reversal_zscore_5d": {"inputs": ["close", "volume"], "func": seas_017_january_effect_reversal_zscore_5d},
    "seas_018_january_effect_reversal_rank_5d": {"inputs": ["close", "volume"], "func": seas_018_january_effect_reversal_rank_5d},
    "seas_019_january_effect_reversal_lvl_21d": {"inputs": ["close", "volume"], "func": seas_019_january_effect_reversal_lvl_21d},
    "seas_020_january_effect_reversal_zscore_21d": {"inputs": ["close", "volume"], "func": seas_020_january_effect_reversal_zscore_21d},
    "seas_021_january_effect_reversal_rank_21d": {"inputs": ["close", "volume"], "func": seas_021_january_effect_reversal_rank_21d},
    "seas_022_january_effect_reversal_lvl_63d": {"inputs": ["close", "volume"], "func": seas_022_january_effect_reversal_lvl_63d},
    "seas_023_january_effect_reversal_zscore_63d": {"inputs": ["close", "volume"], "func": seas_023_january_effect_reversal_zscore_63d},
    "seas_024_january_effect_reversal_rank_63d": {"inputs": ["close", "volume"], "func": seas_024_january_effect_reversal_rank_63d},
    "seas_025_january_effect_reversal_lvl_126d": {"inputs": ["close", "volume"], "func": seas_025_january_effect_reversal_lvl_126d},
    "seas_026_january_effect_reversal_zscore_126d": {"inputs": ["close", "volume"], "func": seas_026_january_effect_reversal_zscore_126d},
    "seas_027_january_effect_reversal_rank_126d": {"inputs": ["close", "volume"], "func": seas_027_january_effect_reversal_rank_126d},
    "seas_028_january_effect_reversal_lvl_252d": {"inputs": ["close", "volume"], "func": seas_028_january_effect_reversal_lvl_252d},
    "seas_029_january_effect_reversal_zscore_252d": {"inputs": ["close", "volume"], "func": seas_029_january_effect_reversal_zscore_252d},
    "seas_030_january_effect_reversal_rank_252d": {"inputs": ["close", "volume"], "func": seas_030_january_effect_reversal_rank_252d},
    "seas_031_quarter_end_window_dressing_lvl_5d": {"inputs": ["close", "volume"], "func": seas_031_quarter_end_window_dressing_lvl_5d},
    "seas_032_quarter_end_window_dressing_zscore_5d": {"inputs": ["close", "volume"], "func": seas_032_quarter_end_window_dressing_zscore_5d},
    "seas_033_quarter_end_window_dressing_rank_5d": {"inputs": ["close", "volume"], "func": seas_033_quarter_end_window_dressing_rank_5d},
    "seas_034_quarter_end_window_dressing_lvl_21d": {"inputs": ["close", "volume"], "func": seas_034_quarter_end_window_dressing_lvl_21d},
    "seas_035_quarter_end_window_dressing_zscore_21d": {"inputs": ["close", "volume"], "func": seas_035_quarter_end_window_dressing_zscore_21d},
    "seas_036_quarter_end_window_dressing_rank_21d": {"inputs": ["close", "volume"], "func": seas_036_quarter_end_window_dressing_rank_21d},
    "seas_037_quarter_end_window_dressing_lvl_63d": {"inputs": ["close", "volume"], "func": seas_037_quarter_end_window_dressing_lvl_63d},
    "seas_038_quarter_end_window_dressing_zscore_63d": {"inputs": ["close", "volume"], "func": seas_038_quarter_end_window_dressing_zscore_63d},
    "seas_039_quarter_end_window_dressing_rank_63d": {"inputs": ["close", "volume"], "func": seas_039_quarter_end_window_dressing_rank_63d},
    "seas_040_quarter_end_window_dressing_lvl_126d": {"inputs": ["close", "volume"], "func": seas_040_quarter_end_window_dressing_lvl_126d},
    "seas_041_quarter_end_window_dressing_zscore_126d": {"inputs": ["close", "volume"], "func": seas_041_quarter_end_window_dressing_zscore_126d},
    "seas_042_quarter_end_window_dressing_rank_126d": {"inputs": ["close", "volume"], "func": seas_042_quarter_end_window_dressing_rank_126d},
    "seas_043_quarter_end_window_dressing_lvl_252d": {"inputs": ["close", "volume"], "func": seas_043_quarter_end_window_dressing_lvl_252d},
    "seas_044_quarter_end_window_dressing_zscore_252d": {"inputs": ["close", "volume"], "func": seas_044_quarter_end_window_dressing_zscore_252d},
    "seas_045_quarter_end_window_dressing_rank_252d": {"inputs": ["close", "volume"], "func": seas_045_quarter_end_window_dressing_rank_252d},
    "seas_046_seasonal_volatility_lvl_5d": {"inputs": ["close", "volume"], "func": seas_046_seasonal_volatility_lvl_5d},
    "seas_047_seasonal_volatility_zscore_5d": {"inputs": ["close", "volume"], "func": seas_047_seasonal_volatility_zscore_5d},
    "seas_048_seasonal_volatility_rank_5d": {"inputs": ["close", "volume"], "func": seas_048_seasonal_volatility_rank_5d},
    "seas_049_seasonal_volatility_lvl_21d": {"inputs": ["close", "volume"], "func": seas_049_seasonal_volatility_lvl_21d},
    "seas_050_seasonal_volatility_zscore_21d": {"inputs": ["close", "volume"], "func": seas_050_seasonal_volatility_zscore_21d},
    "seas_051_seasonal_volatility_rank_21d": {"inputs": ["close", "volume"], "func": seas_051_seasonal_volatility_rank_21d},
    "seas_052_seasonal_volatility_lvl_63d": {"inputs": ["close", "volume"], "func": seas_052_seasonal_volatility_lvl_63d},
    "seas_053_seasonal_volatility_zscore_63d": {"inputs": ["close", "volume"], "func": seas_053_seasonal_volatility_zscore_63d},
    "seas_054_seasonal_volatility_rank_63d": {"inputs": ["close", "volume"], "func": seas_054_seasonal_volatility_rank_63d},
    "seas_055_seasonal_volatility_lvl_126d": {"inputs": ["close", "volume"], "func": seas_055_seasonal_volatility_lvl_126d},
    "seas_056_seasonal_volatility_zscore_126d": {"inputs": ["close", "volume"], "func": seas_056_seasonal_volatility_zscore_126d},
    "seas_057_seasonal_volatility_rank_126d": {"inputs": ["close", "volume"], "func": seas_057_seasonal_volatility_rank_126d},
    "seas_058_seasonal_volatility_lvl_252d": {"inputs": ["close", "volume"], "func": seas_058_seasonal_volatility_lvl_252d},
    "seas_059_seasonal_volatility_zscore_252d": {"inputs": ["close", "volume"], "func": seas_059_seasonal_volatility_zscore_252d},
    "seas_060_seasonal_volatility_rank_252d": {"inputs": ["close", "volume"], "func": seas_060_seasonal_volatility_rank_252d},
    "seas_061_month_of_year_returns_lvl_5d": {"inputs": ["close", "volume"], "func": seas_061_month_of_year_returns_lvl_5d},
    "seas_062_month_of_year_returns_zscore_5d": {"inputs": ["close", "volume"], "func": seas_062_month_of_year_returns_zscore_5d},
    "seas_063_month_of_year_returns_rank_5d": {"inputs": ["close", "volume"], "func": seas_063_month_of_year_returns_rank_5d},
    "seas_064_month_of_year_returns_lvl_21d": {"inputs": ["close", "volume"], "func": seas_064_month_of_year_returns_lvl_21d},
    "seas_065_month_of_year_returns_zscore_21d": {"inputs": ["close", "volume"], "func": seas_065_month_of_year_returns_zscore_21d},
    "seas_066_month_of_year_returns_rank_21d": {"inputs": ["close", "volume"], "func": seas_066_month_of_year_returns_rank_21d},
    "seas_067_month_of_year_returns_lvl_63d": {"inputs": ["close", "volume"], "func": seas_067_month_of_year_returns_lvl_63d},
    "seas_068_month_of_year_returns_zscore_63d": {"inputs": ["close", "volume"], "func": seas_068_month_of_year_returns_zscore_63d},
    "seas_069_month_of_year_returns_rank_63d": {"inputs": ["close", "volume"], "func": seas_069_month_of_year_returns_rank_63d},
    "seas_070_month_of_year_returns_lvl_126d": {"inputs": ["close", "volume"], "func": seas_070_month_of_year_returns_lvl_126d},
    "seas_071_month_of_year_returns_zscore_126d": {"inputs": ["close", "volume"], "func": seas_071_month_of_year_returns_zscore_126d},
    "seas_072_month_of_year_returns_rank_126d": {"inputs": ["close", "volume"], "func": seas_072_month_of_year_returns_rank_126d},
    "seas_073_month_of_year_returns_lvl_252d": {"inputs": ["close", "volume"], "func": seas_073_month_of_year_returns_lvl_252d},
    "seas_074_month_of_year_returns_zscore_252d": {"inputs": ["close", "volume"], "func": seas_074_month_of_year_returns_zscore_252d},
    "seas_075_month_of_year_returns_rank_252d": {"inputs": ["close", "volume"], "func": seas_075_month_of_year_returns_rank_252d},
    "seas_076_seasonal_drawdown_lvl_5d": {"inputs": ["close", "volume"], "func": seas_076_seasonal_drawdown_lvl_5d},
    "seas_077_seasonal_drawdown_zscore_5d": {"inputs": ["close", "volume"], "func": seas_077_seasonal_drawdown_zscore_5d},
    "seas_078_seasonal_drawdown_rank_5d": {"inputs": ["close", "volume"], "func": seas_078_seasonal_drawdown_rank_5d},
    "seas_079_seasonal_drawdown_lvl_21d": {"inputs": ["close", "volume"], "func": seas_079_seasonal_drawdown_lvl_21d},
    "seas_080_seasonal_drawdown_zscore_21d": {"inputs": ["close", "volume"], "func": seas_080_seasonal_drawdown_zscore_21d},
    "seas_081_seasonal_drawdown_rank_21d": {"inputs": ["close", "volume"], "func": seas_081_seasonal_drawdown_rank_21d},
    "seas_082_seasonal_drawdown_lvl_63d": {"inputs": ["close", "volume"], "func": seas_082_seasonal_drawdown_lvl_63d},
    "seas_083_seasonal_drawdown_zscore_63d": {"inputs": ["close", "volume"], "func": seas_083_seasonal_drawdown_zscore_63d},
    "seas_084_seasonal_drawdown_rank_63d": {"inputs": ["close", "volume"], "func": seas_084_seasonal_drawdown_rank_63d},
    "seas_085_seasonal_drawdown_lvl_126d": {"inputs": ["close", "volume"], "func": seas_085_seasonal_drawdown_lvl_126d},
    "seas_086_seasonal_drawdown_zscore_126d": {"inputs": ["close", "volume"], "func": seas_086_seasonal_drawdown_zscore_126d},
    "seas_087_seasonal_drawdown_rank_126d": {"inputs": ["close", "volume"], "func": seas_087_seasonal_drawdown_rank_126d},
    "seas_088_seasonal_drawdown_lvl_252d": {"inputs": ["close", "volume"], "func": seas_088_seasonal_drawdown_lvl_252d},
    "seas_089_seasonal_drawdown_zscore_252d": {"inputs": ["close", "volume"], "func": seas_089_seasonal_drawdown_zscore_252d},
    "seas_090_seasonal_drawdown_rank_252d": {"inputs": ["close", "volume"], "func": seas_090_seasonal_drawdown_rank_252d},
    "seas_091_monthly_momentum_lvl_5d": {"inputs": ["close", "volume"], "func": seas_091_monthly_momentum_lvl_5d},
    "seas_092_monthly_momentum_zscore_5d": {"inputs": ["close", "volume"], "func": seas_092_monthly_momentum_zscore_5d},
    "seas_093_monthly_momentum_rank_5d": {"inputs": ["close", "volume"], "func": seas_093_monthly_momentum_rank_5d},
    "seas_094_monthly_momentum_lvl_21d": {"inputs": ["close", "volume"], "func": seas_094_monthly_momentum_lvl_21d},
    "seas_095_monthly_momentum_zscore_21d": {"inputs": ["close", "volume"], "func": seas_095_monthly_momentum_zscore_21d},
    "seas_096_monthly_momentum_rank_21d": {"inputs": ["close", "volume"], "func": seas_096_monthly_momentum_rank_21d},
    "seas_097_monthly_momentum_lvl_63d": {"inputs": ["close", "volume"], "func": seas_097_monthly_momentum_lvl_63d},
    "seas_098_monthly_momentum_zscore_63d": {"inputs": ["close", "volume"], "func": seas_098_monthly_momentum_zscore_63d},
    "seas_099_monthly_momentum_rank_63d": {"inputs": ["close", "volume"], "func": seas_099_monthly_momentum_rank_63d},
    "seas_100_monthly_momentum_lvl_126d": {"inputs": ["close", "volume"], "func": seas_100_monthly_momentum_lvl_126d},
    "seas_101_monthly_momentum_zscore_126d": {"inputs": ["close", "volume"], "func": seas_101_monthly_momentum_zscore_126d},
    "seas_102_monthly_momentum_rank_126d": {"inputs": ["close", "volume"], "func": seas_102_monthly_momentum_rank_126d},
    "seas_103_monthly_momentum_lvl_252d": {"inputs": ["close", "volume"], "func": seas_103_monthly_momentum_lvl_252d},
    "seas_104_monthly_momentum_zscore_252d": {"inputs": ["close", "volume"], "func": seas_104_monthly_momentum_zscore_252d},
    "seas_105_monthly_momentum_rank_252d": {"inputs": ["close", "volume"], "func": seas_105_monthly_momentum_rank_252d},
    "seas_106_september_distress_lvl_5d": {"inputs": ["close", "volume"], "func": seas_106_september_distress_lvl_5d},
    "seas_107_september_distress_zscore_5d": {"inputs": ["close", "volume"], "func": seas_107_september_distress_zscore_5d},
    "seas_108_september_distress_rank_5d": {"inputs": ["close", "volume"], "func": seas_108_september_distress_rank_5d},
    "seas_109_september_distress_lvl_21d": {"inputs": ["close", "volume"], "func": seas_109_september_distress_lvl_21d},
    "seas_110_september_distress_zscore_21d": {"inputs": ["close", "volume"], "func": seas_110_september_distress_zscore_21d},
    "seas_111_september_distress_rank_21d": {"inputs": ["close", "volume"], "func": seas_111_september_distress_rank_21d},
    "seas_112_september_distress_lvl_63d": {"inputs": ["close", "volume"], "func": seas_112_september_distress_lvl_63d},
    "seas_113_september_distress_zscore_63d": {"inputs": ["close", "volume"], "func": seas_113_september_distress_zscore_63d},
    "seas_114_september_distress_rank_63d": {"inputs": ["close", "volume"], "func": seas_114_september_distress_rank_63d},
    "seas_115_september_distress_lvl_126d": {"inputs": ["close", "volume"], "func": seas_115_september_distress_lvl_126d},
    "seas_116_september_distress_zscore_126d": {"inputs": ["close", "volume"], "func": seas_116_september_distress_zscore_126d},
    "seas_117_september_distress_rank_126d": {"inputs": ["close", "volume"], "func": seas_117_september_distress_rank_126d},
    "seas_118_september_distress_lvl_252d": {"inputs": ["close", "volume"], "func": seas_118_september_distress_lvl_252d},
    "seas_119_september_distress_zscore_252d": {"inputs": ["close", "volume"], "func": seas_119_september_distress_zscore_252d},
    "seas_120_september_distress_rank_252d": {"inputs": ["close", "volume"], "func": seas_120_september_distress_rank_252d},
}
