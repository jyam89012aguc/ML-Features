"""
102_seasonal_distress — Velocity (2nd Derivatives)
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

def seas_226_tax_loss_selling_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_226_tax_loss_selling_vel_5d
    ECONOMIC RATIONALE: Velocity of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(5)

def seas_227_tax_loss_selling_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_227_tax_loss_selling_vel_21d
    ECONOMIC RATIONALE: Velocity of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(21)

def seas_228_tax_loss_selling_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_228_tax_loss_selling_vel_63d
    ECONOMIC RATIONALE: Velocity of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(63)

def seas_229_tax_loss_selling_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_229_tax_loss_selling_vel_126d
    ECONOMIC RATIONALE: Velocity of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(126)

def seas_230_tax_loss_selling_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_230_tax_loss_selling_vel_252d
    ECONOMIC RATIONALE: Velocity of tax_loss_selling. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).diff(252)

def seas_231_january_effect_reversal_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_231_january_effect_reversal_vel_5d
    ECONOMIC RATIONALE: Velocity of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(5)

def seas_232_january_effect_reversal_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_232_january_effect_reversal_vel_21d
    ECONOMIC RATIONALE: Velocity of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(21)

def seas_233_january_effect_reversal_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_233_january_effect_reversal_vel_63d
    ECONOMIC RATIONALE: Velocity of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(63)

def seas_234_january_effect_reversal_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_234_january_effect_reversal_vel_126d
    ECONOMIC RATIONALE: Velocity of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(126)

def seas_235_january_effect_reversal_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_235_january_effect_reversal_vel_252d
    ECONOMIC RATIONALE: Velocity of january_effect_reversal. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).diff(252)

def seas_236_quarter_end_window_dressing_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_236_quarter_end_window_dressing_vel_5d
    ECONOMIC RATIONALE: Velocity of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(5)

def seas_237_quarter_end_window_dressing_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_237_quarter_end_window_dressing_vel_21d
    ECONOMIC RATIONALE: Velocity of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(21)

def seas_238_quarter_end_window_dressing_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_238_quarter_end_window_dressing_vel_63d
    ECONOMIC RATIONALE: Velocity of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(63)

def seas_239_quarter_end_window_dressing_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_239_quarter_end_window_dressing_vel_126d
    ECONOMIC RATIONALE: Velocity of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(126)

def seas_240_quarter_end_window_dressing_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_240_quarter_end_window_dressing_vel_252d
    ECONOMIC RATIONALE: Velocity of quarter_end_window_dressing. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).diff(252)

def seas_241_seasonal_volatility_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_241_seasonal_volatility_vel_5d
    ECONOMIC RATIONALE: Velocity of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(5)

def seas_242_seasonal_volatility_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_242_seasonal_volatility_vel_21d
    ECONOMIC RATIONALE: Velocity of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(21)

def seas_243_seasonal_volatility_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_243_seasonal_volatility_vel_63d
    ECONOMIC RATIONALE: Velocity of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(63)

def seas_244_seasonal_volatility_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_244_seasonal_volatility_vel_126d
    ECONOMIC RATIONALE: Velocity of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(126)

def seas_245_seasonal_volatility_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_245_seasonal_volatility_vel_252d
    ECONOMIC RATIONALE: Velocity of seasonal_volatility. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).diff(252)

def seas_246_month_of_year_returns_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_246_month_of_year_returns_vel_5d
    ECONOMIC RATIONALE: Velocity of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(5)

def seas_247_month_of_year_returns_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_247_month_of_year_returns_vel_21d
    ECONOMIC RATIONALE: Velocity of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(21)

def seas_248_month_of_year_returns_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_248_month_of_year_returns_vel_63d
    ECONOMIC RATIONALE: Velocity of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(63)

def seas_249_month_of_year_returns_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_249_month_of_year_returns_vel_126d
    ECONOMIC RATIONALE: Velocity of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(126)

def seas_250_month_of_year_returns_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_250_month_of_year_returns_vel_252d
    ECONOMIC RATIONALE: Velocity of month_of_year_returns. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).diff(252)

def seas_251_seasonal_drawdown_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_251_seasonal_drawdown_vel_5d
    ECONOMIC RATIONALE: Velocity of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(5)

def seas_252_seasonal_drawdown_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_252_seasonal_drawdown_vel_21d
    ECONOMIC RATIONALE: Velocity of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(21)

def seas_253_seasonal_drawdown_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_253_seasonal_drawdown_vel_63d
    ECONOMIC RATIONALE: Velocity of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(63)

def seas_254_seasonal_drawdown_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_254_seasonal_drawdown_vel_126d
    ECONOMIC RATIONALE: Velocity of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(126)

def seas_255_seasonal_drawdown_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_255_seasonal_drawdown_vel_252d
    ECONOMIC RATIONALE: Velocity of seasonal_drawdown. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).diff(252)

def seas_256_monthly_momentum_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_256_monthly_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(5)

def seas_257_monthly_momentum_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_257_monthly_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(21)

def seas_258_monthly_momentum_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_258_monthly_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(63)

def seas_259_monthly_momentum_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_259_monthly_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(126)

def seas_260_monthly_momentum_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_260_monthly_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of monthly_momentum. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).diff(252)

def seas_261_september_distress_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_261_september_distress_vel_5d
    ECONOMIC RATIONALE: Velocity of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(5)

def seas_262_september_distress_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_262_september_distress_vel_21d
    ECONOMIC RATIONALE: Velocity of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(21)

def seas_263_september_distress_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_263_september_distress_vel_63d
    ECONOMIC RATIONALE: Velocity of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(63)

def seas_264_september_distress_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_264_september_distress_vel_126d
    ECONOMIC RATIONALE: Velocity of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(126)

def seas_265_september_distress_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_265_september_distress_vel_252d
    ECONOMIC RATIONALE: Velocity of september_distress. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).diff(252)

def seas_266_may_sell_signal_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_266_may_sell_signal_vel_5d
    ECONOMIC RATIONALE: Velocity of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(5)

def seas_267_may_sell_signal_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_267_may_sell_signal_vel_21d
    ECONOMIC RATIONALE: Velocity of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(21)

def seas_268_may_sell_signal_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_268_may_sell_signal_vel_63d
    ECONOMIC RATIONALE: Velocity of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(63)

def seas_269_may_sell_signal_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_269_may_sell_signal_vel_126d
    ECONOMIC RATIONALE: Velocity of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(126)

def seas_270_may_sell_signal_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_270_may_sell_signal_vel_252d
    ECONOMIC RATIONALE: Velocity of may_sell_signal. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).diff(252)

def seas_271_quarterly_seasonality_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_271_quarterly_seasonality_vel_5d
    ECONOMIC RATIONALE: Velocity of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(5)

def seas_272_quarterly_seasonality_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_272_quarterly_seasonality_vel_21d
    ECONOMIC RATIONALE: Velocity of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(21)

def seas_273_quarterly_seasonality_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_273_quarterly_seasonality_vel_63d
    ECONOMIC RATIONALE: Velocity of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(63)

def seas_274_quarterly_seasonality_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_274_quarterly_seasonality_vel_126d
    ECONOMIC RATIONALE: Velocity of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(126)

def seas_275_quarterly_seasonality_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_275_quarterly_seasonality_vel_252d
    ECONOMIC RATIONALE: Velocity of quarterly_seasonality. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).diff(252)

def seas_276_seasonal_zscore_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_276_seasonal_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(5)

def seas_277_seasonal_zscore_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_277_seasonal_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(21)

def seas_278_seasonal_zscore_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_278_seasonal_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(63)

def seas_279_seasonal_zscore_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_279_seasonal_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(126)

def seas_280_seasonal_zscore_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_280_seasonal_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of seasonal_zscore. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).diff(252)

def seas_281_holiday_liquidity_drain_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_281_holiday_liquidity_drain_vel_5d
    ECONOMIC RATIONALE: Velocity of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(5)

def seas_282_holiday_liquidity_drain_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_282_holiday_liquidity_drain_vel_21d
    ECONOMIC RATIONALE: Velocity of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(21)

def seas_283_holiday_liquidity_drain_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_283_holiday_liquidity_drain_vel_63d
    ECONOMIC RATIONALE: Velocity of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(63)

def seas_284_holiday_liquidity_drain_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_284_holiday_liquidity_drain_vel_126d
    ECONOMIC RATIONALE: Velocity of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(126)

def seas_285_holiday_liquidity_drain_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_285_holiday_liquidity_drain_vel_252d
    ECONOMIC RATIONALE: Velocity of holiday_liquidity_drain. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).diff(252)

def seas_286_seasonal_trend_strength_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_286_seasonal_trend_strength_vel_5d
    ECONOMIC RATIONALE: Velocity of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(5)

def seas_287_seasonal_trend_strength_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_287_seasonal_trend_strength_vel_21d
    ECONOMIC RATIONALE: Velocity of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(21)

def seas_288_seasonal_trend_strength_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_288_seasonal_trend_strength_vel_63d
    ECONOMIC RATIONALE: Velocity of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(63)

def seas_289_seasonal_trend_strength_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_289_seasonal_trend_strength_vel_126d
    ECONOMIC RATIONALE: Velocity of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(126)

def seas_290_seasonal_trend_strength_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_290_seasonal_trend_strength_vel_252d
    ECONOMIC RATIONALE: Velocity of seasonal_trend_strength. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).diff(252)

def seas_291_periodic_reversal_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_291_periodic_reversal_vel_5d
    ECONOMIC RATIONALE: Velocity of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(5)

def seas_292_periodic_reversal_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_292_periodic_reversal_vel_21d
    ECONOMIC RATIONALE: Velocity of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(21)

def seas_293_periodic_reversal_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_293_periodic_reversal_vel_63d
    ECONOMIC RATIONALE: Velocity of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(63)

def seas_294_periodic_reversal_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_294_periodic_reversal_vel_126d
    ECONOMIC RATIONALE: Velocity of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(126)

def seas_295_periodic_reversal_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_295_periodic_reversal_vel_252d
    ECONOMIC RATIONALE: Velocity of periodic_reversal. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).diff(252)

def seas_296_cycle_position_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_296_cycle_position_vel_5d
    ECONOMIC RATIONALE: Velocity of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(5)

def seas_297_cycle_position_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_297_cycle_position_vel_21d
    ECONOMIC RATIONALE: Velocity of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(21)

def seas_298_cycle_position_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_298_cycle_position_vel_63d
    ECONOMIC RATIONALE: Velocity of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(63)

def seas_299_cycle_position_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_299_cycle_position_vel_126d
    ECONOMIC RATIONALE: Velocity of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(126)

def seas_300_cycle_position_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_300_cycle_position_vel_252d
    ECONOMIC RATIONALE: Velocity of cycle_position. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V102_REGISTRY_VEL = {
    "seas_226_tax_loss_selling_vel_5d": {"inputs": ["close", "volume"], "func": seas_226_tax_loss_selling_vel_5d},
    "seas_227_tax_loss_selling_vel_21d": {"inputs": ["close", "volume"], "func": seas_227_tax_loss_selling_vel_21d},
    "seas_228_tax_loss_selling_vel_63d": {"inputs": ["close", "volume"], "func": seas_228_tax_loss_selling_vel_63d},
    "seas_229_tax_loss_selling_vel_126d": {"inputs": ["close", "volume"], "func": seas_229_tax_loss_selling_vel_126d},
    "seas_230_tax_loss_selling_vel_252d": {"inputs": ["close", "volume"], "func": seas_230_tax_loss_selling_vel_252d},
    "seas_231_january_effect_reversal_vel_5d": {"inputs": ["close", "volume"], "func": seas_231_january_effect_reversal_vel_5d},
    "seas_232_january_effect_reversal_vel_21d": {"inputs": ["close", "volume"], "func": seas_232_january_effect_reversal_vel_21d},
    "seas_233_january_effect_reversal_vel_63d": {"inputs": ["close", "volume"], "func": seas_233_january_effect_reversal_vel_63d},
    "seas_234_january_effect_reversal_vel_126d": {"inputs": ["close", "volume"], "func": seas_234_january_effect_reversal_vel_126d},
    "seas_235_january_effect_reversal_vel_252d": {"inputs": ["close", "volume"], "func": seas_235_january_effect_reversal_vel_252d},
    "seas_236_quarter_end_window_dressing_vel_5d": {"inputs": ["close", "volume"], "func": seas_236_quarter_end_window_dressing_vel_5d},
    "seas_237_quarter_end_window_dressing_vel_21d": {"inputs": ["close", "volume"], "func": seas_237_quarter_end_window_dressing_vel_21d},
    "seas_238_quarter_end_window_dressing_vel_63d": {"inputs": ["close", "volume"], "func": seas_238_quarter_end_window_dressing_vel_63d},
    "seas_239_quarter_end_window_dressing_vel_126d": {"inputs": ["close", "volume"], "func": seas_239_quarter_end_window_dressing_vel_126d},
    "seas_240_quarter_end_window_dressing_vel_252d": {"inputs": ["close", "volume"], "func": seas_240_quarter_end_window_dressing_vel_252d},
    "seas_241_seasonal_volatility_vel_5d": {"inputs": ["close", "volume"], "func": seas_241_seasonal_volatility_vel_5d},
    "seas_242_seasonal_volatility_vel_21d": {"inputs": ["close", "volume"], "func": seas_242_seasonal_volatility_vel_21d},
    "seas_243_seasonal_volatility_vel_63d": {"inputs": ["close", "volume"], "func": seas_243_seasonal_volatility_vel_63d},
    "seas_244_seasonal_volatility_vel_126d": {"inputs": ["close", "volume"], "func": seas_244_seasonal_volatility_vel_126d},
    "seas_245_seasonal_volatility_vel_252d": {"inputs": ["close", "volume"], "func": seas_245_seasonal_volatility_vel_252d},
    "seas_246_month_of_year_returns_vel_5d": {"inputs": ["close", "volume"], "func": seas_246_month_of_year_returns_vel_5d},
    "seas_247_month_of_year_returns_vel_21d": {"inputs": ["close", "volume"], "func": seas_247_month_of_year_returns_vel_21d},
    "seas_248_month_of_year_returns_vel_63d": {"inputs": ["close", "volume"], "func": seas_248_month_of_year_returns_vel_63d},
    "seas_249_month_of_year_returns_vel_126d": {"inputs": ["close", "volume"], "func": seas_249_month_of_year_returns_vel_126d},
    "seas_250_month_of_year_returns_vel_252d": {"inputs": ["close", "volume"], "func": seas_250_month_of_year_returns_vel_252d},
    "seas_251_seasonal_drawdown_vel_5d": {"inputs": ["close", "volume"], "func": seas_251_seasonal_drawdown_vel_5d},
    "seas_252_seasonal_drawdown_vel_21d": {"inputs": ["close", "volume"], "func": seas_252_seasonal_drawdown_vel_21d},
    "seas_253_seasonal_drawdown_vel_63d": {"inputs": ["close", "volume"], "func": seas_253_seasonal_drawdown_vel_63d},
    "seas_254_seasonal_drawdown_vel_126d": {"inputs": ["close", "volume"], "func": seas_254_seasonal_drawdown_vel_126d},
    "seas_255_seasonal_drawdown_vel_252d": {"inputs": ["close", "volume"], "func": seas_255_seasonal_drawdown_vel_252d},
    "seas_256_monthly_momentum_vel_5d": {"inputs": ["close", "volume"], "func": seas_256_monthly_momentum_vel_5d},
    "seas_257_monthly_momentum_vel_21d": {"inputs": ["close", "volume"], "func": seas_257_monthly_momentum_vel_21d},
    "seas_258_monthly_momentum_vel_63d": {"inputs": ["close", "volume"], "func": seas_258_monthly_momentum_vel_63d},
    "seas_259_monthly_momentum_vel_126d": {"inputs": ["close", "volume"], "func": seas_259_monthly_momentum_vel_126d},
    "seas_260_monthly_momentum_vel_252d": {"inputs": ["close", "volume"], "func": seas_260_monthly_momentum_vel_252d},
    "seas_261_september_distress_vel_5d": {"inputs": ["close", "volume"], "func": seas_261_september_distress_vel_5d},
    "seas_262_september_distress_vel_21d": {"inputs": ["close", "volume"], "func": seas_262_september_distress_vel_21d},
    "seas_263_september_distress_vel_63d": {"inputs": ["close", "volume"], "func": seas_263_september_distress_vel_63d},
    "seas_264_september_distress_vel_126d": {"inputs": ["close", "volume"], "func": seas_264_september_distress_vel_126d},
    "seas_265_september_distress_vel_252d": {"inputs": ["close", "volume"], "func": seas_265_september_distress_vel_252d},
    "seas_266_may_sell_signal_vel_5d": {"inputs": ["close", "volume"], "func": seas_266_may_sell_signal_vel_5d},
    "seas_267_may_sell_signal_vel_21d": {"inputs": ["close", "volume"], "func": seas_267_may_sell_signal_vel_21d},
    "seas_268_may_sell_signal_vel_63d": {"inputs": ["close", "volume"], "func": seas_268_may_sell_signal_vel_63d},
    "seas_269_may_sell_signal_vel_126d": {"inputs": ["close", "volume"], "func": seas_269_may_sell_signal_vel_126d},
    "seas_270_may_sell_signal_vel_252d": {"inputs": ["close", "volume"], "func": seas_270_may_sell_signal_vel_252d},
    "seas_271_quarterly_seasonality_vel_5d": {"inputs": ["close", "volume"], "func": seas_271_quarterly_seasonality_vel_5d},
    "seas_272_quarterly_seasonality_vel_21d": {"inputs": ["close", "volume"], "func": seas_272_quarterly_seasonality_vel_21d},
    "seas_273_quarterly_seasonality_vel_63d": {"inputs": ["close", "volume"], "func": seas_273_quarterly_seasonality_vel_63d},
    "seas_274_quarterly_seasonality_vel_126d": {"inputs": ["close", "volume"], "func": seas_274_quarterly_seasonality_vel_126d},
    "seas_275_quarterly_seasonality_vel_252d": {"inputs": ["close", "volume"], "func": seas_275_quarterly_seasonality_vel_252d},
    "seas_276_seasonal_zscore_vel_5d": {"inputs": ["close", "volume"], "func": seas_276_seasonal_zscore_vel_5d},
    "seas_277_seasonal_zscore_vel_21d": {"inputs": ["close", "volume"], "func": seas_277_seasonal_zscore_vel_21d},
    "seas_278_seasonal_zscore_vel_63d": {"inputs": ["close", "volume"], "func": seas_278_seasonal_zscore_vel_63d},
    "seas_279_seasonal_zscore_vel_126d": {"inputs": ["close", "volume"], "func": seas_279_seasonal_zscore_vel_126d},
    "seas_280_seasonal_zscore_vel_252d": {"inputs": ["close", "volume"], "func": seas_280_seasonal_zscore_vel_252d},
    "seas_281_holiday_liquidity_drain_vel_5d": {"inputs": ["close", "volume"], "func": seas_281_holiday_liquidity_drain_vel_5d},
    "seas_282_holiday_liquidity_drain_vel_21d": {"inputs": ["close", "volume"], "func": seas_282_holiday_liquidity_drain_vel_21d},
    "seas_283_holiday_liquidity_drain_vel_63d": {"inputs": ["close", "volume"], "func": seas_283_holiday_liquidity_drain_vel_63d},
    "seas_284_holiday_liquidity_drain_vel_126d": {"inputs": ["close", "volume"], "func": seas_284_holiday_liquidity_drain_vel_126d},
    "seas_285_holiday_liquidity_drain_vel_252d": {"inputs": ["close", "volume"], "func": seas_285_holiday_liquidity_drain_vel_252d},
    "seas_286_seasonal_trend_strength_vel_5d": {"inputs": ["close", "volume"], "func": seas_286_seasonal_trend_strength_vel_5d},
    "seas_287_seasonal_trend_strength_vel_21d": {"inputs": ["close", "volume"], "func": seas_287_seasonal_trend_strength_vel_21d},
    "seas_288_seasonal_trend_strength_vel_63d": {"inputs": ["close", "volume"], "func": seas_288_seasonal_trend_strength_vel_63d},
    "seas_289_seasonal_trend_strength_vel_126d": {"inputs": ["close", "volume"], "func": seas_289_seasonal_trend_strength_vel_126d},
    "seas_290_seasonal_trend_strength_vel_252d": {"inputs": ["close", "volume"], "func": seas_290_seasonal_trend_strength_vel_252d},
    "seas_291_periodic_reversal_vel_5d": {"inputs": ["close", "volume"], "func": seas_291_periodic_reversal_vel_5d},
    "seas_292_periodic_reversal_vel_21d": {"inputs": ["close", "volume"], "func": seas_292_periodic_reversal_vel_21d},
    "seas_293_periodic_reversal_vel_63d": {"inputs": ["close", "volume"], "func": seas_293_periodic_reversal_vel_63d},
    "seas_294_periodic_reversal_vel_126d": {"inputs": ["close", "volume"], "func": seas_294_periodic_reversal_vel_126d},
    "seas_295_periodic_reversal_vel_252d": {"inputs": ["close", "volume"], "func": seas_295_periodic_reversal_vel_252d},
    "seas_296_cycle_position_vel_5d": {"inputs": ["close", "volume"], "func": seas_296_cycle_position_vel_5d},
    "seas_297_cycle_position_vel_21d": {"inputs": ["close", "volume"], "func": seas_297_cycle_position_vel_21d},
    "seas_298_cycle_position_vel_63d": {"inputs": ["close", "volume"], "func": seas_298_cycle_position_vel_63d},
    "seas_299_cycle_position_vel_126d": {"inputs": ["close", "volume"], "func": seas_299_cycle_position_vel_126d},
    "seas_300_cycle_position_vel_252d": {"inputs": ["close", "volume"], "func": seas_300_cycle_position_vel_252d},
}
