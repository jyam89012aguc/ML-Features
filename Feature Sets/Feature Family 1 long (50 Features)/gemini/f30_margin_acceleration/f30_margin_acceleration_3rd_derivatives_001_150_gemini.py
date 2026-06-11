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


def f30_margin_acceleration_gp_jerk_w5_s10_j21_v001_signal(gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: gp smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change (acceleration of slope) for gp.
    """
    # Step 1: Smooth the data for noise reduction using SMA 5
    smoothed_data_input = _sma(gp, 5)
    # Step 2: Calculate the first derivative proxy (slope over 10 days)
    first_derivative_slope = _slope(smoothed_data_input, 10)
    # Step 3: Calculate the second derivative proxy (jerk over 21 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 21)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_opinc_ratio_jerk_w10_s21_j42_v002_signal(gp, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to opinc smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the gp/opinc ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, opinc)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_ebitda_ratio_jerk_w21_s42_j63_v003_signal(gp, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to ebitda smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the gp/ebitda ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, ebitda)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_netinc_ratio_jerk_w42_s63_j126_v004_signal(gp, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to netinc smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the gp/netinc ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, netinc)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_revenue_ratio_jerk_w63_s126_j252_v005_signal(gp, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to revenue smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the gp/revenue ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, revenue)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_gp_ratio_jerk_w126_s252_j504_v006_signal(opinc, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to gp smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the opinc/gp ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, gp)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_jerk_w252_s504_j756_v007_signal(opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: opinc smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change (acceleration of slope) for opinc.
    """
    # Step 1: Smooth the data for noise reduction using SMA 252
    smoothed_data_input = _sma(opinc, 252)
    # Step 2: Calculate the first derivative proxy (slope over 504 days)
    first_derivative_slope = _slope(smoothed_data_input, 504)
    # Step 3: Calculate the second derivative proxy (jerk over 756 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 756)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_ebitda_ratio_jerk_w504_s756_j5_v008_signal(opinc, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to ebitda smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the opinc/ebitda ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, ebitda)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_netinc_ratio_jerk_w756_s5_j10_v009_signal(opinc, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to netinc smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the opinc/netinc ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, netinc)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_revenue_ratio_jerk_w5_s10_j21_v010_signal(opinc, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to revenue smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the opinc/revenue ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, revenue)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_gp_ratio_jerk_w10_s21_j42_v011_signal(ebitda, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to gp smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the ebitda/gp ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, gp)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_opinc_ratio_jerk_w21_s42_j63_v012_signal(ebitda, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to opinc smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the ebitda/opinc ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, opinc)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_jerk_w42_s63_j126_v013_signal(ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: ebitda smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change (acceleration of slope) for ebitda.
    """
    # Step 1: Smooth the data for noise reduction using SMA 42
    smoothed_data_input = _sma(ebitda, 42)
    # Step 2: Calculate the first derivative proxy (slope over 63 days)
    first_derivative_slope = _slope(smoothed_data_input, 63)
    # Step 3: Calculate the second derivative proxy (jerk over 126 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 126)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_netinc_ratio_jerk_w63_s126_j252_v014_signal(ebitda, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to netinc smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the ebitda/netinc ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, netinc)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_revenue_ratio_jerk_w126_s252_j504_v015_signal(ebitda, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to revenue smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the ebitda/revenue ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, revenue)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_gp_ratio_jerk_w252_s504_j756_v016_signal(netinc, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to gp smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the netinc/gp ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, gp)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_opinc_ratio_jerk_w504_s756_j5_v017_signal(netinc, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to opinc smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the netinc/opinc ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, opinc)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_ebitda_ratio_jerk_w756_s5_j10_v018_signal(netinc, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to ebitda smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the netinc/ebitda ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, ebitda)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_jerk_w5_s10_j21_v019_signal(netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: netinc smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change (acceleration of slope) for netinc.
    """
    # Step 1: Smooth the data for noise reduction using SMA 5
    smoothed_data_input = _sma(netinc, 5)
    # Step 2: Calculate the first derivative proxy (slope over 10 days)
    first_derivative_slope = _slope(smoothed_data_input, 10)
    # Step 3: Calculate the second derivative proxy (jerk over 21 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 21)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_revenue_ratio_jerk_w10_s21_j42_v020_signal(netinc, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to revenue smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the netinc/revenue ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, revenue)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_gp_ratio_jerk_w21_s42_j63_v021_signal(revenue, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to gp smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the revenue/gp ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, gp)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_opinc_ratio_jerk_w42_s63_j126_v022_signal(revenue, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to opinc smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the revenue/opinc ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, opinc)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_ebitda_ratio_jerk_w63_s126_j252_v023_signal(revenue, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to ebitda smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the revenue/ebitda ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ebitda)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_netinc_ratio_jerk_w126_s252_j504_v024_signal(revenue, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to netinc smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the revenue/netinc ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, netinc)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_jerk_w252_s504_j756_v025_signal(revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: revenue smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change (acceleration of slope) for revenue.
    """
    # Step 1: Smooth the data for noise reduction using SMA 252
    smoothed_data_input = _sma(revenue, 252)
    # Step 2: Calculate the first derivative proxy (slope over 504 days)
    first_derivative_slope = _slope(smoothed_data_input, 504)
    # Step 3: Calculate the second derivative proxy (jerk over 756 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 756)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_jerk_w504_s756_j5_v026_signal(gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: gp smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change (acceleration of slope) for gp.
    """
    # Step 1: Smooth the data for noise reduction using SMA 504
    smoothed_data_input = _sma(gp, 504)
    # Step 2: Calculate the first derivative proxy (slope over 756 days)
    first_derivative_slope = _slope(smoothed_data_input, 756)
    # Step 3: Calculate the second derivative proxy (jerk over 5 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 5)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_opinc_ratio_jerk_w756_s5_j10_v027_signal(gp, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to opinc smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the gp/opinc ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, opinc)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_ebitda_ratio_jerk_w5_s10_j21_v028_signal(gp, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to ebitda smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the gp/ebitda ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, ebitda)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_netinc_ratio_jerk_w10_s21_j42_v029_signal(gp, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to netinc smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the gp/netinc ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, netinc)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_revenue_ratio_jerk_w21_s42_j63_v030_signal(gp, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the gp/revenue ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, revenue)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_gp_ratio_jerk_w42_s63_j126_v031_signal(opinc, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to gp smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the opinc/gp ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, gp)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_jerk_w63_s126_j252_v032_signal(opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: opinc smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change (acceleration of slope) for opinc.
    """
    # Step 1: Smooth the data for noise reduction using SMA 63
    smoothed_data_input = _sma(opinc, 63)
    # Step 2: Calculate the first derivative proxy (slope over 126 days)
    first_derivative_slope = _slope(smoothed_data_input, 126)
    # Step 3: Calculate the second derivative proxy (jerk over 252 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 252)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_ebitda_ratio_jerk_w126_s252_j504_v033_signal(opinc, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to ebitda smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the opinc/ebitda ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, ebitda)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_netinc_ratio_jerk_w252_s504_j756_v034_signal(opinc, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to netinc smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the opinc/netinc ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, netinc)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_revenue_ratio_jerk_w504_s756_j5_v035_signal(opinc, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to revenue smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the opinc/revenue ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, revenue)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_gp_ratio_jerk_w756_s5_j10_v036_signal(ebitda, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to gp smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the ebitda/gp ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, gp)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_opinc_ratio_jerk_w5_s10_j21_v037_signal(ebitda, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to opinc smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the ebitda/opinc ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, opinc)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_jerk_w10_s21_j42_v038_signal(ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: ebitda smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change (acceleration of slope) for ebitda.
    """
    # Step 1: Smooth the data for noise reduction using SMA 10
    smoothed_data_input = _sma(ebitda, 10)
    # Step 2: Calculate the first derivative proxy (slope over 21 days)
    first_derivative_slope = _slope(smoothed_data_input, 21)
    # Step 3: Calculate the second derivative proxy (jerk over 42 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 42)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_netinc_ratio_jerk_w21_s42_j63_v039_signal(ebitda, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to netinc smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the ebitda/netinc ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, netinc)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_revenue_ratio_jerk_w42_s63_j126_v040_signal(ebitda, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to revenue smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the ebitda/revenue ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, revenue)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_gp_ratio_jerk_w63_s126_j252_v041_signal(netinc, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to gp smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the netinc/gp ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, gp)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_opinc_ratio_jerk_w126_s252_j504_v042_signal(netinc, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to opinc smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the netinc/opinc ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, opinc)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_ebitda_ratio_jerk_w252_s504_j756_v043_signal(netinc, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to ebitda smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the netinc/ebitda ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, ebitda)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_jerk_w504_s756_j5_v044_signal(netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: netinc smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change (acceleration of slope) for netinc.
    """
    # Step 1: Smooth the data for noise reduction using SMA 504
    smoothed_data_input = _sma(netinc, 504)
    # Step 2: Calculate the first derivative proxy (slope over 756 days)
    first_derivative_slope = _slope(smoothed_data_input, 756)
    # Step 3: Calculate the second derivative proxy (jerk over 5 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 5)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_revenue_ratio_jerk_w756_s5_j10_v045_signal(netinc, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to revenue smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the netinc/revenue ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, revenue)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_gp_ratio_jerk_w5_s10_j21_v046_signal(revenue, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to gp smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the revenue/gp ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, gp)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_opinc_ratio_jerk_w10_s21_j42_v047_signal(revenue, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to opinc smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the revenue/opinc ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, opinc)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_ebitda_ratio_jerk_w21_s42_j63_v048_signal(revenue, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to ebitda smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the revenue/ebitda ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ebitda)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_netinc_ratio_jerk_w42_s63_j126_v049_signal(revenue, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to netinc smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the revenue/netinc ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, netinc)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_jerk_w63_s126_j252_v050_signal(revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: revenue smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change (acceleration of slope) for revenue.
    """
    # Step 1: Smooth the data for noise reduction using SMA 63
    smoothed_data_input = _sma(revenue, 63)
    # Step 2: Calculate the first derivative proxy (slope over 126 days)
    first_derivative_slope = _slope(smoothed_data_input, 126)
    # Step 3: Calculate the second derivative proxy (jerk over 252 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 252)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_jerk_w126_s252_j504_v051_signal(gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: gp smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change (acceleration of slope) for gp.
    """
    # Step 1: Smooth the data for noise reduction using SMA 126
    smoothed_data_input = _sma(gp, 126)
    # Step 2: Calculate the first derivative proxy (slope over 252 days)
    first_derivative_slope = _slope(smoothed_data_input, 252)
    # Step 3: Calculate the second derivative proxy (jerk over 504 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 504)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_opinc_ratio_jerk_w252_s504_j756_v052_signal(gp, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to opinc smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the gp/opinc ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, opinc)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_ebitda_ratio_jerk_w504_s756_j5_v053_signal(gp, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to ebitda smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the gp/ebitda ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, ebitda)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_netinc_ratio_jerk_w756_s5_j10_v054_signal(gp, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to netinc smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the gp/netinc ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, netinc)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_gp_revenue_ratio_jerk_w5_s10_j21_v055_signal(gp, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of gp to revenue smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the gp/revenue ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(gp, revenue)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_gp_ratio_jerk_w10_s21_j42_v056_signal(opinc, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to gp smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the opinc/gp ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, gp)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_jerk_w21_s42_j63_v057_signal(opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: opinc smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change (acceleration of slope) for opinc.
    """
    # Step 1: Smooth the data for noise reduction using SMA 21
    smoothed_data_input = _sma(opinc, 21)
    # Step 2: Calculate the first derivative proxy (slope over 42 days)
    first_derivative_slope = _slope(smoothed_data_input, 42)
    # Step 3: Calculate the second derivative proxy (jerk over 63 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 63)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_ebitda_ratio_jerk_w42_s63_j126_v058_signal(opinc, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to ebitda smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the opinc/ebitda ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, ebitda)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_netinc_ratio_jerk_w63_s126_j252_v059_signal(opinc, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to netinc smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the opinc/netinc ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, netinc)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_opinc_revenue_ratio_jerk_w126_s252_j504_v060_signal(opinc, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of opinc to revenue smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change for the opinc/revenue ratio over 504 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(opinc, revenue)
    # Step 2: Apply smoothing to the ratio over 126 periods
    smoothed_ratio_calc = _sma(computed_ratio, 126)
    # Step 3: Compute the slope of the smoothed ratio over 252 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 252)
    # Step 4: Compute the jerk (change in slope) over 504 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 504)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_gp_ratio_jerk_w252_s504_j756_v061_signal(ebitda, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to gp smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the ebitda/gp ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, gp)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_opinc_ratio_jerk_w504_s756_j5_v062_signal(ebitda, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to opinc smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the ebitda/opinc ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, opinc)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_jerk_w756_s5_j10_v063_signal(ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: ebitda smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change (acceleration of slope) for ebitda.
    """
    # Step 1: Smooth the data for noise reduction using SMA 756
    smoothed_data_input = _sma(ebitda, 756)
    # Step 2: Calculate the first derivative proxy (slope over 5 days)
    first_derivative_slope = _slope(smoothed_data_input, 5)
    # Step 3: Calculate the second derivative proxy (jerk over 10 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 10)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_netinc_ratio_jerk_w5_s10_j21_v064_signal(ebitda, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to netinc smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the ebitda/netinc ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, netinc)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_ebitda_revenue_ratio_jerk_w10_s21_j42_v065_signal(ebitda, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of ebitda to revenue smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the ebitda/revenue ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(ebitda, revenue)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_gp_ratio_jerk_w21_s42_j63_v066_signal(netinc, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to gp smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change for the netinc/gp ratio over 63 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, gp)
    # Step 2: Apply smoothing to the ratio over 21 periods
    smoothed_ratio_calc = _sma(computed_ratio, 21)
    # Step 3: Compute the slope of the smoothed ratio over 42 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 42)
    # Step 4: Compute the jerk (change in slope) over 63 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 63)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_opinc_ratio_jerk_w42_s63_j126_v067_signal(netinc, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to opinc smoothed 42d, slope 63d, jerk 126d.
    Measures the second-order rate of change for the netinc/opinc ratio over 126 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, opinc)
    # Step 2: Apply smoothing to the ratio over 42 periods
    smoothed_ratio_calc = _sma(computed_ratio, 42)
    # Step 3: Compute the slope of the smoothed ratio over 63 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 63)
    # Step 4: Compute the jerk (change in slope) over 126 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 126)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_ebitda_ratio_jerk_w63_s126_j252_v068_signal(netinc, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to ebitda smoothed 63d, slope 126d, jerk 252d.
    Measures the second-order rate of change for the netinc/ebitda ratio over 252 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, ebitda)
    # Step 2: Apply smoothing to the ratio over 63 periods
    smoothed_ratio_calc = _sma(computed_ratio, 63)
    # Step 3: Compute the slope of the smoothed ratio over 126 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 126)
    # Step 4: Compute the jerk (change in slope) over 252 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 252)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_jerk_w126_s252_j504_v069_signal(netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: netinc smoothed 126d, slope 252d, jerk 504d.
    Measures the second-order rate of change (acceleration of slope) for netinc.
    """
    # Step 1: Smooth the data for noise reduction using SMA 126
    smoothed_data_input = _sma(netinc, 126)
    # Step 2: Calculate the first derivative proxy (slope over 252 days)
    first_derivative_slope = _slope(smoothed_data_input, 252)
    # Step 3: Calculate the second derivative proxy (jerk over 504 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 504)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_netinc_revenue_ratio_jerk_w252_s504_j756_v070_signal(netinc, revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of netinc to revenue smoothed 252d, slope 504d, jerk 756d.
    Measures the second-order rate of change for the netinc/revenue ratio over 756 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(netinc, revenue)
    # Step 2: Apply smoothing to the ratio over 252 periods
    smoothed_ratio_calc = _sma(computed_ratio, 252)
    # Step 3: Compute the slope of the smoothed ratio over 504 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 504)
    # Step 4: Compute the jerk (change in slope) over 756 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 756)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_gp_ratio_jerk_w504_s756_j5_v071_signal(revenue, gp) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to gp smoothed 504d, slope 756d, jerk 5d.
    Measures the second-order rate of change for the revenue/gp ratio over 5 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, gp)
    # Step 2: Apply smoothing to the ratio over 504 periods
    smoothed_ratio_calc = _sma(computed_ratio, 504)
    # Step 3: Compute the slope of the smoothed ratio over 756 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 756)
    # Step 4: Compute the jerk (change in slope) over 5 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 5)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_opinc_ratio_jerk_w756_s5_j10_v072_signal(revenue, opinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to opinc smoothed 756d, slope 5d, jerk 10d.
    Measures the second-order rate of change for the revenue/opinc ratio over 10 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, opinc)
    # Step 2: Apply smoothing to the ratio over 756 periods
    smoothed_ratio_calc = _sma(computed_ratio, 756)
    # Step 3: Compute the slope of the smoothed ratio over 5 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 5)
    # Step 4: Compute the jerk (change in slope) over 10 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 10)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_ebitda_ratio_jerk_w5_s10_j21_v073_signal(revenue, ebitda) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to ebitda smoothed 5d, slope 10d, jerk 21d.
    Measures the second-order rate of change for the revenue/ebitda ratio over 21 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, ebitda)
    # Step 2: Apply smoothing to the ratio over 5 periods
    smoothed_ratio_calc = _sma(computed_ratio, 5)
    # Step 3: Compute the slope of the smoothed ratio over 10 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 10)
    # Step 4: Compute the jerk (change in slope) over 21 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 21)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_netinc_ratio_jerk_w10_s21_j42_v074_signal(revenue, netinc) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: Ratio of revenue to netinc smoothed 10d, slope 21d, jerk 42d.
    Measures the second-order rate of change for the revenue/netinc ratio over 42 days.
    """
    # Step 1: Compute the base ratio of the two series
    computed_ratio = _ratio(revenue, netinc)
    # Step 2: Apply smoothing to the ratio over 10 periods
    smoothed_ratio_calc = _sma(computed_ratio, 10)
    # Step 3: Compute the slope of the smoothed ratio over 21 periods
    slope_ratio_calc = _slope(smoothed_ratio_calc, 21)
    # Step 4: Compute the jerk (change in slope) over 42 periods
    jerk_ratio_calc = _jerk(slope_ratio_calc, 42)
    # Step 5: Replace infinities for stable output
    return jerk_ratio_calc.replace([np.inf, -np.inf], np.nan)

def f30_margin_acceleration_revenue_jerk_w21_s42_j63_v075_signal(revenue) -> pd.Series:
    """
    Jerk Signal for f30_margin_acceleration: revenue smoothed 21d, slope 42d, jerk 63d.
    Measures the second-order rate of change (acceleration of slope) for revenue.
    """
    # Step 1: Smooth the data for noise reduction using SMA 21
    smoothed_data_input = _sma(revenue, 21)
    # Step 2: Calculate the first derivative proxy (slope over 42 days)
    first_derivative_slope = _slope(smoothed_data_input, 42)
    # Step 3: Calculate the second derivative proxy (jerk over 63 days)
    second_derivative_jerk = _jerk(first_derivative_slope, 63)
    # Step 4: Return cleaned series
    return second_derivative_jerk.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({col: np.abs(np.random.normal(100, 20, n).cumsum()) + 1 for col in ['gp', 'opinc', 'ebitda', 'netinc', 'revenue']})
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f30_margin_acceleration_'))]
    print(f"Testing {len(funcs)} functions for f30_margin_acceleration\f30_margin_acceleration_jerk_001_150_gemini.py...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        assert isinstance(y1, pd.Series), f"{func.__name__} did not return a Series"
        assert not y1.isna().all(), f"{func.__name__} is all NaNs"
    print(f"All {len(funcs)} tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f30_margin_acceleration_'))]}
F30_MARGIN_ACCELERATION_REGISTRY_JERK_1_150 = REGISTRY
