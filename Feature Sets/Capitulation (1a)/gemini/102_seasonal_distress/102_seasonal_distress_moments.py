"""
102_seasonal_distress — Statistical Moments
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

def seas_376_tax_loss_selling_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_376_tax_loss_selling_skew_5d
    ECONOMIC RATIONALE: Skewness of tax_loss_selling over 5d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(5).skew()

def seas_377_tax_loss_selling_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_377_tax_loss_selling_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tax_loss_selling over 5d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(5).kurt()

def seas_378_tax_loss_selling_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_378_tax_loss_selling_skew_21d
    ECONOMIC RATIONALE: Skewness of tax_loss_selling over 21d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(21).skew()

def seas_379_tax_loss_selling_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_379_tax_loss_selling_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tax_loss_selling over 21d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(21).kurt()

def seas_380_tax_loss_selling_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_380_tax_loss_selling_skew_63d
    ECONOMIC RATIONALE: Skewness of tax_loss_selling over 63d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(63).skew()

def seas_381_tax_loss_selling_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_381_tax_loss_selling_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tax_loss_selling over 63d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(63).kurt()

def seas_382_tax_loss_selling_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_382_tax_loss_selling_skew_126d
    ECONOMIC RATIONALE: Skewness of tax_loss_selling over 126d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(126).skew()

def seas_383_tax_loss_selling_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_383_tax_loss_selling_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tax_loss_selling over 126d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(126).kurt()

def seas_384_tax_loss_selling_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_384_tax_loss_selling_skew_252d
    ECONOMIC RATIONALE: Skewness of tax_loss_selling over 252d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(252).skew()

def seas_385_tax_loss_selling_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_385_tax_loss_selling_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tax_loss_selling over 252d. Deeply negative annual returns increase year-end selling pressure.
    """
    return (close.pct_change(252) < -0.3).rolling(252).kurt()

def seas_386_january_effect_reversal_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_386_january_effect_reversal_skew_5d
    ECONOMIC RATIONALE: Skewness of january_effect_reversal over 5d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(5).skew()

def seas_387_january_effect_reversal_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_387_january_effect_reversal_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of january_effect_reversal over 5d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(5).kurt()

def seas_388_january_effect_reversal_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_388_january_effect_reversal_skew_21d
    ECONOMIC RATIONALE: Skewness of january_effect_reversal over 21d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(21).skew()

def seas_389_january_effect_reversal_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_389_january_effect_reversal_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of january_effect_reversal over 21d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(21).kurt()

def seas_390_january_effect_reversal_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_390_january_effect_reversal_skew_63d
    ECONOMIC RATIONALE: Skewness of january_effect_reversal over 63d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(63).skew()

def seas_391_january_effect_reversal_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_391_january_effect_reversal_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of january_effect_reversal over 63d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(63).kurt()

def seas_392_january_effect_reversal_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_392_january_effect_reversal_skew_126d
    ECONOMIC RATIONALE: Skewness of january_effect_reversal over 126d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(126).skew()

def seas_393_january_effect_reversal_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_393_january_effect_reversal_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of january_effect_reversal over 126d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(126).kurt()

def seas_394_january_effect_reversal_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_394_january_effect_reversal_skew_252d
    ECONOMIC RATIONALE: Skewness of january_effect_reversal over 252d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(252).skew()

def seas_395_january_effect_reversal_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_395_january_effect_reversal_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of january_effect_reversal over 252d. Mean reversion potential in January for oversold stocks.
    """
    return (close.pct_change(21)).rolling(252).kurt()

def seas_396_quarter_end_window_dressing_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_396_quarter_end_window_dressing_skew_5d
    ECONOMIC RATIONALE: Skewness of quarter_end_window_dressing over 5d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(5).skew()

def seas_397_quarter_end_window_dressing_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_397_quarter_end_window_dressing_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of quarter_end_window_dressing over 5d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(5).kurt()

def seas_398_quarter_end_window_dressing_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_398_quarter_end_window_dressing_skew_21d
    ECONOMIC RATIONALE: Skewness of quarter_end_window_dressing over 21d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(21).skew()

def seas_399_quarter_end_window_dressing_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_399_quarter_end_window_dressing_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of quarter_end_window_dressing over 21d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(21).kurt()

def seas_400_quarter_end_window_dressing_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_400_quarter_end_window_dressing_skew_63d
    ECONOMIC RATIONALE: Skewness of quarter_end_window_dressing over 63d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(63).skew()

def seas_401_quarter_end_window_dressing_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_401_quarter_end_window_dressing_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of quarter_end_window_dressing over 63d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(63).kurt()

def seas_402_quarter_end_window_dressing_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_402_quarter_end_window_dressing_skew_126d
    ECONOMIC RATIONALE: Skewness of quarter_end_window_dressing over 126d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(126).skew()

def seas_403_quarter_end_window_dressing_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_403_quarter_end_window_dressing_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of quarter_end_window_dressing over 126d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(126).kurt()

def seas_404_quarter_end_window_dressing_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_404_quarter_end_window_dressing_skew_252d
    ECONOMIC RATIONALE: Skewness of quarter_end_window_dressing over 252d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(252).skew()

def seas_405_quarter_end_window_dressing_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_405_quarter_end_window_dressing_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of quarter_end_window_dressing over 252d. Performance during quarter-end reporting periods.
    """
    return (close.pct_change(63)).rolling(252).kurt()

def seas_406_seasonal_volatility_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_406_seasonal_volatility_skew_5d
    ECONOMIC RATIONALE: Skewness of seasonal_volatility over 5d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(5).skew()

def seas_407_seasonal_volatility_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_407_seasonal_volatility_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of seasonal_volatility over 5d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(5).kurt()

def seas_408_seasonal_volatility_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_408_seasonal_volatility_skew_21d
    ECONOMIC RATIONALE: Skewness of seasonal_volatility over 21d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(21).skew()

def seas_409_seasonal_volatility_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_409_seasonal_volatility_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of seasonal_volatility over 21d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(21).kurt()

