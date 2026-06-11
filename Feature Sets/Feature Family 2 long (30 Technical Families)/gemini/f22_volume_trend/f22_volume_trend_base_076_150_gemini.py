# f22_volume_trend_base_076_150_gemini.py
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

# Volume MA Trend 5/42
def f22vt_f22_volume_trend_ma_trend_5_42_v076_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 5-day fast and 42-day slow moving averages."""
    res = _vol_ma_trend(volume, 5, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/126

# Volume ROC 10

# Volume ROC 63

# Volume Force Index 21

# Volume Force Index 126

# Volume Consistency 252d vs 63d MA
def f22vt_f22_volume_trend_consistency_63_252_v082_signal(volume: pd.Series) -> pd.Series:
    """Percentage of days in the last 252 days where volume is above its 63-day MA."""
    ma = _sma(volume, 63)
    res = (volume > ma).rolling(252).mean()
    _vol_ma_trend(volume, 1, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Trend Acceleration 10/42/126
def f22vt_f22_volume_trend_acceleration_10_42_126_v083_signal(volume: pd.Series) -> pd.Series:
    """Volume trend acceleration: 10-day MA trend minus 42-day MA trend."""
    res = _vol_ma_trend(volume, 10, 42) - _vol_ma_trend(volume, 42, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# EMA Volume MA Trend 10/42
def f22vt_f22_volume_trend_ema_ma_trend_10_42_v084_signal(volume: pd.Series) -> pd.Series:
    """EMA-based Volume MA trend using 10-day fast and 42-day slow spans."""
    v_ema_fast = _ema(volume, 10)
    v_ema_slow = _ema(volume, 42)
    res = (v_ema_fast - v_ema_slow) / v_ema_slow.replace(0, np.nan)
    _vol_ma_trend(volume, 10, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC Z-Score 126
def f22vt_f22_volume_trend_roc_zscore_126_v085_signal(volume: pd.Series) -> pd.Series:
    """Z-score of volume ROC over 126 days."""
    roc = _vol_roc(volume, 21)
    res = (roc - roc.rolling(126).mean()) / roc.rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Force Index Normalized 126
def f22vt_f22_volume_trend_force_norm_126_v086_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index normalized by its 252-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 126)
    res = force / force.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC Smoothing 10d ROC 42d SMA
def f22vt_f22_volume_trend_roc_smooth_10_42_v087_signal(volume: pd.Series) -> pd.Series:
    """Smoothed volume ROC: 10-day ROC smoothed with a 42-day SMA."""
    roc = _vol_roc(volume, 10)
    res = _sma(roc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index EMA 63
def f22vt_f22_volume_trend_force_ema_63_v088_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """EMA-smoothed Force Index over 63 days using adjusted close."""
    force = volume * (closeadj - closeadj.shift(1))
    res = _ema(force, 63)
    _vol_force(volume, closeadj, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend Ratio 10/42 over 42/126
def f22vt_f22_volume_trend_ma_trend_ratio_10_42_126_v089_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 10/42 volume MA trend to 42/126 volume MA trend."""
    res = _vol_ma_trend(volume, 10, 42) / _vol_ma_trend(volume, 42, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index ROC 10
def f22vt_f22_volume_trend_force_roc_10_v090_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Rate of change of the 10-day Force Index."""
    force = _vol_force(volume, close, 10)
    res = (force - force.shift(10)) / force.shift(10).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/252
def f22vt_f22_volume_trend_ma_trend_5_252_v091_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 5-day fast and 252-day slow moving averages."""
    res = _vol_ma_trend(volume, 5, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 21 over 126d
def f22vt_f22_volume_trend_roc_21_126_v092_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 21 days, compared to 126 days ago."""
    res = _vol_roc(volume, 21) - _vol_roc(volume, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Ratio 10/42
def f22vt_f22_volume_trend_force_ratio_10_42_v093_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 10-day Force Index to 42-day Force Index."""
    res = _vol_force(volume, close, 10) / _vol_force(volume, close, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 63/504
def f22vt_f22_volume_trend_ma_trend_63_504_v094_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 63-day fast and 504-day slow moving averages."""
    res = _vol_ma_trend(volume, 63, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 10/126
def f22vt_f22_volume_trend_force_10_126_v095_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 10-day and 126-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 10) - _vol_force(volume, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 1/21
def f22vt_f22_volume_trend_ma_trend_1_21_v096_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 1-day fast and 21-day slow moving averages."""
    res = _vol_ma_trend(volume, 1, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 5/126
def f22vt_f22_volume_trend_roc_5_126_v097_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day ROC to 126-day ROC."""
    res = _vol_roc(volume, 5) / _vol_roc(volume, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 21 (v2)
def f22vt_f22_volume_trend_force_norm_21_v2_v098_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Force Index over 21 days normalized by its 126-day standard deviation."""
    force = _vol_force(volume, close, 21)
    res = force / force.rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/42
def f22vt_f22_volume_trend_ma_trend_21_42_v099_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 21-day fast and 42-day slow moving averages."""
    res = _vol_ma_trend(volume, 21, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 21d SMA of 63d ROC
def f22vt_f22_volume_trend_roc_smooth_63_21_v100_signal(volume: pd.Series) -> pd.Series:
    """63-day volume ROC smoothed with a 21-day SMA."""
    roc = _vol_roc(volume, 63)
    res = _sma(roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 5/21 (v2)
def f22vt_f22_volume_trend_force_5_21_v2_v101_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Difference between 5-day and 21-day Force Index averages."""
    res = _vol_force(volume, close, 5) - _vol_force(volume, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/63 (v2)

# Volume ROC 1/63
def f22vt_f22_volume_trend_roc_1_63_v103_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 1-day ROC to 63-day ROC."""
    res = _vol_roc(volume, 1) / _vol_roc(volume, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 42
def f22vt_f22_volume_trend_force_norm_42_v104_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index over 42 days normalized by its 126-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 42)
    res = force / force.rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/504
def f22vt_f22_volume_trend_ma_trend_21_504_v105_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 21-day fast and 504-day slow moving averages."""
    res = _vol_ma_trend(volume, 21, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 63d SMA of 126d ROC
def f22vt_f22_volume_trend_roc_smooth_126_63_v106_signal(volume: pd.Series) -> pd.Series:
    """126-day volume ROC smoothed with a 63-day SMA."""
    roc = _vol_roc(volume, 126)
    res = _sma(roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 21/252
def f22vt_f22_volume_trend_force_21_252_v107_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 21-day and 252-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 21) - _vol_force(volume, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/504
def f22vt_f22_volume_trend_ma_trend_10_504_v108_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 10-day fast and 504-day slow moving averages."""
    res = _vol_ma_trend(volume, 10, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 5 over 252d
def f22vt_f22_volume_trend_roc_5_252_v109_signal(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 5 days, compared to 252 days ago."""
    res = _vol_roc(volume, 5) - _vol_roc(volume, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Ratio 21/126
def f22vt_f22_volume_trend_force_ratio_21_126_v110_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of 21-day Force Index to 126-day Force Index using adjusted close."""
    res = _vol_force(volume, closeadj, 21) / _vol_force(volume, closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 42/252
def f22vt_f22_volume_trend_ma_trend_42_252_v111_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 42-day fast and 252-day slow moving averages."""
    res = _vol_ma_trend(volume, 42, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 126d SMA of 10d ROC
def f22vt_f22_volume_trend_roc_smooth_10_126_v112_signal(volume: pd.Series) -> pd.Series:
    """10-day volume ROC smoothed with a 126-day SMA."""
    roc = _vol_roc(volume, 10)
    res = _sma(roc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 10/252
def f22vt_f22_volume_trend_force_10_252_v113_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 10-day and 252-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 10) - _vol_force(volume, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 1/126
def f22vt_f22_volume_trend_ma_trend_1_126_v114_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 1-day fast and 126-day slow moving averages."""
    res = _vol_ma_trend(volume, 1, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 21/252
def f22vt_f22_volume_trend_roc_21_252_v115_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day ROC to 252-day ROC."""
    res = _vol_roc(volume, 21) / _vol_roc(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 63 (v2)
def f22vt_f22_volume_trend_force_norm_63_v2_v116_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index over 63 days normalized by its 252-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 63)
    res = force / force.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/504
def f22vt_f22_volume_trend_ma_trend_5_504_v117_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 5-day fast and 504-day slow moving averages."""
    res = _vol_ma_trend(volume, 5, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 252d SMA of 5d ROC
def f22vt_f22_volume_trend_roc_smooth_5_252_v118_signal(volume: pd.Series) -> pd.Series:
    """5-day volume ROC smoothed with a 252-day SMA."""
    roc = _vol_roc(volume, 5)
    res = _sma(roc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 5/126
def f22vt_f22_volume_trend_force_5_126_v119_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 5-day and 126-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 5) - _vol_force(volume, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 42/504
def f22vt_f22_volume_trend_ma_trend_42_504_v120_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 42-day fast and 504-day slow moving averages."""
    res = _vol_ma_trend(volume, 42, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 10/126
def f22vt_f22_volume_trend_roc_10_126_v121_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 10-day ROC to 126-day ROC."""
    res = _vol_roc(volume, 10) / _vol_roc(volume, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 126 (v2)
def f22vt_f22_volume_trend_force_norm_126_v2_v122_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index over 126 days normalized by its 504-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 126)
    res = force / force.rolling(504).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/63 (v2)

# Volume ROC 252d SMA of 21d ROC
def f22vt_f22_volume_trend_roc_smooth_21_252_v124_signal(volume: pd.Series) -> pd.Series:
    """21-day volume ROC smoothed with a 252-day SMA."""
    roc = _vol_roc(volume, 21)
    res = _sma(roc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 63/504
def f22vt_f22_volume_trend_force_63_504_v125_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 63-day and 504-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 63) - _vol_force(volume, closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 1/252
def f22vt_f22_volume_trend_ma_trend_1_252_v126_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 1-day fast and 252-day slow moving averages."""
    res = _vol_ma_trend(volume, 1, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 63/252
def f22vt_f22_volume_trend_roc_63_252_v127_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day ROC to 252-day ROC."""
    res = _vol_roc(volume, 63) / _vol_roc(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 252
def f22vt_f22_volume_trend_force_norm_252_v128_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index over 252 days normalized by its 504-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 252)
    res = force / force.rolling(504).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/42 (v2)

# Volume ROC 252d SMA of 63d ROC
def f22vt_f22_volume_trend_roc_smooth_63_252_v130_signal(volume: pd.Series) -> pd.Series:
    """63-day volume ROC smoothed with a 252-day SMA."""
    roc = _vol_roc(volume, 63)
    res = _sma(roc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 126/504
def f22vt_f22_volume_trend_force_126_504_v131_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 126-day and 504-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 126) - _vol_force(volume, closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 1/504
def f22vt_f22_volume_trend_ma_trend_1_504_v132_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 1-day fast and 504-day slow moving averages."""
    res = _vol_ma_trend(volume, 1, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 126/252
def f22vt_f22_volume_trend_roc_126_252_v133_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 126-day ROC to 252-day ROC."""
    res = _vol_roc(volume, 126) / _vol_roc(volume, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 10 (v2)
def f22vt_f22_volume_trend_force_norm_10_v2_v134_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Force Index over 10 days normalized by its 126-day standard deviation."""
    force = _vol_force(volume, close, 10)
    res = force / force.rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/126 (v2)

# Volume ROC 504d SMA of 5d ROC
def f22vt_f22_volume_trend_roc_smooth_5_504_v136_signal(volume: pd.Series) -> pd.Series:
    """5-day volume ROC smoothed with a 504-day SMA."""
    roc = _vol_roc(volume, 5)
    res = _sma(roc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 10/63
def f22vt_f22_volume_trend_force_10_63_v137_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 10-day and 63-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 10) - _vol_force(volume, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 21/126 (v2)

# Volume ROC 5/21 (v2)
def f22vt_f22_volume_trend_roc_5_21_v139_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day ROC to 21-day ROC."""
    res = _vol_roc(volume, 5) / _vol_roc(volume, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 21 (v3)
def f22vt_f22_volume_trend_force_norm_21_v3_v140_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index over 21 days normalized by its 252-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 21)
    res = force / force.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 5/21 (v2)

# Volume ROC 504d SMA of 21d ROC
def f22vt_f22_volume_trend_roc_smooth_21_504_v142_signal(volume: pd.Series) -> pd.Series:
    """21-day volume ROC smoothed with a 504-day SMA."""
    roc = _vol_roc(volume, 21)
    res = _sma(roc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 5/42
def f22vt_f22_volume_trend_force_5_42_v143_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Difference between 5-day and 42-day Force Index averages."""
    res = _vol_force(volume, close, 5) - _vol_force(volume, close, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 10/63 (v2)

# Volume ROC 10/42
def f22vt_f22_volume_trend_roc_10_42_v145_signal(volume: pd.Series) -> pd.Series:
    """Ratio of 10-day ROC to 42-day ROC."""
    res = _vol_roc(volume, 10) / _vol_roc(volume, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index Normalized 42 (v2)
def f22vt_f22_volume_trend_force_norm_42_v2_v146_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Force Index over 42 days normalized by its 252-day standard deviation using adjusted close."""
    force = _vol_force(volume, closeadj, 42)
    res = force / force.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 63/126
def f22vt_f22_volume_trend_ma_trend_63_126_v147_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 63-day fast and 126-day slow moving averages."""
    res = _vol_ma_trend(volume, 63, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume ROC 504d SMA of 63d ROC
def f22vt_f22_volume_trend_roc_smooth_63_504_v148_signal(volume: pd.Series) -> pd.Series:
    """63-day volume ROC smoothed with a 504-day SMA."""
    roc = _vol_roc(volume, 63)
    res = _sma(roc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume Force Index 21/63
def f22vt_f22_volume_trend_force_21_63_v149_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Difference between 21-day and 63-day Force Index averages using adjusted close."""
    res = _vol_force(volume, closeadj, 21) - _vol_force(volume, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volume MA Trend 126/252
def f22vt_f22_volume_trend_ma_trend_126_252_v150_signal(volume: pd.Series) -> pd.Series:
    """Volume MA trend using 126-day fast and 252-day slow moving averages."""
    res = _vol_ma_trend(volume, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f22vt_") and f.endswith("_signal")]

F22_VOLUME_TREND_BASE_REGISTRY_076_150 = {
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
    for n, c in F22_VOLUME_TREND_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
