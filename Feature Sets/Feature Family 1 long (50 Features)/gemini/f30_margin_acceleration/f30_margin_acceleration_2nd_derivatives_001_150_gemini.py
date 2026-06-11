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


def f30_margin_acceleration_gp_slope_w5_s10_v001_signal(gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: gp smoothed over 5 days, slope over 10 days.
    Captures the rate of change of the smoothed gp series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 5
    base_smoothed_val = _sma(gp, 5)
    # Step 2: Calculate the slope of the smoothed series over 10 periods
    calculated_slope = _slope(base_smoothed_val, 10)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_gp_opinc_ratio_slope_w10_s21_v002_signal(gp, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to opinc smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between gp and opinc using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, opinc)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_ebitda_ratio_slope_w21_s42_v003_signal(gp, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to ebitda smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between gp and ebitda using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, ebitda)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_netinc_ratio_slope_w42_s63_v004_signal(gp, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to netinc smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between gp and netinc using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, netinc)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_revenue_ratio_slope_w63_s126_v005_signal(gp, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to revenue smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between gp and revenue using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, revenue)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_gp_ratio_slope_w126_s252_v006_signal(opinc, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to gp smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between opinc and gp using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, gp)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_slope_w252_s504_v007_signal(opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: opinc smoothed over 252 days, slope over 504 days.
    Captures the rate of change of the smoothed opinc series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 252
    base_smoothed_val = _sma(opinc, 252)
    # Step 2: Calculate the slope of the smoothed series over 504 periods
    calculated_slope = _slope(base_smoothed_val, 504)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_opinc_ebitda_ratio_slope_w504_s756_v008_signal(opinc, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to ebitda smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between opinc and ebitda using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, ebitda)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_netinc_ratio_slope_w756_s5_v009_signal(opinc, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to netinc smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between opinc and netinc using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, netinc)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_revenue_ratio_slope_w5_s10_v010_signal(opinc, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to revenue smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between opinc and revenue using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, revenue)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_gp_ratio_slope_w10_s21_v011_signal(ebitda, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to gp smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between ebitda and gp using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, gp)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_opinc_ratio_slope_w21_s42_v012_signal(ebitda, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to opinc smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between ebitda and opinc using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, opinc)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_slope_w42_s63_v013_signal(ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: ebitda smoothed over 42 days, slope over 63 days.
    Captures the rate of change of the smoothed ebitda series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 42
    base_smoothed_val = _sma(ebitda, 42)
    # Step 2: Calculate the slope of the smoothed series over 63 periods
    calculated_slope = _slope(base_smoothed_val, 63)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_ebitda_netinc_ratio_slope_w63_s126_v014_signal(ebitda, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to netinc smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between ebitda and netinc using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, netinc)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_revenue_ratio_slope_w126_s252_v015_signal(ebitda, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to revenue smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between ebitda and revenue using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, revenue)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_gp_ratio_slope_w252_s504_v016_signal(netinc, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to gp smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between netinc and gp using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, gp)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_opinc_ratio_slope_w504_s756_v017_signal(netinc, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to opinc smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between netinc and opinc using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, opinc)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_ebitda_ratio_slope_w756_s5_v018_signal(netinc, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to ebitda smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between netinc and ebitda using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, ebitda)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_slope_w5_s10_v019_signal(netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: netinc smoothed over 5 days, slope over 10 days.
    Captures the rate of change of the smoothed netinc series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 5
    base_smoothed_val = _sma(netinc, 5)
    # Step 2: Calculate the slope of the smoothed series over 10 periods
    calculated_slope = _slope(base_smoothed_val, 10)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_netinc_revenue_ratio_slope_w10_s21_v020_signal(netinc, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to revenue smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between netinc and revenue using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, revenue)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_gp_ratio_slope_w21_s42_v021_signal(revenue, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to gp smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between revenue and gp using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, gp)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_opinc_ratio_slope_w42_s63_v022_signal(revenue, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to opinc smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between revenue and opinc using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, opinc)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_ebitda_ratio_slope_w63_s126_v023_signal(revenue, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to ebitda smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between revenue and ebitda using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ebitda)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_netinc_ratio_slope_w126_s252_v024_signal(revenue, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to netinc smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between revenue and netinc using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, netinc)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_slope_w252_s504_v025_signal(revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: revenue smoothed over 252 days, slope over 504 days.
    Captures the rate of change of the smoothed revenue series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 252
    base_smoothed_val = _sma(revenue, 252)
    # Step 2: Calculate the slope of the smoothed series over 504 periods
    calculated_slope = _slope(base_smoothed_val, 504)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_gp_slope_w504_s756_v026_signal(gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: gp smoothed over 504 days, slope over 756 days.
    Captures the rate of change of the smoothed gp series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 504
    base_smoothed_val = _sma(gp, 504)
    # Step 2: Calculate the slope of the smoothed series over 756 periods
    calculated_slope = _slope(base_smoothed_val, 756)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_gp_opinc_ratio_slope_w756_s5_v027_signal(gp, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to opinc smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between gp and opinc using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, opinc)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_ebitda_ratio_slope_w5_s10_v028_signal(gp, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to ebitda smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between gp and ebitda using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, ebitda)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_netinc_ratio_slope_w10_s21_v029_signal(gp, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to netinc smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between gp and netinc using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, netinc)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_revenue_ratio_slope_w21_s42_v030_signal(gp, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to revenue smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between gp and revenue using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, revenue)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_gp_ratio_slope_w42_s63_v031_signal(opinc, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to gp smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between opinc and gp using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, gp)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_slope_w63_s126_v032_signal(opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: opinc smoothed over 63 days, slope over 126 days.
    Captures the rate of change of the smoothed opinc series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 63
    base_smoothed_val = _sma(opinc, 63)
    # Step 2: Calculate the slope of the smoothed series over 126 periods
    calculated_slope = _slope(base_smoothed_val, 126)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_opinc_ebitda_ratio_slope_w126_s252_v033_signal(opinc, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to ebitda smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between opinc and ebitda using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, ebitda)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_netinc_ratio_slope_w252_s504_v034_signal(opinc, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to netinc smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between opinc and netinc using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, netinc)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_revenue_ratio_slope_w504_s756_v035_signal(opinc, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to revenue smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between opinc and revenue using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, revenue)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_gp_ratio_slope_w756_s5_v036_signal(ebitda, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to gp smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between ebitda and gp using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, gp)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_opinc_ratio_slope_w5_s10_v037_signal(ebitda, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to opinc smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between ebitda and opinc using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, opinc)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_slope_w10_s21_v038_signal(ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: ebitda smoothed over 10 days, slope over 21 days.
    Captures the rate of change of the smoothed ebitda series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 10
    base_smoothed_val = _sma(ebitda, 10)
    # Step 2: Calculate the slope of the smoothed series over 21 periods
    calculated_slope = _slope(base_smoothed_val, 21)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_ebitda_netinc_ratio_slope_w21_s42_v039_signal(ebitda, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to netinc smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between ebitda and netinc using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, netinc)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_revenue_ratio_slope_w42_s63_v040_signal(ebitda, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to revenue smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between ebitda and revenue using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, revenue)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_gp_ratio_slope_w63_s126_v041_signal(netinc, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to gp smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between netinc and gp using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, gp)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_opinc_ratio_slope_w126_s252_v042_signal(netinc, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to opinc smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between netinc and opinc using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, opinc)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_ebitda_ratio_slope_w252_s504_v043_signal(netinc, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to ebitda smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between netinc and ebitda using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, ebitda)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_slope_w504_s756_v044_signal(netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: netinc smoothed over 504 days, slope over 756 days.
    Captures the rate of change of the smoothed netinc series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 504
    base_smoothed_val = _sma(netinc, 504)
    # Step 2: Calculate the slope of the smoothed series over 756 periods
    calculated_slope = _slope(base_smoothed_val, 756)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_netinc_revenue_ratio_slope_w756_s5_v045_signal(netinc, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to revenue smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between netinc and revenue using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, revenue)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_gp_ratio_slope_w5_s10_v046_signal(revenue, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to gp smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between revenue and gp using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, gp)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_opinc_ratio_slope_w10_s21_v047_signal(revenue, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to opinc smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between revenue and opinc using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, opinc)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_ebitda_ratio_slope_w21_s42_v048_signal(revenue, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to ebitda smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between revenue and ebitda using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ebitda)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_netinc_ratio_slope_w42_s63_v049_signal(revenue, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to netinc smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between revenue and netinc using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, netinc)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_slope_w63_s126_v050_signal(revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: revenue smoothed over 63 days, slope over 126 days.
    Captures the rate of change of the smoothed revenue series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 63
    base_smoothed_val = _sma(revenue, 63)
    # Step 2: Calculate the slope of the smoothed series over 126 periods
    calculated_slope = _slope(base_smoothed_val, 126)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_gp_slope_w126_s252_v051_signal(gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: gp smoothed over 126 days, slope over 252 days.
    Captures the rate of change of the smoothed gp series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 126
    base_smoothed_val = _sma(gp, 126)
    # Step 2: Calculate the slope of the smoothed series over 252 periods
    calculated_slope = _slope(base_smoothed_val, 252)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_gp_opinc_ratio_slope_w252_s504_v052_signal(gp, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to opinc smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between gp and opinc using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, opinc)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_ebitda_ratio_slope_w504_s756_v053_signal(gp, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to ebitda smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between gp and ebitda using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, ebitda)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_netinc_ratio_slope_w756_s5_v054_signal(gp, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to netinc smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between gp and netinc using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, netinc)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_revenue_ratio_slope_w5_s10_v055_signal(gp, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of gp to revenue smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between gp and revenue using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(gp, revenue)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_gp_ratio_slope_w10_s21_v056_signal(opinc, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to gp smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between opinc and gp using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, gp)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_slope_w21_s42_v057_signal(opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: opinc smoothed over 21 days, slope over 42 days.
    Captures the rate of change of the smoothed opinc series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 21
    base_smoothed_val = _sma(opinc, 21)
    # Step 2: Calculate the slope of the smoothed series over 42 periods
    calculated_slope = _slope(base_smoothed_val, 42)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_opinc_ebitda_ratio_slope_w42_s63_v058_signal(opinc, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to ebitda smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between opinc and ebitda using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, ebitda)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_netinc_ratio_slope_w63_s126_v059_signal(opinc, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to netinc smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between opinc and netinc using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, netinc)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_revenue_ratio_slope_w126_s252_v060_signal(opinc, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of opinc to revenue smoothed 126d, slope 252d.
    Analyzes the momentum of the relationship between opinc and revenue using a 252-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(opinc, revenue)
    # Step 2: Smooth the ratio values over 126 days
    smoothed_ratio_val = _sma(base_ratio_val, 126)
    # Step 3: Determine the slope of the smoothed ratio over 252 days
    result_slope_val = _slope(smoothed_ratio_val, 252)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_gp_ratio_slope_w252_s504_v061_signal(ebitda, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to gp smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between ebitda and gp using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, gp)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_opinc_ratio_slope_w504_s756_v062_signal(ebitda, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to opinc smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between ebitda and opinc using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, opinc)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_slope_w756_s5_v063_signal(ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: ebitda smoothed over 756 days, slope over 5 days.
    Captures the rate of change of the smoothed ebitda series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 756
    base_smoothed_val = _sma(ebitda, 756)
    # Step 2: Calculate the slope of the smoothed series over 5 periods
    calculated_slope = _slope(base_smoothed_val, 5)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_ebitda_netinc_ratio_slope_w5_s10_v064_signal(ebitda, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to netinc smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between ebitda and netinc using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, netinc)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_revenue_ratio_slope_w10_s21_v065_signal(ebitda, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of ebitda to revenue smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between ebitda and revenue using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(ebitda, revenue)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_gp_ratio_slope_w21_s42_v066_signal(netinc, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to gp smoothed 21d, slope 42d.
    Analyzes the momentum of the relationship between netinc and gp using a 42-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, gp)
    # Step 2: Smooth the ratio values over 21 days
    smoothed_ratio_val = _sma(base_ratio_val, 21)
    # Step 3: Determine the slope of the smoothed ratio over 42 days
    result_slope_val = _slope(smoothed_ratio_val, 42)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_opinc_ratio_slope_w42_s63_v067_signal(netinc, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to opinc smoothed 42d, slope 63d.
    Analyzes the momentum of the relationship between netinc and opinc using a 63-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, opinc)
    # Step 2: Smooth the ratio values over 42 days
    smoothed_ratio_val = _sma(base_ratio_val, 42)
    # Step 3: Determine the slope of the smoothed ratio over 63 days
    result_slope_val = _slope(smoothed_ratio_val, 63)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_ebitda_ratio_slope_w63_s126_v068_signal(netinc, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to ebitda smoothed 63d, slope 126d.
    Analyzes the momentum of the relationship between netinc and ebitda using a 126-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, ebitda)
    # Step 2: Smooth the ratio values over 63 days
    smoothed_ratio_val = _sma(base_ratio_val, 63)
    # Step 3: Determine the slope of the smoothed ratio over 126 days
    result_slope_val = _slope(smoothed_ratio_val, 126)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_slope_w126_s252_v069_signal(netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: netinc smoothed over 126 days, slope over 252 days.
    Captures the rate of change of the smoothed netinc series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 126
    base_smoothed_val = _sma(netinc, 126)
    # Step 2: Calculate the slope of the smoothed series over 252 periods
    calculated_slope = _slope(base_smoothed_val, 252)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

def f30_margin_acceleration_netinc_revenue_ratio_slope_w252_s504_v070_signal(netinc, revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of netinc to revenue smoothed 252d, slope 504d.
    Analyzes the momentum of the relationship between netinc and revenue using a 504-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(netinc, revenue)
    # Step 2: Smooth the ratio values over 252 days
    smoothed_ratio_val = _sma(base_ratio_val, 252)
    # Step 3: Determine the slope of the smoothed ratio over 504 days
    result_slope_val = _slope(smoothed_ratio_val, 504)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_gp_ratio_slope_w504_s756_v071_signal(revenue, gp) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to gp smoothed 504d, slope 756d.
    Analyzes the momentum of the relationship between revenue and gp using a 756-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, gp)
    # Step 2: Smooth the ratio values over 504 days
    smoothed_ratio_val = _sma(base_ratio_val, 504)
    # Step 3: Determine the slope of the smoothed ratio over 756 days
    result_slope_val = _slope(smoothed_ratio_val, 756)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_opinc_ratio_slope_w756_s5_v072_signal(revenue, opinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to opinc smoothed 756d, slope 5d.
    Analyzes the momentum of the relationship between revenue and opinc using a 5-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, opinc)
    # Step 2: Smooth the ratio values over 756 days
    smoothed_ratio_val = _sma(base_ratio_val, 756)
    # Step 3: Determine the slope of the smoothed ratio over 5 days
    result_slope_val = _slope(smoothed_ratio_val, 5)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_ebitda_ratio_slope_w5_s10_v073_signal(revenue, ebitda) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to ebitda smoothed 5d, slope 10d.
    Analyzes the momentum of the relationship between revenue and ebitda using a 10-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, ebitda)
    # Step 2: Smooth the ratio values over 5 days
    smoothed_ratio_val = _sma(base_ratio_val, 5)
    # Step 3: Determine the slope of the smoothed ratio over 10 days
    result_slope_val = _slope(smoothed_ratio_val, 10)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_netinc_ratio_slope_w10_s21_v074_signal(revenue, netinc) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: Ratio of revenue to netinc smoothed 10d, slope 21d.
    Analyzes the momentum of the relationship between revenue and netinc using a 21-day slope.
    """
    # Step 1: Calculate the input ratio
    base_ratio_val = _ratio(revenue, netinc)
    # Step 2: Smooth the ratio values over 10 days
    smoothed_ratio_val = _sma(base_ratio_val, 10)
    # Step 3: Determine the slope of the smoothed ratio over 21 days
    result_slope_val = _slope(smoothed_ratio_val, 21)
    # Step 4: Replace infinities with NaN
    return result_slope_val.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_slope_w21_s42_v075_signal(revenue) -> pd.Series:
    """
    Slope Signal for f30_margin_acceleration: revenue smoothed over 21 days, slope over 42 days.
    Captures the rate of change of the smoothed revenue series to detect momentum shifts.
    """
    # Step 1: Smooth the input series using SMA 21
    base_smoothed_val = _sma(revenue, 21)
    # Step 2: Calculate the slope of the smoothed series over 42 periods
    calculated_slope = _slope(base_smoothed_val, 42)
    # Step 3: Ensure no infinity values are returned for downstream stability
    stable_slope = calculated_slope.replace([np.inf, -np.inf], np.nan)
    return stable_slope

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['gp', 'opinc', 'ebitda', 'netinc', 'revenue']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f30_margin_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f30_margin_acceleration\f30_margin_acceleration_slope_001_150_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f30_margin_acceleration_'))]}
F30_MARGIN_ACCELERATION_REGISTRY_SLOPE_1_150 = REGISTRY
