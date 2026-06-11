import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _vwap_deviation(high, low, closeadj, volume, w):
    typical = (high + low + closeadj) / 3.0
    vwap = (typical * volume).rolling(w, min_periods=2).sum() / volume.rolling(w, min_periods=2).sum().replace(0, np.nan)
    return (closeadj - vwap) / vwap.abs().replace(0, np.nan)

# 5d level vwap
def f25vd_f25_vwap_deviation_vwap_level_5d_base_v001_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean vwap
def f25vd_f25_vwap_deviation_vwap_mean_5d_base_v002_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d var vwap
def f25vd_f25_vwap_deviation_vwap_std_5d_base_v003_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d zscore vwap
def f25vd_f25_vwap_deviation_vwap_zscore_5d_base_v004_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = _z(sig, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d change vwap
def f25vd_f25_vwap_deviation_vwap_delta_5d_base_v005_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q75gap vwap
def f25vd_f25_vwap_deviation_vwap_upper_gap_5d_base_v007_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q25gap vwap
def f25vd_f25_vwap_deviation_vwap_lower_gap_5d_base_v008_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d smean gap vwap
def f25vd_f25_vwap_deviation_vwap_short_mean_gap_5d_base_v009_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d energy vwap
def f25vd_f25_vwap_deviation_vwap_energy_5d_base_v010_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d ewm gap vwap
def f25vd_f25_vwap_deviation_vwap_ewm_gap_5d_base_v011_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d tail relief vwap
def f25vd_f25_vwap_deviation_vwap_tail_relief_5d_base_v012_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d peak fade vwap
def f25vd_f25_vwap_deviation_vwap_peak_fade_5d_base_v013_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d absmean vwap
def f25vd_f25_vwap_deviation_vwap_mean_abs_5d_base_v014_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d voladj chg vwap
def f25vd_f25_vwap_deviation_vwap_vol_adj_delta_5d_base_v015_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d level vwap
def f25vd_f25_vwap_deviation_vwap_level_10d_base_v016_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d mean vwap
def f25vd_f25_vwap_deviation_vwap_mean_10d_base_v017_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d var vwap
def f25vd_f25_vwap_deviation_vwap_std_10d_base_v018_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d zscore vwap
def f25vd_f25_vwap_deviation_vwap_zscore_10d_base_v019_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = _z(sig, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d change vwap
def f25vd_f25_vwap_deviation_vwap_delta_10d_base_v020_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q75gap vwap
def f25vd_f25_vwap_deviation_vwap_upper_gap_10d_base_v022_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q25gap vwap
def f25vd_f25_vwap_deviation_vwap_lower_gap_10d_base_v023_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d smean gap vwap
def f25vd_f25_vwap_deviation_vwap_short_mean_gap_10d_base_v024_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d energy vwap
def f25vd_f25_vwap_deviation_vwap_energy_10d_base_v025_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d ewm gap vwap
def f25vd_f25_vwap_deviation_vwap_ewm_gap_10d_base_v026_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d tail relief vwap
def f25vd_f25_vwap_deviation_vwap_tail_relief_10d_base_v027_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d peak fade vwap
def f25vd_f25_vwap_deviation_vwap_peak_fade_10d_base_v028_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d absmean vwap
def f25vd_f25_vwap_deviation_vwap_mean_abs_10d_base_v029_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d voladj chg vwap
def f25vd_f25_vwap_deviation_vwap_vol_adj_delta_10d_base_v030_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d level vwap
def f25vd_f25_vwap_deviation_vwap_level_15d_base_v031_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d mean vwap
def f25vd_f25_vwap_deviation_vwap_mean_15d_base_v032_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d var vwap
def f25vd_f25_vwap_deviation_vwap_std_15d_base_v033_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d zscore vwap
def f25vd_f25_vwap_deviation_vwap_zscore_15d_base_v034_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = _z(sig, 15)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d change vwap
def f25vd_f25_vwap_deviation_vwap_delta_15d_base_v035_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q75gap vwap
def f25vd_f25_vwap_deviation_vwap_upper_gap_15d_base_v037_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q25gap vwap
def f25vd_f25_vwap_deviation_vwap_lower_gap_15d_base_v038_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d smean gap vwap
def f25vd_f25_vwap_deviation_vwap_short_mean_gap_15d_base_v039_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d energy vwap
def f25vd_f25_vwap_deviation_vwap_energy_15d_base_v040_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d ewm gap vwap
def f25vd_f25_vwap_deviation_vwap_ewm_gap_15d_base_v041_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d tail relief vwap
def f25vd_f25_vwap_deviation_vwap_tail_relief_15d_base_v042_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d peak fade vwap
def f25vd_f25_vwap_deviation_vwap_peak_fade_15d_base_v043_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d absmean vwap
def f25vd_f25_vwap_deviation_vwap_mean_abs_15d_base_v044_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d voladj chg vwap
def f25vd_f25_vwap_deviation_vwap_vol_adj_delta_15d_base_v045_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level vwap
def f25vd_f25_vwap_deviation_vwap_level_21d_base_v046_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean vwap
def f25vd_f25_vwap_deviation_vwap_mean_21d_base_v047_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d var vwap
def f25vd_f25_vwap_deviation_vwap_std_21d_base_v048_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d zscore vwap
def f25vd_f25_vwap_deviation_vwap_zscore_21d_base_v049_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = _z(sig, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d change vwap
def f25vd_f25_vwap_deviation_vwap_delta_21d_base_v050_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q75gap vwap
def f25vd_f25_vwap_deviation_vwap_upper_gap_21d_base_v052_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q25gap vwap
def f25vd_f25_vwap_deviation_vwap_lower_gap_21d_base_v053_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smean gap vwap
def f25vd_f25_vwap_deviation_vwap_short_mean_gap_21d_base_v054_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d energy vwap
def f25vd_f25_vwap_deviation_vwap_energy_21d_base_v055_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ewm gap vwap
def f25vd_f25_vwap_deviation_vwap_ewm_gap_21d_base_v056_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d tail relief vwap
def f25vd_f25_vwap_deviation_vwap_tail_relief_21d_base_v057_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d peak fade vwap
def f25vd_f25_vwap_deviation_vwap_peak_fade_21d_base_v058_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d absmean vwap
def f25vd_f25_vwap_deviation_vwap_mean_abs_21d_base_v059_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d voladj chg vwap
def f25vd_f25_vwap_deviation_vwap_vol_adj_delta_21d_base_v060_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d level vwap
def f25vd_f25_vwap_deviation_vwap_level_42d_base_v061_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d mean vwap
def f25vd_f25_vwap_deviation_vwap_mean_42d_base_v062_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d var vwap
def f25vd_f25_vwap_deviation_vwap_std_42d_base_v063_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d zscore vwap
def f25vd_f25_vwap_deviation_vwap_zscore_42d_base_v064_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = _z(sig, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d change vwap
def f25vd_f25_vwap_deviation_vwap_delta_42d_base_v065_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q75gap vwap
def f25vd_f25_vwap_deviation_vwap_upper_gap_42d_base_v067_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q25gap vwap
def f25vd_f25_vwap_deviation_vwap_lower_gap_42d_base_v068_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d smean gap vwap
def f25vd_f25_vwap_deviation_vwap_short_mean_gap_42d_base_v069_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d energy vwap
def f25vd_f25_vwap_deviation_vwap_energy_42d_base_v070_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d ewm gap vwap
def f25vd_f25_vwap_deviation_vwap_ewm_gap_42d_base_v071_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d tail relief vwap
def f25vd_f25_vwap_deviation_vwap_tail_relief_42d_base_v072_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d peak fade vwap
def f25vd_f25_vwap_deviation_vwap_peak_fade_42d_base_v073_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d absmean vwap
def f25vd_f25_vwap_deviation_vwap_mean_abs_42d_base_v074_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d voladj chg vwap
def f25vd_f25_vwap_deviation_vwap_vol_adj_delta_42d_base_v075_signal(high, low, closeadj, volume):
    sig = _vwap_deviation(high, low, closeadj, volume, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['high', 'low', 'closeadj', 'volume'], "func": fn} for fn in [f25vd_f25_vwap_deviation_vwap_level_5d_base_v001_signal, f25vd_f25_vwap_deviation_vwap_mean_5d_base_v002_signal, f25vd_f25_vwap_deviation_vwap_std_5d_base_v003_signal, f25vd_f25_vwap_deviation_vwap_zscore_5d_base_v004_signal, f25vd_f25_vwap_deviation_vwap_delta_5d_base_v005_signal, f25vd_f25_vwap_deviation_vwap_upper_gap_5d_base_v007_signal, f25vd_f25_vwap_deviation_vwap_lower_gap_5d_base_v008_signal, f25vd_f25_vwap_deviation_vwap_short_mean_gap_5d_base_v009_signal, f25vd_f25_vwap_deviation_vwap_energy_5d_base_v010_signal, f25vd_f25_vwap_deviation_vwap_ewm_gap_5d_base_v011_signal, f25vd_f25_vwap_deviation_vwap_tail_relief_5d_base_v012_signal, f25vd_f25_vwap_deviation_vwap_peak_fade_5d_base_v013_signal, f25vd_f25_vwap_deviation_vwap_mean_abs_5d_base_v014_signal, f25vd_f25_vwap_deviation_vwap_vol_adj_delta_5d_base_v015_signal, f25vd_f25_vwap_deviation_vwap_level_10d_base_v016_signal, f25vd_f25_vwap_deviation_vwap_mean_10d_base_v017_signal, f25vd_f25_vwap_deviation_vwap_std_10d_base_v018_signal, f25vd_f25_vwap_deviation_vwap_zscore_10d_base_v019_signal, f25vd_f25_vwap_deviation_vwap_delta_10d_base_v020_signal, f25vd_f25_vwap_deviation_vwap_upper_gap_10d_base_v022_signal, f25vd_f25_vwap_deviation_vwap_lower_gap_10d_base_v023_signal, f25vd_f25_vwap_deviation_vwap_short_mean_gap_10d_base_v024_signal, f25vd_f25_vwap_deviation_vwap_energy_10d_base_v025_signal, f25vd_f25_vwap_deviation_vwap_ewm_gap_10d_base_v026_signal, f25vd_f25_vwap_deviation_vwap_tail_relief_10d_base_v027_signal, f25vd_f25_vwap_deviation_vwap_peak_fade_10d_base_v028_signal, f25vd_f25_vwap_deviation_vwap_mean_abs_10d_base_v029_signal, f25vd_f25_vwap_deviation_vwap_vol_adj_delta_10d_base_v030_signal, f25vd_f25_vwap_deviation_vwap_level_15d_base_v031_signal, f25vd_f25_vwap_deviation_vwap_mean_15d_base_v032_signal, f25vd_f25_vwap_deviation_vwap_std_15d_base_v033_signal, f25vd_f25_vwap_deviation_vwap_zscore_15d_base_v034_signal, f25vd_f25_vwap_deviation_vwap_delta_15d_base_v035_signal, f25vd_f25_vwap_deviation_vwap_upper_gap_15d_base_v037_signal, f25vd_f25_vwap_deviation_vwap_lower_gap_15d_base_v038_signal, f25vd_f25_vwap_deviation_vwap_short_mean_gap_15d_base_v039_signal, f25vd_f25_vwap_deviation_vwap_energy_15d_base_v040_signal, f25vd_f25_vwap_deviation_vwap_ewm_gap_15d_base_v041_signal, f25vd_f25_vwap_deviation_vwap_tail_relief_15d_base_v042_signal, f25vd_f25_vwap_deviation_vwap_peak_fade_15d_base_v043_signal, f25vd_f25_vwap_deviation_vwap_mean_abs_15d_base_v044_signal, f25vd_f25_vwap_deviation_vwap_vol_adj_delta_15d_base_v045_signal, f25vd_f25_vwap_deviation_vwap_level_21d_base_v046_signal, f25vd_f25_vwap_deviation_vwap_mean_21d_base_v047_signal, f25vd_f25_vwap_deviation_vwap_std_21d_base_v048_signal, f25vd_f25_vwap_deviation_vwap_zscore_21d_base_v049_signal, f25vd_f25_vwap_deviation_vwap_delta_21d_base_v050_signal, f25vd_f25_vwap_deviation_vwap_upper_gap_21d_base_v052_signal, f25vd_f25_vwap_deviation_vwap_lower_gap_21d_base_v053_signal, f25vd_f25_vwap_deviation_vwap_short_mean_gap_21d_base_v054_signal, f25vd_f25_vwap_deviation_vwap_energy_21d_base_v055_signal, f25vd_f25_vwap_deviation_vwap_ewm_gap_21d_base_v056_signal, f25vd_f25_vwap_deviation_vwap_tail_relief_21d_base_v057_signal, f25vd_f25_vwap_deviation_vwap_peak_fade_21d_base_v058_signal, f25vd_f25_vwap_deviation_vwap_mean_abs_21d_base_v059_signal, f25vd_f25_vwap_deviation_vwap_vol_adj_delta_21d_base_v060_signal, f25vd_f25_vwap_deviation_vwap_level_42d_base_v061_signal, f25vd_f25_vwap_deviation_vwap_mean_42d_base_v062_signal, f25vd_f25_vwap_deviation_vwap_std_42d_base_v063_signal, f25vd_f25_vwap_deviation_vwap_zscore_42d_base_v064_signal, f25vd_f25_vwap_deviation_vwap_delta_42d_base_v065_signal, f25vd_f25_vwap_deviation_vwap_upper_gap_42d_base_v067_signal, f25vd_f25_vwap_deviation_vwap_lower_gap_42d_base_v068_signal, f25vd_f25_vwap_deviation_vwap_short_mean_gap_42d_base_v069_signal, f25vd_f25_vwap_deviation_vwap_energy_42d_base_v070_signal, f25vd_f25_vwap_deviation_vwap_ewm_gap_42d_base_v071_signal, f25vd_f25_vwap_deviation_vwap_tail_relief_42d_base_v072_signal, f25vd_f25_vwap_deviation_vwap_peak_fade_42d_base_v073_signal, f25vd_f25_vwap_deviation_vwap_mean_abs_42d_base_v074_signal, f25vd_f25_vwap_deviation_vwap_vol_adj_delta_42d_base_v075_signal]}
F25_VWAP_DEVIATION_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    closeadj = base
    high = closeadj * (1.0 + pd.Series(np.random.uniform(0.003, 0.05, n)))
    low = closeadj * (1.0 - pd.Series(np.random.uniform(0.003, 0.05, n)))
    volume = pd.Series(np.random.lognormal(13.0, 0.9, n) * (1.0 + 0.25 * np.sin(t / 13.0)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(high, low, closeadj, volume)
        y2 = func(high, low, closeadj, volume)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_vwap_deviation" in src
    assert ok_nan >= int(0.80 * len(funcs))
