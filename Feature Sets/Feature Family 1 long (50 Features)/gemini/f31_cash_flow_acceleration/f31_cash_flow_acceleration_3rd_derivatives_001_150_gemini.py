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


def f31_cash_flow_acceleration_fcf_jerk_w5_s10_j21_v001_signal(fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: fcf smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change (acceleration of slope) for fcf.
    """
    # Step 1: Smooth the data for noise reduction using SMA 5
    smoothed_data_input = _sma(fcf, 5)
    # Step 2: Calculate the first derivative proxy (slope over 10 days)
    first_derivative_slope = _slope(smoothed_data_input, 10)
    # Step 3: Calculate the second derivative proxy (jerk over 21 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 21)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncfo_ratio_jerk_w10_s21_j42_v002_signal(fcf, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the fcf/ncfo ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, ncfo)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_revenue_ratio_jerk_w21_s42_j63_v003_signal(fcf, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the fcf/revenue ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, revenue)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_capex_ratio_jerk_w42_s63_j126_v004_signal(fcf, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to capex smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the fcf/capex ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, capex)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncfi_ratio_jerk_w63_s126_j252_v005_signal(fcf, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfi smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the fcf/ncfi ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, ncfi)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncff_ratio_jerk_w126_s252_j504_v006_signal(fcf, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to ncff smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the fcf/ncff ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, ncff)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_fcf_ratio_jerk_w252_s504_j756_v007_signal(ncfo, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to fcf smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the ncfo/fcf ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, fcf)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_jerk_w504_s756_j5_v008_signal(ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: ncfo smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change (acceleration of slope) for ncfo.
    """
    # Step 1: Smooth the data for noise reduction using SMA 504
    smoothed_data_input = _sma(ncfo, 504)
    # Step 2: Calculate the first derivative proxy (slope over 756 days)
    first_derivative_slope = _slope(smoothed_data_input, 756)
    # Step 3: Calculate the second derivative proxy (jerk over 5 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 5)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_revenue_ratio_jerk_w756_s5_j10_v009_signal(ncfo, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to revenue smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the ncfo/revenue ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, revenue)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_capex_ratio_jerk_w5_s10_j21_v010_signal(ncfo, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to capex smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the ncfo/capex ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, capex)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_jerk_w10_s21_j42_v011_signal(ncfo, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncfi smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the ncfo/ncfi ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, ncfi)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncff_ratio_jerk_w21_s42_j63_v012_signal(ncfo, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncff smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the ncfo/ncff ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, ncff)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_fcf_ratio_jerk_w42_s63_j126_v013_signal(revenue, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to fcf smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the revenue/fcf ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, fcf)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfo_ratio_jerk_w63_s126_j252_v014_signal(revenue, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfo smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the revenue/ncfo ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ncfo)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_jerk_w126_s252_j504_v015_signal(revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: revenue smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change (acceleration of slope) for revenue.
    """
    # Step 1: Smooth the data for noise reduction using SMA 126
    smoothed_data_input = _sma(revenue, 126)
    # Step 2: Calculate the first derivative proxy (slope over 252 days)
    first_derivative_slope = _slope(smoothed_data_input, 252)
    # Step 3: Calculate the second derivative proxy (jerk over 504 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 504)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_capex_ratio_jerk_w252_s504_j756_v016_signal(revenue, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to capex smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the revenue/capex ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, capex)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfi_ratio_jerk_w504_s756_j5_v017_signal(revenue, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfi smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the revenue/ncfi ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ncfi)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncff_ratio_jerk_w756_s5_j10_v018_signal(revenue, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to ncff smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the revenue/ncff ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ncff)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_fcf_ratio_jerk_w5_s10_j21_v019_signal(capex, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to fcf smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the capex/fcf ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, fcf)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncfo_ratio_jerk_w10_s21_j42_v020_signal(capex, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to ncfo smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the capex/ncfo ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, ncfo)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_revenue_ratio_jerk_w21_s42_j63_v021_signal(capex, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the capex/revenue ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, revenue)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_jerk_w42_s63_j126_v022_signal(capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: capex smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change (acceleration of slope) for capex.
    """
    # Step 1: Smooth the data for noise reduction using SMA 42
    smoothed_data_input = _sma(capex, 42)
    # Step 2: Calculate the first derivative proxy (slope over 63 days)
    first_derivative_slope = _slope(smoothed_data_input, 63)
    # Step 3: Calculate the second derivative proxy (jerk over 126 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 126)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncfi_ratio_jerk_w63_s126_j252_v023_signal(capex, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to ncfi smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the capex/ncfi ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, ncfi)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncff_ratio_jerk_w126_s252_j504_v024_signal(capex, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to ncff smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the capex/ncff ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, ncff)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_fcf_ratio_jerk_w252_s504_j756_v025_signal(ncfi, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to fcf smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the ncfi/fcf ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, fcf)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_jerk_w504_s756_j5_v026_signal(ncfi, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncfo smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the ncfi/ncfo ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, ncfo)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_revenue_ratio_jerk_w756_s5_j10_v027_signal(ncfi, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to revenue smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the ncfi/revenue ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, revenue)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_capex_ratio_jerk_w5_s10_j21_v028_signal(ncfi, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to capex smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the ncfi/capex ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, capex)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_jerk_w10_s21_j42_v029_signal(ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: ncfi smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change (acceleration of slope) for ncfi.
    """
    # Step 1: Smooth the data for noise reduction using SMA 10
    smoothed_data_input = _sma(ncfi, 10)
    # Step 2: Calculate the first derivative proxy (slope over 21 days)
    first_derivative_slope = _slope(smoothed_data_input, 21)
    # Step 3: Calculate the second derivative proxy (jerk over 42 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 42)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_ncff_ratio_jerk_w21_s42_j63_v030_signal(ncfi, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncff smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the ncfi/ncff ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, ncff)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_fcf_ratio_jerk_w42_s63_j126_v031_signal(ncff, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to fcf smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the ncff/fcf ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, fcf)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfo_ratio_jerk_w63_s126_j252_v032_signal(ncff, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfo smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the ncff/ncfo ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, ncfo)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_revenue_ratio_jerk_w126_s252_j504_v033_signal(ncff, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to revenue smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the ncff/revenue ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, revenue)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_capex_ratio_jerk_w252_s504_j756_v034_signal(ncff, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to capex smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the ncff/capex ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, capex)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfi_ratio_jerk_w504_s756_j5_v035_signal(ncff, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfi smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the ncff/ncfi ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, ncfi)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_jerk_w756_s5_j10_v036_signal(ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: ncff smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change (acceleration of slope) for ncff.
    """
    # Step 1: Smooth the data for noise reduction using SMA 756
    smoothed_data_input = _sma(ncff, 756)
    # Step 2: Calculate the first derivative proxy (slope over 5 days)
    first_derivative_slope = _slope(smoothed_data_input, 5)
    # Step 3: Calculate the second derivative proxy (jerk over 10 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 10)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_jerk_w5_s10_j21_v037_signal(fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: fcf smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change (acceleration of slope) for fcf.
    """
    # Step 1: Smooth the data for noise reduction using SMA 5
    smoothed_data_input = _sma(fcf, 5)
    # Step 2: Calculate the first derivative proxy (slope over 10 days)
    first_derivative_slope = _slope(smoothed_data_input, 10)
    # Step 3: Calculate the second derivative proxy (jerk over 21 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 21)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncfo_ratio_jerk_w10_s21_j42_v038_signal(fcf, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the fcf/ncfo ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, ncfo)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_revenue_ratio_jerk_w21_s42_j63_v039_signal(fcf, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the fcf/revenue ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, revenue)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_capex_ratio_jerk_w42_s63_j126_v040_signal(fcf, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to capex smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the fcf/capex ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, capex)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncfi_ratio_jerk_w63_s126_j252_v041_signal(fcf, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfi smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the fcf/ncfi ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, ncfi)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncff_ratio_jerk_w126_s252_j504_v042_signal(fcf, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to ncff smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the fcf/ncff ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, ncff)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_fcf_ratio_jerk_w252_s504_j756_v043_signal(ncfo, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to fcf smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the ncfo/fcf ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, fcf)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_jerk_w504_s756_j5_v044_signal(ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: ncfo smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change (acceleration of slope) for ncfo.
    """
    # Step 1: Smooth the data for noise reduction using SMA 504
    smoothed_data_input = _sma(ncfo, 504)
    # Step 2: Calculate the first derivative proxy (slope over 756 days)
    first_derivative_slope = _slope(smoothed_data_input, 756)
    # Step 3: Calculate the second derivative proxy (jerk over 5 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 5)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_revenue_ratio_jerk_w756_s5_j10_v045_signal(ncfo, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to revenue smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the ncfo/revenue ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, revenue)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_capex_ratio_jerk_w5_s10_j21_v046_signal(ncfo, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to capex smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the ncfo/capex ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, capex)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_jerk_w10_s21_j42_v047_signal(ncfo, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncfi smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the ncfo/ncfi ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, ncfi)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncff_ratio_jerk_w21_s42_j63_v048_signal(ncfo, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncff smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the ncfo/ncff ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfo, ncff)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_fcf_ratio_jerk_w42_s63_j126_v049_signal(revenue, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to fcf smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the revenue/fcf ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, fcf)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfo_ratio_jerk_w63_s126_j252_v050_signal(revenue, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfo smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the revenue/ncfo ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ncfo)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_jerk_w126_s252_j504_v051_signal(revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: revenue smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change (acceleration of slope) for revenue.
    """
    # Step 1: Smooth the data for noise reduction using SMA 126
    smoothed_data_input = _sma(revenue, 126)
    # Step 2: Calculate the first derivative proxy (slope over 252 days)
    first_derivative_slope = _slope(smoothed_data_input, 252)
    # Step 3: Calculate the second derivative proxy (jerk over 504 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 504)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_capex_ratio_jerk_w252_s504_j756_v052_signal(revenue, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to capex smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the revenue/capex ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, capex)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfi_ratio_jerk_w504_s756_j5_v053_signal(revenue, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfi smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the revenue/ncfi ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ncfi)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncff_ratio_jerk_w756_s5_j10_v054_signal(revenue, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of revenue to ncff smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the revenue/ncff ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ncff)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_fcf_ratio_jerk_w5_s10_j21_v055_signal(capex, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to fcf smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the capex/fcf ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, fcf)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncfo_ratio_jerk_w10_s21_j42_v056_signal(capex, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to ncfo smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the capex/ncfo ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, ncfo)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_revenue_ratio_jerk_w21_s42_j63_v057_signal(capex, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the capex/revenue ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, revenue)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_jerk_w42_s63_j126_v058_signal(capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: capex smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change (acceleration of slope) for capex.
    """
    # Step 1: Smooth the data for noise reduction using SMA 42
    smoothed_data_input = _sma(capex, 42)
    # Step 2: Calculate the first derivative proxy (slope over 63 days)
    first_derivative_slope = _slope(smoothed_data_input, 63)
    # Step 3: Calculate the second derivative proxy (jerk over 126 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 126)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncfi_ratio_jerk_w63_s126_j252_v059_signal(capex, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to ncfi smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the capex/ncfi ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, ncfi)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncff_ratio_jerk_w126_s252_j504_v060_signal(capex, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of capex to ncff smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the capex/ncff ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(capex, ncff)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_fcf_ratio_jerk_w252_s504_j756_v061_signal(ncfi, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to fcf smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the ncfi/fcf ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, fcf)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_jerk_w504_s756_j5_v062_signal(ncfi, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncfo smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the ncfi/ncfo ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, ncfo)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_revenue_ratio_jerk_w756_s5_j10_v063_signal(ncfi, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to revenue smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the ncfi/revenue ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, revenue)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_capex_ratio_jerk_w5_s10_j21_v064_signal(ncfi, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to capex smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the ncfi/capex ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, capex)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_jerk_w10_s21_j42_v065_signal(ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: ncfi smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change (acceleration of slope) for ncfi.
    """
    # Step 1: Smooth the data for noise reduction using SMA 10
    smoothed_data_input = _sma(ncfi, 10)
    # Step 2: Calculate the first derivative proxy (slope over 21 days)
    first_derivative_slope = _slope(smoothed_data_input, 21)
    # Step 3: Calculate the second derivative proxy (jerk over 42 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 42)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_ncff_ratio_jerk_w21_s42_j63_v066_signal(ncfi, ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncff smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the ncfi/ncff ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncfi, ncff)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_fcf_ratio_jerk_w42_s63_j126_v067_signal(ncff, fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to fcf smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the ncff/fcf ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, fcf)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfo_ratio_jerk_w63_s126_j252_v068_signal(ncff, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfo smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the ncff/ncfo ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, ncfo)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_revenue_ratio_jerk_w126_s252_j504_v069_signal(ncff, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to revenue smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the ncff/revenue ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, revenue)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_capex_ratio_jerk_w252_s504_j756_v070_signal(ncff, capex) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to capex smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the ncff/capex ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, capex)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfi_ratio_jerk_w504_s756_j5_v071_signal(ncff, ncfi) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfi smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the ncff/ncfi ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ncff, ncfi)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_jerk_w756_s5_j10_v072_signal(ncff) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: ncff smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change (acceleration of slope) for ncff.
    """
    # Step 1: Smooth the data for noise reduction using SMA 756
    smoothed_data_input = _sma(ncff, 756)
    # Step 2: Calculate the first derivative proxy (slope over 5 days)
    first_derivative_slope = _slope(smoothed_data_input, 5)
    # Step 3: Calculate the second derivative proxy (jerk over 10 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 10)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_jerk_w5_s10_j21_v073_signal(fcf) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: fcf smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change (acceleration of slope) for fcf.
    """
    # Step 1: Smooth the data for noise reduction using SMA 5
    smoothed_data_input = _sma(fcf, 5)
    # Step 2: Calculate the first derivative proxy (slope over 10 days)
    first_derivative_slope = _slope(smoothed_data_input, 10)
    # Step 3: Calculate the second derivative proxy (jerk over 21 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 21)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncfo_ratio_jerk_w10_s21_j42_v074_signal(fcf, ncfo) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the fcf/ncfo ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, ncfo)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_revenue_ratio_jerk_w21_s42_j63_v075_signal(fcf, revenue) -> pd.Series:
    """
    Jerk Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the fcf/revenue ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(fcf, revenue)
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
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['fcf', 'ncfo', 'revenue', 'capex', 'ncfi', 'ncff']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f31_cash_flow_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f31_cash_flow_acceleration\f31_cash_flow_acceleration_jerk_001_150_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f31_cash_flow_acceleration_'))]}
F31_CASH_FLOW_ACCELERATION_REGISTRY_JERK_1_150 = REGISTRY
