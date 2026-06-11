# f13_macd_variants_base_001_075_gemini.py
# This file contains base MACD variant features, including standard, short-term, and long-term configurations.
# Features are calculated using the domain primitives _macd_val, _macd_sig, and _macd_h.
# Size requirement: 20KB-75KB.
# Every function is expanded and includes a descriptive comment.
# Returns replace infinity with NaN.
# Window rules for closeadj (windows > 21) are respected.

import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)
def _macd_val(c, f, s):
    return (_ema(c, f) - _ema(c, s)) / _ema(c, s).abs().replace(0, np.nan)
def _macd_sig(macd, sig):
    return _ema(macd, sig)
def _macd_h(macd, signal):
    return macd - signal

# Standard (12, 26) Moving Average Convergence Divergence (MACD) value using the standard close price series.
def f13mv_macd_val_12_26_v001_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# Standard (12, 26, 9) Moving Average Convergence Divergence (MACD) signal line calculated as the 9-day EMA of the MACD value.
def f13mv_macd_sig_12_26_9_v002_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# Standard (12, 26, 9) Moving Average Convergence Divergence (MACD) histogram, representing the difference between the MACD value and its signal line.
def f13mv_macd_h_12_26_9_v003_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term (5, 13) MACD value using the close price, designed to capture faster price movements and trend changes.
def f13mv_macd_val_5_13_v004_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 13)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term (5, 13, 5) MACD signal line, providing a more responsive indicator for short-term trading signals.
def f13mv_macd_sig_5_13_5_v005_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    res = _macd_sig(val, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term (5, 13, 5) MACD histogram, showing the momentum of the short-term MACD value relative to its faster signal line.
def f13mv_macd_h_5_13_5_v006_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 13)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term (21, 50) MACD value using adjusted close price (closeadj), intended for identifying major long-term trend shifts.
def f13mv_macd_val_21_50_v007_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 21, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term (21, 50, 15) MACD signal line using closeadj, providing a smoothed representation of long-term price trends.
def f13mv_macd_sig_21_50_15_v008_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    res = _macd_sig(val, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-term (21, 50, 15) MACD histogram using closeadj, measuring the distance between long-term trend lines.
def f13mv_macd_h_21_50_15_v009_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 21, 50)
    sig = _macd_sig(val, 15)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using typical price (defined as the average of high, low, and close) with (12, 26) windows for broader price representation.
