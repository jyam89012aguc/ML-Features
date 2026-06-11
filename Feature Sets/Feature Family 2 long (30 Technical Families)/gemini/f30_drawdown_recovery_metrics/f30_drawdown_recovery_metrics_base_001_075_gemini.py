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

# drawdown_21d window 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_v001_signal(close) -> pd.Series:
    series = close
    res = _drawdown_val(series, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_21d window 21
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_v002_signal(close) -> pd.Series:
    series = close
    res = _recovery_ratio(series, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_21d window 21
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_v003_signal(close) -> pd.Series:
    series = close
    res = _days_since_peak(series, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_21d window 21
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_v004_signal(close) -> pd.Series:
    series = close
    res = _days_since_trough(series, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_63d window 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_v005_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_63d window 63
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_v006_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_63d window 63
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_v007_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_63d window 63
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_v008_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_126d window 126
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_v009_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_126d window 126
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_v010_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_126d window 126
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_v011_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_126d window 126
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_v012_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_252d window 252
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_v013_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_252d window 252
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_v014_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_252d window 252
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_v015_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_252d window 252
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_v016_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_504d window 504
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_v017_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_504d window 504
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_v018_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_504d window 504
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_v019_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_504d window 504
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_v020_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_21d window 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_v021_signal(close, high, low) -> pd.Series:
    series = close
    res = _drawdown_val(series, 21) / _atr(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_21d window 21
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_v022_signal(close) -> pd.Series:
    series = close
    res = _sma(_drawdown_val(series, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_21d window 21
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_v023_signal(close) -> pd.Series:
    series = close
    res = _recovery_ratio(series, 21).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_21d window 21
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_v024_signal(close) -> pd.Series:
    series = close
    res = (_drawdown_val(series, 21) - _sma(_drawdown_val(series, 21), 21)) / _drawdown_val(series, 21).rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_63d window 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_v025_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 63) / _atr(high, low, close, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_63d window 63
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_v026_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_63d window 63
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_v027_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 63).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_63d window 63
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_v028_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 63) - _sma(_drawdown_val(series, 63), 63)) / _drawdown_val(series, 63).rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_126d window 126
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_v029_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 126) / _atr(high, low, close, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_126d window 126
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_v030_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_126d window 126
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_126d_v031_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 126).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_126d window 126
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_126d_v032_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 126) - _sma(_drawdown_val(series, 126), 126)) / _drawdown_val(series, 126).rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_252d window 252
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_252d_v033_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 252) / _atr(high, low, close, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_252d window 252
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_252d_v034_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_252d window 252
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_252d_v035_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 252).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_252d window 252
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_252d_v036_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 252) - _sma(_drawdown_val(series, 252), 252)) / _drawdown_val(series, 252).rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_504d window 504
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_504d_v037_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 504) / _atr(high, low, close, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_504d window 504
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_504d_v038_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_504d window 504
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_504d_v039_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 504).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_504d window 504
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_504d_v040_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 504) - _sma(_drawdown_val(series, 504), 504)) / _drawdown_val(series, 504).rolling(504).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_21d_v40 window 26
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_v40_v041_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_21d_v41 window 26
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_v41_v042_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_21d_v42 window 26
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_v42_v043_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_21d_v43 window 26
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_v43_v044_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 26)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_63d_v44 window 68
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_v44_v045_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 68)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_63d_v45 window 68
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_v45_v046_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 68)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_63d_v46 window 68
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_v46_v047_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 68)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_63d_v47 window 68
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_v47_v048_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 68)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_126d_v48 window 131
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_v48_v049_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 131)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_126d_v49 window 131
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_v49_v050_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 131)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_126d_v50 window 131
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_v50_v051_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 131)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_126d_v51 window 131
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_v51_v052_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 131)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_252d_v52 window 257
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_v52_v053_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 257)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_252d_v53 window 257
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_v53_v054_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 257)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_252d_v54 window 257
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_v54_v055_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 257)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_252d_v55 window 257
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_v55_v056_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 257)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_504d_v56 window 509
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_v56_v057_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 509)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_504d_v57 window 509
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_v57_v058_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 509)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_504d_v58 window 509
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_v58_v059_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 509)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_504d_v59 window 509
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_v59_v060_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 509)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_21d_v60 window 26
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_v60_v061_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 26) / _atr(high, low, close, 26).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_21d_v61 window 26
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_v61_v062_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 26), 26)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_21d_v62 window 26
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_v62_v063_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 26).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_21d_v63 window 26
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_v63_v064_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 26) - _sma(_drawdown_val(series, 26), 26)) / _drawdown_val(series, 26).rolling(26).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_63d_v64 window 68
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_v64_v065_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 68) / _atr(high, low, close, 68).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_63d_v65 window 68
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_v65_v066_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 68), 68)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_63d_v66 window 68
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_v66_v067_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 68).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_63d_v67 window 68
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_v67_v068_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 68) - _sma(_drawdown_val(series, 68), 68)) / _drawdown_val(series, 68).rolling(68).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_126d_v68 window 131
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_v68_v069_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 131) / _atr(high, low, close, 131).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_126d_v69 window 131
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_v69_v070_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 131), 131)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_126d_v70 window 131
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_126d_v70_v071_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 131).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_126d_v71 window 131
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_126d_v71_v072_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 131) - _sma(_drawdown_val(series, 131), 131)) / _drawdown_val(series, 131).rolling(131).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_252d_v72 window 257
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_252d_v72_v073_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 257) / _atr(high, low, close, 257).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_252d_v73 window 257
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_252d_v73_v074_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 257), 257)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_252d_v74 window 257
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_252d_v74_v075_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 257).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

F30DRM_NAMES = [f for f in globals() if f.startswith("f30drm_") and f.endswith("_signal")]

F30_DRAWDOWN_RECOVERY_METRICS_BASE_REGISTRY_001_075 = {
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
    for n, c in F30_DRAWDOWN_RECOVERY_METRICS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
