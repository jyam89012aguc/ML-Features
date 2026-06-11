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


def f32_leverage_acceleration_debt_w5_v001_signal(debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: debt smoothed over 5 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 5 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(debt, 5)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f32_leverage_acceleration_debt_assets_ratio_w10_v002_signal(debt, assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to assets smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between debt and assets over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, assets)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_equity_ratio_w21_v003_signal(debt, equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to equity smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between debt and equity over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, equity)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_ebitda_ratio_w42_v004_signal(debt, ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to ebitda smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between debt and ebitda over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, ebitda)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_revenue_ratio_w63_v005_signal(debt, revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to revenue smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between debt and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_cash_ratio_w126_v006_signal(debt, cash) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to cash smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between debt and cash over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, cash)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_liabilities_ratio_w252_v007_signal(debt, liabilities) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to liabilities smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between debt and liabilities over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, liabilities)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_opinc_ratio_w504_v008_signal(debt, opinc) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to opinc smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between debt and opinc over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, opinc)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_intexp_ratio_w756_v009_signal(debt, intexp) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to intexp smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between debt and intexp over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, intexp)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_debt_currentratio_ratio_w5_v010_signal(debt, currentratio) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of debt to currentratio smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between debt and currentratio over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(debt, currentratio)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_debt_ratio_w10_v011_signal(assets, debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to debt smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between assets and debt over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, debt)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_w21_v012_signal(assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: assets smoothed over 21 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 21 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(assets, 21)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f32_leverage_acceleration_assets_equity_ratio_w42_v013_signal(assets, equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to equity smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between assets and equity over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, equity)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_ebitda_ratio_w63_v014_signal(assets, ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to ebitda smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between assets and ebitda over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, ebitda)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_revenue_ratio_w126_v015_signal(assets, revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to revenue smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between assets and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_cash_ratio_w252_v016_signal(assets, cash) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to cash smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between assets and cash over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, cash)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_liabilities_ratio_w504_v017_signal(assets, liabilities) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to liabilities smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between assets and liabilities over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, liabilities)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_opinc_ratio_w756_v018_signal(assets, opinc) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to opinc smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between assets and opinc over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, opinc)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_intexp_ratio_w5_v019_signal(assets, intexp) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to intexp smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between assets and intexp over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, intexp)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_assets_currentratio_ratio_w10_v020_signal(assets, currentratio) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of assets to currentratio smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between assets and currentratio over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(assets, currentratio)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_debt_ratio_w21_v021_signal(equity, debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to debt smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between equity and debt over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, debt)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_assets_ratio_w42_v022_signal(equity, assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to assets smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between equity and assets over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, assets)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_w63_v023_signal(equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: equity smoothed over 63 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 63 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(equity, 63)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f32_leverage_acceleration_equity_ebitda_ratio_w126_v024_signal(equity, ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to ebitda smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between equity and ebitda over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, ebitda)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_revenue_ratio_w252_v025_signal(equity, revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to revenue smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between equity and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_cash_ratio_w504_v026_signal(equity, cash) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to cash smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between equity and cash over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, cash)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_liabilities_ratio_w756_v027_signal(equity, liabilities) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to liabilities smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between equity and liabilities over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, liabilities)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_opinc_ratio_w5_v028_signal(equity, opinc) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to opinc smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between equity and opinc over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, opinc)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_intexp_ratio_w10_v029_signal(equity, intexp) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to intexp smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between equity and intexp over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, intexp)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_equity_currentratio_ratio_w21_v030_signal(equity, currentratio) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of equity to currentratio smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between equity and currentratio over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(equity, currentratio)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_debt_ratio_w42_v031_signal(ebitda, debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to debt smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between ebitda and debt over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, debt)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_assets_ratio_w63_v032_signal(ebitda, assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to assets smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between ebitda and assets over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, assets)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_equity_ratio_w126_v033_signal(ebitda, equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to equity smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between ebitda and equity over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, equity)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_w252_v034_signal(ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: ebitda smoothed over 252 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 252 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(ebitda, 252)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f32_leverage_acceleration_ebitda_revenue_ratio_w504_v035_signal(ebitda, revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to revenue smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between ebitda and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_cash_ratio_w756_v036_signal(ebitda, cash) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to cash smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between ebitda and cash over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, cash)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_liabilities_ratio_w5_v037_signal(ebitda, liabilities) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to liabilities smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between ebitda and liabilities over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, liabilities)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_opinc_ratio_w10_v038_signal(ebitda, opinc) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to opinc smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between ebitda and opinc over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, opinc)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_intexp_ratio_w21_v039_signal(ebitda, intexp) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to intexp smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between ebitda and intexp over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, intexp)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_ebitda_currentratio_ratio_w42_v040_signal(ebitda, currentratio) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of ebitda to currentratio smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between ebitda and currentratio over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(ebitda, currentratio)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_debt_ratio_w63_v041_signal(revenue, debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to debt smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between revenue and debt over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, debt)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_assets_ratio_w126_v042_signal(revenue, assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to assets smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between revenue and assets over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, assets)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_equity_ratio_w252_v043_signal(revenue, equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to equity smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between revenue and equity over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, equity)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_ebitda_ratio_w504_v044_signal(revenue, ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to ebitda smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between revenue and ebitda over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, ebitda)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_w756_v045_signal(revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: revenue smoothed over 756 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 756 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(revenue, 756)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f32_leverage_acceleration_revenue_cash_ratio_w5_v046_signal(revenue, cash) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to cash smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between revenue and cash over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, cash)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_liabilities_ratio_w10_v047_signal(revenue, liabilities) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to liabilities smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between revenue and liabilities over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, liabilities)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_opinc_ratio_w21_v048_signal(revenue, opinc) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to opinc smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between revenue and opinc over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, opinc)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_intexp_ratio_w42_v049_signal(revenue, intexp) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to intexp smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between revenue and intexp over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, intexp)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_revenue_currentratio_ratio_w63_v050_signal(revenue, currentratio) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of revenue to currentratio smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between revenue and currentratio over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(revenue, currentratio)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_debt_ratio_w126_v051_signal(cash, debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to debt smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between cash and debt over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, debt)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_assets_ratio_w252_v052_signal(cash, assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to assets smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between cash and assets over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, assets)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_equity_ratio_w504_v053_signal(cash, equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to equity smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between cash and equity over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, equity)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_ebitda_ratio_w756_v054_signal(cash, ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to ebitda smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between cash and ebitda over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, ebitda)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_revenue_ratio_w5_v055_signal(cash, revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to revenue smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between cash and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_w10_v056_signal(cash) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: cash smoothed over 10 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 10 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(cash, 10)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f32_leverage_acceleration_cash_liabilities_ratio_w21_v057_signal(cash, liabilities) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to liabilities smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between cash and liabilities over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, liabilities)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_opinc_ratio_w42_v058_signal(cash, opinc) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to opinc smoothed over 42 days.
    This ratio helps in identifying the relative value or relationship between cash and opinc over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, opinc)
    # Step 2: Smooth the resulting ratio using a moving average of 42 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 42)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_intexp_ratio_w63_v059_signal(cash, intexp) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to intexp smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between cash and intexp over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, intexp)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_cash_currentratio_ratio_w126_v060_signal(cash, currentratio) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of cash to currentratio smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between cash and currentratio over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(cash, currentratio)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_debt_ratio_w252_v061_signal(liabilities, debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to debt smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between liabilities and debt over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, debt)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_assets_ratio_w504_v062_signal(liabilities, assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to assets smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between liabilities and assets over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, assets)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_equity_ratio_w756_v063_signal(liabilities, equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to equity smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between liabilities and equity over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, equity)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_ebitda_ratio_w5_v064_signal(liabilities, ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to ebitda smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between liabilities and ebitda over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, ebitda)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_revenue_ratio_w10_v065_signal(liabilities, revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to revenue smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between liabilities and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_cash_ratio_w21_v066_signal(liabilities, cash) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to cash smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between liabilities and cash over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, cash)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_w42_v067_signal(liabilities) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: liabilities smoothed over 42 days.
    This function calculates a smoothed version of the input series to capture underlying trends.
    It uses a Simple Moving Average with a window of 42 periods.
    """
    # Step 1: Calculate the Simple Moving Average
    smoothed_data = _sma(liabilities, 42)
    # Step 2: Handle infinity values by replacing them with NaN for stability
    clean_result = smoothed_data.replace([np.inf, -np.inf], np.nan)
    return clean_result

def f32_leverage_acceleration_liabilities_opinc_ratio_w63_v068_signal(liabilities, opinc) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to opinc smoothed over 63 days.
    This ratio helps in identifying the relative value or relationship between liabilities and opinc over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, opinc)
    # Step 2: Smooth the resulting ratio using a moving average of 63 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 63)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_intexp_ratio_w126_v069_signal(liabilities, intexp) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to intexp smoothed over 126 days.
    This ratio helps in identifying the relative value or relationship between liabilities and intexp over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, intexp)
    # Step 2: Smooth the resulting ratio using a moving average of 126 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 126)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_liabilities_currentratio_ratio_w252_v070_signal(liabilities, currentratio) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of liabilities to currentratio smoothed over 252 days.
    This ratio helps in identifying the relative value or relationship between liabilities and currentratio over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(liabilities, currentratio)
    # Step 2: Smooth the resulting ratio using a moving average of 252 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 252)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_opinc_debt_ratio_w504_v071_signal(opinc, debt) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of opinc to debt smoothed over 504 days.
    This ratio helps in identifying the relative value or relationship between opinc and debt over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(opinc, debt)
    # Step 2: Smooth the resulting ratio using a moving average of 504 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 504)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_opinc_assets_ratio_w756_v072_signal(opinc, assets) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of opinc to assets smoothed over 756 days.
    This ratio helps in identifying the relative value or relationship between opinc and assets over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(opinc, assets)
    # Step 2: Smooth the resulting ratio using a moving average of 756 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 756)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_opinc_equity_ratio_w5_v073_signal(opinc, equity) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of opinc to equity smoothed over 5 days.
    This ratio helps in identifying the relative value or relationship between opinc and equity over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(opinc, equity)
    # Step 2: Smooth the resulting ratio using a moving average of 5 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 5)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_opinc_ebitda_ratio_w10_v074_signal(opinc, ebitda) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of opinc to ebitda smoothed over 10 days.
    This ratio helps in identifying the relative value or relationship between opinc and ebitda over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(opinc, ebitda)
    # Step 2: Smooth the resulting ratio using a moving average of 10 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 10)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

def f32_leverage_acceleration_opinc_revenue_ratio_w21_v075_signal(opinc, revenue) -> pd.Series:
    """
    Base Signal for f32_leverage_acceleration: Ratio of opinc to revenue smoothed over 21 days.
    This ratio helps in identifying the relative value or relationship between opinc and revenue over time.
    """
    # Step 1: Calculate the raw ratio between the two input series
    raw_ratio_val = _ratio(opinc, revenue)
    # Step 2: Smooth the resulting ratio using a moving average of 21 periods
    smoothed_ratio_series = _sma(raw_ratio_val, 21)
    # Step 3: Replace any potential infinity results with NaN for consistency
    final_output = smoothed_ratio_series.replace([np.inf, -np.inf], np.nan)
    return final_output

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['debt', 'assets', 'equity', 'ebitda', 'revenue', 'cash', 'liabilities', 'opinc', 'intexp', 'currentratio']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f32_leverage_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f32_leverage_acceleration\f32_leverage_acceleration_base_001_075_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f32_leverage_acceleration_'))]}
F32_LEVERAGE_ACCELERATION_REGISTRY_BASE_1_75 = REGISTRY
