# f21_raw_volume_metrics_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _vol_zscore_val(v, w):
    return (v - v.rolling(w).mean()) / v.rolling(w).std().replace(0, np.nan)

def _rel_vol(v, w):
    return v / v.rolling(w).mean().replace(0, np.nan)

def _dollar_vol_intensity(v, closeadj, w):
    dv = v * closeadj
    return dv / dv.rolling(w).mean().replace(0, np.nan)

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

# Generating 150 jerk features using combinations of primitives and ROC windows
# Jerk = pct_change(w).diff(w)

def f21rvm_f21_raw_volume_metrics_vol_zscore_5d_jerk_5d_v001_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_5d_jerk_10d_v002_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_10d_jerk_5d_v003_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_10d_jerk_10d_v004_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_21d_jerk_21d_v005_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_21d_jerk_63d_v006_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_63d_jerk_21d_v007_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_63d_jerk_63d_v008_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 63).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_126d_jerk_63d_v009_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 126).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_126d_jerk_126d_v010_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 126).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_252d_jerk_63d_v011_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 252).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_252d_jerk_252d_v012_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 252).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_5d_jerk_5d_v013_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_5d_jerk_10d_v014_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_10d_jerk_5d_v015_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_10d_jerk_10d_v016_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_21d_jerk_21d_v017_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_21d_jerk_63d_v018_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_63d_jerk_21d_v019_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_63d_jerk_63d_v020_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_126d_jerk_63d_v021_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_126d_jerk_126d_v022_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_252d_jerk_63d_v023_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_252d_jerk_252d_v024_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_21d_jerk_5d_v025_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_21d_jerk_21d_v026_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_63d_jerk_21d_v027_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_63d_jerk_63d_v028_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_126d_jerk_63d_v029_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_126d_jerk_126d_v030_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_252d_jerk_63d_v031_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 252).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_252d_jerk_252d_v032_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 252).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Combinations to reach 150
def f21rvm_f21_raw_volume_metrics_vol_zscore_5d_jerk_21d_v033_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_21d_jerk_5d_v034_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_63d_jerk_5d_v035_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 63).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_126d_jerk_21d_v036_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 126).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_21d_jerk_5d_v037_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_63d_jerk_5d_v038_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_126d_jerk_21d_v039_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_63d_jerk_5d_v040_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_5d_jerk_63d_v041_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_10d_jerk_21d_v042_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_21d_jerk_10d_v043_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_10d_jerk_21d_v044_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_21d_jerk_10d_v045_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_21d_jerk_10d_v046_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma5_vol_zscore_21d_jerk_5d_v047_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 21), 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma10_vol_zscore_63d_jerk_10d_v048_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 63), 10).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma5_rel_vol_21d_jerk_5d_v049_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 21), 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma10_rel_vol_63d_jerk_10d_v050_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 63), 10).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_5d_jerk_126d_v051_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_10d_jerk_63d_v052_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_21d_jerk_126d_v053_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_5d_jerk_63d_v054_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_10d_jerk_63d_v055_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_21d_jerk_126d_v056_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_63d_jerk_252d_v057_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_126d_jerk_21d_v058_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_63d_jerk_126d_v059_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 63).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_252d_jerk_21d_v060_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 252).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_63d_jerk_126d_v061_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_252d_jerk_21d_v062_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_252d_jerk_21d_v063_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 252).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_21d_jerk_63d_v064_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_5d_jerk_252d_v065_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 5).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_21d_jerk_252d_v066_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 21).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_5d_jerk_252d_v067_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_21d_jerk_252d_v068_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 21).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_21d_jerk_126d_v069_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_63d_jerk_126d_v070_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_126d_jerk_5d_v071_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 126).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_252d_jerk_5d_v072_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 252).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_126d_jerk_5d_v073_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_252d_jerk_5d_v074_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_126d_jerk_5d_v075_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_252d_jerk_5d_v076_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 252).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_126d_jerk_10d_v077_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 126).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_252d_jerk_10d_v078_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 252).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_126d_jerk_10d_v079_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_252d_jerk_10d_v080_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_126d_jerk_10d_v081_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 126).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_252d_jerk_10d_v082_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 252).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_63d_jerk_10d_v083_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 63).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_63d_jerk_10d_v084_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 63).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_63d_jerk_10d_v085_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 63).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_10d_jerk_252d_v086_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 10).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_10d_jerk_252d_v087_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 10).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_dollar_vol_int_10d_jerk_252d_v088_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _dollar_vol_intensity(volume, closeadj, 21).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)





































def f21rvm_f21_raw_volume_metrics_vol_zscore_126d_jerk_252d_v2_v125_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 126).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_126d_jerk_252d_v2_v126_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 126).pct_change(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_vol_zscore_252d_jerk_126d_v2_v127_signal(volume: pd.Series) -> pd.Series:
    res = _vol_zscore_val(volume, 252).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_rel_vol_252d_jerk_126d_v2_v128_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 252).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)


def f21rvm_f21_raw_volume_metrics_rel_vol_5d_jerk_21d_v2_v130_signal(volume: pd.Series) -> pd.Series:
    res = _rel_vol(volume, 5).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)











def f21rvm_f21_raw_volume_metrics_sma5_vol_zscore_21d_jerk_21d_v141_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 21), 5).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma10_vol_zscore_63d_jerk_63d_v142_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 63), 10).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma5_rel_vol_21d_jerk_21d_v143_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 21), 5).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma10_rel_vol_63d_jerk_63d_v144_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 63), 10).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma21_vol_zscore_126d_jerk_63d_v145_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 126), 21).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma21_rel_vol_126d_jerk_63d_v146_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 126), 21).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma63_vol_zscore_252d_jerk_126d_v147_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_vol_zscore_val(volume, 252), 63).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma63_rel_vol_252d_jerk_126d_v148_signal(volume: pd.Series) -> pd.Series:
    res = _sma(_rel_vol(volume, 252), 63).pct_change(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma5_dollar_vol_int_21d_jerk_21d_v149_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 21), 5).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21rvm_f21_raw_volume_metrics_sma10_dollar_vol_int_63d_jerk_63d_v150_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _sma(_dollar_vol_intensity(volume, closeadj, 63), 10).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["volume", "closeadj"]}

JERK_NAMES = [f for f in globals() if f.startswith("f21rvm_") and f.endswith("_signal")]

F21_RAW_VOLUME_METRICS_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000; d = pd.DataFrame({"volume": np.random.rand(sz)*1000000, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F21_RAW_VOLUME_METRICS_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