def seas_410_seasonal_volatility_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_410_seasonal_volatility_skew_63d
    ECONOMIC RATIONALE: Skewness of seasonal_volatility over 63d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(63).skew()

def seas_411_seasonal_volatility_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_411_seasonal_volatility_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of seasonal_volatility over 63d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(63).kurt()

def seas_412_seasonal_volatility_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_412_seasonal_volatility_skew_126d
    ECONOMIC RATIONALE: Skewness of seasonal_volatility over 126d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(126).skew()

def seas_413_seasonal_volatility_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_413_seasonal_volatility_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of seasonal_volatility over 126d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(126).kurt()

def seas_414_seasonal_volatility_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_414_seasonal_volatility_skew_252d
    ECONOMIC RATIONALE: Skewness of seasonal_volatility over 252d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(252).skew()

def seas_415_seasonal_volatility_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_415_seasonal_volatility_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of seasonal_volatility over 252d. Historical average volatility for the current month.
    """
    return (close.rolling(21).std().groupby(close.index.month).transform('mean')).rolling(252).kurt()

def seas_416_month_of_year_returns_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_416_month_of_year_returns_skew_5d
    ECONOMIC RATIONALE: Skewness of month_of_year_returns over 5d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(5).skew()

def seas_417_month_of_year_returns_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_417_month_of_year_returns_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of month_of_year_returns over 5d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(5).kurt()

def seas_418_month_of_year_returns_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_418_month_of_year_returns_skew_21d
    ECONOMIC RATIONALE: Skewness of month_of_year_returns over 21d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(21).skew()

def seas_419_month_of_year_returns_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_419_month_of_year_returns_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of month_of_year_returns over 21d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(21).kurt()

def seas_420_month_of_year_returns_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_420_month_of_year_returns_skew_63d
    ECONOMIC RATIONALE: Skewness of month_of_year_returns over 63d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(63).skew()

def seas_421_month_of_year_returns_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_421_month_of_year_returns_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of month_of_year_returns over 63d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(63).kurt()

def seas_422_month_of_year_returns_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_422_month_of_year_returns_skew_126d
    ECONOMIC RATIONALE: Skewness of month_of_year_returns over 126d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(126).skew()

def seas_423_month_of_year_returns_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_423_month_of_year_returns_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of month_of_year_returns over 126d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(126).kurt()

def seas_424_month_of_year_returns_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_424_month_of_year_returns_skew_252d
    ECONOMIC RATIONALE: Skewness of month_of_year_returns over 252d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(252).skew()

def seas_425_month_of_year_returns_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_425_month_of_year_returns_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of month_of_year_returns over 252d. Historical average return for the current month.
    """
    return (close.pct_change(21).groupby(close.index.month).transform('mean')).rolling(252).kurt()

def seas_426_seasonal_drawdown_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_426_seasonal_drawdown_skew_5d
    ECONOMIC RATIONALE: Skewness of seasonal_drawdown over 5d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(5).skew()

def seas_427_seasonal_drawdown_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_427_seasonal_drawdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of seasonal_drawdown over 5d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(5).kurt()

def seas_428_seasonal_drawdown_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_428_seasonal_drawdown_skew_21d
    ECONOMIC RATIONALE: Skewness of seasonal_drawdown over 21d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(21).skew()

def seas_429_seasonal_drawdown_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_429_seasonal_drawdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of seasonal_drawdown over 21d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(21).kurt()

def seas_430_seasonal_drawdown_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_430_seasonal_drawdown_skew_63d
    ECONOMIC RATIONALE: Skewness of seasonal_drawdown over 63d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(63).skew()

def seas_431_seasonal_drawdown_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_431_seasonal_drawdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of seasonal_drawdown over 63d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(63).kurt()

def seas_432_seasonal_drawdown_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_432_seasonal_drawdown_skew_126d
    ECONOMIC RATIONALE: Skewness of seasonal_drawdown over 126d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(126).skew()

def seas_433_seasonal_drawdown_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_433_seasonal_drawdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of seasonal_drawdown over 126d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(126).kurt()

def seas_434_seasonal_drawdown_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_434_seasonal_drawdown_skew_252d
    ECONOMIC RATIONALE: Skewness of seasonal_drawdown over 252d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(252).skew()

def seas_435_seasonal_drawdown_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_435_seasonal_drawdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of seasonal_drawdown over 252d. Drawdown state relative to seasonal cycles.
    """
    return (close / close.rolling(252).max() - 1).rolling(252).kurt()

def seas_436_monthly_momentum_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_436_monthly_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of monthly_momentum over 5d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(5).skew()

def seas_437_monthly_momentum_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_437_monthly_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of monthly_momentum over 5d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(5).kurt()

def seas_438_monthly_momentum_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_438_monthly_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of monthly_momentum over 21d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(21).skew()

def seas_439_monthly_momentum_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_439_monthly_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of monthly_momentum over 21d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(21).kurt()

def seas_440_monthly_momentum_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_440_monthly_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of monthly_momentum over 63d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(63).skew()

def seas_441_monthly_momentum_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_441_monthly_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of monthly_momentum over 63d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(63).kurt()

def seas_442_monthly_momentum_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_442_monthly_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of monthly_momentum over 126d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(126).skew()

def seas_443_monthly_momentum_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_443_monthly_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of monthly_momentum over 126d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(126).kurt()

def seas_444_monthly_momentum_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_444_monthly_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of monthly_momentum over 252d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(252).skew()

def seas_445_monthly_momentum_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_445_monthly_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of monthly_momentum over 252d. Deviation from typical seasonal momentum.
    """
    return (close.pct_change(21) - close.pct_change(126).rolling(21).mean()).rolling(252).kurt()

def seas_446_september_distress_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_446_september_distress_skew_5d
    ECONOMIC RATIONALE: Skewness of september_distress over 5d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(5).skew()

def seas_447_september_distress_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_447_september_distress_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of september_distress over 5d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(5).kurt()

