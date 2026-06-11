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


def f31_cash_flow_acceleration_fcf_w5_v076_signal(fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_ncfo_ratio_w10_v077_signal(fcf, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_revenue_ratio_w21_v078_signal(fcf, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_capex_ratio_w42_v079_signal(fcf, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_ncfi_ratio_w63_v080_signal(fcf, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_ncff_ratio_w126_v081_signal(fcf, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_fcf_ratio_w252_v082_signal(ncfo, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_w504_v083_signal(ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_revenue_ratio_w756_v084_signal(ncfo, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_capex_ratio_w5_v085_signal(ncfo, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_w10_v086_signal(ncfo, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_ncff_ratio_w21_v087_signal(ncfo, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_fcf_ratio_w42_v088_signal(revenue, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_ncfo_ratio_w63_v089_signal(revenue, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_w126_v090_signal(revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_capex_ratio_w252_v091_signal(revenue, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_ncfi_ratio_w504_v092_signal(revenue, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_ncff_ratio_w756_v093_signal(revenue, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_fcf_ratio_w5_v094_signal(capex, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_ncfo_ratio_w10_v095_signal(capex, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_revenue_ratio_w21_v096_signal(capex, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_w42_v097_signal(capex) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_ncfi_ratio_w63_v098_signal(capex, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_ncff_ratio_w126_v099_signal(capex, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_fcf_ratio_w252_v100_signal(ncfi, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_w504_v101_signal(ncfi, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_revenue_ratio_w756_v102_signal(ncfi, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_capex_ratio_w5_v103_signal(ncfi, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_w10_v104_signal(ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_ncff_ratio_w21_v105_signal(ncfi, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_fcf_ratio_w42_v106_signal(ncff, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_ncfo_ratio_w63_v107_signal(ncff, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_revenue_ratio_w126_v108_signal(ncff, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_capex_ratio_w252_v109_signal(ncff, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_ncfi_ratio_w504_v110_signal(ncff, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_w756_v111_signal(ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_w5_v112_signal(fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_ncfo_ratio_w10_v113_signal(fcf, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_revenue_ratio_w21_v114_signal(fcf, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_capex_ratio_w42_v115_signal(fcf, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_ncfi_ratio_w63_v116_signal(fcf, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_ncff_ratio_w126_v117_signal(fcf, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_fcf_ratio_w252_v118_signal(ncfo, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_w504_v119_signal(ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_revenue_ratio_w756_v120_signal(ncfo, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_capex_ratio_w5_v121_signal(ncfo, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_ncfi_ratio_w10_v122_signal(ncfo, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfo_ncff_ratio_w21_v123_signal(ncfo, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_fcf_ratio_w42_v124_signal(revenue, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_ncfo_ratio_w63_v125_signal(revenue, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_w126_v126_signal(revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_capex_ratio_w252_v127_signal(revenue, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_ncfi_ratio_w504_v128_signal(revenue, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_revenue_ncff_ratio_w756_v129_signal(revenue, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_fcf_ratio_w5_v130_signal(capex, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_ncfo_ratio_w10_v131_signal(capex, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_revenue_ratio_w21_v132_signal(capex, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_w42_v133_signal(capex) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_ncfi_ratio_w63_v134_signal(capex, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_capex_ncff_ratio_w126_v135_signal(capex, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_fcf_ratio_w252_v136_signal(ncfi, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_ncfo_ratio_w504_v137_signal(ncfi, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_revenue_ratio_w756_v138_signal(ncfi, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_capex_ratio_w5_v139_signal(ncfi, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_w10_v140_signal(ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_ncfi_ncff_ratio_w21_v141_signal(ncfi, ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_fcf_ratio_w42_v142_signal(ncff, fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_ncfo_ratio_w63_v143_signal(ncff, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_revenue_ratio_w126_v144_signal(ncff, revenue) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_capex_ratio_w252_v145_signal(ncff, capex) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_ncfi_ratio_w504_v146_signal(ncff, ncfi) -> pd.Series:
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

def f31_cash_flow_acceleration_ncff_w756_v147_signal(ncff) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_w5_v148_signal(fcf) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_ncfo_ratio_w10_v149_signal(fcf, ncfo) -> pd.Series:
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

def f31_cash_flow_acceleration_fcf_revenue_ratio_w21_v150_signal(fcf, revenue) -> pd.Series:
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
    print(f"Testing {len(funcs)} functions for f31_cash_flow_acceleration\f31_cash_flow_acceleration_base_076_150_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f31_cash_flow_acceleration_'))]}
F31_CASH_FLOW_ACCELERATION_REGISTRY_BASE_76_150 = REGISTRY
