import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _raw_volume_metric(volume, w):
    v = np.log(volume.replace(0, np.nan))
    return v.rolling(w, min_periods=2).mean() + v.diff(max(1, w//5))

# 5d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_5d_base_v001_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_5d_base_v002_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_5d_base_v003_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(5, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_5d_base_v004_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = _z(sig, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_5d_base_v005_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_5d_base_v007_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_5d_base_v008_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_5d_base_v009_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_5d_base_v010_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_5d_base_v011_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_5d_base_v012_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_5d_base_v013_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_5d_base_v015_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_10d_base_v016_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_10d_base_v017_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_10d_base_v018_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(10, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_10d_base_v019_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = _z(sig, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_10d_base_v020_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_10d_base_v022_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_10d_base_v023_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_10d_base_v024_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_10d_base_v025_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_10d_base_v026_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_10d_base_v027_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_10d_base_v028_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_10d_base_v030_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_15d_base_v031_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_15d_base_v032_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_15d_base_v033_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(15, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_15d_base_v034_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = _z(sig, 15)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_15d_base_v035_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_15d_base_v037_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_15d_base_v038_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_15d_base_v039_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_15d_base_v040_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_15d_base_v041_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_15d_base_v042_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_15d_base_v043_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_15d_base_v045_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_21d_base_v046_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_21d_base_v047_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_21d_base_v048_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(21, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_21d_base_v049_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = _z(sig, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_21d_base_v050_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_21d_base_v052_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_21d_base_v053_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_21d_base_v054_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_21d_base_v055_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_21d_base_v056_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_21d_base_v057_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_21d_base_v058_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_21d_base_v060_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_42d_base_v061_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_42d_base_v062_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_42d_base_v063_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(42, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_42d_base_v064_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = _z(sig, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_42d_base_v065_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_42d_base_v067_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_42d_base_v068_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_42d_base_v069_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_42d_base_v070_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_42d_base_v071_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_42d_base_v072_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_42d_base_v073_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_42d_base_v075_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['volume'], "func": fn} for fn in [f21rvv_f21_raw_volume_metrics_rvol_level_5d_base_v001_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_5d_base_v002_signal, f21rvv_f21_raw_volume_metrics_rvol_std_5d_base_v003_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_5d_base_v004_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_5d_base_v005_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_5d_base_v007_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_5d_base_v008_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_5d_base_v009_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_5d_base_v010_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_5d_base_v011_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_5d_base_v012_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_5d_base_v013_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_5d_base_v015_signal, f21rvv_f21_raw_volume_metrics_rvol_level_10d_base_v016_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_10d_base_v017_signal, f21rvv_f21_raw_volume_metrics_rvol_std_10d_base_v018_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_10d_base_v019_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_10d_base_v020_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_10d_base_v022_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_10d_base_v023_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_10d_base_v024_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_10d_base_v025_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_10d_base_v026_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_10d_base_v027_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_10d_base_v028_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_10d_base_v030_signal, f21rvv_f21_raw_volume_metrics_rvol_level_15d_base_v031_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_15d_base_v032_signal, f21rvv_f21_raw_volume_metrics_rvol_std_15d_base_v033_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_15d_base_v034_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_15d_base_v035_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_15d_base_v037_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_15d_base_v038_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_15d_base_v039_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_15d_base_v040_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_15d_base_v041_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_15d_base_v042_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_15d_base_v043_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_15d_base_v045_signal, f21rvv_f21_raw_volume_metrics_rvol_level_21d_base_v046_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_21d_base_v047_signal, f21rvv_f21_raw_volume_metrics_rvol_std_21d_base_v048_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_21d_base_v049_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_21d_base_v050_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_21d_base_v052_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_21d_base_v053_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_21d_base_v054_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_21d_base_v055_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_21d_base_v056_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_21d_base_v057_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_21d_base_v058_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_21d_base_v060_signal, f21rvv_f21_raw_volume_metrics_rvol_level_42d_base_v061_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_42d_base_v062_signal, f21rvv_f21_raw_volume_metrics_rvol_std_42d_base_v063_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_42d_base_v064_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_42d_base_v065_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_42d_base_v067_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_42d_base_v068_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_42d_base_v069_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_42d_base_v070_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_42d_base_v071_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_42d_base_v072_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_42d_base_v073_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_42d_base_v075_signal]}
F21_RAW_VOLUME_METRICS_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    volume = pd.Series(np.random.lognormal(13.0, 0.9, n) * (1.0 + 0.25 * np.sin(t / 13.0)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(volume)
        y2 = func(volume)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_raw_volume_metric" in src
    assert ok_nan >= int(0.80 * len(funcs))