def seas_448_september_distress_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_448_september_distress_skew_21d
    ECONOMIC RATIONALE: Skewness of september_distress over 21d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(21).skew()

def seas_449_september_distress_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_449_september_distress_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of september_distress over 21d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(21).kurt()

def seas_450_september_distress_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_450_september_distress_skew_63d
    ECONOMIC RATIONALE: Skewness of september_distress over 63d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(63).skew()

def seas_451_september_distress_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_451_september_distress_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of september_distress over 63d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(63).kurt()

def seas_452_september_distress_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_452_september_distress_skew_126d
    ECONOMIC RATIONALE: Skewness of september_distress over 126d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(126).skew()

def seas_453_september_distress_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_453_september_distress_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of september_distress over 126d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(126).kurt()

def seas_454_september_distress_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_454_september_distress_skew_252d
    ECONOMIC RATIONALE: Skewness of september_distress over 252d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(252).skew()

def seas_455_september_distress_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_455_september_distress_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of september_distress over 252d. Historical weakness in September applied to current price.
    """
    return (close.pct_change(21) * (close.index.month == 9).astype(float)).rolling(252).kurt()

def seas_456_may_sell_signal_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_456_may_sell_signal_skew_5d
    ECONOMIC RATIONALE: Skewness of may_sell_signal over 5d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(5).skew()

def seas_457_may_sell_signal_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_457_may_sell_signal_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of may_sell_signal over 5d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(5).kurt()

def seas_458_may_sell_signal_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_458_may_sell_signal_skew_21d
    ECONOMIC RATIONALE: Skewness of may_sell_signal over 21d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(21).skew()

def seas_459_may_sell_signal_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_459_may_sell_signal_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of may_sell_signal over 21d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(21).kurt()

def seas_460_may_sell_signal_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_460_may_sell_signal_skew_63d
    ECONOMIC RATIONALE: Skewness of may_sell_signal over 63d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(63).skew()

def seas_461_may_sell_signal_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_461_may_sell_signal_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of may_sell_signal over 63d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(63).kurt()

def seas_462_may_sell_signal_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_462_may_sell_signal_skew_126d
    ECONOMIC RATIONALE: Skewness of may_sell_signal over 126d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(126).skew()

def seas_463_may_sell_signal_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_463_may_sell_signal_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of may_sell_signal over 126d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(126).kurt()

def seas_464_may_sell_signal_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_464_may_sell_signal_skew_252d
    ECONOMIC RATIONALE: Skewness of may_sell_signal over 252d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(252).skew()

def seas_465_may_sell_signal_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_465_may_sell_signal_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of may_sell_signal over 252d. Seasonal 'sell in May' effect.
    """
    return (close.pct_change(21) * (close.index.month == 5).astype(float)).rolling(252).kurt()

def seas_466_quarterly_seasonality_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_466_quarterly_seasonality_skew_5d
    ECONOMIC RATIONALE: Skewness of quarterly_seasonality over 5d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(5).skew()

def seas_467_quarterly_seasonality_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_467_quarterly_seasonality_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of quarterly_seasonality over 5d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(5).kurt()

def seas_468_quarterly_seasonality_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_468_quarterly_seasonality_skew_21d
    ECONOMIC RATIONALE: Skewness of quarterly_seasonality over 21d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(21).skew()

def seas_469_quarterly_seasonality_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_469_quarterly_seasonality_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of quarterly_seasonality over 21d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(21).kurt()

def seas_470_quarterly_seasonality_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_470_quarterly_seasonality_skew_63d
    ECONOMIC RATIONALE: Skewness of quarterly_seasonality over 63d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(63).skew()

def seas_471_quarterly_seasonality_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_471_quarterly_seasonality_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of quarterly_seasonality over 63d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(63).kurt()

def seas_472_quarterly_seasonality_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_472_quarterly_seasonality_skew_126d
    ECONOMIC RATIONALE: Skewness of quarterly_seasonality over 126d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(126).skew()

def seas_473_quarterly_seasonality_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_473_quarterly_seasonality_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of quarterly_seasonality over 126d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(126).kurt()

def seas_474_quarterly_seasonality_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_474_quarterly_seasonality_skew_252d
    ECONOMIC RATIONALE: Skewness of quarterly_seasonality over 252d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(252).skew()

def seas_475_quarterly_seasonality_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_475_quarterly_seasonality_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of quarterly_seasonality over 252d. Average returns by fiscal quarter.
    """
    return (close.pct_change(63).groupby(close.index.quarter).transform('mean')).rolling(252).kurt()

def seas_476_seasonal_zscore_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_476_seasonal_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of seasonal_zscore over 5d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(5).skew()

def seas_477_seasonal_zscore_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_477_seasonal_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of seasonal_zscore over 5d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(5).kurt()

def seas_478_seasonal_zscore_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_478_seasonal_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of seasonal_zscore over 21d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(21).skew()

def seas_479_seasonal_zscore_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_479_seasonal_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of seasonal_zscore over 21d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(21).kurt()

def seas_480_seasonal_zscore_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_480_seasonal_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of seasonal_zscore over 63d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(63).skew()

def seas_481_seasonal_zscore_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_481_seasonal_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of seasonal_zscore over 63d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(63).kurt()

def seas_482_seasonal_zscore_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_482_seasonal_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of seasonal_zscore over 126d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(126).skew()

def seas_483_seasonal_zscore_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_483_seasonal_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of seasonal_zscore over 126d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(126).kurt()

def seas_484_seasonal_zscore_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_484_seasonal_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of seasonal_zscore over 252d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(252).skew()

def seas_485_seasonal_zscore_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_485_seasonal_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of seasonal_zscore over 252d. Returns relative to the rolling annual distribution.
    """
    return (_zscore_rolling(close.pct_change(21), 252)).rolling(252).kurt()

def seas_486_holiday_liquidity_drain_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_486_holiday_liquidity_drain_skew_5d
    ECONOMIC RATIONALE: Skewness of holiday_liquidity_drain over 5d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(5).skew()