def f13mv_macd_val_typical_12_26_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typical = (high + low + close) / 3
    res = _macd_val(typical, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal line using typical price with (12, 26, 9) configuration, smoothing the typical price based MACD value.
def f13mv_macd_sig_typical_12_26_9_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typical = (high + low + close) / 3
    val = _macd_val(typical, 12, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using typical price with (12, 26, 9) configuration, highlighting momentum changes in the typical price trend.
def f13mv_macd_h_typical_12_26_9_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typical = (high + low + close) / 3
    val = _macd_val(typical, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using median price (average of high and low) with (12, 26) windows, focusing on the midpoint of the daily trading range.
def f13mv_macd_val_median_12_26_v013_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    median = (high + low) / 2
    res = _macd_val(median, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD signal line using median price with (12, 26, 9) configuration, offering a stable view of price convergence and divergence.
def f13mv_macd_sig_median_12_26_9_v014_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    median = (high + low) / 2
    val = _macd_val(median, 12, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD histogram using median price with (12, 26, 9) configuration, emphasizing the difference between median price trends.
def f13mv_macd_h_median_12_26_9_v015_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    median = (high + low) / 2
    val = _macd_val(median, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of the standard (12, 26, 9) MACD histogram calculated over a 21-day rolling window to normalize momentum readings.
def f13mv_macd_h_zscore_21_v016_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    sig = _macd_sig(val, 9)
    h = _macd_h(val, sig)
    res = _z(h, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of the standard (12, 26) MACD value series over a 21-day rolling period, providing a statistical context for MACD levels.
def f13mv_macd_val_zscore_21_v017_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 12, 26)
    res = _z(val, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Alternative MACD value using (10, 20) windows, offering a slightly more responsive profile than the standard settings.
def f13mv_macd_val_10_20_v018_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 10, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for the (10, 20) MACD using a 7-day EMA, designed for capturing medium-term momentum shifts.
def f13mv_macd_sig_10_20_7_v019_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 20)
    res = _macd_sig(val, 7)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for the (10, 20) MACD with a 7-day signal line, tracking the rate of change in trend strength.
def f13mv_macd_h_10_20_7_v020_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 10, 20)
    sig = _macd_sig(val, 7)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Medium-term (20, 40) MACD value using adjusted close price (closeadj) for enhanced trend identification over multiple weeks.
def f13mv_macd_val_20_40_v021_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 20, 40)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for the (20, 40) MACD using a 9-day EMA, filtering noise from the medium-term adjusted price trend.
def f13mv_macd_sig_20_40_9_v022_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 20, 40)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for the (20, 40) MACD using adjusted close price, measuring the gap between medium-term trends.
def f13mv_macd_h_20_40_9_v023_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 20, 40)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Very long-term (50, 100) MACD value using closeadj, used for spotting secular trend reversals in price action.
def f13mv_macd_val_50_100_v024_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 50, 100)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for the very long-term (50, 100) MACD using a 20-day EMA, smoothing secular price momentum readings.
def f13mv_macd_sig_50_100_20_v025_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 50, 100)
    res = _macd_sig(val, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for the (50, 100) MACD using adjusted close price, indicating changes in the strength of secular trends.
def f13mv_macd_h_50_100_20_v026_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 50, 100)
    sig = _macd_sig(val, 20)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Ultra short-term (3, 10) MACD value using close price, highly sensitive to immediate price action and noise.
def f13mv_macd_val_3_10_v027_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for the ultra short-term (3, 10) MACD using a 16-day EMA, which is unusually long for such fast settings.
def f13mv_macd_sig_3_10_16_v028_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 3, 10)
    res = _macd_sig(val, 16)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for the (3, 10) MACD with a 16-day signal line, tracking rapid divergence from a slower signal base.
def f13mv_macd_h_3_10_16_v029_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 3, 10)
    sig = _macd_sig(val, 16)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using high price series with standard (12, 26) configuration, tracking momentum of the upper range.
def f13mv_macd_val_high_12_26_v030_signal(high: pd.Series) -> pd.Series:
    res = _macd_val(high, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using low price series with standard (12, 26) configuration, tracking momentum of the lower range.
def f13mv_macd_val_low_12_26_v031_signal(low: pd.Series) -> pd.Series:
    res = _macd_val(low, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# Intermediate (8, 17) MACD value using close price, balancing responsiveness and trend stability.
def f13mv_macd_val_8_17_v032_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 8, 17)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for (8, 17) MACD using 9-day EMA, offering clear convergence signals for intermediate timeframes.
def f13mv_macd_sig_8_17_9_v033_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 8, 17)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (8, 17) MACD, showing the ebb and flow of intermediate term price momentum.
def f13mv_macd_h_8_17_9_v034_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 8, 17)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Extended medium-term (24, 52) MACD value using closeadj, designed for trend following in slower markets.
def f13mv_macd_val_24_52_v035_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 24, 52)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for (24, 52) MACD using 18-day EMA, providing a very smooth representation of trend direction.
def f13mv_macd_sig_24_52_18_v036_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 24, 52)
    res = _macd_sig(val, 18)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (24, 52) MACD using closeadj, tracking significant shifts in the adjusted medium-term price trend.
def f13mv_macd_h_24_52_18_v037_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 24, 52)
    sig = _macd_sig(val, 18)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Wide-band (5, 35) MACD value using close price, measuring divergence between very fast and slow price averages.
