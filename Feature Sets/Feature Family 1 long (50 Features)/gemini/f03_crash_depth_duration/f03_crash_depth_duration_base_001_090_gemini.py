import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)
def _f03_depth(c, w): return (c / c.rolling(w, min_periods=1).max().replace(0, np.nan) - 1)
def _f03_dur(c, w): return (w - 1 - c.rolling(w, min_periods=1).apply(np.argmax, raw=True))

def f03_crash_depth_duration_depth_open_5d_base_v001_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_depth(arg_open, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_5d_base_v002_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_dur(arg_open, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_5d_base_v003_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 5) * _f03_dur(arg_open, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_5d_base_v004_signal(arg_open: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_open, 5), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_5d_base_v005_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 5) / 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_5d_base_v006_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 5) / (_f03_dur(arg_open, 5) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_5d_base_v007_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_depth(arg_high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_5d_base_v008_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_dur(arg_high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_5d_base_v009_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 5) * _f03_dur(arg_high, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_5d_base_v010_signal(arg_high: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_high, 5), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_5d_base_v011_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 5) / 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_5d_base_v012_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 5) / (_f03_dur(arg_high, 5) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_5d_base_v013_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_depth(arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_5d_base_v014_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_dur(arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_5d_base_v015_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 5) * _f03_dur(arg_low, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_5d_base_v016_signal(arg_low: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_low, 5), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_5d_base_v017_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 5) / 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_5d_base_v018_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 5) / (_f03_dur(arg_low, 5) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_5d_base_v019_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_depth(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_5d_base_v020_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_dur(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_5d_base_v021_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 5) * _f03_dur(arg_close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_5d_base_v022_signal(arg_close: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_close, 5), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_5d_base_v023_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 5) / 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_5d_base_v024_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 5) / (_f03_dur(arg_close, 5) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_5d_base_v025_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_depth(arg_closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_5d_base_v026_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_dur(arg_closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_5d_base_v027_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 5) * _f03_dur(arg_closeadj, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_5d_base_v028_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_closeadj, 5), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_5d_base_v029_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 5) / 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_5d_base_v030_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 5) / (_f03_dur(arg_closeadj, 5) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_10d_base_v031_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_depth(arg_open, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_10d_base_v032_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_dur(arg_open, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_10d_base_v033_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 10) * _f03_dur(arg_open, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_10d_base_v034_signal(arg_open: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_open, 10), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_10d_base_v035_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 10) / 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_10d_base_v036_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 10) / (_f03_dur(arg_open, 10) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_10d_base_v037_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_depth(arg_high, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_10d_base_v038_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_dur(arg_high, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_10d_base_v039_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 10) * _f03_dur(arg_high, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_10d_base_v040_signal(arg_high: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_high, 10), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_10d_base_v041_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 10) / 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_10d_base_v042_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 10) / (_f03_dur(arg_high, 10) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_10d_base_v043_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_depth(arg_low, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_10d_base_v044_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_dur(arg_low, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_10d_base_v045_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 10) * _f03_dur(arg_low, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_10d_base_v046_signal(arg_low: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_low, 10), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_10d_base_v047_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 10) / 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_10d_base_v048_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 10) / (_f03_dur(arg_low, 10) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_10d_base_v049_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_depth(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_10d_base_v050_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_dur(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_10d_base_v051_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 10) * _f03_dur(arg_close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_10d_base_v052_signal(arg_close: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_close, 10), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_10d_base_v053_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 10) / 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_10d_base_v054_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 10) / (_f03_dur(arg_close, 10) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_10d_base_v055_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_depth(arg_closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_10d_base_v056_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_dur(arg_closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_10d_base_v057_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 10) * _f03_dur(arg_closeadj, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_10d_base_v058_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_closeadj, 10), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_10d_base_v059_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 10) / 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_10d_base_v060_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 10) / (_f03_dur(arg_closeadj, 10) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_open_21d_base_v061_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_depth(arg_open, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_open_21d_base_v062_signal(arg_open: pd.Series) -> pd.Series:
    res = _f03_dur(arg_open, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_open_21d_base_v063_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 21) * _f03_dur(arg_open, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_open_21d_base_v064_signal(arg_open: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_open, 21), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_open_21d_base_v065_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_open, 21) / 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_open_21d_base_v066_signal(arg_open: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_open, 21) / (_f03_dur(arg_open, 21) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_high_21d_base_v067_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_depth(arg_high, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_high_21d_base_v068_signal(arg_high: pd.Series) -> pd.Series:
    res = _f03_dur(arg_high, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_high_21d_base_v069_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 21) * _f03_dur(arg_high, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_high_21d_base_v070_signal(arg_high: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_high, 21), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_high_21d_base_v071_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_high, 21) / 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_high_21d_base_v072_signal(arg_high: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_high, 21) / (_f03_dur(arg_high, 21) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_low_21d_base_v073_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_depth(arg_low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_low_21d_base_v074_signal(arg_low: pd.Series) -> pd.Series:
    res = _f03_dur(arg_low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_low_21d_base_v075_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 21) * _f03_dur(arg_low, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_low_21d_base_v076_signal(arg_low: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_low, 21), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_low_21d_base_v077_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_low, 21) / 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_low_21d_base_v078_signal(arg_low: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_low, 21) / (_f03_dur(arg_low, 21) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_close_21d_base_v079_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_depth(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_close_21d_base_v080_signal(arg_close: pd.Series) -> pd.Series:
    res = _f03_dur(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_close_21d_base_v081_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 21) * _f03_dur(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_close_21d_base_v082_signal(arg_close: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_close, 21), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_close_21d_base_v083_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_close, 21) / 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_close_21d_base_v084_signal(arg_close: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_close, 21) / (_f03_dur(arg_close, 21) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_closeadj_21d_base_v085_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_depth(arg_closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_closeadj_21d_base_v086_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _f03_dur(arg_closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_severity_closeadj_21d_base_v087_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 21) * _f03_dur(arg_closeadj, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_zscore_closeadj_21d_base_v088_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = _z(_f03_depth(arg_closeadj, 21), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_dur_norm_closeadj_21d_base_v089_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_dur(arg_closeadj, 21) / 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_crash_depth_duration_depth_norm_closeadj_21d_base_v090_signal(arg_closeadj: pd.Series) -> pd.Series:
    res = (_f03_depth(arg_closeadj, 21) / (_f03_dur(arg_closeadj, 21) + 1))
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f03_crash_depth_duration_depth_open_5d_base_v001_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_5d_base_v001_signal},
    "f03_crash_depth_duration_dur_open_5d_base_v002_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_5d_base_v002_signal},
    "f03_crash_depth_duration_severity_open_5d_base_v003_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_5d_base_v003_signal},
    "f03_crash_depth_duration_depth_zscore_open_5d_base_v004_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_5d_base_v004_signal},
    "f03_crash_depth_duration_dur_norm_open_5d_base_v005_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_5d_base_v005_signal},
    "f03_crash_depth_duration_depth_norm_open_5d_base_v006_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_5d_base_v006_signal},
    "f03_crash_depth_duration_depth_high_5d_base_v007_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_5d_base_v007_signal},
    "f03_crash_depth_duration_dur_high_5d_base_v008_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_5d_base_v008_signal},
    "f03_crash_depth_duration_severity_high_5d_base_v009_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_5d_base_v009_signal},
    "f03_crash_depth_duration_depth_zscore_high_5d_base_v010_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_5d_base_v010_signal},
    "f03_crash_depth_duration_dur_norm_high_5d_base_v011_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_5d_base_v011_signal},
    "f03_crash_depth_duration_depth_norm_high_5d_base_v012_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_5d_base_v012_signal},
    "f03_crash_depth_duration_depth_low_5d_base_v013_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_5d_base_v013_signal},
    "f03_crash_depth_duration_dur_low_5d_base_v014_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_5d_base_v014_signal},
    "f03_crash_depth_duration_severity_low_5d_base_v015_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_5d_base_v015_signal},
    "f03_crash_depth_duration_depth_zscore_low_5d_base_v016_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_5d_base_v016_signal},
    "f03_crash_depth_duration_dur_norm_low_5d_base_v017_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_5d_base_v017_signal},
    "f03_crash_depth_duration_depth_norm_low_5d_base_v018_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_5d_base_v018_signal},
    "f03_crash_depth_duration_depth_close_5d_base_v019_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_5d_base_v019_signal},
    "f03_crash_depth_duration_dur_close_5d_base_v020_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_5d_base_v020_signal},
    "f03_crash_depth_duration_severity_close_5d_base_v021_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_5d_base_v021_signal},
    "f03_crash_depth_duration_depth_zscore_close_5d_base_v022_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_5d_base_v022_signal},
    "f03_crash_depth_duration_dur_norm_close_5d_base_v023_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_5d_base_v023_signal},
    "f03_crash_depth_duration_depth_norm_close_5d_base_v024_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_5d_base_v024_signal},
    "f03_crash_depth_duration_depth_closeadj_5d_base_v025_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_5d_base_v025_signal},
    "f03_crash_depth_duration_dur_closeadj_5d_base_v026_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_5d_base_v026_signal},
    "f03_crash_depth_duration_severity_closeadj_5d_base_v027_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_5d_base_v027_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_5d_base_v028_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_5d_base_v028_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_5d_base_v029_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_5d_base_v029_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_5d_base_v030_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_5d_base_v030_signal},
    "f03_crash_depth_duration_depth_open_10d_base_v031_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_10d_base_v031_signal},
    "f03_crash_depth_duration_dur_open_10d_base_v032_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_10d_base_v032_signal},
    "f03_crash_depth_duration_severity_open_10d_base_v033_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_10d_base_v033_signal},
    "f03_crash_depth_duration_depth_zscore_open_10d_base_v034_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_10d_base_v034_signal},
    "f03_crash_depth_duration_dur_norm_open_10d_base_v035_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_10d_base_v035_signal},
    "f03_crash_depth_duration_depth_norm_open_10d_base_v036_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_10d_base_v036_signal},
    "f03_crash_depth_duration_depth_high_10d_base_v037_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_10d_base_v037_signal},
    "f03_crash_depth_duration_dur_high_10d_base_v038_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_10d_base_v038_signal},
    "f03_crash_depth_duration_severity_high_10d_base_v039_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_10d_base_v039_signal},
    "f03_crash_depth_duration_depth_zscore_high_10d_base_v040_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_10d_base_v040_signal},
    "f03_crash_depth_duration_dur_norm_high_10d_base_v041_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_10d_base_v041_signal},
    "f03_crash_depth_duration_depth_norm_high_10d_base_v042_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_10d_base_v042_signal},
    "f03_crash_depth_duration_depth_low_10d_base_v043_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_10d_base_v043_signal},
    "f03_crash_depth_duration_dur_low_10d_base_v044_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_10d_base_v044_signal},
    "f03_crash_depth_duration_severity_low_10d_base_v045_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_10d_base_v045_signal},
    "f03_crash_depth_duration_depth_zscore_low_10d_base_v046_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_10d_base_v046_signal},
    "f03_crash_depth_duration_dur_norm_low_10d_base_v047_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_10d_base_v047_signal},
    "f03_crash_depth_duration_depth_norm_low_10d_base_v048_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_10d_base_v048_signal},
    "f03_crash_depth_duration_depth_close_10d_base_v049_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_10d_base_v049_signal},
    "f03_crash_depth_duration_dur_close_10d_base_v050_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_10d_base_v050_signal},
    "f03_crash_depth_duration_severity_close_10d_base_v051_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_10d_base_v051_signal},
    "f03_crash_depth_duration_depth_zscore_close_10d_base_v052_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_10d_base_v052_signal},
    "f03_crash_depth_duration_dur_norm_close_10d_base_v053_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_10d_base_v053_signal},
    "f03_crash_depth_duration_depth_norm_close_10d_base_v054_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_10d_base_v054_signal},
    "f03_crash_depth_duration_depth_closeadj_10d_base_v055_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_10d_base_v055_signal},
    "f03_crash_depth_duration_dur_closeadj_10d_base_v056_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_10d_base_v056_signal},
    "f03_crash_depth_duration_severity_closeadj_10d_base_v057_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_10d_base_v057_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_10d_base_v058_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_10d_base_v058_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_10d_base_v059_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_10d_base_v059_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_10d_base_v060_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_10d_base_v060_signal},
    "f03_crash_depth_duration_depth_open_21d_base_v061_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_open_21d_base_v061_signal},
    "f03_crash_depth_duration_dur_open_21d_base_v062_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_open_21d_base_v062_signal},
    "f03_crash_depth_duration_severity_open_21d_base_v063_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_severity_open_21d_base_v063_signal},
    "f03_crash_depth_duration_depth_zscore_open_21d_base_v064_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_zscore_open_21d_base_v064_signal},
    "f03_crash_depth_duration_dur_norm_open_21d_base_v065_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_dur_norm_open_21d_base_v065_signal},
    "f03_crash_depth_duration_depth_norm_open_21d_base_v066_signal": {"inputs": ["open"], "func": f03_crash_depth_duration_depth_norm_open_21d_base_v066_signal},
    "f03_crash_depth_duration_depth_high_21d_base_v067_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_high_21d_base_v067_signal},
    "f03_crash_depth_duration_dur_high_21d_base_v068_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_high_21d_base_v068_signal},
    "f03_crash_depth_duration_severity_high_21d_base_v069_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_severity_high_21d_base_v069_signal},
    "f03_crash_depth_duration_depth_zscore_high_21d_base_v070_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_zscore_high_21d_base_v070_signal},
    "f03_crash_depth_duration_dur_norm_high_21d_base_v071_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_dur_norm_high_21d_base_v071_signal},
    "f03_crash_depth_duration_depth_norm_high_21d_base_v072_signal": {"inputs": ["high"], "func": f03_crash_depth_duration_depth_norm_high_21d_base_v072_signal},
    "f03_crash_depth_duration_depth_low_21d_base_v073_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_low_21d_base_v073_signal},
    "f03_crash_depth_duration_dur_low_21d_base_v074_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_low_21d_base_v074_signal},
    "f03_crash_depth_duration_severity_low_21d_base_v075_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_severity_low_21d_base_v075_signal},
    "f03_crash_depth_duration_depth_zscore_low_21d_base_v076_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_zscore_low_21d_base_v076_signal},
    "f03_crash_depth_duration_dur_norm_low_21d_base_v077_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_dur_norm_low_21d_base_v077_signal},
    "f03_crash_depth_duration_depth_norm_low_21d_base_v078_signal": {"inputs": ["low"], "func": f03_crash_depth_duration_depth_norm_low_21d_base_v078_signal},
    "f03_crash_depth_duration_depth_close_21d_base_v079_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_close_21d_base_v079_signal},
    "f03_crash_depth_duration_dur_close_21d_base_v080_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_close_21d_base_v080_signal},
    "f03_crash_depth_duration_severity_close_21d_base_v081_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_severity_close_21d_base_v081_signal},
    "f03_crash_depth_duration_depth_zscore_close_21d_base_v082_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_zscore_close_21d_base_v082_signal},
    "f03_crash_depth_duration_dur_norm_close_21d_base_v083_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_dur_norm_close_21d_base_v083_signal},
    "f03_crash_depth_duration_depth_norm_close_21d_base_v084_signal": {"inputs": ["close"], "func": f03_crash_depth_duration_depth_norm_close_21d_base_v084_signal},
    "f03_crash_depth_duration_depth_closeadj_21d_base_v085_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_closeadj_21d_base_v085_signal},
    "f03_crash_depth_duration_dur_closeadj_21d_base_v086_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_closeadj_21d_base_v086_signal},
    "f03_crash_depth_duration_severity_closeadj_21d_base_v087_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_severity_closeadj_21d_base_v087_signal},
    "f03_crash_depth_duration_depth_zscore_closeadj_21d_base_v088_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_zscore_closeadj_21d_base_v088_signal},
    "f03_crash_depth_duration_dur_norm_closeadj_21d_base_v089_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_dur_norm_closeadj_21d_base_v089_signal},
    "f03_crash_depth_duration_depth_norm_closeadj_21d_base_v090_signal": {"inputs": ["closeadj"], "func": f03_crash_depth_duration_depth_norm_closeadj_21d_base_v090_signal}
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
