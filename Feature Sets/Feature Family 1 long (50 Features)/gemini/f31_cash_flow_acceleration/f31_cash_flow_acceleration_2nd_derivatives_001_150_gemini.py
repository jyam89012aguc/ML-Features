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


def f31_cash_flow_acceleration_fcf_slope_w5_s10_v001_signal(fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: fcf smoothed over 5 days, slope over 10 days.
    Captures the rate of change of the smoothed fcf series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 5
    base_smoothed_val = _sma(fcf, 5)
    # Step 2: Calculate the slope of the smoothed series over 10 periods
    calculated_slope = _slope(base_smoothed_val, 10)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_fcf_ncfo_ratio_slope_w10_s21_v002_signal(fcf, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between fcf and ncfo using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, ncfo)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_revenue_ratio_slope_w21_s42_v003_signal(fcf, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between fcf and revenue using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, revenue)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_capex_ratio_slope_w42_s63_v004_signal(fcf, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to capex smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between fcf and capex using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, capex)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncfi_ratio_slope_w63_s126_v005_signal(fcf, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfi smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between fcf and ncfi using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, ncfi)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncff_ratio_slope_w126_s252_v006_signal(fcf, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to ncff smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between fcf and ncff using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, ncff)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_fcf_ratio_slope_w252_s504_v007_signal(ncfo, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to fcf smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between ncfo and fcf using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, fcf)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_slope_w504_s756_v008_signal(ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: ncfo smoothed over 504 days, slope over 756 days.
    Captures the rate of change of the smoothed ncfo series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 504
    base_smoothed_val = _sma(ncfo, 504)
    # Step 2: Calculate the slope of the smoothed series over 756 periods
    calculated_slope = _slope(base_smoothed_val, 756)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_ncfo_revenue_ratio_slope_w756_s5_v009_signal(ncfo, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to revenue smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between ncfo and revenue using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, revenue)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_capex_ratio_slope_w5_s10_v010_signal(ncfo, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to capex smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between ncfo and capex using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, capex)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_slope_w10_s21_v011_signal(ncfo, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncfi smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between ncfo and ncfi using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, ncfi)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncff_ratio_slope_w21_s42_v012_signal(ncfo, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncff smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between ncfo and ncff using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, ncff)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_fcf_ratio_slope_w42_s63_v013_signal(revenue, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to fcf smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between revenue and fcf using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, fcf)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfo_ratio_slope_w63_s126_v014_signal(revenue, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfo smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between revenue and ncfo using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ncfo)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_slope_w126_s252_v015_signal(revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: revenue smoothed over 126 days, slope over 252 days.
    Captures the rate of change of the smoothed revenue series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 126
    base_smoothed_val = _sma(revenue, 126)
    # Step 2: Calculate the slope of the smoothed series over 252 periods
    calculated_slope = _slope(base_smoothed_val, 252)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_revenue_capex_ratio_slope_w252_s504_v016_signal(revenue, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to capex smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between revenue and capex using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, capex)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfi_ratio_slope_w504_s756_v017_signal(revenue, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfi smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between revenue and ncfi using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ncfi)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncff_ratio_slope_w756_s5_v018_signal(revenue, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to ncff smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between revenue and ncff using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ncff)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_fcf_ratio_slope_w5_s10_v019_signal(capex, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to fcf smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between capex and fcf using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, fcf)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncfo_ratio_slope_w10_s21_v020_signal(capex, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to ncfo smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between capex and ncfo using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, ncfo)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_revenue_ratio_slope_w21_s42_v021_signal(capex, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to revenue smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between capex and revenue using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, revenue)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_slope_w42_s63_v022_signal(capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: capex smoothed over 42 days, slope over 63 days.
    Captures the rate of change of the smoothed capex series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 42
    base_smoothed_val = _sma(capex, 42)
    # Step 2: Calculate the slope of the smoothed series over 63 periods
    calculated_slope = _slope(base_smoothed_val, 63)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_capex_ncfi_ratio_slope_w63_s126_v023_signal(capex, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to ncfi smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between capex and ncfi using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, ncfi)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncff_ratio_slope_w126_s252_v024_signal(capex, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to ncff smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between capex and ncff using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, ncff)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_fcf_ratio_slope_w252_s504_v025_signal(ncfi, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to fcf smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between ncfi and fcf using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, fcf)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_slope_w504_s756_v026_signal(ncfi, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncfo smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between ncfi and ncfo using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, ncfo)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_revenue_ratio_slope_w756_s5_v027_signal(ncfi, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to revenue smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between ncfi and revenue using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, revenue)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_capex_ratio_slope_w5_s10_v028_signal(ncfi, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to capex smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between ncfi and capex using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, capex)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_slope_w10_s21_v029_signal(ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: ncfi smoothed over 10 days, slope over 21 days.
    Captures the rate of change of the smoothed ncfi series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 10
    base_smoothed_val = _sma(ncfi, 10)
    # Step 2: Calculate the slope of the smoothed series over 21 periods
    calculated_slope = _slope(base_smoothed_val, 21)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_ncfi_ncff_ratio_slope_w21_s42_v030_signal(ncfi, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncff smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between ncfi and ncff using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, ncff)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_fcf_ratio_slope_w42_s63_v031_signal(ncff, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to fcf smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between ncff and fcf using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, fcf)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfo_ratio_slope_w63_s126_v032_signal(ncff, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfo smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between ncff and ncfo using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, ncfo)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_revenue_ratio_slope_w126_s252_v033_signal(ncff, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to revenue smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between ncff and revenue using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, revenue)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_capex_ratio_slope_w252_s504_v034_signal(ncff, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to capex smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between ncff and capex using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, capex)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfi_ratio_slope_w504_s756_v035_signal(ncff, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfi smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between ncff and ncfi using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, ncfi)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_slope_w756_s5_v036_signal(ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: ncff smoothed over 756 days, slope over 5 days.
    Captures the rate of change of the smoothed ncff series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 756
    base_smoothed_val = _sma(ncff, 756)
    # Step 2: Calculate the slope of the smoothed series over 5 periods
    calculated_slope = _slope(base_smoothed_val, 5)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_fcf_slope_w5_s10_v037_signal(fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: fcf smoothed over 5 days, slope over 10 days.
    Captures the rate of change of the smoothed fcf series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 5
    base_smoothed_val = _sma(fcf, 5)
    # Step 2: Calculate the slope of the smoothed series over 10 periods
    calculated_slope = _slope(base_smoothed_val, 10)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_fcf_ncfo_ratio_slope_w10_s21_v038_signal(fcf, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between fcf and ncfo using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, ncfo)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_revenue_ratio_slope_w21_s42_v039_signal(fcf, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between fcf and revenue using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, revenue)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_capex_ratio_slope_w42_s63_v040_signal(fcf, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to capex smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between fcf and capex using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, capex)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncfi_ratio_slope_w63_s126_v041_signal(fcf, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfi smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between fcf and ncfi using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, ncfi)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_ncff_ratio_slope_w126_s252_v042_signal(fcf, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to ncff smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between fcf and ncff using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, ncff)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_fcf_ratio_slope_w252_s504_v043_signal(ncfo, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to fcf smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between ncfo and fcf using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, fcf)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_slope_w504_s756_v044_signal(ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: ncfo smoothed over 504 days, slope over 756 days.
    Captures the rate of change of the smoothed ncfo series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 504
    base_smoothed_val = _sma(ncfo, 504)
    # Step 2: Calculate the slope of the smoothed series over 756 periods
    calculated_slope = _slope(base_smoothed_val, 756)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_ncfo_revenue_ratio_slope_w756_s5_v045_signal(ncfo, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to revenue smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between ncfo and revenue using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, revenue)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_capex_ratio_slope_w5_s10_v046_signal(ncfo, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to capex smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between ncfo and capex using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, capex)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_slope_w10_s21_v047_signal(ncfo, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncfi smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between ncfo and ncfi using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, ncfi)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfo_ncff_ratio_slope_w21_s42_v048_signal(ncfo, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncff smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between ncfo and ncff using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfo, ncff)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_fcf_ratio_slope_w42_s63_v049_signal(revenue, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to fcf smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between revenue and fcf using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, fcf)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfo_ratio_slope_w63_s126_v050_signal(revenue, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfo smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between revenue and ncfo using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ncfo)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_slope_w126_s252_v051_signal(revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: revenue smoothed over 126 days, slope over 252 days.
    Captures the rate of change of the smoothed revenue series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 126
    base_smoothed_val = _sma(revenue, 126)
    # Step 2: Calculate the slope of the smoothed series over 252 periods
    calculated_slope = _slope(base_smoothed_val, 252)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_revenue_capex_ratio_slope_w252_s504_v052_signal(revenue, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to capex smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between revenue and capex using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, capex)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncfi_ratio_slope_w504_s756_v053_signal(revenue, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfi smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between revenue and ncfi using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ncfi)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_revenue_ncff_ratio_slope_w756_s5_v054_signal(revenue, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of revenue to ncff smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between revenue and ncff using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ncff)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_fcf_ratio_slope_w5_s10_v055_signal(capex, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to fcf smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between capex and fcf using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, fcf)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncfo_ratio_slope_w10_s21_v056_signal(capex, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to ncfo smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between capex and ncfo using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, ncfo)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_revenue_ratio_slope_w21_s42_v057_signal(capex, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to revenue smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between capex and revenue using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, revenue)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_slope_w42_s63_v058_signal(capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: capex smoothed over 42 days, slope over 63 days.
    Captures the rate of change of the smoothed capex series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 42
    base_smoothed_val = _sma(capex, 42)
    # Step 2: Calculate the slope of the smoothed series over 63 periods
    calculated_slope = _slope(base_smoothed_val, 63)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_capex_ncfi_ratio_slope_w63_s126_v059_signal(capex, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to ncfi smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between capex and ncfi using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, ncfi)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_capex_ncff_ratio_slope_w126_s252_v060_signal(capex, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of capex to ncff smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between capex and ncff using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(capex, ncff)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_fcf_ratio_slope_w252_s504_v061_signal(ncfi, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to fcf smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between ncfi and fcf using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, fcf)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_slope_w504_s756_v062_signal(ncfi, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncfo smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between ncfi and ncfo using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, ncfo)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_revenue_ratio_slope_w756_s5_v063_signal(ncfi, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to revenue smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between ncfi and revenue using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, revenue)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_capex_ratio_slope_w5_s10_v064_signal(ncfi, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to capex smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between ncfi and capex using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, capex)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncfi_slope_w10_s21_v065_signal(ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: ncfi smoothed over 10 days, slope over 21 days.
    Captures the rate of change of the smoothed ncfi series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 10
    base_smoothed_val = _sma(ncfi, 10)
    # Step 2: Calculate the slope of the smoothed series over 21 periods
    calculated_slope = _slope(base_smoothed_val, 21)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_ncfi_ncff_ratio_slope_w21_s42_v066_signal(ncfi, ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncff smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between ncfi and ncff using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncfi, ncff)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_fcf_ratio_slope_w42_s63_v067_signal(ncff, fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to fcf smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between ncff and fcf using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, fcf)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfo_ratio_slope_w63_s126_v068_signal(ncff, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfo smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between ncff and ncfo using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, ncfo)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_revenue_ratio_slope_w126_s252_v069_signal(ncff, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to revenue smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between ncff and revenue using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, revenue)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_capex_ratio_slope_w252_s504_v070_signal(ncff, capex) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to capex smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between ncff and capex using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, capex)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_ncfi_ratio_slope_w504_s756_v071_signal(ncff, ncfi) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfi smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between ncff and ncfi using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ncff, ncfi)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_ncff_slope_w756_s5_v072_signal(ncff) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: ncff smoothed over 756 days, slope over 5 days.
    Captures the rate of change of the smoothed ncff series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 756
    base_smoothed_val = _sma(ncff, 756)
    # Step 2: Calculate the slope of the smoothed series over 5 periods
    calculated_slope = _slope(base_smoothed_val, 5)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_fcf_slope_w5_s10_v073_signal(fcf) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: fcf smoothed over 5 days, slope over 10 days.
    Captures the rate of change of the smoothed fcf series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 5
    base_smoothed_val = _sma(fcf, 5)
    # Step 2: Calculate the slope of the smoothed series over 10 periods
    calculated_slope = _slope(base_smoothed_val, 10)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f31_cash_flow_acceleration_fcf_ncfo_ratio_slope_w10_s21_v074_signal(fcf, ncfo) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between fcf and ncfo using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, ncfo)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f31_cash_flow_acceleration_fcf_revenue_ratio_slope_w21_s42_v075_signal(fcf, revenue) -> pd.Series:
    """
    Slope Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between fcf and revenue using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(fcf, revenue)
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
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['fcf', 'ncfo', 'revenue', 'capex', 'ncfi', 'ncff']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f31_cash_flow_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f31_cash_flow_acceleration\f31_cash_flow_acceleration_slope_001_150_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f31_cash_flow_acceleration_'))]}
F31_CASH_FLOW_ACCELERATION_REGISTRY_SLOPE_1_150 = REGISTRY
