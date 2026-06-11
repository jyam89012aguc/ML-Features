import pandas as pd
import numpy as np
import inspect

def _sma(s, w):
    """Simple Moving Average with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()

def _std(s, w):
    """Standard Deviation with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _zscore(s, w):
    """Z-Score calculation."""
    sma = _sma(s, w)
    std = _std(s, w)
    return (s - sma) / std.replace(0, np.nan)

def _ratio(num, den):
    """Ratio of two series with zero handling."""
    return num / den.replace(0, np.nan)

def _growth(s, w):
    """Percentage change over w periods."""
    return s.pct_change(w)

def _accel(s, w1, w2):
    """Acceleration: growth of growth."""
    return _growth(_growth(s, w1), w2)

def _slope(s, w):
    """Slope: difference normalized by absolute value."""
    return s.diff(w) / s.abs().replace(0, np.nan)

def _jerk(s, w):
    """Jerk: change in slope or third derivative proxy."""
    return s.diff(w)


def f32_leverage_acceleration_debt_slope_w5_s10_v001_signal(debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: debt smoothed over 5 days, slope over 10 days.
    Captures the rate of change of the smoothed debt series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 5
    base_smoothed_val = _sma(debt, 5)
    # Step 2: Calculate the slope of the smoothed series over 10 periods
    calculated_slope = _slope(base_smoothed_val, 10)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f32_leverage_acceleration_debt_assets_ratio_slope_w10_s21_v002_signal(debt, assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to assets smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between debt and assets using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, assets)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_equity_ratio_slope_w21_s42_v003_signal(debt, equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to equity smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between debt and equity using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, equity)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_ebitda_ratio_slope_w42_s63_v004_signal(debt, ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to ebitda smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between debt and ebitda using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, ebitda)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_revenue_ratio_slope_w63_s126_v005_signal(debt, revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to revenue smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between debt and revenue using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, revenue)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_cash_ratio_slope_w126_s252_v006_signal(debt, cash) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to cash smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between debt and cash using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, cash)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_liabilities_ratio_slope_w252_s504_v007_signal(debt, liabilities) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to liabilities smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between debt and liabilities using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, liabilities)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_opinc_ratio_slope_w504_s756_v008_signal(debt, opinc) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to opinc smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between debt and opinc using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, opinc)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_intexp_ratio_slope_w756_s5_v009_signal(debt, intexp) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to intexp smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between debt and intexp using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, intexp)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_currentratio_ratio_slope_w5_s10_v010_signal(debt, currentratio) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of debt to currentratio smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between debt and currentratio using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(debt, currentratio)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_debt_ratio_slope_w10_s21_v011_signal(assets, debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to debt smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between assets and debt using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, debt)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_slope_w21_s42_v012_signal(assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: assets smoothed over 21 days, slope over 42 days.
    Captures the rate of change of the smoothed assets series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 21
    base_smoothed_val = _sma(assets, 21)
    # Step 2: Calculate the slope of the smoothed series over 42 periods
    calculated_slope = _slope(base_smoothed_val, 42)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f32_leverage_acceleration_assets_equity_ratio_slope_w42_s63_v013_signal(assets, equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to equity smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between assets and equity using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, equity)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_ebitda_ratio_slope_w63_s126_v014_signal(assets, ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to ebitda smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between assets and ebitda using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, ebitda)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_revenue_ratio_slope_w126_s252_v015_signal(assets, revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to revenue smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between assets and revenue using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, revenue)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_cash_ratio_slope_w252_s504_v016_signal(assets, cash) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to cash smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between assets and cash using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, cash)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_liabilities_ratio_slope_w504_s756_v017_signal(assets, liabilities) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to liabilities smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between assets and liabilities using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, liabilities)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_opinc_ratio_slope_w756_s5_v018_signal(assets, opinc) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to opinc smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between assets and opinc using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, opinc)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_intexp_ratio_slope_w5_s10_v019_signal(assets, intexp) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to intexp smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between assets and intexp using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, intexp)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_currentratio_ratio_slope_w10_s21_v020_signal(assets, currentratio) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of assets to currentratio smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between assets and currentratio using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(assets, currentratio)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_debt_ratio_slope_w21_s42_v021_signal(equity, debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to debt smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between equity and debt using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, debt)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_assets_ratio_slope_w42_s63_v022_signal(equity, assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to assets smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between equity and assets using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, assets)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_slope_w63_s126_v023_signal(equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: equity smoothed over 63 days, slope over 126 days.
    Captures the rate of change of the smoothed equity series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 63
    base_smoothed_val = _sma(equity, 63)
    # Step 2: Calculate the slope of the smoothed series over 126 periods
    calculated_slope = _slope(base_smoothed_val, 126)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f32_leverage_acceleration_equity_ebitda_ratio_slope_w126_s252_v024_signal(equity, ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to ebitda smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between equity and ebitda using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, ebitda)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_revenue_ratio_slope_w252_s504_v025_signal(equity, revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to revenue smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between equity and revenue using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, revenue)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_cash_ratio_slope_w504_s756_v026_signal(equity, cash) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to cash smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between equity and cash using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, cash)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_liabilities_ratio_slope_w756_s5_v027_signal(equity, liabilities) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to liabilities smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between equity and liabilities using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, liabilities)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_opinc_ratio_slope_w5_s10_v028_signal(equity, opinc) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to opinc smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between equity and opinc using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, opinc)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_intexp_ratio_slope_w10_s21_v029_signal(equity, intexp) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to intexp smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between equity and intexp using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, intexp)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_currentratio_ratio_slope_w21_s42_v030_signal(equity, currentratio) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of equity to currentratio smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between equity and currentratio using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(equity, currentratio)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_debt_ratio_slope_w42_s63_v031_signal(ebitda, debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to debt smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between ebitda and debt using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, debt)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_assets_ratio_slope_w63_s126_v032_signal(ebitda, assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to assets smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between ebitda and assets using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, assets)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_equity_ratio_slope_w126_s252_v033_signal(ebitda, equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to equity smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between ebitda and equity using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, equity)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_slope_w252_s504_v034_signal(ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: ebitda smoothed over 252 days, slope over 504 days.
    Captures the rate of change of the smoothed ebitda series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 252
    base_smoothed_val = _sma(ebitda, 252)
    # Step 2: Calculate the slope of the smoothed series over 504 periods
    calculated_slope = _slope(base_smoothed_val, 504)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f32_leverage_acceleration_ebitda_revenue_ratio_slope_w504_s756_v035_signal(ebitda, revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to revenue smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between ebitda and revenue using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, revenue)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_cash_ratio_slope_w756_s5_v036_signal(ebitda, cash) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to cash smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between ebitda and cash using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, cash)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_liabilities_ratio_slope_w5_s10_v037_signal(ebitda, liabilities) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to liabilities smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between ebitda and liabilities using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, liabilities)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_opinc_ratio_slope_w10_s21_v038_signal(ebitda, opinc) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to opinc smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between ebitda and opinc using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, opinc)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_intexp_ratio_slope_w21_s42_v039_signal(ebitda, intexp) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to intexp smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between ebitda and intexp using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, intexp)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_currentratio_ratio_slope_w42_s63_v040_signal(ebitda, currentratio) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of ebitda to currentratio smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between ebitda and currentratio using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, currentratio)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_debt_ratio_slope_w63_s126_v041_signal(revenue, debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to debt smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between revenue and debt using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, debt)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_assets_ratio_slope_w126_s252_v042_signal(revenue, assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to assets smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between revenue and assets using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, assets)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_equity_ratio_slope_w252_s504_v043_signal(revenue, equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to equity smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between revenue and equity using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, equity)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_ebitda_ratio_slope_w504_s756_v044_signal(revenue, ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to ebitda smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between revenue and ebitda using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ebitda)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_slope_w756_s5_v045_signal(revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: revenue smoothed over 756 days, slope over 5 days.
    Captures the rate of change of the smoothed revenue series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 756
    base_smoothed_val = _sma(revenue, 756)
    # Step 2: Calculate the slope of the smoothed series over 5 periods
    calculated_slope = _slope(base_smoothed_val, 5)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f32_leverage_acceleration_revenue_cash_ratio_slope_w5_s10_v046_signal(revenue, cash) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to cash smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between revenue and cash using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, cash)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_liabilities_ratio_slope_w10_s21_v047_signal(revenue, liabilities) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to liabilities smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between revenue and liabilities using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, liabilities)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_opinc_ratio_slope_w21_s42_v048_signal(revenue, opinc) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to opinc smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between revenue and opinc using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, opinc)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_intexp_ratio_slope_w42_s63_v049_signal(revenue, intexp) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to intexp smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between revenue and intexp using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, intexp)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_currentratio_ratio_slope_w63_s126_v050_signal(revenue, currentratio) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of revenue to currentratio smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between revenue and currentratio using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, currentratio)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_debt_ratio_slope_w126_s252_v051_signal(cash, debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to debt smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between cash and debt using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, debt)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_assets_ratio_slope_w252_s504_v052_signal(cash, assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to assets smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between cash and assets using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, assets)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_equity_ratio_slope_w504_s756_v053_signal(cash, equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to equity smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between cash and equity using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, equity)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_ebitda_ratio_slope_w756_s5_v054_signal(cash, ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to ebitda smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between cash and ebitda using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, ebitda)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_revenue_ratio_slope_w5_s10_v055_signal(cash, revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to revenue smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between cash and revenue using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, revenue)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_slope_w10_s21_v056_signal(cash) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: cash smoothed over 10 days, slope over 21 days.
    Captures the rate of change of the smoothed cash series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 10
    base_smoothed_val = _sma(cash, 10)
    # Step 2: Calculate the slope of the smoothed series over 21 periods
    calculated_slope = _slope(base_smoothed_val, 21)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f32_leverage_acceleration_cash_liabilities_ratio_slope_w21_s42_v057_signal(cash, liabilities) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to liabilities smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between cash and liabilities using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, liabilities)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_opinc_ratio_slope_w42_s63_v058_signal(cash, opinc) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to opinc smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between cash and opinc using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, opinc)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_intexp_ratio_slope_w63_s126_v059_signal(cash, intexp) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to intexp smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between cash and intexp using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, intexp)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_currentratio_ratio_slope_w126_s252_v060_signal(cash, currentratio) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of cash to currentratio smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between cash and currentratio using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(cash, currentratio)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_debt_ratio_slope_w252_s504_v061_signal(liabilities, debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to debt smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between liabilities and debt using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, debt)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_assets_ratio_slope_w504_s756_v062_signal(liabilities, assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to assets smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between liabilities and assets using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, assets)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_equity_ratio_slope_w756_s5_v063_signal(liabilities, equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to equity smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between liabilities and equity using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, equity)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_ebitda_ratio_slope_w5_s10_v064_signal(liabilities, ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to ebitda smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between liabilities and ebitda using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, ebitda)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_revenue_ratio_slope_w10_s21_v065_signal(liabilities, revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to revenue smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between liabilities and revenue using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, revenue)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_cash_ratio_slope_w21_s42_v066_signal(liabilities, cash) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to cash smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between liabilities and cash using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, cash)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_slope_w42_s63_v067_signal(liabilities) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: liabilities smoothed over 42 days, slope over 63 days.
    Captures the rate of change of the smoothed liabilities series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 42
    base_smoothed_val = _sma(liabilities, 42)
    # Step 2: Calculate the slope of the smoothed series over 63 periods
    calculated_slope = _slope(base_smoothed_val, 63)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f32_leverage_acceleration_liabilities_opinc_ratio_slope_w63_s126_v068_signal(liabilities, opinc) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to opinc smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between liabilities and opinc using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, opinc)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_intexp_ratio_slope_w126_s252_v069_signal(liabilities, intexp) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to intexp smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between liabilities and intexp using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, intexp)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_currentratio_ratio_slope_w252_s504_v070_signal(liabilities, currentratio) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of liabilities to currentratio smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between liabilities and currentratio using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(liabilities, currentratio)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_debt_ratio_slope_w504_s756_v071_signal(opinc, debt) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of opinc to debt smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between opinc and debt using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, debt)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_assets_ratio_slope_w756_s5_v072_signal(opinc, assets) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of opinc to assets smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between opinc and assets using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, assets)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_equity_ratio_slope_w5_s10_v073_signal(opinc, equity) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of opinc to equity smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between opinc and equity using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, equity)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_ebitda_ratio_slope_w10_s21_v074_signal(opinc, ebitda) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of opinc to ebitda smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between opinc and ebitda using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, ebitda)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_revenue_ratio_slope_w21_s42_v075_signal(opinc, revenue) -> pd.Series:
    """
    Slope Signal for f32_leverage_acceleration: Ratio of opinc to revenue smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between opinc and revenue using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, revenue)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['debt', 'assets', 'equity', 'ebitda', 'revenue', 'cash', 'liabilities', 'opinc', 'intexp', 'currentratio']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f32_leverage_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f32_leverage_acceleration\f32_leverage_acceleration_slope_001_150_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f32_leverage_acceleration_'))]}
F32_LEVERAGE_ACCELERATION_REGISTRY_SLOPE_1_150 = REGISTRY
