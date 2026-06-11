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

# drawdown_zscore_252d_v75 window 257
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_252d_v75_v076_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 257) - _sma(_drawdown_val(series, 257), 257)) / _drawdown_val(series, 257).rolling(257).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_504d_v76 window 509
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_504d_v76_v077_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 509) / _atr(high, low, close, 509).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_504d_v77 window 509
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_504d_v77_v078_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 509), 509)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_504d_v78 window 509
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_504d_v78_v079_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 509).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_504d_v79 window 509
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_504d_v79_v080_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 509) - _sma(_drawdown_val(series, 509), 509)) / _drawdown_val(series, 509).rolling(509).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_21d_v80 window 31
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_v80_v081_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 31)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_21d_v81 window 31
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_v81_v082_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 31)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_21d_v82 window 31
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_v82_v083_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 31)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_21d_v83 window 31
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_v83_v084_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 31)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_63d_v84 window 73
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_v84_v085_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 73)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_63d_v85 window 73
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_v85_v086_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 73)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_63d_v86 window 73
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_v86_v087_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 73)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_63d_v87 window 73
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_v87_v088_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 73)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_126d_v88 window 136
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_v88_v089_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 136)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_126d_v89 window 136
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_v89_v090_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 136)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_126d_v90 window 136
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_v90_v091_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 136)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_126d_v91 window 136
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_v91_v092_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 136)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_252d_v92 window 262
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_v92_v093_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 262)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_252d_v93 window 262
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_v93_v094_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 262)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_252d_v94 window 262
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_v94_v095_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 262)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_252d_v95 window 262
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_v95_v096_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 262)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_504d_v96 window 514
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_v96_v097_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 514)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_504d_v97 window 514
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_v97_v098_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 514)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_504d_v98 window 514
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_v98_v099_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 514)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_504d_v99 window 514
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_v99_v100_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 514)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_21d_v100 window 31
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_v100_v101_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 31) / _atr(high, low, close, 31).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_21d_v101 window 31
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_v101_v102_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 31), 31)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_21d_v102 window 31
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_v102_v103_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 31).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_21d_v103 window 31
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_v103_v104_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 31) - _sma(_drawdown_val(series, 31), 31)) / _drawdown_val(series, 31).rolling(31).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_63d_v104 window 73
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_v104_v105_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 73) / _atr(high, low, close, 73).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_63d_v105 window 73
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_v105_v106_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 73), 73)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_63d_v106 window 73
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_v106_v107_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 73).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_63d_v107 window 73
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_v107_v108_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 73) - _sma(_drawdown_val(series, 73), 73)) / _drawdown_val(series, 73).rolling(73).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_126d_v108 window 136
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_v108_v109_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 136) / _atr(high, low, close, 136).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_126d_v109 window 136
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_v109_v110_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 136), 136)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_126d_v110 window 136
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_126d_v110_v111_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 136).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_126d_v111 window 136
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_126d_v111_v112_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 136) - _sma(_drawdown_val(series, 136), 136)) / _drawdown_val(series, 136).rolling(136).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_252d_v112 window 262
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_252d_v112_v113_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 262) / _atr(high, low, close, 262).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_252d_v113 window 262
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_252d_v113_v114_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 262), 262)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_252d_v114 window 262
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_252d_v114_v115_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 262).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_252d_v115 window 262
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_252d_v115_v116_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 262) - _sma(_drawdown_val(series, 262), 262)) / _drawdown_val(series, 262).rolling(262).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_504d_v116 window 514
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_504d_v116_v117_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 514) / _atr(high, low, close, 514).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_504d_v117 window 514
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_504d_v117_v118_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 514), 514)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_504d_v118 window 514
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_504d_v118_v119_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 514).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_504d_v119 window 514
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_504d_v119_v120_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 514) - _sma(_drawdown_val(series, 514), 514)) / _drawdown_val(series, 514).rolling(514).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_21d_v120 window 36
def f30drm_f30_drawdown_recovery_metrics_drawdown_21d_v120_v121_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 36)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_21d_v121 window 36
def f30drm_f30_drawdown_recovery_metrics_recovery_21d_v121_v122_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 36)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_21d_v122 window 36
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_21d_v122_v123_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 36)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_21d_v123 window 36
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_21d_v123_v124_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 36)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_63d_v124 window 78
def f30drm_f30_drawdown_recovery_metrics_drawdown_63d_v124_v125_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 78)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_63d_v125 window 78
def f30drm_f30_drawdown_recovery_metrics_recovery_63d_v125_v126_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 78)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_63d_v126 window 78
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_63d_v126_v127_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 78)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_63d_v127 window 78
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_63d_v127_v128_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 78)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_126d_v128 window 141
def f30drm_f30_drawdown_recovery_metrics_drawdown_126d_v128_v129_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 141)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_126d_v129 window 141
def f30drm_f30_drawdown_recovery_metrics_recovery_126d_v129_v130_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 141)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_126d_v130 window 141
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_126d_v130_v131_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 141)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_126d_v131 window 141
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_126d_v131_v132_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 141)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_252d_v132 window 267
def f30drm_f30_drawdown_recovery_metrics_drawdown_252d_v132_v133_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 267)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_252d_v133 window 267
def f30drm_f30_drawdown_recovery_metrics_recovery_252d_v133_v134_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 267)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_252d_v134 window 267
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_252d_v134_v135_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 267)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_252d_v135 window 267
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_252d_v135_v136_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 267)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_504d_v136 window 519
def f30drm_f30_drawdown_recovery_metrics_drawdown_504d_v136_v137_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 519)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_504d_v137 window 519
def f30drm_f30_drawdown_recovery_metrics_recovery_504d_v137_v138_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 519)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_peak_504d_v138 window 519
def f30drm_f30_drawdown_recovery_metrics_days_since_peak_504d_v138_v139_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_peak(series, 519)
    return res.replace([np.inf, -np.inf], np.nan)

