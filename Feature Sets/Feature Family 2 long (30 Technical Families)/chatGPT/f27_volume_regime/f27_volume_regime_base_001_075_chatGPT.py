import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _volume_regime_ratio(volume, w):
    v = np.log(volume.replace(0, np.nan))
    return v.rolling(max(2, w//3), min_periods=2).std() / v.rolling(w, min_periods=2).std().replace(0, np.nan)

# 5d level vregm
def f27vg_f27_volume_regime_vregm_level_5d_base_v001_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean vregm
def f27vg_f27_volume_regime_vregm_mean_5d_base_v002_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d var vregm
def f27vg_f27_volume_regime_vregm_std_5d_base_v003_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(5, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_5d_base_v004_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = _z(sig, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d change vregm
def f27vg_f27_volume_regime_vregm_delta_5d_base_v005_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_5d_base_v007_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_5d_base_v008_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_5d_base_v009_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d energy vregm
def f27vg_f27_volume_regime_vregm_energy_5d_base_v010_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_5d_base_v011_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_5d_base_v012_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_5d_base_v013_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_5d_base_v015_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d level vregm
def f27vg_f27_volume_regime_vregm_level_10d_base_v016_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d mean vregm
def f27vg_f27_volume_regime_vregm_mean_10d_base_v017_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d var vregm
def f27vg_f27_volume_regime_vregm_std_10d_base_v018_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(10, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_10d_base_v019_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = _z(sig, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d change vregm
def f27vg_f27_volume_regime_vregm_delta_10d_base_v020_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_10d_base_v022_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_10d_base_v023_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_10d_base_v024_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d energy vregm
def f27vg_f27_volume_regime_vregm_energy_10d_base_v025_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_10d_base_v026_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_10d_base_v027_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_10d_base_v028_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_10d_base_v030_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d level vregm
def f27vg_f27_volume_regime_vregm_level_15d_base_v031_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d mean vregm
def f27vg_f27_volume_regime_vregm_mean_15d_base_v032_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d var vregm
def f27vg_f27_volume_regime_vregm_std_15d_base_v033_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(15, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_15d_base_v034_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = _z(sig, 15)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d change vregm
def f27vg_f27_volume_regime_vregm_delta_15d_base_v035_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_15d_base_v037_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_15d_base_v038_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_15d_base_v039_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d energy vregm
def f27vg_f27_volume_regime_vregm_energy_15d_base_v040_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_15d_base_v041_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_15d_base_v042_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_15d_base_v043_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_15d_base_v045_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level vregm
def f27vg_f27_volume_regime_vregm_level_21d_base_v046_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean vregm
def f27vg_f27_volume_regime_vregm_mean_21d_base_v047_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d var vregm
def f27vg_f27_volume_regime_vregm_std_21d_base_v048_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(21, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_21d_base_v049_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = _z(sig, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d change vregm
def f27vg_f27_volume_regime_vregm_delta_21d_base_v050_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_21d_base_v052_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_21d_base_v053_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_21d_base_v054_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d energy vregm
def f27vg_f27_volume_regime_vregm_energy_21d_base_v055_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_21d_base_v056_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_21d_base_v057_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_21d_base_v058_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_21d_base_v060_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d level vregm
def f27vg_f27_volume_regime_vregm_level_42d_base_v061_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d mean vregm
def f27vg_f27_volume_regime_vregm_mean_42d_base_v062_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d var vregm
def f27vg_f27_volume_regime_vregm_std_42d_base_v063_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(42, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_42d_base_v064_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = _z(sig, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d change vregm
def f27vg_f27_volume_regime_vregm_delta_42d_base_v065_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_42d_base_v067_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_42d_base_v068_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_42d_base_v069_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d energy vregm
def f27vg_f27_volume_regime_vregm_energy_42d_base_v070_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_42d_base_v071_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_42d_base_v072_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_42d_base_v073_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_42d_base_v075_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['volume'], "func": fn} for fn in [f27vg_f27_volume_regime_vregm_level_5d_base_v001_signal, f27vg_f27_volume_regime_vregm_mean_5d_base_v002_signal, f27vg_f27_volume_regime_vregm_std_5d_base_v003_signal, f27vg_f27_volume_regime_vregm_zscore_5d_base_v004_signal, f27vg_f27_volume_regime_vregm_delta_5d_base_v005_signal, f27vg_f27_volume_regime_vregm_upper_gap_5d_base_v007_signal, f27vg_f27_volume_regime_vregm_lower_gap_5d_base_v008_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_5d_base_v009_signal, f27vg_f27_volume_regime_vregm_energy_5d_base_v010_signal, f27vg_f27_volume_regime_vregm_ewm_gap_5d_base_v011_signal, f27vg_f27_volume_regime_vregm_tail_relief_5d_base_v012_signal, f27vg_f27_volume_regime_vregm_peak_fade_5d_base_v013_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_5d_base_v015_signal, f27vg_f27_volume_regime_vregm_level_10d_base_v016_signal, f27vg_f27_volume_regime_vregm_mean_10d_base_v017_signal, f27vg_f27_volume_regime_vregm_std_10d_base_v018_signal, f27vg_f27_volume_regime_vregm_zscore_10d_base_v019_signal, f27vg_f27_volume_regime_vregm_delta_10d_base_v020_signal, f27vg_f27_volume_regime_vregm_upper_gap_10d_base_v022_signal, f27vg_f27_volume_regime_vregm_lower_gap_10d_base_v023_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_10d_base_v024_signal, f27vg_f27_volume_regime_vregm_energy_10d_base_v025_signal, f27vg_f27_volume_regime_vregm_ewm_gap_10d_base_v026_signal, f27vg_f27_volume_regime_vregm_tail_relief_10d_base_v027_signal, f27vg_f27_volume_regime_vregm_peak_fade_10d_base_v028_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_10d_base_v030_signal, f27vg_f27_volume_regime_vregm_level_15d_base_v031_signal, f27vg_f27_volume_regime_vregm_mean_15d_base_v032_signal, f27vg_f27_volume_regime_vregm_std_15d_base_v033_signal, f27vg_f27_volume_regime_vregm_zscore_15d_base_v034_signal, f27vg_f27_volume_regime_vregm_delta_15d_base_v035_signal, f27vg_f27_volume_regime_vregm_upper_gap_15d_base_v037_signal, f27vg_f27_volume_regime_vregm_lower_gap_15d_base_v038_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_15d_base_v039_signal, f27vg_f27_volume_regime_vregm_energy_15d_base_v040_signal, f27vg_f27_volume_regime_vregm_ewm_gap_15d_base_v041_signal, f27vg_f27_volume_regime_vregm_tail_relief_15d_base_v042_signal, f27vg_f27_volume_regime_vregm_peak_fade_15d_base_v043_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_15d_base_v045_signal, f27vg_f27_volume_regime_vregm_level_21d_base_v046_signal, f27vg_f27_volume_regime_vregm_mean_21d_base_v047_signal, f27vg_f27_volume_regime_vregm_std_21d_base_v048_signal, f27vg_f27_volume_regime_vregm_zscore_21d_base_v049_signal, f27vg_f27_volume_regime_vregm_delta_21d_base_v050_signal, f27vg_f27_volume_regime_vregm_upper_gap_21d_base_v052_signal, f27vg_f27_volume_regime_vregm_lower_gap_21d_base_v053_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_21d_base_v054_signal, f27vg_f27_volume_regime_vregm_energy_21d_base_v055_signal, f27vg_f27_volume_regime_vregm_ewm_gap_21d_base_v056_signal, f27vg_f27_volume_regime_vregm_tail_relief_21d_base_v057_signal, f27vg_f27_volume_regime_vregm_peak_fade_21d_base_v058_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_21d_base_v060_signal, f27vg_f27_volume_regime_vregm_level_42d_base_v061_signal, f27vg_f27_volume_regime_vregm_mean_42d_base_v062_signal, f27vg_f27_volume_regime_vregm_std_42d_base_v063_signal, f27vg_f27_volume_regime_vregm_zscore_42d_base_v064_signal, f27vg_f27_volume_regime_vregm_delta_42d_base_v065_signal, f27vg_f27_volume_regime_vregm_upper_gap_42d_base_v067_signal, f27vg_f27_volume_regime_vregm_lower_gap_42d_base_v068_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_42d_base_v069_signal, f27vg_f27_volume_regime_vregm_energy_42d_base_v070_signal, f27vg_f27_volume_regime_vregm_ewm_gap_42d_base_v071_signal, f27vg_f27_volume_regime_vregm_tail_relief_42d_base_v072_signal, f27vg_f27_volume_regime_vregm_peak_fade_42d_base_v073_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_42d_base_v075_signal]}
F27_VOLUME_REGIME_REGISTRY_001_075 = REGISTRY

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
        assert "_volume_regime_ratio" in src
    assert ok_nan >= int(0.80 * len(funcs))
