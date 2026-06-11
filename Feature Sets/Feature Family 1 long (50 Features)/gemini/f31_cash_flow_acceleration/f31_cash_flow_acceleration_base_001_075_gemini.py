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


def f31_cash_flow_acceleration_fcf_w5_v001_signal(fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: fcf smoothed over 5 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 5 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(fcf, 5)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_fcf_ncfo_ratio_w10_v002_signal(fcf, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between fcf and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_revenue_ratio_w21_v003_signal(fcf, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between fcf and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_capex_ratio_w42_v004_signal(fcf, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to capex smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between fcf and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_ncfi_ratio_w63_v005_signal(fcf, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfi smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between fcf and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_ncff_ratio_w126_v006_signal(fcf, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to ncff smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between fcf and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_fcf_ratio_w252_v007_signal(ncfo, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to fcf smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between ncfo and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_w504_v008_signal(ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: ncfo smoothed over 504 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 504 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(ncfo, 504)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_ncfo_revenue_ratio_w756_v009_signal(ncfo, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to revenue smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between ncfo and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_capex_ratio_w5_v010_signal(ncfo, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to capex smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between ncfo and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_w10_v011_signal(ncfo, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncfi smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between ncfo and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_ncff_ratio_w21_v012_signal(ncfo, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncff smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between ncfo and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_fcf_ratio_w42_v013_signal(revenue, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to fcf smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between revenue and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_ncfo_ratio_w63_v014_signal(revenue, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfo smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between revenue and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_w126_v015_signal(revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: revenue smoothed over 126 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 126 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(revenue, 126)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_revenue_capex_ratio_w252_v016_signal(revenue, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to capex smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between revenue and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_ncfi_ratio_w504_v017_signal(revenue, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfi smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between revenue and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_ncff_ratio_w756_v018_signal(revenue, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to ncff smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between revenue and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_fcf_ratio_w5_v019_signal(capex, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to fcf smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between capex and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_ncfo_ratio_w10_v020_signal(capex, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to ncfo smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between capex and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_revenue_ratio_w21_v021_signal(capex, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to revenue smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between capex and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_w42_v022_signal(capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: capex smoothed over 42 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 42 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(capex, 42)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_capex_ncfi_ratio_w63_v023_signal(capex, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to ncfi smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between capex and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_ncff_ratio_w126_v024_signal(capex, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to ncff smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between capex and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_fcf_ratio_w252_v025_signal(ncfi, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to fcf smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between ncfi and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_w504_v026_signal(ncfi, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncfo smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between ncfi and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_revenue_ratio_w756_v027_signal(ncfi, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to revenue smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between ncfi and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_capex_ratio_w5_v028_signal(ncfi, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to capex smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between ncfi and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_w10_v029_signal(ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: ncfi smoothed over 10 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 10 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(ncfi, 10)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_ncfi_ncff_ratio_w21_v030_signal(ncfi, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncff smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between ncfi and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_fcf_ratio_w42_v031_signal(ncff, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to fcf smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between ncff and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_ncfo_ratio_w63_v032_signal(ncff, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfo smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between ncff and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_revenue_ratio_w126_v033_signal(ncff, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to revenue smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between ncff and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_capex_ratio_w252_v034_signal(ncff, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to capex smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between ncff and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_ncfi_ratio_w504_v035_signal(ncff, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfi smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between ncff and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_w756_v036_signal(ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: ncff smoothed over 756 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 756 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(ncff, 756)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_fcf_w5_v037_signal(fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: fcf smoothed over 5 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 5 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(fcf, 5)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_fcf_ncfo_ratio_w10_v038_signal(fcf, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between fcf and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_revenue_ratio_w21_v039_signal(fcf, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between fcf and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_capex_ratio_w42_v040_signal(fcf, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to capex smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between fcf and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_ncfi_ratio_w63_v041_signal(fcf, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfi smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between fcf and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_ncff_ratio_w126_v042_signal(fcf, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to ncff smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between fcf and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_fcf_ratio_w252_v043_signal(ncfo, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to fcf smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between ncfo and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_w504_v044_signal(ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: ncfo smoothed over 504 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 504 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(ncfo, 504)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_ncfo_revenue_ratio_w756_v045_signal(ncfo, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to revenue smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between ncfo and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_capex_ratio_w5_v046_signal(ncfo, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to capex smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between ncfo and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_w10_v047_signal(ncfo, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncfi smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between ncfo and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfo_ncff_ratio_w21_v048_signal(ncfo, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfo to ncff smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between ncfo and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfo, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_fcf_ratio_w42_v049_signal(revenue, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to fcf smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between revenue and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_ncfo_ratio_w63_v050_signal(revenue, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfo smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between revenue and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_w126_v051_signal(revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: revenue smoothed over 126 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 126 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(revenue, 126)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_revenue_capex_ratio_w252_v052_signal(revenue, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to capex smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between revenue and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_ncfi_ratio_w504_v053_signal(revenue, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to ncfi smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between revenue and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_revenue_ncff_ratio_w756_v054_signal(revenue, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of revenue to ncff smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between revenue and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_fcf_ratio_w5_v055_signal(capex, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to fcf smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between capex and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_ncfo_ratio_w10_v056_signal(capex, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to ncfo smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between capex and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_revenue_ratio_w21_v057_signal(capex, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to revenue smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between capex and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_w42_v058_signal(capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: capex smoothed over 42 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 42 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(capex, 42)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_capex_ncfi_ratio_w63_v059_signal(capex, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to ncfi smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between capex and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_capex_ncff_ratio_w126_v060_signal(capex, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of capex to ncff smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between capex and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(capex, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_fcf_ratio_w252_v061_signal(ncfi, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to fcf smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between ncfi and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_w504_v062_signal(ncfi, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncfo smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between ncfi and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_revenue_ratio_w756_v063_signal(ncfi, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to revenue smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between ncfi and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_capex_ratio_w5_v064_signal(ncfi, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to capex smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between ncfi and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncfi_w10_v065_signal(ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: ncfi smoothed over 10 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 10 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(ncfi, 10)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_ncfi_ncff_ratio_w21_v066_signal(ncfi, ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncfi to ncff smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between ncfi and ncff over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncfi, ncff)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_fcf_ratio_w42_v067_signal(ncff, fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to fcf smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between ncff and fcf over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, fcf)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_ncfo_ratio_w63_v068_signal(ncff, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfo smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between ncff and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_revenue_ratio_w126_v069_signal(ncff, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to revenue smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between ncff and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_capex_ratio_w252_v070_signal(ncff, capex) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to capex smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between ncff and capex over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, capex)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_ncfi_ratio_w504_v071_signal(ncff, ncfi) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of ncff to ncfi smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between ncff and ncfi over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ncff, ncfi)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_ncff_w756_v072_signal(ncff) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: ncff smoothed over 756 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 756 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(ncff, 756)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_fcf_w5_v073_signal(fcf) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: fcf smoothed over 5 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 5 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(fcf, 5)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f31_cash_flow_acceleration_fcf_ncfo_ratio_w10_v074_signal(fcf, ncfo) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to ncfo smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between fcf and ncfo over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, ncfo)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f31_cash_flow_acceleration_fcf_revenue_ratio_w21_v075_signal(fcf, revenue) -> pd.Series:
    """
    Base Signal for f31_cash_flow_acceleration: Ratio of fcf to revenue smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between fcf and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(fcf, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['fcf', 'ncfo', 'revenue', 'capex', 'ncfi', 'ncff']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f31_cash_flow_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f31_cash_flow_acceleration\f31_cash_flow_acceleration_base_001_075_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f31_cash_flow_acceleration_'))]}
F31_CASH_FLOW_ACCELERATION_REGISTRY_BASE_1_75 = REGISTRY