def seas_487_holiday_liquidity_drain_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_487_holiday_liquidity_drain_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of holiday_liquidity_drain over 5d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(5).kurt()

def seas_488_holiday_liquidity_drain_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_488_holiday_liquidity_drain_skew_21d
    ECONOMIC RATIONALE: Skewness of holiday_liquidity_drain over 21d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(21).skew()

def seas_489_holiday_liquidity_drain_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_489_holiday_liquidity_drain_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of holiday_liquidity_drain over 21d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(21).kurt()

def seas_490_holiday_liquidity_drain_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_490_holiday_liquidity_drain_skew_63d
    ECONOMIC RATIONALE: Skewness of holiday_liquidity_drain over 63d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(63).skew()

def seas_491_holiday_liquidity_drain_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_491_holiday_liquidity_drain_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of holiday_liquidity_drain over 63d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(63).kurt()

def seas_492_holiday_liquidity_drain_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_492_holiday_liquidity_drain_skew_126d
    ECONOMIC RATIONALE: Skewness of holiday_liquidity_drain over 126d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(126).skew()

def seas_493_holiday_liquidity_drain_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_493_holiday_liquidity_drain_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of holiday_liquidity_drain over 126d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(126).kurt()

def seas_494_holiday_liquidity_drain_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_494_holiday_liquidity_drain_skew_252d
    ECONOMIC RATIONALE: Skewness of holiday_liquidity_drain over 252d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(252).skew()

def seas_495_holiday_liquidity_drain_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_495_holiday_liquidity_drain_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of holiday_liquidity_drain over 252d. Volume drops around holiday periods.
    """
    return (volume / volume.rolling(252).mean()).rolling(252).kurt()

def seas_496_seasonal_trend_strength_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_496_seasonal_trend_strength_skew_5d
    ECONOMIC RATIONALE: Skewness of seasonal_trend_strength over 5d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(5).skew()

def seas_497_seasonal_trend_strength_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_497_seasonal_trend_strength_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of seasonal_trend_strength over 5d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(5).kurt()

def seas_498_seasonal_trend_strength_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_498_seasonal_trend_strength_skew_21d
    ECONOMIC RATIONALE: Skewness of seasonal_trend_strength over 21d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(21).skew()

def seas_499_seasonal_trend_strength_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_499_seasonal_trend_strength_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of seasonal_trend_strength over 21d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(21).kurt()

def seas_500_seasonal_trend_strength_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_500_seasonal_trend_strength_skew_63d
    ECONOMIC RATIONALE: Skewness of seasonal_trend_strength over 63d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(63).skew()

def seas_501_seasonal_trend_strength_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_501_seasonal_trend_strength_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of seasonal_trend_strength over 63d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(63).kurt()

def seas_502_seasonal_trend_strength_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_502_seasonal_trend_strength_skew_126d
    ECONOMIC RATIONALE: Skewness of seasonal_trend_strength over 126d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(126).skew()

def seas_503_seasonal_trend_strength_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_503_seasonal_trend_strength_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of seasonal_trend_strength over 126d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(126).kurt()

def seas_504_seasonal_trend_strength_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_504_seasonal_trend_strength_skew_252d
    ECONOMIC RATIONALE: Skewness of seasonal_trend_strength over 252d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(252).skew()

def seas_505_seasonal_trend_strength_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_505_seasonal_trend_strength_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of seasonal_trend_strength over 252d. Medium vs long term structural trend.
    """
    return (close.rolling(63).mean() / close.rolling(252).mean()).rolling(252).kurt()

def seas_506_periodic_reversal_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_506_periodic_reversal_skew_5d
    ECONOMIC RATIONALE: Skewness of periodic_reversal over 5d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(5).skew()

def seas_507_periodic_reversal_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_507_periodic_reversal_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of periodic_reversal over 5d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(5).kurt()

def seas_508_periodic_reversal_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_508_periodic_reversal_skew_21d
    ECONOMIC RATIONALE: Skewness of periodic_reversal over 21d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(21).skew()

def seas_509_periodic_reversal_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_509_periodic_reversal_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of periodic_reversal over 21d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(21).kurt()

def seas_510_periodic_reversal_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_510_periodic_reversal_skew_63d
    ECONOMIC RATIONALE: Skewness of periodic_reversal over 63d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(63).skew()

def seas_511_periodic_reversal_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_511_periodic_reversal_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of periodic_reversal over 63d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(63).kurt()

def seas_512_periodic_reversal_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_512_periodic_reversal_skew_126d
    ECONOMIC RATIONALE: Skewness of periodic_reversal over 126d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(126).skew()

def seas_513_periodic_reversal_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_513_periodic_reversal_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of periodic_reversal over 126d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(126).kurt()

def seas_514_periodic_reversal_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_514_periodic_reversal_skew_252d
    ECONOMIC RATIONALE: Skewness of periodic_reversal over 252d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(252).skew()

