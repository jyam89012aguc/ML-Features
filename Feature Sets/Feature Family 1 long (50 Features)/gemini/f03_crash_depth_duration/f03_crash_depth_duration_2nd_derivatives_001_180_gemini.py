import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)
def _f03_depth(c, w): return (c / c.rolling(w, min_periods=1).max().replace(0, np.nan) - 1)
def _f03_dur(c, w): return (w - 1 - c.rolling(w, min_periods=1).apply(np.argmax, raw=True))

def f03_crash_depth_duration_depth_open_5d_slope_v001_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_5d_slope_v002_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_5d_slope_v003_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 5) * _f03_dur(arg_open, 5))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_5d_slope_v004_signal(arg_open: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_open, 5), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_5d_slope_v005_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_open, 5) / 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_5d_slope_v006_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 5) / (_f03_dur(arg_open, 5) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_5d_slope_v007_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_5d_slope_v008_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_5d_slope_v009_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 5) * _f03_dur(arg_high, 5))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_5d_slope_v010_signal(arg_high: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_high, 5), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_5d_slope_v011_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_high, 5) / 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_5d_slope_v012_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 5) / (_f03_dur(arg_high, 5) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_5d_slope_v013_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_5d_slope_v014_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_5d_slope_v015_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 5) * _f03_dur(arg_low, 5))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_5d_slope_v016_signal(arg_low: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_low, 5), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_5d_slope_v017_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_low, 5) / 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_5d_slope_v018_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 5) / (_f03_dur(arg_low, 5) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_5d_slope_v019_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_5d_slope_v020_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_5d_slope_v021_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 5) * _f03_dur(arg_close, 5))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_5d_slope_v022_signal(arg_close: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_close, 5), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_5d_slope_v023_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_close, 5) / 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_5d_slope_v024_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 5) / (_f03_dur(arg_close, 5) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_5d_slope_v025_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_5d_slope_v026_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_5d_slope_v027_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 5) * _f03_dur(arg_closeadj, 5))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_5d_slope_v028_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_closeadj, 5), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_5d_slope_v029_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_closeadj, 5) / 5)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_5d_slope_v030_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 5) / (_f03_dur(arg_closeadj, 5) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_10d_slope_v031_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_10d_slope_v032_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_10d_slope_v033_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 10) * _f03_dur(arg_open, 10))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_10d_slope_v034_signal(arg_open: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_open, 10), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_10d_slope_v035_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_open, 10) / 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_10d_slope_v036_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 10) / (_f03_dur(arg_open, 10) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_10d_slope_v037_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_10d_slope_v038_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_10d_slope_v039_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 10) * _f03_dur(arg_high, 10))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_10d_slope_v040_signal(arg_high: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_high, 10), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_10d_slope_v041_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_high, 10) / 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_10d_slope_v042_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 10) / (_f03_dur(arg_high, 10) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_10d_slope_v043_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_10d_slope_v044_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_10d_slope_v045_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 10) * _f03_dur(arg_low, 10))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_10d_slope_v046_signal(arg_low: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_low, 10), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_10d_slope_v047_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_low, 10) / 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_10d_slope_v048_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 10) / (_f03_dur(arg_low, 10) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_10d_slope_v049_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_10d_slope_v050_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_10d_slope_v051_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 10) * _f03_dur(arg_close, 10))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_10d_slope_v052_signal(arg_close: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_close, 10), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_10d_slope_v053_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_close, 10) / 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_10d_slope_v054_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 10) / (_f03_dur(arg_close, 10) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_10d_slope_v055_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_10d_slope_v056_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_10d_slope_v057_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 10) * _f03_dur(arg_closeadj, 10))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_10d_slope_v058_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_closeadj, 10), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_10d_slope_v059_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_closeadj, 10) / 10)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_10d_slope_v060_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 10) / (_f03_dur(arg_closeadj, 10) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_21d_slope_v061_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_21d_slope_v062_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_21d_slope_v063_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 21) * _f03_dur(arg_open, 21))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_21d_slope_v064_signal(arg_open: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_open, 21), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_21d_slope_v065_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_open, 21) / 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_21d_slope_v066_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 21) / (_f03_dur(arg_open, 21) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_21d_slope_v067_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_21d_slope_v068_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_21d_slope_v069_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 21) * _f03_dur(arg_high, 21))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_21d_slope_v070_signal(arg_high: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_high, 21), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_21d_slope_v071_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_high, 21) / 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_21d_slope_v072_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 21) / (_f03_dur(arg_high, 21) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_21d_slope_v073_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_21d_slope_v074_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_21d_slope_v075_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 21) * _f03_dur(arg_low, 21))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_21d_slope_v076_signal(arg_low: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_low, 21), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_21d_slope_v077_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_low, 21) / 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_21d_slope_v078_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 21) / (_f03_dur(arg_low, 21) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_21d_slope_v079_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_21d_slope_v080_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_21d_slope_v081_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 21) * _f03_dur(arg_close, 21))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_21d_slope_v082_signal(arg_close: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_close, 21), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_21d_slope_v083_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_close, 21) / 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_21d_slope_v084_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 21) / (_f03_dur(arg_close, 21) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_21d_slope_v085_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_21d_slope_v086_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_21d_slope_v087_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 21) * _f03_dur(arg_closeadj, 21))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_21d_slope_v088_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_closeadj, 21), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_21d_slope_v089_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_closeadj, 21) / 21)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_21d_slope_v090_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 21) / (_f03_dur(arg_closeadj, 21) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_63d_slope_v091_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_63d_slope_v092_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_63d_slope_v093_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 63) * _f03_dur(arg_open, 63))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_63d_slope_v094_signal(arg_open: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_open, 63), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_63d_slope_v095_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_open, 63) / 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_63d_slope_v096_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 63) / (_f03_dur(arg_open, 63) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_63d_slope_v097_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_63d_slope_v098_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_63d_slope_v099_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 63) * _f03_dur(arg_high, 63))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_63d_slope_v100_signal(arg_high: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_high, 63), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_63d_slope_v101_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_high, 63) / 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_63d_slope_v102_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 63) / (_f03_dur(arg_high, 63) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_63d_slope_v103_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_63d_slope_v104_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_63d_slope_v105_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 63) * _f03_dur(arg_low, 63))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_63d_slope_v106_signal(arg_low: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_low, 63), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_63d_slope_v107_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_low, 63) / 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_63d_slope_v108_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 63) / (_f03_dur(arg_low, 63) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_63d_slope_v109_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_63d_slope_v110_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_63d_slope_v111_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 63) * _f03_dur(arg_close, 63))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_63d_slope_v112_signal(arg_close: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_close, 63), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_63d_slope_v113_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_close, 63) / 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_63d_slope_v114_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 63) / (_f03_dur(arg_close, 63) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_63d_slope_v115_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_63d_slope_v116_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_63d_slope_v117_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 63) * _f03_dur(arg_closeadj, 63))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_63d_slope_v118_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_closeadj, 63), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_63d_slope_v119_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_closeadj, 63) / 63)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_63d_slope_v120_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 63) / (_f03_dur(arg_closeadj, 63) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_126d_slope_v121_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_126d_slope_v122_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_126d_slope_v123_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 126) * _f03_dur(arg_open, 126))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_126d_slope_v124_signal(arg_open: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_open, 126), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_126d_slope_v125_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_open, 126) / 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_126d_slope_v126_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 126) / (_f03_dur(arg_open, 126) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_126d_slope_v127_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_126d_slope_v128_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_126d_slope_v129_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 126) * _f03_dur(arg_high, 126))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_126d_slope_v130_signal(arg_high: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_high, 126), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_126d_slope_v131_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_high, 126) / 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_126d_slope_v132_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 126) / (_f03_dur(arg_high, 126) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_126d_slope_v133_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_126d_slope_v134_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_126d_slope_v135_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 126) * _f03_dur(arg_low, 126))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_126d_slope_v136_signal(arg_low: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_low, 126), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_126d_slope_v137_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_low, 126) / 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_126d_slope_v138_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 126) / (_f03_dur(arg_low, 126) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_126d_slope_v139_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_126d_slope_v140_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_126d_slope_v141_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 126) * _f03_dur(arg_close, 126))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_126d_slope_v142_signal(arg_close: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_close, 126), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_126d_slope_v143_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_close, 126) / 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_126d_slope_v144_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 126) / (_f03_dur(arg_close, 126) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_126d_slope_v145_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_126d_slope_v146_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_126d_slope_v147_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 126) * _f03_dur(arg_closeadj, 126))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_126d_slope_v148_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_closeadj, 126), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_126d_slope_v149_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_closeadj, 126) / 126)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_126d_slope_v150_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 126) / (_f03_dur(arg_closeadj, 126) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_252d_slope_v151_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_252d_slope_v152_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_252d_slope_v153_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 252) * _f03_dur(arg_open, 252))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_252d_slope_v154_signal(arg_open: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_open, 252), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_252d_slope_v155_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_open, 252) / 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_252d_slope_v156_signal(arg_open: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_open, 252) / (_f03_dur(arg_open, 252) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_252d_slope_v157_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_252d_slope_v158_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_252d_slope_v159_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 252) * _f03_dur(arg_high, 252))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_252d_slope_v160_signal(arg_high: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_high, 252), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_252d_slope_v161_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_high, 252) / 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_252d_slope_v162_signal(arg_high: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_high, 252) / (_f03_dur(arg_high, 252) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_252d_slope_v163_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_252d_slope_v164_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_252d_slope_v165_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 252) * _f03_dur(arg_low, 252))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_252d_slope_v166_signal(arg_low: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_low, 252), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_252d_slope_v167_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_low, 252) / 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_252d_slope_v168_signal(arg_low: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_low, 252) / (_f03_dur(arg_low, 252) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_252d_slope_v169_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_252d_slope_v170_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_252d_slope_v171_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 252) * _f03_dur(arg_close, 252))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_252d_slope_v172_signal(arg_close: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_close, 252), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_252d_slope_v173_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_close, 252) / 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_252d_slope_v174_signal(arg_close: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_close, 252) / (_f03_dur(arg_close, 252) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_252d_slope_v175_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_252d_slope_v176_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_252d_slope_v177_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 252) * _f03_dur(arg_closeadj, 252))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_252d_slope_v178_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_z(_f03_depth(arg_closeadj, 252), 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_252d_slope_v179_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_dur(arg_closeadj, 252) / 252)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_252d_slope_v180_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = ((_f03_depth(arg_closeadj, 252) / (_f03_dur(arg_closeadj, 252) + 1))).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f03_crash_depth_duration_depth_open_5d_slope_v001_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_5d_slope_v001_signal},
    "f03_crash_depth_duration_dur_open_5d_slope_v002_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_5d_slope_v002_signal},
    "f03_crash_depth_duration_severity_open_5d_slope_v003_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_5d_slope_v003_signal},
    "f03_crash_depth_duration_depth_zscore_open_5d_slope_v004_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_5d_slope_v004_signal},
    "f03_crash_depth_duration_dur_norm_open_5d_slope_v005_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_5d_slope_v005_signal},
    "f03_crash_depth_duration_depth_norm_open_5d_slope_v006_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_5d_slope_v006_signal},
    "f03_crash_depth_duration_depth_high_5d_slope_v007_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_5d_slope_v007_signal},
    "f03_crash_depth_duration_dur_high_5d_slope_v008_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_5d_slope_v008_signal},
    "f03_crash_depth_duration_severity_high_5d_slope_v009_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_5d_slope_v009_signal},
    "f03_crash_depth_duration_depth_zscore_high_5d_slope_v010_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_5d_slope_v010_signal},
    "f03_crash_depth_duration_dur_norm_high_5d_slope_v011_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_5d_slope_v011_signal},
    "f03_crash_depth_duration_depth_norm_high_5d_slope_v012_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_5d_slope_v012_signal},
    "f03_crash_depth_duration_depth_low_5d_slope_v013_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_5d_slope_v013_signal},
    "f03_crash_depth_duration_dur_low_5d_slope_v014_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_5d_slope_v014_signal},
    "f03_crash_depth_duration_severity_low_5d_slope_v015_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_5d_slope_v015_signal},
    "f03_crash_depth_duration_depth_zscore_low_5d_slope_v016_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_5d_slope_v016_signal},
    "f03_crash_depth_duration_dur_norm_low_5d_slope_v017_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_5d_slope_v017_signal},
    "f03_crash_depth_duration_depth_norm_low_5d_slope_v018_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_5d_slope_v018_signal},
    "f03_crash_depth_duration_depth_close_5d_slope_v019_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_5d_slope_v019_signal},
    "f03_crash_depth_duration_dur_close_5d_slope_v020_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_5d_slope_v020_signal},
    "f03_crash_depth_duration_severity_close_5d_slope_v021_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_5d_slope_v021_signal},
    "f03_crash_depth_duration_depth_zscore_close_5d_slope_v022_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_5d_slope_v022_signal},
    "f03_crash_depth_duration_dur_norm_close_5d_slope_v023_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_5d_slope_v023_signal},
    "f03_crash_depth_duration_depth_norm_close_5d_slope_v024_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_5d_slope_v024_signal},
    "f03_crash_depth_duration_depth_closeadj_5d_slope_v025_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_5d_slope_v025_signal},
    "f03_crash_depth_duration_dur_closeadj_5d_slope_v026_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_5d_slope_v026_signal},
    "f03_crash_depth_duration_severity_closeadj_5d_slope_v027_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_5d_slope_v027_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_5d_slope_v028_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_5d_slope_v028_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_5d_slope_v029_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_5d_slope_v029_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_5d_slope_v030_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_5d_slope_v030_signal},
    "f03_crash_depth_duration_depth_open_10d_slope_v031_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_10d_slope_v031_signal},
    "f03_crash_depth_duration_dur_open_10d_slope_v032_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_10d_slope_v032_signal},
    "f03_crash_depth_duration_severity_open_10d_slope_v033_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_10d_slope_v033_signal},
    "f03_crash_depth_duration_depth_zscore_open_10d_slope_v034_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_10d_slope_v034_signal},
    "f03_crash_depth_duration_dur_norm_open_10d_slope_v035_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_10d_slope_v035_signal},
    "f03_crash_depth_duration_depth_norm_open_10d_slope_v036_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_10d_slope_v036_signal},
    "f03_crash_depth_duration_depth_high_10d_slope_v037_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_10d_slope_v037_signal},
    "f03_crash_depth_duration_dur_high_10d_slope_v038_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_10d_slope_v038_signal},
    "f03_crash_depth_duration_severity_high_10d_slope_v039_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_10d_slope_v039_signal},
    "f03_crash_depth_duration_depth_zscore_high_10d_slope_v040_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_10d_slope_v040_signal},
    "f03_crash_depth_duration_dur_norm_high_10d_slope_v041_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_10d_slope_v041_signal},
    "f03_crash_depth_duration_depth_norm_high_10d_slope_v042_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_10d_slope_v042_signal},
    "f03_crash_depth_duration_depth_low_10d_slope_v043_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_10d_slope_v043_signal},
    "f03_crash_depth_duration_dur_low_10d_slope_v044_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_10d_slope_v044_signal},
    "f03_crash_depth_duration_severity_low_10d_slope_v045_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_10d_slope_v045_signal},
    "f03_crash_depth_duration_depth_zscore_low_10d_slope_v046_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_10d_slope_v046_signal},
    "f03_crash_depth_duration_dur_norm_low_10d_slope_v047_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_10d_slope_v047_signal},
    "f03_crash_depth_duration_depth_norm_low_10d_slope_v048_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_10d_slope_v048_signal},
    "f03_crash_depth_duration_depth_close_10d_slope_v049_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_10d_slope_v049_signal},
    "f03_crash_depth_duration_dur_close_10d_slope_v050_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_10d_slope_v050_signal},
    "f03_crash_depth_duration_severity_close_10d_slope_v051_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_10d_slope_v051_signal},
    "f03_crash_depth_duration_depth_zscore_close_10d_slope_v052_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_10d_slope_v052_signal},
    "f03_crash_depth_duration_dur_norm_close_10d_slope_v053_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_10d_slope_v053_signal},
    "f03_crash_depth_duration_depth_norm_close_10d_slope_v054_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_10d_slope_v054_signal},
    "f03_crash_depth_duration_depth_closeadj_10d_slope_v055_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_10d_slope_v055_signal},
    "f03_crash_depth_duration_dur_closeadj_10d_slope_v056_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_10d_slope_v056_signal},
    "f03_crash_depth_duration_severity_closeadj_10d_slope_v057_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_10d_slope_v057_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_10d_slope_v058_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_10d_slope_v058_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_10d_slope_v059_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_10d_slope_v059_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_10d_slope_v060_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_10d_slope_v060_signal},
    "f03_crash_depth_duration_depth_open_21d_slope_v061_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_21d_slope_v061_signal},
    "f03_crash_depth_duration_dur_open_21d_slope_v062_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_21d_slope_v062_signal},
    "f03_crash_depth_duration_severity_open_21d_slope_v063_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_21d_slope_v063_signal},
    "f03_crash_depth_duration_depth_zscore_open_21d_slope_v064_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_21d_slope_v064_signal},
    "f03_crash_depth_duration_dur_norm_open_21d_slope_v065_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_21d_slope_v065_signal},
    "f03_crash_depth_duration_depth_norm_open_21d_slope_v066_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_21d_slope_v066_signal},
    "f03_crash_depth_duration_depth_high_21d_slope_v067_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_21d_slope_v067_signal},
    "f03_crash_depth_duration_dur_high_21d_slope_v068_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_21d_slope_v068_signal},
    "f03_crash_depth_duration_severity_high_21d_slope_v069_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_21d_slope_v069_signal},
    "f03_crash_depth_duration_depth_zscore_high_21d_slope_v070_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_21d_slope_v070_signal},
    "f03_crash_depth_duration_dur_norm_high_21d_slope_v071_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_21d_slope_v071_signal},
    "f03_crash_depth_duration_depth_norm_high_21d_slope_v072_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_21d_slope_v072_signal},
    "f03_crash_depth_duration_depth_low_21d_slope_v073_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_21d_slope_v073_signal},
    "f03_crash_depth_duration_dur_low_21d_slope_v074_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_21d_slope_v074_signal},
    "f03_crash_depth_duration_severity_low_21d_slope_v075_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_21d_slope_v075_signal},
    "f03_crash_depth_duration_depth_zscore_low_21d_slope_v076_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_21d_slope_v076_signal},
    "f03_crash_depth_duration_dur_norm_low_21d_slope_v077_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_21d_slope_v077_signal},
    "f03_crash_depth_duration_depth_norm_low_21d_slope_v078_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_21d_slope_v078_signal},
    "f03_crash_depth_duration_depth_close_21d_slope_v079_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_21d_slope_v079_signal},
    "f03_crash_depth_duration_dur_close_21d_slope_v080_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_21d_slope_v080_signal},
    "f03_crash_depth_duration_severity_close_21d_slope_v081_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_21d_slope_v081_signal},
    "f03_crash_depth_duration_depth_zscore_close_21d_slope_v082_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_21d_slope_v082_signal},
    "f03_crash_depth_duration_dur_norm_close_21d_slope_v083_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_21d_slope_v083_signal},
    "f03_crash_depth_duration_depth_norm_close_21d_slope_v084_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_21d_slope_v084_signal},
    "f03_crash_depth_duration_depth_closeadj_21d_slope_v085_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_21d_slope_v085_signal},
    "f03_crash_depth_duration_dur_closeadj_21d_slope_v086_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_21d_slope_v086_signal},
    "f03_crash_depth_duration_severity_closeadj_21d_slope_v087_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_21d_slope_v087_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_21d_slope_v088_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_21d_slope_v088_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_21d_slope_v089_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_21d_slope_v089_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_21d_slope_v090_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_21d_slope_v090_signal},
    "f03_crash_depth_duration_depth_open_63d_slope_v091_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_63d_slope_v091_signal},
    "f03_crash_depth_duration_dur_open_63d_slope_v092_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_63d_slope_v092_signal},
    "f03_crash_depth_duration_severity_open_63d_slope_v093_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_63d_slope_v093_signal},
    "f03_crash_depth_duration_depth_zscore_open_63d_slope_v094_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_63d_slope_v094_signal},
    "f03_crash_depth_duration_dur_norm_open_63d_slope_v095_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_63d_slope_v095_signal},
    "f03_crash_depth_duration_depth_norm_open_63d_slope_v096_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_63d_slope_v096_signal},
    "f03_crash_depth_duration_depth_high_63d_slope_v097_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_63d_slope_v097_signal},
    "f03_crash_depth_duration_dur_high_63d_slope_v098_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_63d_slope_v098_signal},
    "f03_crash_depth_duration_severity_high_63d_slope_v099_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_63d_slope_v099_signal},
    "f03_crash_depth_duration_depth_zscore_high_63d_slope_v100_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_63d_slope_v100_signal},
    "f03_crash_depth_duration_dur_norm_high_63d_slope_v101_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_63d_slope_v101_signal},
    "f03_crash_depth_duration_depth_norm_high_63d_slope_v102_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_63d_slope_v102_signal},
    "f03_crash_depth_duration_depth_low_63d_slope_v103_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_63d_slope_v103_signal},
    "f03_crash_depth_duration_dur_low_63d_slope_v104_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_63d_slope_v104_signal},
    "f03_crash_depth_duration_severity_low_63d_slope_v105_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_63d_slope_v105_signal},
    "f03_crash_depth_duration_depth_zscore_low_63d_slope_v106_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_63d_slope_v106_signal},
    "f03_crash_depth_duration_dur_norm_low_63d_slope_v107_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_63d_slope_v107_signal},
    "f03_crash_depth_duration_depth_norm_low_63d_slope_v108_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_63d_slope_v108_signal},
    "f03_crash_depth_duration_depth_close_63d_slope_v109_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_63d_slope_v109_signal},
    "f03_crash_depth_duration_dur_close_63d_slope_v110_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_63d_slope_v110_signal},
    "f03_crash_depth_duration_severity_close_63d_slope_v111_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_63d_slope_v111_signal},
    "f03_crash_depth_duration_depth_zscore_close_63d_slope_v112_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_63d_slope_v112_signal},
    "f03_crash_depth_duration_dur_norm_close_63d_slope_v113_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_63d_slope_v113_signal},
    "f03_crash_depth_duration_depth_norm_close_63d_slope_v114_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_63d_slope_v114_signal},
    "f03_crash_depth_duration_depth_closeadj_63d_slope_v115_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_63d_slope_v115_signal},
    "f03_crash_depth_duration_dur_closeadj_63d_slope_v116_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_63d_slope_v116_signal},
    "f03_crash_depth_duration_severity_closeadj_63d_slope_v117_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_63d_slope_v117_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_63d_slope_v118_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_63d_slope_v118_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_63d_slope_v119_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_63d_slope_v119_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_63d_slope_v120_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_63d_slope_v120_signal},
    "f03_crash_depth_duration_depth_open_126d_slope_v121_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_126d_slope_v121_signal},
    "f03_crash_depth_duration_dur_open_126d_slope_v122_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_126d_slope_v122_signal},
    "f03_crash_depth_duration_severity_open_126d_slope_v123_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_126d_slope_v123_signal},
    "f03_crash_depth_duration_depth_zscore_open_126d_slope_v124_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_126d_slope_v124_signal},
    "f03_crash_depth_duration_dur_norm_open_126d_slope_v125_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_126d_slope_v125_signal},
    "f03_crash_depth_duration_depth_norm_open_126d_slope_v126_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_126d_slope_v126_signal},
    "f03_crash_depth_duration_depth_high_126d_slope_v127_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_126d_slope_v127_signal},
    "f03_crash_depth_duration_dur_high_126d_slope_v128_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_126d_slope_v128_signal},
    "f03_crash_depth_duration_severity_high_126d_slope_v129_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_126d_slope_v129_signal},
    "f03_crash_depth_duration_depth_zscore_high_126d_slope_v130_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_126d_slope_v130_signal},
    "f03_crash_depth_duration_dur_norm_high_126d_slope_v131_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_126d_slope_v131_signal},
    "f03_crash_depth_duration_depth_norm_high_126d_slope_v132_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_126d_slope_v132_signal},
    "f03_crash_depth_duration_depth_low_126d_slope_v133_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_126d_slope_v133_signal},
    "f03_crash_depth_duration_dur_low_126d_slope_v134_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_126d_slope_v134_signal},
    "f03_crash_depth_duration_severity_low_126d_slope_v135_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_126d_slope_v135_signal},
    "f03_crash_depth_duration_depth_zscore_low_126d_slope_v136_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_126d_slope_v136_signal},
    "f03_crash_depth_duration_dur_norm_low_126d_slope_v137_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_126d_slope_v137_signal},
    "f03_crash_depth_duration_depth_norm_low_126d_slope_v138_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_126d_slope_v138_signal},
    "f03_crash_depth_duration_depth_close_126d_slope_v139_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_126d_slope_v139_signal},
    "f03_crash_depth_duration_dur_close_126d_slope_v140_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_126d_slope_v140_signal},
    "f03_crash_depth_duration_severity_close_126d_slope_v141_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_126d_slope_v141_signal},
    "f03_crash_depth_duration_depth_zscore_close_126d_slope_v142_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_126d_slope_v142_signal},
    "f03_crash_depth_duration_dur_norm_close_126d_slope_v143_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_126d_slope_v143_signal},
    "f03_crash_depth_duration_depth_norm_close_126d_slope_v144_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_126d_slope_v144_signal},
    "f03_crash_depth_duration_depth_closeadj_126d_slope_v145_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_126d_slope_v145_signal},
    "f03_crash_depth_duration_dur_closeadj_126d_slope_v146_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_126d_slope_v146_signal},
    "f03_crash_depth_duration_severity_closeadj_126d_slope_v147_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_126d_slope_v147_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_126d_slope_v148_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_126d_slope_v148_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_126d_slope_v149_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_126d_slope_v149_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_126d_slope_v150_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_126d_slope_v150_signal},
    "f03_crash_depth_duration_depth_open_252d_slope_v151_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_252d_slope_v151_signal},
    "f03_crash_depth_duration_dur_open_252d_slope_v152_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_252d_slope_v152_signal},
    "f03_crash_depth_duration_severity_open_252d_slope_v153_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_252d_slope_v153_signal},
    "f03_crash_depth_duration_depth_zscore_open_252d_slope_v154_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_252d_slope_v154_signal},
    "f03_crash_depth_duration_dur_norm_open_252d_slope_v155_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_252d_slope_v155_signal},
    "f03_crash_depth_duration_depth_norm_open_252d_slope_v156_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_252d_slope_v156_signal},
    "f03_crash_depth_duration_depth_high_252d_slope_v157_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_252d_slope_v157_signal},
    "f03_crash_depth_duration_dur_high_252d_slope_v158_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_252d_slope_v158_signal},
    "f03_crash_depth_duration_severity_high_252d_slope_v159_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_252d_slope_v159_signal},
    "f03_crash_depth_duration_depth_zscore_high_252d_slope_v160_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_252d_slope_v160_signal},
    "f03_crash_depth_duration_dur_norm_high_252d_slope_v161_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_252d_slope_v161_signal},
    "f03_crash_depth_duration_depth_norm_high_252d_slope_v162_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_252d_slope_v162_signal},
    "f03_crash_depth_duration_depth_low_252d_slope_v163_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_252d_slope_v163_signal},
    "f03_crash_depth_duration_dur_low_252d_slope_v164_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_252d_slope_v164_signal},
    "f03_crash_depth_duration_severity_low_252d_slope_v165_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_252d_slope_v165_signal},
    "f03_crash_depth_duration_depth_zscore_low_252d_slope_v166_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_252d_slope_v166_signal},
    "f03_crash_depth_duration_dur_norm_low_252d_slope_v167_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_252d_slope_v167_signal},
    "f03_crash_depth_duration_depth_norm_low_252d_slope_v168_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_252d_slope_v168_signal},
    "f03_crash_depth_duration_depth_close_252d_slope_v169_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_252d_slope_v169_signal},
    "f03_crash_depth_duration_dur_close_252d_slope_v170_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_252d_slope_v170_signal},
    "f03_crash_depth_duration_severity_close_252d_slope_v171_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_252d_slope_v171_signal},
    "f03_crash_depth_duration_depth_zscore_close_252d_slope_v172_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_252d_slope_v172_signal},
    "f03_crash_depth_duration_dur_norm_close_252d_slope_v173_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_252d_slope_v173_signal},
    "f03_crash_depth_duration_depth_norm_close_252d_slope_v174_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_252d_slope_v174_signal},
    "f03_crash_depth_duration_depth_closeadj_252d_slope_v175_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_252d_slope_v175_signal},
    "f03_crash_depth_duration_dur_closeadj_252d_slope_v176_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_252d_slope_v176_signal},
    "f03_crash_depth_duration_severity_closeadj_252d_slope_v177_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_252d_slope_v177_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_252d_slope_v178_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_252d_slope_v178_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_252d_slope_v179_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_252d_slope_v179_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_252d_slope_v180_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_252d_slope_v180_signal}
}

if __name__ == "__main__":
    np.random.seed(42)
    n = 2500
    close = pd.Series(np.exp(np.random.normal(-0.02, 0.1, n).cumsum()) * 100)
    df = pd.DataFrame({
        'close': close, 'closeadj': close,
        'open': close.shift(1) * np.exp(np.random.normal(0, 0.02, n)),
        'high': close * np.exp(np.random.uniform(0, 0.05, n)),
        'low': close * np.exp(np.random.uniform(-0.05, 0, n)),
        'volume': np.random.randint(1000, 1000000, n).astype(float)
    }).ffill().bfill()
    
    for name, info in REGISTRY.items():
        res = info["func"](*[df[col] for col in info["inputs"]])
        assert len(res) > 0
        assert not res.isna().all()
    print("OK")