def f13mv_macd_val_5_35_v038_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 5, 35)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for wide-band (5, 35) MACD using 5-day EMA, emphasizing rapid changes in the divergence profile.
def f13mv_macd_sig_5_35_5_v039_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 35)
    res = _macd_sig(val, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (5, 35) MACD, identifying quick breakouts from a wide baseline momentum.
def f13mv_macd_h_5_35_5_v040_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 5, 35)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Decadal (10, 100) MACD value using adjusted close price, measuring extreme long-term relative momentum.
def f13mv_macd_val_10_100_v041_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 10, 100)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for (10, 100) MACD using 10-day EMA, filtering long-term adjusted momentum readings.
def f13mv_macd_sig_10_100_10_v042_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 100)
    res = _macd_sig(val, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (10, 100) MACD using adjusted price, highlighting deep structural changes in price trends.
def f13mv_macd_h_10_100_10_v043_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 10, 100)
    sig = _macd_sig(val, 10)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Standard (12, 26) MACD value using adjusted close price (closeadj), accounting for corporate actions and dividends.
def f13mv_macd_val_12_26_adj_v044_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for the standard (12, 26) MACD using adjusted close price, offering reliable adjusted trend smoothing.
def f13mv_macd_sig_12_26_9_adj_v045_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for the standard (12, 26) MACD using adjusted close price, measuring relative momentum on adjusted returns.
def f13mv_macd_h_12_26_9_adj_v046_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Short-term (5, 13) MACD value using adjusted close price, focusing on fast trend changes in dividend-adjusted series.
def f13mv_macd_val_5_13_adj_v047_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 5, 13)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for adjusted short-term (5, 13) MACD, offering highly responsive indicators on corporate action adjusted price data.
def f13mv_macd_sig_5_13_5_adj_v048_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 5, 13)
    res = _macd_sig(val, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for adjusted short-term (5, 13) MACD, tracking rapid momentum shifts in the adjusted close series.
def f13mv_macd_h_5_13_5_adj_v049_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 5, 13)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Medium-term (19, 39) MACD value using adjusted close price, a common alternative for identifying primary trend direction.
def f13mv_macd_val_19_39_v050_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 19, 39)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for (19, 39) adjusted MACD using 9-day EMA, offering a balanced smoothing for medium-term price trends.
def f13mv_macd_sig_19_39_9_v051_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 19, 39)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (19, 39) adjusted MACD, tracking shifts in trend strength for primary adjusted price movements.
def f13mv_macd_h_19_39_9_v052_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 19, 39)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# MACD value using (H+L)/2 median price with standard (12, 26) configuration, tracking central price momentum.
def f13mv_macd_val_hl2_12_26_v053_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    hl2 = (high + low) / 2
    res = _macd_val(hl2, 12, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for (H+L)/2 median MACD using 9-day EMA, offering convergence signals based on central trading range.
def f13mv_macd_sig_hl2_12_26_9_v054_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    hl2 = (high + low) / 2
    val = _macd_val(hl2, 12, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (H+L)/2 median MACD, measuring divergence between central price trend averages.
def f13mv_macd_h_hl2_12_26_9_v055_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    hl2 = (high + low) / 2
    val = _macd_val(hl2, 12, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Faster intermediate (6, 13) MACD value using close price, providing a quick response to price action shifts.
def f13mv_macd_val_6_13_v056_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 6, 13)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for faster intermediate (6, 13) MACD using 4-day EMA, creating a high-sensitivity momentum indicator.
def f13mv_macd_sig_6_13_4_v057_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 6, 13)
    res = _macd_sig(val, 4)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (6, 13) MACD, identifying fast momentum changes in the daily close price.
def f13mv_macd_h_6_13_4_v058_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 6, 13)
    sig = _macd_sig(val, 4)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Slower standard-based (13, 26) MACD value using close price, providing a slightly lagging but more stable trend indicator.
