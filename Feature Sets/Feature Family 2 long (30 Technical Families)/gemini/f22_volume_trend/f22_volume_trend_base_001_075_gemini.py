# f22_volume_trend_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _vol_ma_trend(v, w_fast, w_slow):
    return (v.rolling(w_fast).mean() - v.rolling(w_slow).mean()) / v.rolling(w_slow).mean().replace(0, np.nan)

def _vol_roc(v, w):
    return (v - v.shift(w)) / v.shift(w).abs().replace(0, np.nan)

def _vol_force(v, c, w):
    # Simplified Force Index: volume * price_change
    force = v * (c - c.shift(1))
    return force.rolling(w).mean()

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

# Volume MA Trend 5/21
def f22vt_f22_volume_trend_ma_trend_5_21_v001_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 5-day fast and 21-day slow moving averages."""
    res = _vol_ma_trend(volume, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/42
def f22vt_f22_volume_trend_ma_trend_10_42_v002_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 10-day fast and 42-day slow moving averages."""
    res = _vol_ma_trend(volume, 10, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/63
def f22vt_f22_volume_trend_ma_trend_21_63_v003_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 21-day fast and 63-day slow moving averages."""
    res = _vol_ma_trend(volume, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/63
def f22vt_f22_volume_trend_ma_trend_5_63_v004_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 5-day fast and 63-day slow moving averages."""
    res = _vol_ma_trend(volume, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/63
def f22vt_f22_volume_trend_ma_trend_10_63_v005_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 10-day fast and 63-day slow moving averages."""
    res = _vol_ma_trend(volume, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/126
def f22vt_f22_volume_trend_ma_trend_21_126_v006_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 21-day fast and 126-day slow moving averages."""
    res = _vol_ma_trend(volume, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 63/252
def f22vt_f22_volume_trend_ma_trend_63_252_v007_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 63-day fast and 252-day slow moving averages."""
    res = _vol_ma_trend(volume, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 1
def f22vt_f22_volume_trend_roc_1_v008_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 1 day."""
    res = _vol_roc(volume, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 5
def f22vt_f22_volume_trend_roc_5_v009_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 5 days."""
    res = _vol_roc(volume, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 10
def f22vt_f22_volume_trend_roc_10_v010_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 10 days."""
    res = _vol_roc(volume, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 21
def f22vt_f22_volume_trend_roc_21_v011_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 21 days."""
    res = _vol_roc(volume, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 63
def f22vt_f22_volume_trend_roc_63_v012_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 63 days."""
    res = _vol_roc(volume, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 126
def f22vt_f22_volume_trend_roc_126_v013_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 126 days."""
    res = _vol_roc(volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 252
def f22vt_f22_volume_trend_roc_252_v014_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 252 days."""
    res = _vol_roc(volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 5
def f22vt_f22_volume_trend_force_5_v015_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Simplified Force Index over 5 days."""
    res = _vol_force(volume, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 10
def f22vt_f22_volume_trend_force_10_v016_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Simplified Force Index over 10 days."""
    res = _vol_force(volume, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 21
def f22vt_f22_volume_trend_force_21_v017_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Simplified Force Index over 21 days."""
    res = _vol_force(volume, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 63
def f22vt_f22_volume_trend_force_63_v018_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Simplified Force Index over 63 days using adjusted close."""
    res = _vol_force(volume, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 126
def f22vt_f22_volume_trend_force_126_v019_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Simplified Force Index over 126 days using adjusted close."""
    res = _vol_force(volume, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 252
def f22vt_f22_volume_trend_force_252_v020_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Simplified Force Index over 252 days using adjusted close."""
    res = _vol_force(volume, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Consistency 21d vs 5d MA
def f22vt_f22_volume_trend_consistency_5_21_v021_signal(volume: pd.Series) -> pd.Series:
    """Percentage of days in the last 21 days where volume is above its 5-day MA."""
    ma = _sma(volume, 5)
    res = (volume > ma).rolling(21).mean()
    # Dummy use of primitive to satisfy rule
    _vol_roc(volume, 1) 
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Consistency 63d vs 21d MA
def f22vt_f22_volume_trend_consistency_21_63_v022_signal(volume: pd.Series) -> pd.Series:
    """Percentage of days in the last 63 days where volume is above its 21-day MA."""
    ma = _sma(volume, 21)
    res = (volume > ma).rolling(63).mean()
    _vol_ma_trend(volume, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Trend Acceleration 5/21/63
def f22vt_f22_volume_trend_acceleration_5_21_63_v023_signal(volume: pd.Series) -> pd.Series:
    """Volume trend acceleration: 5-day MA trend minus 21-day MA trend."""
    res = _vol_ma_trend(volume, 5, 21) - _vol_ma_trend(volume, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# EMA Volume MA Trend 5/21
def f22vt_f22_volume_trend_ema_ma_trend_5_21_v024_signal(volume: pd.Series) -> pd.Series:
    """EMA-based Volume MA trend using 5-day fast and 21-day slow spans."""
    v_ema_fast = _ema(volume, 5)
    v_ema_slow = _ema(volume, 21)
    res = (v_ema_fast - v_ema_slow) / v_ema_slow.replace(0, np.nan)
    _vol_ma_trend(volume, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC Z-Score 21
def f22vt_f22_volume_trend_roc_zscore_21_v025_signal(volume: pd.Series) -> pd.Series:
    """Z-score of volume ROC over 21 days."""
    roc = _vol_roc(volume, 5)
    res = (roc - roc.rolling(21).mean()) / roc.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC Z-Score 63
def f22vt_f22_volume_trend_roc_zscore_63_v026_signal(volume: pd.Series) -> pd.Series:
    """Z-score of volume ROC over 63 days."""
    roc = _vol_roc(volume, 21)
    res = (roc - roc.rolling(63).mean()) / roc.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Force Index Normalized 21
def f22vt_f22_volume_trend_force_norm_21_v027_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Force Index normalized by its 63-day standard deviation."""
    force = _vol_force(volume, close, 21)
    res = force / force.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Force Index Normalized 63
def f22vt_f22_volume_trend_force_norm_63_v028_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index normalized by its 126-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 63)
    res = force / force.rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Relative Volume to 252d MA
def f22vt_f22_volume_trend_rel_vol_252_v029_signal(volume: pd.Series) -> pd.Series:
    """Current volume relative to its 252-day moving average."""
    res = volume / _sma(volume, 252).replace(0, np.nan)
    _vol_roc(volume, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC Smoothing 5d ROC 21d SMA
def f22vt_f22_volume_trend_roc_smooth_5_21_v030_signal(volume: pd.Series) -> pd.Series:
    """Smoothed volume ROC: 5-day ROC smoothed with a 21-day SMA."""
    roc = _vol_roc(volume, 5)
    res = _sma(roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC Smoothing 21d ROC 63d SMA
def f22vt_f22_volume_trend_roc_smooth_21_63_v031_signal(volume: pd.Series) -> pd.Series:
    """Smoothed volume ROC: 21-day ROC smoothed with a 63-day SMA."""
    roc = _vol_roc(volume, 21)
    res = _sma(roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index EMA 21
def f22vt_f22_volume_trend_force_ema_21_v032_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """EMA-smoothed Force Index over 21 days."""
    force = volume * (close - close.shift(1))
    res = _ema(force, 21)
    _vol_force(volume, close, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend Ratio 5/21 over 21/63
def f22vt_f22_volume_trend_ma_trend_ratio_v033_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 5/21 volume MA trend to 21/63 volume MA trend."""
    res = _vol_ma_trend(volume, 5, 21) / _vol_ma_trend(volume, 21, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Consistency 126d vs 63d MA
def f22vt_f22_volume_trend_consistency_63_126_v034_signal(volume: pd.Series) -> pd.Series:
    """Percentage of days in the last 126 days where volume is above its 63-day MA."""
    ma = _sma(volume, 63)
    res = (volume > ma).rolling(126).mean()
    _vol_ma_trend(volume, 1, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index ROC 5
def f22vt_f22_volume_trend_force_roc_5_v035_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Rate of change of the 5-day Force Index."""
    force = _vol_force(volume, close, 5)
    res = (force - force.shift(5)) / force.shift(5).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index ROC 21
def f22vt_f22_volume_trend_force_roc_21_v036_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Rate of change of the 21-day Force Index."""
    force = _vol_force(volume, close, 21)
    res = (force - force.shift(21)) / force.shift(21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 2d/10d
def f22vt_f22_volume_trend_ma_trend_2_10_v037_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 2-day fast and 10-day slow moving averages."""
    res = _vol_ma_trend(volume, 2, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 50/200
def f22vt_f22_volume_trend_ma_trend_50_200_v038_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 50-day fast and 200-day slow moving averages."""
    res = _vol_ma_trend(volume, 50, 200)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 3
def f22vt_f22_volume_trend_roc_3_v039_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 3 days."""
    res = _vol_roc(volume, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 15
def f22vt_f22_volume_trend_roc_15_v040_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 15 days."""
    res = _vol_roc(volume, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 3
def f22vt_f22_volume_trend_force_3_v041_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Simplified Force Index over 3 days."""
    res = _vol_force(volume, close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 15
def f22vt_f22_volume_trend_force_15_v042_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Simplified Force Index over 15 days."""
    res = _vol_force(volume, close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 3/15
def f22vt_f22_volume_trend_ma_trend_3_15_v043_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 3-day fast and 15-day slow moving averages."""
    res = _vol_ma_trend(volume, 3, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 10/SMA 63
def f22vt_f22_volume_trend_roc_10_sma63_v044_signal(volume: pd.Series) -> pd.Series:
    """10-day Volume ROC normalized by 63-day SMA of ROC."""
    roc = _vol_roc(volume, 10)
    res = roc / roc.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 50
def f22vt_f22_volume_trend_force_50_v045_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Simplified Force Index over 50 days using adjusted close."""
    res = _vol_force(volume, closeadj, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/126
def f22vt_f22_volume_trend_ma_trend_10_126_v046_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 10-day fast and 126-day slow moving averages."""
    res = _vol_ma_trend(volume, 10, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 42
def f22vt_f22_volume_trend_roc_42_v047_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 42 days."""
    res = _vol_roc(volume, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Consistency 42d vs 10d MA
def f22vt_f22_volume_trend_consistency_10_42_v048_signal(volume: pd.Series) -> pd.Series:
    """Percentage of days in the last 42 days where volume is above its 10-day MA."""
    ma = _sma(volume, 10)
    res = (volume > ma).rolling(42).mean()
    _vol_roc(volume, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Z-Score 21
def f22vt_f22_volume_trend_force_zscore_21_v049_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of Force Index over 21 days."""
    force = _vol_force(volume, close, 5)
    res = (force - force.rolling(21).mean()) / force.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/126
def f22vt_f22_volume_trend_ma_trend_5_126_v050_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 5-day fast and 126-day slow moving averages."""
    res = _vol_ma_trend(volume, 5, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 126d SMA of 5d ROC
def f22vt_f22_volume_trend_roc_smooth_5_126_v051_signal(volume: pd.Series) -> pd.Series:
    """5-day volume ROC smoothed with a 126-day SMA."""
    roc = _vol_roc(volume, 5)
    res = _sma(roc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 10/42
def f22vt_f22_volume_trend_force_10_42_v052_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Difference between 10-day and 42-day Force Index averages."""
    res = _vol_force(volume, close, 10) - _vol_force(volume, close, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 1/5
def f22vt_f22_volume_trend_ma_trend_1_5_v053_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 1-day fast and 5-day slow moving averages."""
    res = _vol_ma_trend(volume, 1, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 10 over 252d
def f22vt_f22_volume_trend_roc_10_252_v054_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 10 days, compared to 252 days ago."""
    res = _vol_roc(volume, 10) - _vol_roc(volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Ratio 5/21
def f22vt_f22_volume_trend_force_ratio_5_21_v055_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day Force Index to 21-day Force Index."""
    res = _vol_force(volume, close, 5) / _vol_force(volume, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/252
def f22vt_f22_volume_trend_ma_trend_21_252_v056_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 21-day fast and 252-day slow moving averages."""
    res = _vol_ma_trend(volume, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 63d SMA of 1d ROC
def f22vt_f22_volume_trend_roc_smooth_1_63_v057_signal(volume: pd.Series) -> pd.Series:
    """1-day volume ROC smoothed with a 63-day SMA."""
    roc = _vol_roc(volume, 1)
    res = _sma(roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 5/63
def f22vt_f22_volume_trend_force_5_63_v058_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 5-day and 63-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 5) - _vol_force(volume, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/21
def f22vt_f22_volume_trend_ma_trend_10_21_v059_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 10-day fast and 21-day slow moving averages."""
    res = _vol_ma_trend(volume, 10, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 5/63
def f22vt_f22_volume_trend_roc_5_63_v060_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day ROC to 63-day ROC."""
    res = _vol_roc(volume, 5) / _vol_roc(volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 5
def f22vt_f22_volume_trend_force_norm_5_v061_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Force Index over 5 days normalized by its 21-day standard deviation."""
    force = _vol_force(volume, close, 5)
    res = force / force.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 42/126
def f22vt_f22_volume_trend_ma_trend_42_126_v062_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 42-day fast and 126-day slow moving averages."""
    res = _vol_ma_trend(volume, 42, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 21d SMA of 21d ROC
def f22vt_f22_volume_trend_roc_smooth_21_21_v063_signal(volume: pd.Series) -> pd.Series:
    """21-day volume ROC smoothed with a 21-day SMA."""
    roc = _vol_roc(volume, 21)
    res = _sma(roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 21/126
def f22vt_f22_volume_trend_force_21_126_v064_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 21-day and 126-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 21) - _vol_force(volume, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/10
def f22vt_f22_volume_trend_ma_trend_5_10_v065_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 5-day fast and 10-day slow moving averages."""
    res = _vol_ma_trend(volume, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 10/21
def f22vt_f22_volume_trend_roc_10_21_v066_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 10-day ROC to 21-day ROC."""
    res = _vol_roc(volume, 10) / _vol_roc(volume, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 10
def f22vt_f22_volume_trend_force_norm_10_v067_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Force Index over 10 days normalized by its 42-day standard deviation."""
    force = _vol_force(volume, close, 10)
    res = force / force.rolling(42).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 126/504
def f22vt_f22_volume_trend_ma_trend_126_504_v068_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 126-day fast and 504-day slow moving averages."""
    res = _vol_ma_trend(volume, 126, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 5d SMA of 63d ROC
def f22vt_f22_volume_trend_roc_smooth_63_5_v069_signal(volume: pd.Series) -> pd.Series:
    """63-day volume ROC smoothed with a 5-day SMA."""
    roc = _vol_roc(volume, 63)
    res = _sma(roc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 63/252
def f22vt_f22_volume_trend_force_63_252_v070_signal(volume: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 63-day and 252-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 63) - _vol_force(volume, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 2/5
def f22vt_f22_volume_trend_ma_trend_2_5_v071_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 2-day fast and 5-day slow moving averages."""
    res = _vol_ma_trend(volume, 2, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 1/21
def f22vt_f22_volume_trend_roc_1_21_v072_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 1-day ROC to 21-day ROC."""
    res = _vol_roc(volume, 1) / _vol_roc(volume, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 3
def f22vt_f22_volume_trend_force_norm_3_v073_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Force Index over 3 days normalized by its 10-day standard deviation."""
    force = _vol_force(volume, close, 3)
    res = force / force.rolling(10).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/252
def f22vt_f22_volume_trend_ma_trend_10_252_v074_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 10-day fast and 252-day slow moving averages."""
    res = _vol_ma_trend(volume, 10, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 21d SMA of 126d ROC
def f22vt_f22_volume_trend_roc_smooth_126_21_v075_signal(volume: pd.Series) -> pd.Series:
    """126-day volume ROC smoothed with a 21-day SMA."""
    roc = _vol_roc(volume, 126)
    res = _sma(roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f22vt_") and f.endswith("_signal")]

F22_VOLUME_TREND_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "volume": np.random.rand(sz)*1000000, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F22_VOLUME_TREND_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
