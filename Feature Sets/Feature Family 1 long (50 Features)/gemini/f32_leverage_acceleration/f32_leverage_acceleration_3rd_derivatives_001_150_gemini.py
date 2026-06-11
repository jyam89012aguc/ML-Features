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


def f32_leverage_acceleration_debt_jerk_w5_s10_j21_v001_signal(debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: debt smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change (acceleration of slope) for debt.
    """
    # Step 1: Smooth the data for noise reduction using SMA 5
    smoothed_data_input = _sma(debt, 5)
    # Step 2: Calculate the first derivative proxy (slope over 10 days)
    first_derivative_slope = _slope(smoothed_data_input, 10)
    # Step 3: Calculate the second derivative proxy (jerk over 21 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 21)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_assets_ratio_jerk_w10_s21_j42_v002_signal(debt, assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to assets smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the debt/assets ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, assets)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_equity_ratio_jerk_w21_s42_j63_v003_signal(debt, equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to equity smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the debt/equity ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, equity)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_ebitda_ratio_jerk_w42_s63_j126_v004_signal(debt, ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to ebitda smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the debt/ebitda ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, ebitda)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_revenue_ratio_jerk_w63_s126_j252_v005_signal(debt, revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to revenue smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the debt/revenue ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, revenue)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_cash_ratio_jerk_w126_s252_j504_v006_signal(debt, cash) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to cash smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the debt/cash ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, cash)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_liabilities_ratio_jerk_w252_s504_j756_v007_signal(debt, liabilities) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to liabilities smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the debt/liabilities ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, liabilities)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_opinc_ratio_jerk_w504_s756_j5_v008_signal(debt, opinc) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to opinc smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the debt/opinc ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, opinc)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_intexp_ratio_jerk_w756_s5_j10_v009_signal(debt, intexp) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to intexp smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the debt/intexp ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, intexp)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_debt_currentratio_ratio_jerk_w5_s10_j21_v010_signal(debt, currentratio) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of debt to currentratio smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the debt/currentratio ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(debt, currentratio)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_debt_ratio_jerk_w10_s21_j42_v011_signal(assets, debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to debt smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the assets/debt ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, debt)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_jerk_w21_s42_j63_v012_signal(assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: assets smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change (acceleration of slope) for assets.
    """
    # Step 1: Smooth the data for noise reduction using SMA 21
    smoothed_data_input = _sma(assets, 21)
    # Step 2: Calculate the first derivative proxy (slope over 42 days)
    first_derivative_slope = _slope(smoothed_data_input, 42)
    # Step 3: Calculate the second derivative proxy (jerk over 63 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 63)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_equity_ratio_jerk_w42_s63_j126_v013_signal(assets, equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to equity smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the assets/equity ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, equity)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_ebitda_ratio_jerk_w63_s126_j252_v014_signal(assets, ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to ebitda smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the assets/ebitda ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, ebitda)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_revenue_ratio_jerk_w126_s252_j504_v015_signal(assets, revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to revenue smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the assets/revenue ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, revenue)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_cash_ratio_jerk_w252_s504_j756_v016_signal(assets, cash) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to cash smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the assets/cash ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, cash)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_liabilities_ratio_jerk_w504_s756_j5_v017_signal(assets, liabilities) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to liabilities smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the assets/liabilities ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, liabilities)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_opinc_ratio_jerk_w756_s5_j10_v018_signal(assets, opinc) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to opinc smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the assets/opinc ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, opinc)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_intexp_ratio_jerk_w5_s10_j21_v019_signal(assets, intexp) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to intexp smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the assets/intexp ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, intexp)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_assets_currentratio_ratio_jerk_w10_s21_j42_v020_signal(assets, currentratio) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of assets to currentratio smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the assets/currentratio ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(assets, currentratio)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_debt_ratio_jerk_w21_s42_j63_v021_signal(equity, debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to debt smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the equity/debt ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, debt)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_assets_ratio_jerk_w42_s63_j126_v022_signal(equity, assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to assets smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the equity/assets ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, assets)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_jerk_w63_s126_j252_v023_signal(equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: equity smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change (acceleration of slope) for equity.
    """
    # Step 1: Smooth the data for noise reduction using SMA 63
    smoothed_data_input = _sma(equity, 63)
    # Step 2: Calculate the first derivative proxy (slope over 126 days)
    first_derivative_slope = _slope(smoothed_data_input, 126)
    # Step 3: Calculate the second derivative proxy (jerk over 252 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 252)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_ebitda_ratio_jerk_w126_s252_j504_v024_signal(equity, ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to ebitda smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the equity/ebitda ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, ebitda)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_revenue_ratio_jerk_w252_s504_j756_v025_signal(equity, revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to revenue smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the equity/revenue ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, revenue)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_cash_ratio_jerk_w504_s756_j5_v026_signal(equity, cash) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to cash smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the equity/cash ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, cash)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_liabilities_ratio_jerk_w756_s5_j10_v027_signal(equity, liabilities) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to liabilities smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the equity/liabilities ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, liabilities)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_opinc_ratio_jerk_w5_s10_j21_v028_signal(equity, opinc) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to opinc smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the equity/opinc ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, opinc)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_intexp_ratio_jerk_w10_s21_j42_v029_signal(equity, intexp) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to intexp smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the equity/intexp ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, intexp)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_equity_currentratio_ratio_jerk_w21_s42_j63_v030_signal(equity, currentratio) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of equity to currentratio smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the equity/currentratio ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(equity, currentratio)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_debt_ratio_jerk_w42_s63_j126_v031_signal(ebitda, debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to debt smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the ebitda/debt ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, debt)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_assets_ratio_jerk_w63_s126_j252_v032_signal(ebitda, assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to assets smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the ebitda/assets ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, assets)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_equity_ratio_jerk_w126_s252_j504_v033_signal(ebitda, equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to equity smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the ebitda/equity ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, equity)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_jerk_w252_s504_j756_v034_signal(ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: ebitda smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change (acceleration of slope) for ebitda.
    """
    # Step 1: Smooth the data for noise reduction using SMA 252
    smoothed_data_input = _sma(ebitda, 252)
    # Step 2: Calculate the first derivative proxy (slope over 504 days)
    first_derivative_slope = _slope(smoothed_data_input, 504)
    # Step 3: Calculate the second derivative proxy (jerk over 756 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 756)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_revenue_ratio_jerk_w504_s756_j5_v035_signal(ebitda, revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to revenue smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the ebitda/revenue ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, revenue)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_cash_ratio_jerk_w756_s5_j10_v036_signal(ebitda, cash) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to cash smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the ebitda/cash ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, cash)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_liabilities_ratio_jerk_w5_s10_j21_v037_signal(ebitda, liabilities) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to liabilities smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the ebitda/liabilities ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, liabilities)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_opinc_ratio_jerk_w10_s21_j42_v038_signal(ebitda, opinc) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to opinc smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the ebitda/opinc ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, opinc)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_intexp_ratio_jerk_w21_s42_j63_v039_signal(ebitda, intexp) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to intexp smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the ebitda/intexp ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, intexp)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_ebitda_currentratio_ratio_jerk_w42_s63_j126_v040_signal(ebitda, currentratio) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of ebitda to currentratio smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the ebitda/currentratio ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, currentratio)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_debt_ratio_jerk_w63_s126_j252_v041_signal(revenue, debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to debt smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the revenue/debt ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, debt)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_assets_ratio_jerk_w126_s252_j504_v042_signal(revenue, assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to assets smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the revenue/assets ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, assets)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_equity_ratio_jerk_w252_s504_j756_v043_signal(revenue, equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to equity smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the revenue/equity ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, equity)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_ebitda_ratio_jerk_w504_s756_j5_v044_signal(revenue, ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to ebitda smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the revenue/ebitda ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ebitda)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_jerk_w756_s5_j10_v045_signal(revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: revenue smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change (acceleration of slope) for revenue.
    """
    # Step 1: Smooth the data for noise reduction using SMA 756
    smoothed_data_input = _sma(revenue, 756)
    # Step 2: Calculate the first derivative proxy (slope over 5 days)
    first_derivative_slope = _slope(smoothed_data_input, 5)
    # Step 3: Calculate the second derivative proxy (jerk over 10 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 10)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_cash_ratio_jerk_w5_s10_j21_v046_signal(revenue, cash) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to cash smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the revenue/cash ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, cash)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_liabilities_ratio_jerk_w10_s21_j42_v047_signal(revenue, liabilities) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to liabilities smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the revenue/liabilities ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, liabilities)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_opinc_ratio_jerk_w21_s42_j63_v048_signal(revenue, opinc) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to opinc smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the revenue/opinc ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, opinc)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_intexp_ratio_jerk_w42_s63_j126_v049_signal(revenue, intexp) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to intexp smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the revenue/intexp ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, intexp)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_revenue_currentratio_ratio_jerk_w63_s126_j252_v050_signal(revenue, currentratio) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of revenue to currentratio smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the revenue/currentratio ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, currentratio)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_debt_ratio_jerk_w126_s252_j504_v051_signal(cash, debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to debt smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the cash/debt ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, debt)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_assets_ratio_jerk_w252_s504_j756_v052_signal(cash, assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to assets smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the cash/assets ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, assets)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_equity_ratio_jerk_w504_s756_j5_v053_signal(cash, equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to equity smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the cash/equity ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, equity)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_ebitda_ratio_jerk_w756_s5_j10_v054_signal(cash, ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to ebitda smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the cash/ebitda ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, ebitda)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_revenue_ratio_jerk_w5_s10_j21_v055_signal(cash, revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to revenue smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the cash/revenue ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, revenue)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_jerk_w10_s21_j42_v056_signal(cash) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: cash smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change (acceleration of slope) for cash.
    """
    # Step 1: Smooth the data for noise reduction using SMA 10
    smoothed_data_input = _sma(cash, 10)
    # Step 2: Calculate the first derivative proxy (slope over 21 days)
    first_derivative_slope = _slope(smoothed_data_input, 21)
    # Step 3: Calculate the second derivative proxy (jerk over 42 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 42)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_liabilities_ratio_jerk_w21_s42_j63_v057_signal(cash, liabilities) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to liabilities smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the cash/liabilities ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, liabilities)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_opinc_ratio_jerk_w42_s63_j126_v058_signal(cash, opinc) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to opinc smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the cash/opinc ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, opinc)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_intexp_ratio_jerk_w63_s126_j252_v059_signal(cash, intexp) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to intexp smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the cash/intexp ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, intexp)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_cash_currentratio_ratio_jerk_w126_s252_j504_v060_signal(cash, currentratio) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of cash to currentratio smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the cash/currentratio ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(cash, currentratio)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_debt_ratio_jerk_w252_s504_j756_v061_signal(liabilities, debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to debt smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the liabilities/debt ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, debt)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_assets_ratio_jerk_w504_s756_j5_v062_signal(liabilities, assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to assets smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the liabilities/assets ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, assets)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_equity_ratio_jerk_w756_s5_j10_v063_signal(liabilities, equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to equity smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the liabilities/equity ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, equity)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_ebitda_ratio_jerk_w5_s10_j21_v064_signal(liabilities, ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to ebitda smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the liabilities/ebitda ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, ebitda)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_revenue_ratio_jerk_w10_s21_j42_v065_signal(liabilities, revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to revenue smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the liabilities/revenue ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, revenue)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_cash_ratio_jerk_w21_s42_j63_v066_signal(liabilities, cash) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to cash smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the liabilities/cash ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, cash)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_jerk_w42_s63_j126_v067_signal(liabilities) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: liabilities smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change (acceleration of slope) for liabilities.
    """
    # Step 1: Smooth the data for noise reduction using SMA 42
    smoothed_data_input = _sma(liabilities, 42)
    # Step 2: Calculate the first derivative proxy (slope over 63 days)
    first_derivative_slope = _slope(smoothed_data_input, 63)
    # Step 3: Calculate the second derivative proxy (jerk over 126 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 126)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_opinc_ratio_jerk_w63_s126_j252_v068_signal(liabilities, opinc) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to opinc smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the liabilities/opinc ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, opinc)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_intexp_ratio_jerk_w126_s252_j504_v069_signal(liabilities, intexp) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to intexp smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the liabilities/intexp ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, intexp)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_liabilities_currentratio_ratio_jerk_w252_s504_j756_v070_signal(liabilities, currentratio) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of liabilities to currentratio smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the liabilities/currentratio ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(liabilities, currentratio)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_debt_ratio_jerk_w504_s756_j5_v071_signal(opinc, debt) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of opinc to debt smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the opinc/debt ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, debt)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_assets_ratio_jerk_w756_s5_j10_v072_signal(opinc, assets) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of opinc to assets smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the opinc/assets ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, assets)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_equity_ratio_jerk_w5_s10_j21_v073_signal(opinc, equity) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of opinc to equity smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the opinc/equity ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, equity)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_ebitda_ratio_jerk_w10_s21_j42_v074_signal(opinc, ebitda) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of opinc to ebitda smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the opinc/ebitda ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, ebitda)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f32_leverage_acceleration_opinc_revenue_ratio_jerk_w21_s42_j63_v075_signal(opinc, revenue) -> pd.Series:
    """
    Jerk Signal for f32_leverage_acceleration: Ratio of opinc to revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the opinc/revenue ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, revenue)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['debt', 'assets', 'equity', 'ebitda', 'revenue', 'cash', 'liabilities', 'opinc', 'intexp', 'currentratio']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f32_leverage_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f32_leverage_acceleration\f32_leverage_acceleration_jerk_001_150_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f32_leverage_acceleration_'))]}
F32_LEVERAGE_ACCELERATION_REGISTRY_JERK_1_150 = REGISTRY