def f13mv_macd_val_13_26_v059_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 13, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for (13, 26) MACD using standard 9-day EMA, offering clear trend confirmation signals.
def f13mv_macd_sig_13_26_9_v060_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 13, 26)
    res = _macd_sig(val, 9)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for (13, 26) MACD, highlighting the divergence between slightly slower price averages.
def f13mv_macd_h_13_26_9_v061_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 13, 26)
    sig = _macd_sig(val, 9)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Ultra-fast (2, 5) MACD value using close price, intended for high-frequency or extremely sensitive momentum tracking.
def f13mv_macd_val_2_5_v062_signal(close: pd.Series) -> pd.Series:
    res = _macd_val(close, 2, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for ultra-fast (2, 5) MACD using 2-day EMA, tracking immediate price convergences.
def f13mv_macd_sig_2_5_2_v063_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 2, 5)
    res = _macd_sig(val, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for ultra-fast (2, 5) MACD, capturing the highest frequency shifts in close price momentum.
def f13mv_macd_h_2_5_2_v064_signal(close: pd.Series) -> pd.Series:
    val = _macd_val(close, 2, 5)
    sig = _macd_sig(val, 2)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Long-period (40, 80) MACD value using adjusted close price, measuring structural momentum shifts over months.
def f13mv_macd_val_40_80_v065_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 40, 80)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for long-period (40, 80) adjusted MACD using 20-day EMA, filtering long-range adjusted trend data.
def f13mv_macd_sig_40_80_20_v066_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 40, 80)
    res = _macd_sig(val, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for adjusted (40, 80) MACD, identifying significant reversals in structural price trends.
def f13mv_macd_h_40_80_20_v067_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 40, 80)
    sig = _macd_sig(val, 20)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Secular (100, 200) MACD value using adjusted close price, used for identifying multi-year cycle turning points.
def f13mv_macd_val_100_200_v068_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 100, 200)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for secular (100, 200) adjusted MACD using 50-day EMA, providing high-level smoothing of secular price cycles.
def f13mv_macd_sig_100_200_50_v069_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 100, 200)
    res = _macd_sig(val, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for adjusted secular (100, 200) MACD, measuring the strength of primary secular trend shifts.
def f13mv_macd_h_100_200_50_v070_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 100, 200)
    sig = _macd_sig(val, 50)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of adjusted (12, 26) MACD value over a 63-day period, normalizing adjusted price momentum for comparison across stocks.
def f13mv_macd_val_adj_zscore_63_v071_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    res = _z(val, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of adjusted standard (12, 26, 9) MACD histogram over a 63-day window, providing a relative strength measure of momentum.
def f13mv_macd_h_adj_zscore_63_v072_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 12, 26)
    sig = _macd_sig(val, 9)
    h = _macd_h(val, sig)
    res = _z(h, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Wide-band (5, 35) adjusted MACD value using closeadj price, identifying primary trend divergence in adjusted returns.
def f13mv_macd_val_5_35_adj_v073_signal(closeadj: pd.Series) -> pd.Series:
    res = _macd_val(closeadj, 5, 35)
    return res.replace([np.inf, -np.inf], np.nan)

# Signal line for adjusted wide-band (5, 35) MACD using 5-day EMA, offering responsive signals on long-baseline momentum.
def f13mv_macd_sig_5_35_5_adj_v074_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 5, 35)
    res = _macd_sig(val, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Histogram for adjusted wide-band (5, 35) MACD, identifying fast adjusted momentum shifts relative to a broad trend.
def f13mv_macd_h_5_35_5_adj_v075_signal(closeadj: pd.Series) -> pd.Series:
    val = _macd_val(closeadj, 5, 35)
    sig = _macd_sig(val, 5)
    res = _macd_h(val, sig)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f13mv_") and f.endswith("_signal")]

F13_MACD_VARIANTS_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum() + 100,
        "closeadj": np.random.randn(sz).cumsum() + 100,
        "high": np.random.randn(sz).cumsum() + 110,
        "low": np.random.randn(sz).cumsum() + 90,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F13_MACD_VARIANTS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001_075 OK")