def seas_515_periodic_reversal_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_515_periodic_reversal_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of periodic_reversal over 252d. Short-term reaction vs long-term cycle.
    """
    return (close.pct_change(5) / close.pct_change(252)).rolling(252).kurt()

def seas_516_cycle_position_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_516_cycle_position_skew_5d
    ECONOMIC RATIONALE: Skewness of cycle_position over 5d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(5).skew()

def seas_517_cycle_position_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_517_cycle_position_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of cycle_position over 5d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(5).kurt()

def seas_518_cycle_position_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_518_cycle_position_skew_21d
    ECONOMIC RATIONALE: Skewness of cycle_position over 21d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(21).skew()

def seas_519_cycle_position_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_519_cycle_position_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of cycle_position over 21d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(21).kurt()

def seas_520_cycle_position_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_520_cycle_position_skew_63d
    ECONOMIC RATIONALE: Skewness of cycle_position over 63d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(63).skew()

def seas_521_cycle_position_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_521_cycle_position_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of cycle_position over 63d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(63).kurt()

def seas_522_cycle_position_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_522_cycle_position_skew_126d
    ECONOMIC RATIONALE: Skewness of cycle_position over 126d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(126).skew()

def seas_523_cycle_position_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_523_cycle_position_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of cycle_position over 126d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(126).kurt()

def seas_524_cycle_position_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_524_cycle_position_skew_252d
    ECONOMIC RATIONALE: Skewness of cycle_position over 252d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(252).skew()

def seas_525_cycle_position_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    seas_525_cycle_position_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of cycle_position over 252d. Sinusoidal representation of the annual cycle.
    """
    return (np.sin(2 * np.pi * close.index.dayofyear / 365.25)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V102_REGISTRY_MOMENTS = {
    "seas_376_tax_loss_selling_skew_5d": {"inputs": ["close", "volume"], "func": seas_376_tax_loss_selling_skew_5d},
    "seas_377_tax_loss_selling_kurt_5d": {"inputs": ["close", "volume"], "func": seas_377_tax_loss_selling_kurt_5d},
    "seas_378_tax_loss_selling_skew_21d": {"inputs": ["close", "volume"], "func": seas_378_tax_loss_selling_skew_21d},
    "seas_379_tax_loss_selling_kurt_21d": {"inputs": ["close", "volume"], "func": seas_379_tax_loss_selling_kurt_21d},
    "seas_380_tax_loss_selling_skew_63d": {"inputs": ["close", "volume"], "func": seas_380_tax_loss_selling_skew_63d},
    "seas_381_tax_loss_selling_kurt_63d": {"inputs": ["close", "volume"], "func": seas_381_tax_loss_selling_kurt_63d},
    "seas_382_tax_loss_selling_skew_126d": {"inputs": ["close", "volume"], "func": seas_382_tax_loss_selling_skew_126d},
    "seas_383_tax_loss_selling_kurt_126d": {"inputs": ["close", "volume"], "func": seas_383_tax_loss_selling_kurt_126d},
    "seas_384_tax_loss_selling_skew_252d": {"inputs": ["close", "volume"], "func": seas_384_tax_loss_selling_skew_252d},
    "seas_385_tax_loss_selling_kurt_252d": {"inputs": ["close", "volume"], "func": seas_385_tax_loss_selling_kurt_252d},
    "seas_386_january_effect_reversal_skew_5d": {"inputs": ["close", "volume"], "func": seas_386_january_effect_reversal_skew_5d},
    "seas_387_january_effect_reversal_kurt_5d": {"inputs": ["close", "volume"], "func": seas_387_january_effect_reversal_kurt_5d},
    "seas_388_january_effect_reversal_skew_21d": {"inputs": ["close", "volume"], "func": seas_388_january_effect_reversal_skew_21d},
    "seas_389_january_effect_reversal_kurt_21d": {"inputs": ["close", "volume"], "func": seas_389_january_effect_reversal_kurt_21d},
    "seas_390_january_effect_reversal_skew_63d": {"inputs": ["close", "volume"], "func": seas_390_january_effect_reversal_skew_63d},
    "seas_391_january_effect_reversal_kurt_63d": {"inputs": ["close", "volume"], "func": seas_391_january_effect_reversal_kurt_63d},
    "seas_392_january_effect_reversal_skew_126d": {"inputs": ["close", "volume"], "func": seas_392_january_effect_reversal_skew_126d},
    "seas_393_january_effect_reversal_kurt_126d": {"inputs": ["close", "volume"], "func": seas_393_january_effect_reversal_kurt_126d},
    "seas_394_january_effect_reversal_skew_252d": {"inputs": ["close", "volume"], "func": seas_394_january_effect_reversal_skew_252d},
    "seas_395_january_effect_reversal_kurt_252d": {"inputs": ["close", "volume"], "func": seas_395_january_effect_reversal_kurt_252d},
    "seas_396_quarter_end_window_dressing_skew_5d": {"inputs": ["close", "volume"], "func": seas_396_quarter_end_window_dressing_skew_5d},
    "seas_397_quarter_end_window_dressing_kurt_5d": {"inputs": ["close", "volume"], "func": seas_397_quarter_end_window_dressing_kurt_5d},
    "seas_398_quarter_end_window_dressing_skew_21d": {"inputs": ["close", "volume"], "func": seas_398_quarter_end_window_dressing_skew_21d},
    "seas_399_quarter_end_window_dressing_kurt_21d": {"inputs": ["close", "volume"], "func": seas_399_quarter_end_window_dressing_kurt_21d},
    "seas_400_quarter_end_window_dressing_skew_63d": {"inputs": ["close", "volume"], "func": seas_400_quarter_end_window_dressing_skew_63d},
    "seas_401_quarter_end_window_dressing_kurt_63d": {"inputs": ["close", "volume"], "func": seas_401_quarter_end_window_dressing_kurt_63d},
    "seas_402_quarter_end_window_dressing_skew_126d": {"inputs": ["close", "volume"], "func": seas_402_quarter_end_window_dressing_skew_126d},
    "seas_403_quarter_end_window_dressing_kurt_126d": {"inputs": ["close", "volume"], "func": seas_403_quarter_end_window_dressing_kurt_126d},
    "seas_404_quarter_end_window_dressing_skew_252d": {"inputs": ["close", "volume"], "func": seas_404_quarter_end_window_dressing_skew_252d},
    "seas_405_quarter_end_window_dressing_kurt_252d": {"inputs": ["close", "volume"], "func": seas_405_quarter_end_window_dressing_kurt_252d},
    "seas_406_seasonal_volatility_skew_5d": {"inputs": ["close", "volume"], "func": seas_406_seasonal_volatility_skew_5d},
    "seas_407_seasonal_volatility_kurt_5d": {"inputs": ["close", "volume"], "func": seas_407_seasonal_volatility_kurt_5d},
    "seas_408_seasonal_volatility_skew_21d": {"inputs": ["close", "volume"], "func": seas_408_seasonal_volatility_skew_21d},
    "seas_409_seasonal_volatility_kurt_21d": {"inputs": ["close", "volume"], "func": seas_409_seasonal_volatility_kurt_21d},
    "seas_410_seasonal_volatility_skew_63d": {"inputs": ["close", "volume"], "func": seas_410_seasonal_volatility_skew_63d},
    "seas_411_seasonal_volatility_kurt_63d": {"inputs": ["close", "volume"], "func": seas_411_seasonal_volatility_kurt_63d},
    "seas_412_seasonal_volatility_skew_126d": {"inputs": ["close", "volume"], "func": seas_412_seasonal_volatility_skew_126d},
    "seas_413_seasonal_volatility_kurt_126d": {"inputs": ["close", "volume"], "func": seas_413_seasonal_volatility_kurt_126d},
    "seas_414_seasonal_volatility_skew_252d": {"inputs": ["close", "volume"], "func": seas_414_seasonal_volatility_skew_252d},
    "seas_415_seasonal_volatility_kurt_252d": {"inputs": ["close", "volume"], "func": seas_415_seasonal_volatility_kurt_252d},
    "seas_416_month_of_year_returns_skew_5d": {"inputs": ["close", "volume"], "func": seas_416_month_of_year_returns_skew_5d},
    "seas_417_month_of_year_returns_kurt_5d": {"inputs": ["close", "volume"], "func": seas_417_month_of_year_returns_kurt_5d},
    "seas_418_month_of_year_returns_skew_21d": {"inputs": ["close", "volume"], "func": seas_418_month_of_year_returns_skew_21d},
    "seas_419_month_of_year_returns_kurt_21d": {"inputs": ["close", "volume"], "func": seas_419_month_of_year_returns_kurt_21d},
    "seas_420_month_of_year_returns_skew_63d": {"inputs": ["close", "volume"], "func": seas_420_month_of_year_returns_skew_63d},
    "seas_421_month_of_year_returns_kurt_63d": {"inputs": ["close", "volume"], "func": seas_421_month_of_year_returns_kurt_63d},
    "seas_422_month_of_year_returns_skew_126d": {"inputs": ["close", "volume"], "func": seas_422_month_of_year_returns_skew_126d},
    "seas_423_month_of_year_returns_kurt_126d": {"inputs": ["close", "volume"], "func": seas_423_month_of_year_returns_kurt_126d},
    "seas_424_month_of_year_returns_skew_252d": {"inputs": ["close", "volume"], "func": seas_424_month_of_year_returns_skew_252d},
    "seas_425_month_of_year_returns_kurt_252d": {"inputs": ["close", "volume"], "func": seas_425_month_of_year_returns_kurt_252d},
    "seas_426_seasonal_drawdown_skew_5d": {"inputs": ["close", "volume"], "func": seas_426_seasonal_drawdown_skew_5d},
    "seas_427_seasonal_drawdown_kurt_5d": {"inputs": ["close", "volume"], "func": seas_427_seasonal_drawdown_kurt_5d},
    "seas_428_seasonal_drawdown_skew_21d": {"inputs": ["close", "volume"], "func": seas_428_seasonal_drawdown_skew_21d},
    "seas_429_seasonal_drawdown_kurt_21d": {"inputs": ["close", "volume"], "func": seas_429_seasonal_drawdown_kurt_21d},
    "seas_430_seasonal_drawdown_skew_63d": {"inputs": ["close", "volume"], "func": seas_430_seasonal_drawdown_skew_63d},
    "seas_431_seasonal_drawdown_kurt_63d": {"inputs": ["close", "volume"], "func": seas_431_seasonal_drawdown_kurt_63d},
    "seas_432_seasonal_drawdown_skew_126d": {"inputs": ["close", "volume"], "func": seas_432_seasonal_drawdown_skew_126d},
    "seas_433_seasonal_drawdown_kurt_126d": {"inputs": ["close", "volume"], "func": seas_433_seasonal_drawdown_kurt_126d},
    "seas_434_seasonal_drawdown_skew_252d": {"inputs": ["close", "volume"], "func": seas_434_seasonal_drawdown_skew_252d},
    "seas_435_seasonal_drawdown_kurt_252d": {"inputs": ["close", "volume"], "func": seas_435_seasonal_drawdown_kurt_252d},
    "seas_436_monthly_momentum_skew_5d": {"inputs": ["close", "volume"], "func": seas_436_monthly_momentum_skew_5d},
    "seas_437_monthly_momentum_kurt_5d": {"inputs": ["close", "volume"], "func": seas_437_monthly_momentum_kurt_5d},
    "seas_438_monthly_momentum_skew_21d": {"inputs": ["close", "volume"], "func": seas_438_monthly_momentum_skew_21d},
    "seas_439_monthly_momentum_kurt_21d": {"inputs": ["close", "volume"], "func": seas_439_monthly_momentum_kurt_21d},
    "seas_440_monthly_momentum_skew_63d": {"inputs": ["close", "volume"], "func": seas_440_monthly_momentum_skew_63d},
    "seas_441_monthly_momentum_kurt_63d": {"inputs": ["close", "volume"], "func": seas_441_monthly_momentum_kurt_63d},
    "seas_442_monthly_momentum_skew_126d": {"inputs": ["close", "volume"], "func": seas_442_monthly_momentum_skew_126d},
    "seas_443_monthly_momentum_kurt_126d": {"inputs": ["close", "volume"], "func": seas_443_monthly_momentum_kurt_126d},
    "seas_444_monthly_momentum_skew_252d": {"inputs": ["close", "volume"], "func": seas_444_monthly_momentum_skew_252d},
    "seas_445_monthly_momentum_kurt_252d": {"inputs": ["close", "volume"], "func": seas_445_monthly_momentum_kurt_252d},
    "seas_446_september_distress_skew_5d": {"inputs": ["close", "volume"], "func": seas_446_september_distress_skew_5d},
    "seas_447_september_distress_kurt_5d": {"inputs": ["close", "volume"], "func": seas_447_september_distress_kurt_5d},
    "seas_448_september_distress_skew_21d": {"inputs": ["close", "volume"], "func": seas_448_september_distress_skew_21d},
    "seas_449_september_distress_kurt_21d": {"inputs": ["close", "volume"], "func": seas_449_september_distress_kurt_21d},
    "seas_450_september_distress_skew_63d": {"inputs": ["close", "volume"], "func": seas_450_september_distress_skew_63d},
    "seas_451_september_distress_kurt_63d": {"inputs": ["close", "volume"], "func": seas_451_september_distress_kurt_63d},
    "seas_452_september_distress_skew_126d": {"inputs": ["close", "volume"], "func": seas_452_september_distress_skew_126d},
    "seas_453_september_distress_kurt_126d": {"inputs": ["close", "volume"], "func": seas_453_september_distress_kurt_126d},
    "seas_454_september_distress_skew_252d": {"inputs": ["close", "volume"], "func": seas_454_september_distress_skew_252d},
    "seas_455_september_distress_kurt_252d": {"inputs": ["close", "volume"], "func": seas_455_september_distress_kurt_252d},
    "seas_456_may_sell_signal_skew_5d": {"inputs": ["close", "volume"], "func": seas_456_may_sell_signal_skew_5d},
    "seas_457_may_sell_signal_kurt_5d": {"inputs": ["close", "volume"], "func": seas_457_may_sell_signal_kurt_5d},
    "seas_458_may_sell_signal_skew_21d": {"inputs": ["close", "volume"], "func": seas_458_may_sell_signal_skew_21d},
    "seas_459_may_sell_signal_kurt_21d": {"inputs": ["close", "volume"], "func": seas_459_may_sell_signal_kurt_21d},
    "seas_460_may_sell_signal_skew_63d": {"inputs": ["close", "volume"], "func": seas_460_may_sell_signal_skew_63d},
    "seas_461_may_sell_signal_kurt_63d": {"inputs": ["close", "volume"], "func": seas_461_may_sell_signal_kurt_63d},
    "seas_462_may_sell_signal_skew_126d": {"inputs": ["close", "volume"], "func": seas_462_may_sell_signal_skew_126d},
    "seas_463_may_sell_signal_kurt_126d": {"inputs": ["close", "volume"], "func": seas_463_may_sell_signal_kurt_126d},
    "seas_464_may_sell_signal_skew_252d": {"inputs": ["close", "volume"], "func": seas_464_may_sell_signal_skew_252d},
    "seas_465_may_sell_signal_kurt_252d": {"inputs": ["close", "volume"], "func": seas_465_may_sell_signal_kurt_252d},
    "seas_466_quarterly_seasonality_skew_5d": {"inputs": ["close", "volume"], "func": seas_466_quarterly_seasonality_skew_5d},
    "seas_467_quarterly_seasonality_kurt_5d": {"inputs": ["close", "volume"], "func": seas_467_quarterly_seasonality_kurt_5d},
    "seas_468_quarterly_seasonality_skew_21d": {"inputs": ["close", "volume"], "func": seas_468_quarterly_seasonality_skew_21d},
    "seas_469_quarterly_seasonality_kurt_21d": {"inputs": ["close", "volume"], "func": seas_469_quarterly_seasonality_kurt_21d},
    "seas_470_quarterly_seasonality_skew_63d": {"inputs": ["close", "volume"], "func": seas_470_quarterly_seasonality_skew_63d},
    "seas_471_quarterly_seasonality_kurt_63d": {"inputs": ["close", "volume"], "func": seas_471_quarterly_seasonality_kurt_63d},
    "seas_472_quarterly_seasonality_skew_126d": {"inputs": ["close", "volume"], "func": seas_472_quarterly_seasonality_skew_126d},
    "seas_473_quarterly_seasonality_kurt_126d": {"inputs": ["close", "volume"], "func": seas_473_quarterly_seasonality_kurt_126d},
    "seas_474_quarterly_seasonality_skew_252d": {"inputs": ["close", "volume"], "func": seas_474_quarterly_seasonality_skew_252d},
    "seas_475_quarterly_seasonality_kurt_252d": {"inputs": ["close", "volume"], "func": seas_475_quarterly_seasonality_kurt_252d},
    "seas_476_seasonal_zscore_skew_5d": {"inputs": ["close", "volume"], "func": seas_476_seasonal_zscore_skew_5d},
    "seas_477_seasonal_zscore_kurt_5d": {"inputs": ["close", "volume"], "func": seas_477_seasonal_zscore_kurt_5d},
    "seas_478_seasonal_zscore_skew_21d": {"inputs": ["close", "volume"], "func": seas_478_seasonal_zscore_skew_21d},
    "seas_479_seasonal_zscore_kurt_21d": {"inputs": ["close", "volume"], "func": seas_479_seasonal_zscore_kurt_21d},
    "seas_480_seasonal_zscore_skew_63d": {"inputs": ["close", "volume"], "func": seas_480_seasonal_zscore_skew_63d},
    "seas_481_seasonal_zscore_kurt_63d": {"inputs": ["close", "volume"], "func": seas_481_seasonal_zscore_kurt_63d},
    "seas_482_seasonal_zscore_skew_126d": {"inputs": ["close", "volume"], "func": seas_482_seasonal_zscore_skew_126d},
    "seas_483_seasonal_zscore_kurt_126d": {"inputs": ["close", "volume"], "func": seas_483_seasonal_zscore_kurt_126d},
    "seas_484_seasonal_zscore_skew_252d": {"inputs": ["close", "volume"], "func": seas_484_seasonal_zscore_skew_252d},
    "seas_485_seasonal_zscore_kurt_252d": {"inputs": ["close", "volume"], "func": seas_485_seasonal_zscore_kurt_252d},
    "seas_486_holiday_liquidity_drain_skew_5d": {"inputs": ["close", "volume"], "func": seas_486_holiday_liquidity_drain_skew_5d},
    "seas_487_holiday_liquidity_drain_kurt_5d": {"inputs": ["close", "volume"], "func": seas_487_holiday_liquidity_drain_kurt_5d},
    "seas_488_holiday_liquidity_drain_skew_21d": {"inputs": ["close", "volume"], "func": seas_488_holiday_liquidity_drain_skew_21d},
    "seas_489_holiday_liquidity_drain_kurt_21d": {"inputs": ["close", "volume"], "func": seas_489_holiday_liquidity_drain_kurt_21d},
    "seas_490_holiday_liquidity_drain_skew_63d": {"inputs": ["close", "volume"], "func": seas_490_holiday_liquidity_drain_skew_63d},
    "seas_491_holiday_liquidity_drain_kurt_63d": {"inputs": ["close", "volume"], "func": seas_491_holiday_liquidity_drain_kurt_63d},
    "seas_492_holiday_liquidity_drain_skew_126d": {"inputs": ["close", "volume"], "func": seas_492_holiday_liquidity_drain_skew_126d},
    "seas_493_holiday_liquidity_drain_kurt_126d": {"inputs": ["close", "volume"], "func": seas_493_holiday_liquidity_drain_kurt_126d},
    "seas_494_holiday_liquidity_drain_skew_252d": {"inputs": ["close", "volume"], "func": seas_494_holiday_liquidity_drain_skew_252d},
    "seas_495_holiday_liquidity_drain_kurt_252d": {"inputs": ["close", "volume"], "func": seas_495_holiday_liquidity_drain_kurt_252d},
    "seas_496_seasonal_trend_strength_skew_5d": {"inputs": ["close", "volume"], "func": seas_496_seasonal_trend_strength_skew_5d},
    "seas_497_seasonal_trend_strength_kurt_5d": {"inputs": ["close", "volume"], "func": seas_497_seasonal_trend_strength_kurt_5d},
    "seas_498_seasonal_trend_strength_skew_21d": {"inputs": ["close", "volume"], "func": seas_498_seasonal_trend_strength_skew_21d},
    "seas_499_seasonal_trend_strength_kurt_21d": {"inputs": ["close", "volume"], "func": seas_499_seasonal_trend_strength_kurt_21d},
    "seas_500_seasonal_trend_strength_skew_63d": {"inputs": ["close", "volume"], "func": seas_500_seasonal_trend_strength_skew_63d},
    "seas_501_seasonal_trend_strength_kurt_63d": {"inputs": ["close", "volume"], "func": seas_501_seasonal_trend_strength_kurt_63d},
    "seas_502_seasonal_trend_strength_skew_126d": {"inputs": ["close", "volume"], "func": seas_502_seasonal_trend_strength_skew_126d},
    "seas_503_seasonal_trend_strength_kurt_126d": {"inputs": ["close", "volume"], "func": seas_503_seasonal_trend_strength_kurt_126d},
    "seas_504_seasonal_trend_strength_skew_252d": {"inputs": ["close", "volume"], "func": seas_504_seasonal_trend_strength_skew_252d},
    "seas_505_seasonal_trend_strength_kurt_252d": {"inputs": ["close", "volume"], "func": seas_505_seasonal_trend_strength_kurt_252d},
    "seas_506_periodic_reversal_skew_5d": {"inputs": ["close", "volume"], "func": seas_506_periodic_reversal_skew_5d},
    "seas_507_periodic_reversal_kurt_5d": {"inputs": ["close", "volume"], "func": seas_507_periodic_reversal_kurt_5d},
    "seas_508_periodic_reversal_skew_21d": {"inputs": ["close", "volume"], "func": seas_508_periodic_reversal_skew_21d},
    "seas_509_periodic_reversal_kurt_21d": {"inputs": ["close", "volume"], "func": seas_509_periodic_reversal_kurt_21d},
    "seas_510_periodic_reversal_skew_63d": {"inputs": ["close", "volume"], "func": seas_510_periodic_reversal_skew_63d},
    "seas_511_periodic_reversal_kurt_63d": {"inputs": ["close", "volume"], "func": seas_511_periodic_reversal_kurt_63d},
    "seas_512_periodic_reversal_skew_126d": {"inputs": ["close", "volume"], "func": seas_512_periodic_reversal_skew_126d},
    "seas_513_periodic_reversal_kurt_126d": {"inputs": ["close", "volume"], "func": seas_513_periodic_reversal_kurt_126d},
    "seas_514_periodic_reversal_skew_252d": {"inputs": ["close", "volume"], "func": seas_514_periodic_reversal_skew_252d},
    "seas_515_periodic_reversal_kurt_252d": {"inputs": ["close", "volume"], "func": seas_515_periodic_reversal_kurt_252d},
    "seas_516_cycle_position_skew_5d": {"inputs": ["close", "volume"], "func": seas_516_cycle_position_skew_5d},
    "seas_517_cycle_position_kurt_5d": {"inputs": ["close", "volume"], "func": seas_517_cycle_position_kurt_5d},
    "seas_518_cycle_position_skew_21d": {"inputs": ["close", "volume"], "func": seas_518_cycle_position_skew_21d},
    "seas_519_cycle_position_kurt_21d": {"inputs": ["close", "volume"], "func": seas_519_cycle_position_kurt_21d},
    "seas_520_cycle_position_skew_63d": {"inputs": ["close", "volume"], "func": seas_520_cycle_position_skew_63d},
    "seas_521_cycle_position_kurt_63d": {"inputs": ["close", "volume"], "func": seas_521_cycle_position_kurt_63d},
    "seas_522_cycle_position_skew_126d": {"inputs": ["close", "volume"], "func": seas_522_cycle_position_skew_126d},
    "seas_523_cycle_position_kurt_126d": {"inputs": ["close", "volume"], "func": seas_523_cycle_position_kurt_126d},
    "seas_524_cycle_position_skew_252d": {"inputs": ["close", "volume"], "func": seas_524_cycle_position_skew_252d},
    "seas_525_cycle_position_kurt_252d": {"inputs": ["close", "volume"], "func": seas_525_cycle_position_kurt_252d},
}
