"""
102_seasonal_distress — Acceleration (3rd Derivatives)
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

def seas_301_tax_loss_selling_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_301_tax_loss_selling_accel_5d
    ECONOMIC RATIONALE: Acceleration of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(5).diff(_TD_MON)

def seas_302_tax_loss_selling_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_302_tax_loss_selling_accel_21d
    ECONOMIC RATIONALE: Acceleration of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(21).diff(_TD_MON)

def seas_303_tax_loss_selling_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_303_tax_loss_selling_accel_63d
    ECONOMIC RATIONALE: Acceleration of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(63).diff(_TD_MON)

def seas_304_tax_loss_selling_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_304_tax_loss_selling_accel_126d
    ECONOMIC RATIONALE: Acceleration of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(126).diff(_TD_MON)

def seas_305_tax_loss_selling_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_305_tax_loss_selling_accel_252d
    ECONOMIC RATIONALE: Acceleration of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(252).diff(_TD_MON)

def seas_306_january_effect_reversal_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_306_january_effect_reversal_accel_5d
    ECONOMIC RATIONALE: Acceleration of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(5).diff(_TD_MON)

def seas_307_january_effect_reversal_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_307_january_effect_reversal_accel_21d
    ECONOMIC RATIONALE: Acceleration of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(21).diff(_TD_MON)

def seas_308_january_effect_reversal_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_308_january_effect_reversal_accel_63d
    ECONOMIC RATIONALE: Acceleration of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(63).diff(_TD_MON)

def seas_309_january_effect_reversal_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_309_january_effect_reversal_accel_126d
    ECONOMIC RATIONALE: Acceleration of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(126).diff(_TD_MON)

def seas_310_january_effect_reversal_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_310_january_effect_reversal_accel_252d
    ECONOMIC RATIONALE: Acceleration of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(252).diff(_TD_MON)

def seas_311_quarter_end_window_dressing_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_311_quarter_end_window_dressing_accel_5d
    ECONOMIC RATIONALE: Acceleration of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(5).diff(_TD_MON)

def seas_312_quarter_end_window_dressing_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_312_quarter_end_window_dressing_accel_21d
    ECONOMIC RATIONALE: Acceleration of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(21).diff(_TD_MON)

def seas_313_quarter_end_window_dressing_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_313_quarter_end_window_dressing_accel_63d
    ECONOMIC RATIONALE: Acceleration of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(63).diff(_TD_MON)

def seas_314_quarter_end_window_dressing_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_314_quarter_end_window_dressing_accel_126d
    ECONOMIC RATIONALE: Acceleration of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(126).diff(_TD_MON)

def seas_315_quarter_end_window_dressing_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_315_quarter_end_window_dressing_accel_252d
    ECONOMIC RATIONALE: Acceleration of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(252).diff(_TD_MON)

def seas_316_seasonal_volatility_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_316_seasonal_volatility_accel_5d
    ECONOMIC RATIONALE: Acceleration of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(5).diff(_TD_MON)

def seas_317_seasonal_volatility_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_317_seasonal_volatility_accel_21d
    ECONOMIC RATIONALE: Acceleration of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(21).diff(_TD_MON)

def seas_318_seasonal_volatility_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_318_seasonal_volatility_accel_63d
    ECONOMIC RATIONALE: Acceleration of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(63).diff(_TD_MON)

def seas_319_seasonal_volatility_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_319_seasonal_volatility_accel_126d
    ECONOMIC RATIONALE: Acceleration of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(126).diff(_TD_MON)

def seas_320_seasonal_volatility_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_320_seasonal_volatility_accel_252d
    ECONOMIC RATIONALE: Acceleration of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(252).diff(_TD_MON)

def seas_321_month_of_year_returns_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_321_month_of_year_returns_accel_5d
    ECONOMIC RATIONALE: Acceleration of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(5).diff(_TD_MON)

def seas_322_month_of_year_returns_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_322_month_of_year_returns_accel_21d
    ECONOMIC RATIONALE: Acceleration of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(21).diff(_TD_MON)

def seas_323_month_of_year_returns_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_323_month_of_year_returns_accel_63d
    ECONOMIC RATIONALE: Acceleration of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(63).diff(_TD_MON)

def seas_324_month_of_year_returns_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_324_month_of_year_returns_accel_126d
    ECONOMIC RATIONALE: Acceleration of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(126).diff(_TD_MON)

def seas_325_month_of_year_returns_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_325_month_of_year_returns_accel_252d
    ECONOMIC RATIONALE: Acceleration of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(252).diff(_TD_MON)

def seas_326_seasonal_drawdown_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_326_seasonal_drawdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(5).diff(_TD_MON)

def seas_327_seasonal_drawdown_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_327_seasonal_drawdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(21).diff(_TD_MON)

def seas_328_seasonal_drawdown_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_328_seasonal_drawdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(63).diff(_TD_MON)

def seas_329_seasonal_drawdown_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_329_seasonal_drawdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(126).diff(_TD_MON)

def seas_330_seasonal_drawdown_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_330_seasonal_drawdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(252).diff(_TD_MON)

def seas_331_monthly_momentum_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_331_monthly_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(5).diff(_TD_MON)

def seas_332_monthly_momentum_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_332_monthly_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(21).diff(_TD_MON)

def seas_333_monthly_momentum_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_333_monthly_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(63).diff(_TD_MON)

def seas_334_monthly_momentum_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_334_monthly_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(126).diff(_TD_MON)

def seas_335_monthly_momentum_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_335_monthly_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(252).diff(_TD_MON)

def seas_336_september_distress_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_336_september_distress_accel_5d
    ECONOMIC RATIONALE: Acceleration of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(5).diff(_TD_MON)

def seas_337_september_distress_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_337_september_distress_accel_21d
    ECONOMIC RATIONALE: Acceleration of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(21).diff(_TD_MON)

def seas_338_september_distress_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_338_september_distress_accel_63d
    ECONOMIC RATIONALE: Acceleration of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(63).diff(_TD_MON)

def seas_339_september_distress_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_339_september_distress_accel_126d
    ECONOMIC RATIONALE: Acceleration of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(126).diff(_TD_MON)

def seas_340_september_distress_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_340_september_distress_accel_252d
    ECONOMIC RATIONALE: Acceleration of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(252).diff(_TD_MON)

def seas_341_may_sell_signal_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_341_may_sell_signal_accel_5d
    ECONOMIC RATIONALE: Acceleration of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(5).diff(_TD_MON)

def seas_342_may_sell_signal_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_342_may_sell_signal_accel_21d
    ECONOMIC RATIONALE: Acceleration of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(21).diff(_TD_MON)

def seas_343_may_sell_signal_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_343_may_sell_signal_accel_63d
    ECONOMIC RATIONALE: Acceleration of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(63).diff(_TD_MON)

def seas_344_may_sell_signal_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_344_may_sell_signal_accel_126d
    ECONOMIC RATIONALE: Acceleration of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(126).diff(_TD_MON)

def seas_345_may_sell_signal_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_345_may_sell_signal_accel_252d
    ECONOMIC RATIONALE: Acceleration of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(252).diff(_TD_MON)

def seas_346_quarterly_seasonality_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_346_quarterly_seasonality_accel_5d
    ECONOMIC RATIONALE: Acceleration of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(5).diff(_TD_MON)

def seas_347_quarterly_seasonality_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_347_quarterly_seasonality_accel_21d
    ECONOMIC RATIONALE: Acceleration of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(21).diff(_TD_MON)

def seas_348_quarterly_seasonality_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_348_quarterly_seasonality_accel_63d
    ECONOMIC RATIONALE: Acceleration of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(63).diff(_TD_MON)

def seas_349_quarterly_seasonality_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_349_quarterly_seasonality_accel_126d
    ECONOMIC RATIONALE: Acceleration of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(126).diff(_TD_MON)

def seas_350_quarterly_seasonality_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_350_quarterly_seasonality_accel_252d
    ECONOMIC RATIONALE: Acceleration of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(252).diff(_TD_MON)

def seas_351_seasonal_zscore_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_351_seasonal_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(5).diff(_TD_MON)

def seas_352_seasonal_zscore_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_352_seasonal_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(21).diff(_TD_MON)

def seas_353_seasonal_zscore_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_353_seasonal_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(63).diff(_TD_MON)

def seas_354_seasonal_zscore_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_354_seasonal_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(126).diff(_TD_MON)

def seas_355_seasonal_zscore_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_355_seasonal_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(252).diff(_TD_MON)

def seas_356_holiday_liquidity_drain_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_356_holiday_liquidity_drain_accel_5d
    ECONOMIC RATIONALE: Acceleration of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(5).diff(_TD_MON)

def seas_357_holiday_liquidity_drain_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_357_holiday_liquidity_drain_accel_21d
    ECONOMIC RATIONALE: Acceleration of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(21).diff(_TD_MON)

def seas_358_holiday_liquidity_drain_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_358_holiday_liquidity_drain_accel_63d
    ECONOMIC RATIONALE: Acceleration of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(63).diff(_TD_MON)

def seas_359_holiday_liquidity_drain_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_359_holiday_liquidity_drain_accel_126d
    ECONOMIC RATIONALE: Acceleration of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(126).diff(_TD_MON)

def seas_360_holiday_liquidity_drain_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_360_holiday_liquidity_drain_accel_252d
    ECONOMIC RATIONALE: Acceleration of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(252).diff(_TD_MON)

def seas_361_seasonal_trend_strength_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_361_seasonal_trend_strength_accel_5d
    ECONOMIC RATIONALE: Acceleration of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(5).diff(_TD_MON)

def seas_362_seasonal_trend_strength_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_362_seasonal_trend_strength_accel_21d
    ECONOMIC RATIONALE: Acceleration of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(21).diff(_TD_MON)

def seas_363_seasonal_trend_strength_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_363_seasonal_trend_strength_accel_63d
    ECONOMIC RATIONALE: Acceleration of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(63).diff(_TD_MON)

def seas_364_seasonal_trend_strength_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_364_seasonal_trend_strength_accel_126d
    ECONOMIC RATIONALE: Acceleration of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(126).diff(_TD_MON)

def seas_365_seasonal_trend_strength_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_365_seasonal_trend_strength_accel_252d
    ECONOMIC RATIONALE: Acceleration of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(252).diff(_TD_MON)

def seas_366_periodic_reversal_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_366_periodic_reversal_accel_5d
    ECONOMIC RATIONALE: Acceleration of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(5).diff(_TD_MON)

def seas_367_periodic_reversal_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_367_periodic_reversal_accel_21d
    ECONOMIC RATIONALE: Acceleration of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(21).diff(_TD_MON)

def seas_368_periodic_reversal_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_368_periodic_reversal_accel_63d
    ECONOMIC RATIONALE: Acceleration of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(63).diff(_TD_MON)

def seas_369_periodic_reversal_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_369_periodic_reversal_accel_126d
    ECONOMIC RATIONALE: Acceleration of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(126).diff(_TD_MON)

def seas_370_periodic_reversal_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_370_periodic_reversal_accel_252d
    ECONOMIC RATIONALE: Acceleration of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(252).diff(_TD_MON)

def seas_371_cycle_position_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_371_cycle_position_accel_5d
    ECONOMIC RATIONALE: Acceleration of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(5).diff(_TD_MON)

def seas_372_cycle_position_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_372_cycle_position_accel_21d
    ECONOMIC RATIONALE: Acceleration of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(21).diff(_TD_MON)

def seas_373_cycle_position_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_373_cycle_position_accel_63d
    ECONOMIC RATIONALE: Acceleration of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(63).diff(_TD_MON)

def seas_374_cycle_position_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_374_cycle_position_accel_126d
    ECONOMIC RATIONALE: Acceleration of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(126).diff(_TD_MON)

def seas_375_cycle_position_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_375_cycle_position_accel_252d
    ECONOMIC RATIONALE: Acceleration of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V102_REGISTRY_ACCEL = {
    "seas_301_tax_loss_selling_accel_5d": {"inputs": ["close", "volume"], "func": seas_301_tax_loss_selling_accel_5d},
    "seas_302_tax_loss_selling_accel_21d": {"inputs": ["close", "volume"], "func": seas_302_tax_loss_selling_accel_21d},
    "seas_303_tax_loss_selling_accel_63d": {"inputs": ["close", "volume"], "func": seas_303_tax_loss_selling_accel_63d},
    "seas_304_tax_loss_selling_accel_126d": {"inputs": ["close", "volume"], "func": seas_304_tax_loss_selling_accel_126d},
    "seas_305_tax_loss_selling_accel_252d": {"inputs": ["close", "volume"], "func": seas_305_tax_loss_selling_accel_252d},
    "seas_306_january_effect_reversal_accel_5d": {"inputs": ["close", "volume"], "func": seas_306_january_effect_reversal_accel_5d},
    "seas_307_january_effect_reversal_accel_21d": {"inputs": ["close", "volume"], "func": seas_307_january_effect_reversal_accel_21d},
    "seas_308_january_effect_reversal_accel_63d": {"inputs": ["close", "volume"], "func": seas_308_january_effect_reversal_accel_63d},
    "seas_309_january_effect_reversal_accel_126d": {"inputs": ["close", "volume"], "func": seas_309_january_effect_reversal_accel_126d},
    "seas_310_january_effect_reversal_accel_252d": {"inputs": ["close", "volume"], "func": seas_310_january_effect_reversal_accel_252d},
    "seas_311_quarter_end_window_dressing_accel_5d": {"inputs": ["close", "volume"], "func": seas_311_quarter_end_window_dressing_accel_5d},
    "seas_312_quarter_end_window_dressing_accel_21d": {"inputs": ["close", "volume"], "func": seas_312_quarter_end_window_dressing_accel_21d},
    "seas_313_quarter_end_window_dressing_accel_63d": {"inputs": ["close", "volume"], "func": seas_313_quarter_end_window_dressing_accel_63d},
    "seas_314_quarter_end_window_dressing_accel_126d": {"inputs": ["close", "volume"], "func": seas_314_quarter_end_window_dressing_accel_126d},
    "seas_315_quarter_end_window_dressing_accel_252d": {"inputs": ["close", "volume"], "func": seas_315_quarter_end_window_dressing_accel_252d},
    "seas_316_seasonal_volatility_accel_5d": {"inputs": ["close", "volume"], "func": seas_316_seasonal_volatility_accel_5d},
    "seas_317_seasonal_volatility_accel_21d": {"inputs": ["close", "volume"], "func": seas_317_seasonal_volatility_accel_21d},
    "seas_318_seasonal_volatility_accel_63d": {"inputs": ["close", "volume"], "func": seas_318_seasonal_volatility_accel_63d},
    "seas_319_seasonal_volatility_accel_126d": {"inputs": ["close", "volume"], "func": seas_319_seasonal_volatility_accel_126d},
    "seas_320_seasonal_volatility_accel_252d": {"inputs": ["close", "volume"], "func": seas_320_seasonal_volatility_accel_252d},
    "seas_321_month_of_year_returns_accel_5d": {"inputs": ["close", "volume"], "func": seas_321_month_of_year_returns_accel_5d},
    "seas_322_month_of_year_returns_accel_21d": {"inputs": ["close", "volume"], "func": seas_322_month_of_year_returns_accel_21d},
    "seas_323_month_of_year_returns_accel_63d": {"inputs": ["close", "volume"], "func": seas_323_month_of_year_returns_accel_63d},
    "seas_324_month_of_year_returns_accel_126d": {"inputs": ["close", "volume"], "func": seas_324_month_of_year_returns_accel_126d},
    "seas_325_month_of_year_returns_accel_252d": {"inputs": ["close", "volume"], "func": seas_325_month_of_year_returns_accel_252d},
    "seas_326_seasonal_drawdown_accel_5d": {"inputs": ["close", "volume"], "func": seas_326_seasonal_drawdown_accel_5d},
    "seas_327_seasonal_drawdown_accel_21d": {"inputs": ["close", "volume"], "func": seas_327_seasonal_drawdown_accel_21d},
    "seas_328_seasonal_drawdown_accel_63d": {"inputs": ["close", "volume"], "func": seas_328_seasonal_drawdown_accel_63d},
    "seas_329_seasonal_drawdown_accel_126d": {"inputs": ["close", "volume"], "func": seas_329_seasonal_drawdown_accel_126d},
    "seas_330_seasonal_drawdown_accel_252d": {"inputs": ["close", "volume"], "func": seas_330_seasonal_drawdown_accel_252d},
    "seas_331_monthly_momentum_accel_5d": {"inputs": ["close", "volume"], "func": seas_331_monthly_momentum_accel_5d},
    "seas_332_monthly_momentum_accel_21d": {"inputs": ["close", "volume"], "func": seas_332_monthly_momentum_accel_21d},
    "seas_333_monthly_momentum_accel_63d": {"inputs": ["close", "volume"], "func": seas_333_monthly_momentum_accel_63d},
    "seas_334_monthly_momentum_accel_126d": {"inputs": ["close", "volume"], "func": seas_334_monthly_momentum_accel_126d},
    "seas_335_monthly_momentum_accel_252d": {"inputs": ["close", "volume"], "func": seas_335_monthly_momentum_accel_252d},
    "seas_336_september_distress_accel_5d": {"inputs": ["close", "volume"], "func": seas_336_september_distress_accel_5d},
    "seas_337_september_distress_accel_21d": {"inputs": ["close", "volume"], "func": seas_337_september_distress_accel_21d},
    "seas_338_september_distress_accel_63d": {"inputs": ["close", "volume"], "func": seas_338_september_distress_accel_63d},
    "seas_339_september_distress_accel_126d": {"inputs": ["close", "volume"], "func": seas_339_september_distress_accel_126d},
    "seas_340_september_distress_accel_252d": {"inputs": ["close", "volume"], "func": seas_340_september_distress_accel_252d},
    "seas_341_may_sell_signal_accel_5d": {"inputs": ["close", "volume"], "func": seas_341_may_sell_signal_accel_5d},
    "seas_342_may_sell_signal_accel_21d": {"inputs": ["close", "volume"], "func": seas_342_may_sell_signal_accel_21d},
    "seas_343_may_sell_signal_accel_63d": {"inputs": ["close", "volume"], "func": seas_343_may_sell_signal_accel_63d},
    "seas_344_may_sell_signal_accel_126d": {"inputs": ["close", "volume"], "func": seas_344_may_sell_signal_accel_126d},
    "seas_345_may_sell_signal_accel_252d": {"inputs": ["close", "volume"], "func": seas_345_may_sell_signal_accel_252d},
    "seas_346_quarterly_seasonality_accel_5d": {"inputs": ["close", "volume"], "func": seas_346_quarterly_seasonality_accel_5d},
    "seas_347_quarterly_seasonality_accel_21d": {"inputs": ["close", "volume"], "func": seas_347_quarterly_seasonality_accel_21d},
    "seas_348_quarterly_seasonality_accel_63d": {"inputs": ["close", "volume"], "func": seas_348_quarterly_seasonality_accel_63d},
    "seas_349_quarterly_seasonality_accel_126d": {"inputs": ["close", "volume"], "func": seas_349_quarterly_seasonality_accel_126d},
    "seas_350_quarterly_seasonality_accel_252d": {"inputs": ["close", "volume"], "func": seas_350_quarterly_seasonality_accel_252d},
    "seas_351_seasonal_zscore_accel_5d": {"inputs": ["close", "volume"], "func": seas_351_seasonal_zscore_accel_5d},
    "seas_352_seasonal_zscore_accel_21d": {"inputs": ["close", "volume"], "func": seas_352_seasonal_zscore_accel_21d},
    "seas_353_seasonal_zscore_accel_63d": {"inputs": ["close", "volume"], "func": seas_353_seasonal_zscore_accel_63d},
    "seas_354_seasonal_zscore_accel_126d": {"inputs": ["close", "volume"], "func": seas_354_seasonal_zscore_accel_126d},
    "seas_355_seasonal_zscore_accel_252d": {"inputs": ["close", "volume"], "func": seas_355_seasonal_zscore_accel_252d},
    "seas_356_holiday_liquidity_drain_accel_5d": {"inputs": ["close", "volume"], "func": seas_356_holiday_liquidity_drain_accel_5d},
    "seas_357_holiday_liquidity_drain_accel_21d": {"inputs": ["close", "volume"], "func": seas_357_holiday_liquidity_drain_accel_21d},
    "seas_358_holiday_liquidity_drain_accel_63d": {"inputs": ["close", "volume"], "func": seas_358_holiday_liquidity_drain_accel_63d},
    "seas_359_holiday_liquidity_drain_accel_126d": {"inputs": ["close", "volume"], "func": seas_359_holiday_liquidity_drain_accel_126d},
    "seas_360_holiday_liquidity_drain_accel_252d": {"inputs": ["close", "volume"], "func": seas_360_holiday_liquidity_drain_accel_252d},
    "seas_361_seasonal_trend_strength_accel_5d": {"inputs": ["close", "volume"], "func": seas_361_seasonal_trend_strength_accel_5d},
    "seas_362_seasonal_trend_strength_accel_21d": {"inputs": ["close", "volume"], "func": seas_362_seasonal_trend_strength_accel_21d},
    "seas_363_seasonal_trend_strength_accel_63d": {"inputs": ["close", "volume"], "func": seas_363_seasonal_trend_strength_accel_63d},
    "seas_364_seasonal_trend_strength_accel_126d": {"inputs": ["close", "volume"], "func": seas_364_seasonal_trend_strength_accel_126d},
    "seas_365_seasonal_trend_strength_accel_252d": {"inputs": ["close", "volume"], "func": seas_365_seasonal_trend_strength_accel_252d},
    "seas_366_periodic_reversal_accel_5d": {"inputs": ["close", "volume"], "func": seas_366_periodic_reversal_accel_5d},
    "seas_367_periodic_reversal_accel_21d": {"inputs": ["close", "volume"], "func": seas_367_periodic_reversal_accel_21d},
    "seas_368_periodic_reversal_accel_63d": {"inputs": ["close", "volume"], "func": seas_368_periodic_reversal_accel_63d},
    "seas_369_periodic_reversal_accel_126d": {"inputs": ["close", "volume"], "func": seas_369_periodic_reversal_accel_126d},
    "seas_370_periodic_reversal_accel_252d": {"inputs": ["close", "volume"], "func": seas_370_periodic_reversal_accel_252d},
    "seas_371_cycle_position_accel_5d": {"inputs": ["close", "volume"], "func": seas_371_cycle_position_accel_5d},
    "seas_372_cycle_position_accel_21d": {"inputs": ["close", "volume"], "func": seas_372_cycle_position_accel_21d},
    "seas_373_cycle_position_accel_63d": {"inputs": ["close", "volume"], "func": seas_373_cycle_position_accel_63d},
    "seas_374_cycle_position_accel_126d": {"inputs": ["close", "volume"], "func": seas_374_cycle_position_accel_126d},
    "seas_375_cycle_position_accel_252d": {"inputs": ["close", "volume"], "func": seas_375_cycle_position_accel_252d},
}
