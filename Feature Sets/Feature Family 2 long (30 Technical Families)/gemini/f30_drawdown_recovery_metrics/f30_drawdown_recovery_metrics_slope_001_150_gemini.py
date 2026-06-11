# f30_drawdown_recovery_metrics
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)
def _atr(h, l, c, w): return _sma(_tr(h, l, c), w)

def _drawdown_val(c, w):
    peak = c.rolling(w, min_periods=min(w, 5)).max()
    return (c - peak) / peak.abs().replace(0, np.nan)

def _recovery_ratio(c, w):
    trough = c.rolling(w, min_periods=min(w, 5)).min()
    peak = c.rolling(w, min_periods=min(w, 5)).max()
    return (c - trough) / (peak - trough).abs().replace(0, np.nan)

def _days_since_peak(c, w):
    return c.rolling(w, min_periods=min(w, 5)).apply(lambda x: len(x) - np.argmax(x) - 1, raw=True)

def _days_since_trough(c, w):
    return c.rolling(w, min_periods=min(w, 5)).apply(lambda x: len(x) - np.argmin(x) - 1, raw=True)

# Slope of drawdown_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_slope_v001_signal(close) -> pd.Series:
    series = close
    base = _drawdown_val(series, 21)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_slope_v002_signal(close) -> pd.Series:
    series = close
    base = _recovery_ratio(series, 21)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_slope_v003_signal(close) -> pd.Series:
    series = close
    base = _days_since_peak(series, 21)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_slope_v004_signal(close) -> pd.Series:
    series = close
    base = _days_since_trough(series, 21)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_slope_v005_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 63)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_slope_v006_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 63)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_slope_v007_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 63)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_slope_v008_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 63)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_slope_v009_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 126)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_slope_v010_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 126)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_slope_v011_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 126)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_slope_v012_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 126)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_slope_v013_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 252)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_slope_v014_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 252)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_slope_v015_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 252)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_slope_v016_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 252)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_slope_v017_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 504)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_slope_v018_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 504)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_slope_v019_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 504)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_slope_v020_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 504)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_slope_v021_signal(close, high, low) -> pd.Series:
    series = close
    base = _drawdown_val(series, 21) / _atr(high, low, close, 21).replace(0, np.nan)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_slope_v022_signal(close) -> pd.Series:
    series = close
    base = _sma(_drawdown_val(series, 21), 21)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_slope_v023_signal(close) -> pd.Series:
    series = close
    base = _recovery_ratio(series, 21).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_21d window 21 with ROC 5
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_slope_v024_signal(close) -> pd.Series:
    series = close
    base = (_drawdown_val(series, 21) - _sma(_drawdown_val(series, 21), 21)) / _drawdown_val(series, 21).rolling(21).std().replace(0, np.nan)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_slope_v025_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 63) / _atr(high, low, close, 63).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_slope_v026_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 63), 63)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_slope_v027_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 63).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_63d window 63 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_slope_v028_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 63) - _sma(_drawdown_val(series, 63), 63)) / _drawdown_val(series, 63).rolling(63).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_slope_v029_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 126) / _atr(high, low, close, 126).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_slope_v030_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 126), 126)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_126d_slope_v031_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 126).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_126d window 126 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_126d_slope_v032_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 126) - _sma(_drawdown_val(series, 126), 126)) / _drawdown_val(series, 126).rolling(126).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_252d_slope_v033_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 252) / _atr(high, low, close, 252).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_252d_slope_v034_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 252), 252)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_252d_slope_v035_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 252).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_252d window 252 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_252d_slope_v036_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 252) - _sma(_drawdown_val(series, 252), 252)) / _drawdown_val(series, 252).rolling(252).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_504d_slope_v037_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 504) / _atr(high, low, close, 504).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_504d_slope_v038_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 504), 504)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_504d_slope_v039_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 504).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_504d window 504 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_504d_slope_v040_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 504) - _sma(_drawdown_val(series, 504), 504)) / _drawdown_val(series, 504).rolling(504).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_21d_v40 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_v40_slope_v041_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 26)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_21d_v41 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_v41_slope_v042_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 26)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_21d_v42 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_v42_slope_v043_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 26)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_21d_v43 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_v43_slope_v044_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 26)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_63d_v44 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_v44_slope_v045_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 68)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_63d_v45 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_v45_slope_v046_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 68)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_63d_v46 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_v46_slope_v047_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 68)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_63d_v47 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_v47_slope_v048_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 68)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_126d_v48 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_v48_slope_v049_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 131)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_126d_v49 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_v49_slope_v050_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 131)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_126d_v50 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_v50_slope_v051_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 131)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_126d_v51 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_v51_slope_v052_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 131)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_252d_v52 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_v52_slope_v053_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 257)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_252d_v53 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_v53_slope_v054_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 257)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_252d_v54 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_v54_slope_v055_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 257)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_252d_v55 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_v55_slope_v056_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 257)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_504d_v56 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_v56_slope_v057_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 509)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_504d_v57 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_v57_slope_v058_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 509)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_504d_v58 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_v58_slope_v059_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 509)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_504d_v59 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_v59_slope_v060_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 509)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_21d_v60 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_v60_slope_v061_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 26) / _atr(high, low, close, 26).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_21d_v61 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_v61_slope_v062_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 26), 26)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_21d_v62 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_v62_slope_v063_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 26).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_21d_v63 window 26 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_v63_slope_v064_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 26) - _sma(_drawdown_val(series, 26), 26)) / _drawdown_val(series, 26).rolling(26).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_63d_v64 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_v64_slope_v065_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 68) / _atr(high, low, close, 68).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_63d_v65 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_v65_slope_v066_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 68), 68)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_63d_v66 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_v66_slope_v067_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 68).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_63d_v67 window 68 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_v67_slope_v068_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 68) - _sma(_drawdown_val(series, 68), 68)) / _drawdown_val(series, 68).rolling(68).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_126d_v68 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_v68_slope_v069_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 131) / _atr(high, low, close, 131).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_126d_v69 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_v69_slope_v070_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 131), 131)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_126d_v70 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_126d_v70_slope_v071_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 131).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_126d_v71 window 131 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_126d_v71_slope_v072_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 131) - _sma(_drawdown_val(series, 131), 131)) / _drawdown_val(series, 131).rolling(131).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_252d_v72 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_252d_v72_slope_v073_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 257) / _atr(high, low, close, 257).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_252d_v73 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_252d_v73_slope_v074_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 257), 257)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_252d_v74 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_252d_v74_slope_v075_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 257).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_252d_v75 window 257 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_252d_v75_slope_v076_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 257) - _sma(_drawdown_val(series, 257), 257)) / _drawdown_val(series, 257).rolling(257).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_504d_v76 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_504d_v76_slope_v077_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 509) / _atr(high, low, close, 509).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_504d_v77 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_504d_v77_slope_v078_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 509), 509)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_504d_v78 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_504d_v78_slope_v079_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 509).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_504d_v79 window 509 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_504d_v79_slope_v080_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 509) - _sma(_drawdown_val(series, 509), 509)) / _drawdown_val(series, 509).rolling(509).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_21d_v80 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_v80_slope_v081_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 31)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_21d_v81 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_v81_slope_v082_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 31)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_21d_v82 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_v82_slope_v083_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 31)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_21d_v83 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_v83_slope_v084_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 31)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_63d_v84 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_v84_slope_v085_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 73)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_63d_v85 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_v85_slope_v086_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 73)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_63d_v86 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_v86_slope_v087_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 73)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_63d_v87 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_v87_slope_v088_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 73)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_126d_v88 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_v88_slope_v089_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 136)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_126d_v89 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_v89_slope_v090_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 136)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_126d_v90 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_v90_slope_v091_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 136)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_126d_v91 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_v91_slope_v092_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 136)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_252d_v92 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_v92_slope_v093_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 262)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_252d_v93 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_v93_slope_v094_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 262)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_252d_v94 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_v94_slope_v095_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 262)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_252d_v95 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_v95_slope_v096_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 262)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_504d_v96 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_v96_slope_v097_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 514)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_504d_v97 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_v97_slope_v098_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 514)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_504d_v98 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_v98_slope_v099_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 514)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_504d_v99 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_v99_slope_v100_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 514)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_21d_v100 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_v100_slope_v101_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 31) / _atr(high, low, close, 31).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_21d_v101 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_v101_slope_v102_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 31), 31)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_21d_v102 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_v102_slope_v103_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 31).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_21d_v103 window 31 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_v103_slope_v104_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 31) - _sma(_drawdown_val(series, 31), 31)) / _drawdown_val(series, 31).rolling(31).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_63d_v104 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_v104_slope_v105_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 73) / _atr(high, low, close, 73).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_63d_v105 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_v105_slope_v106_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 73), 73)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_63d_v106 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_v106_slope_v107_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 73).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_63d_v107 window 73 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_v107_slope_v108_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 73) - _sma(_drawdown_val(series, 73), 73)) / _drawdown_val(series, 73).rolling(73).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_126d_v108 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_v108_slope_v109_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 136) / _atr(high, low, close, 136).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_126d_v109 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_v109_slope_v110_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 136), 136)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_126d_v110 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_126d_v110_slope_v111_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 136).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_126d_v111 window 136 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_126d_v111_slope_v112_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 136) - _sma(_drawdown_val(series, 136), 136)) / _drawdown_val(series, 136).rolling(136).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_252d_v112 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_252d_v112_slope_v113_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 262) / _atr(high, low, close, 262).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_252d_v113 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_252d_v113_slope_v114_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 262), 262)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_252d_v114 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_252d_v114_slope_v115_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 262).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_252d_v115 window 262 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_252d_v115_slope_v116_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 262) - _sma(_drawdown_val(series, 262), 262)) / _drawdown_val(series, 262).rolling(262).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_504d_v116 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_504d_v116_slope_v117_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 514) / _atr(high, low, close, 514).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_504d_v117 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_504d_v117_slope_v118_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 514), 514)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_504d_v118 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_504d_v118_slope_v119_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 514).diff(5)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_504d_v119 window 514 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_504d_v119_slope_v120_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 514) - _sma(_drawdown_val(series, 514), 514)) / _drawdown_val(series, 514).rolling(514).std().replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_21d_v120 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_v120_slope_v121_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 36)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_21d_v121 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_v121_slope_v122_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 36)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_21d_v122 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_v122_slope_v123_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 36)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_21d_v123 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_v123_slope_v124_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 36)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_63d_v124 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_v124_slope_v125_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 78)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_63d_v125 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_v125_slope_v126_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 78)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_63d_v126 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_v126_slope_v127_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 78)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_63d_v127 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_v127_slope_v128_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 78)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_126d_v128 window 141 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_v128_slope_v129_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 141)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_126d_v129 window 141 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_v129_slope_v130_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 141)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_126d_v130 window 141 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_v130_slope_v131_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 141)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_126d_v131 window 141 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_v131_slope_v132_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 141)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_252d_v132 window 267 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_v132_slope_v133_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 267)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_252d_v133 window 267 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_v133_slope_v134_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 267)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_252d_v134 window 267 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_v134_slope_v135_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 267)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_252d_v135 window 267 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_v135_slope_v136_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 267)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_504d_v136 window 519 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_v136_slope_v137_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 519)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_504d_v137 window 519 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_v137_slope_v138_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 519)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_peak_504d_v138 window 519 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_v138_slope_v139_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_peak(series, 519)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of days_since_trough_504d_v139 window 519 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_v139_slope_v140_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _days_since_trough(series, 519)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_21d_v140 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_v140_slope_v141_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 36) / _atr(high, low, close, 36).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_21d_v141 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_v141_slope_v142_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 36), 36)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_21d_v142 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_v142_slope_v143_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 36).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_21d_v143 window 36 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_v143_slope_v144_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 36) - _sma(_drawdown_val(series, 36), 36)) / _drawdown_val(series, 36).rolling(36).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_63d_v144 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_v144_slope_v145_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 78) / _atr(high, low, close, 78).replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_63d_v145 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_v145_slope_v146_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 78), 78)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery_accel_63d_v146 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_v146_slope_v147_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _recovery_ratio(series, 78).diff(5)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_zscore_63d_v147 window 78 with ROC 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_v147_slope_v148_signal(closeadj) -> pd.Series:
    series = closeadj
    base = (_drawdown_val(series, 78) - _sma(_drawdown_val(series, 78), 78)) / _drawdown_val(series, 78).rolling(78).std().replace(0, np.nan)
    res = base.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown_to_atr_126d_v148 window 141 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_v148_slope_v149_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    base = _drawdown_val(series, 141) / _atr(high, low, close, 141).replace(0, np.nan)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling_mean_drawdown_126d_v149 window 141 with ROC 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_v149_slope_v150_signal(closeadj) -> pd.Series:
    series = closeadj
    base = _sma(_drawdown_val(series, 141), 141)
    res = base.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

F30DRM_NAMES = [f for f in globals() if f.startswith("f30drm_") and f.endswith("_signal")]

F30_DRAWDOWN_RECOVERY_METRICS_SLOPE_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(F30DRM_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F30_DRAWDOWN_RECOVERY_METRICS_SLOPE_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("slope 001-150 OK")