# days_since_trough_504d_v139 window 519
def f30drm_f30_drawdown_recovery_metrics_days_since_trough_504d_v139_v140_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _days_since_trough(series, 519)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_21d_v140 window 36
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_21d_v140_v141_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 36) / _atr(high, low, close, 36).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_21d_v141 window 36
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_21d_v141_v142_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 36), 36)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_21d_v142 window 36
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_21d_v142_v143_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 36).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_21d_v143 window 36
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_21d_v143_v144_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 36) - _sma(_drawdown_val(series, 36), 36)) / _drawdown_val(series, 36).rolling(36).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_63d_v144 window 78
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_63d_v144_v145_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 78) / _atr(high, low, close, 78).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_63d_v145 window 78
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_63d_v145_v146_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 78), 78)
    return res.replace([np.inf, -np.inf], np.nan)

# recovery_accel_63d_v146 window 78
def f30drm_f30_drawdown_recovery_metrics_recovery_accel_63d_v146_v147_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _recovery_ratio(series, 78).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_zscore_63d_v147 window 78
def f30drm_f30_drawdown_recovery_metrics_drawdown_zscore_63d_v147_v148_signal(closeadj) -> pd.Series:
    series = closeadj
    res = (_drawdown_val(series, 78) - _sma(_drawdown_val(series, 78), 78)) / _drawdown_val(series, 78).rolling(78).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# drawdown_to_atr_126d_v148 window 141
def f30drm_f30_drawdown_recovery_metrics_drawdown_to_atr_126d_v148_v149_signal(closeadj, high, low, close) -> pd.Series:
    series = closeadj
    res = _drawdown_val(series, 141) / _atr(high, low, close, 141).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# rolling_mean_drawdown_126d_v149 window 141
def f30drm_f30_drawdown_recovery_metrics_rolling_mean_drawdown_126d_v149_v150_signal(closeadj) -> pd.Series:
    series = closeadj
    res = _sma(_drawdown_val(series, 141), 141)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

F30DRM_NAMES = [f for f in globals() if f.startswith("f30drm_") and f.endswith("_signal")]

F30_DRAWDOWN_RECOVERY_METRICS_BASE_REGISTRY_076_150 = {
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
    for n, c in F30_DRAWDOWN_RECOVERY_METRICS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
