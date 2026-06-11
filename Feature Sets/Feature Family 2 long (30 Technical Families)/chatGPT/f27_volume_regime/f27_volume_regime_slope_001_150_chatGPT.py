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

# sl5 5d level vregm
def f27vg_f27_volume_regime_vregm_level_5d_slope_v001_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d mean vregm
def f27vg_f27_volume_regime_vregm_mean_5d_slope_v002_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d var vregm
def f27vg_f27_volume_regime_vregm_std_5d_slope_v003_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(5, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_5d_slope_v004_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = _z(sig, 5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d change vregm
def f27vg_f27_volume_regime_vregm_delta_5d_slope_v005_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_5d_slope_v006_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_5d_slope_v007_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_5d_slope_v008_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_5d_slope_v009_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d energy vregm
def f27vg_f27_volume_regime_vregm_energy_5d_slope_v010_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_5d_slope_v011_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_5d_slope_v012_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_5d_slope_v013_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_5d_slope_v015_signal(volume):
    sig = _volume_regime_ratio(volume, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d level vregm
def f27vg_f27_volume_regime_vregm_level_10d_slope_v016_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d mean vregm
def f27vg_f27_volume_regime_vregm_mean_10d_slope_v017_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d var vregm
def f27vg_f27_volume_regime_vregm_std_10d_slope_v018_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(10, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_10d_slope_v019_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = _z(sig, 10)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d change vregm
def f27vg_f27_volume_regime_vregm_delta_10d_slope_v020_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_10d_slope_v021_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_10d_slope_v022_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_10d_slope_v023_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_10d_slope_v024_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d energy vregm
def f27vg_f27_volume_regime_vregm_energy_10d_slope_v025_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_10d_slope_v026_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_10d_slope_v027_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_10d_slope_v028_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_10d_slope_v030_signal(volume):
    sig = _volume_regime_ratio(volume, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d level vregm
def f27vg_f27_volume_regime_vregm_level_15d_slope_v031_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d mean vregm
def f27vg_f27_volume_regime_vregm_mean_15d_slope_v032_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d var vregm
def f27vg_f27_volume_regime_vregm_std_15d_slope_v033_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(15, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_15d_slope_v034_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = _z(sig, 15)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d change vregm
def f27vg_f27_volume_regime_vregm_delta_15d_slope_v035_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_15d_slope_v036_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_15d_slope_v037_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_15d_slope_v038_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_15d_slope_v039_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d energy vregm
def f27vg_f27_volume_regime_vregm_energy_15d_slope_v040_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_15d_slope_v041_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_15d_slope_v042_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_15d_slope_v043_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_15d_slope_v045_signal(volume):
    sig = _volume_regime_ratio(volume, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d level vregm
def f27vg_f27_volume_regime_vregm_level_21d_slope_v046_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d mean vregm
def f27vg_f27_volume_regime_vregm_mean_21d_slope_v047_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d var vregm
def f27vg_f27_volume_regime_vregm_std_21d_slope_v048_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(21, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_21d_slope_v049_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = _z(sig, 21)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d change vregm
def f27vg_f27_volume_regime_vregm_delta_21d_slope_v050_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_21d_slope_v051_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_21d_slope_v052_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_21d_slope_v053_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_21d_slope_v054_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d energy vregm
def f27vg_f27_volume_regime_vregm_energy_21d_slope_v055_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_21d_slope_v056_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_21d_slope_v057_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_21d_slope_v058_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_21d_slope_v060_signal(volume):
    sig = _volume_regime_ratio(volume, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d level vregm
def f27vg_f27_volume_regime_vregm_level_42d_slope_v061_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d mean vregm
def f27vg_f27_volume_regime_vregm_mean_42d_slope_v062_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d var vregm
def f27vg_f27_volume_regime_vregm_std_42d_slope_v063_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(42, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_42d_slope_v064_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = _z(sig, 42)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d change vregm
def f27vg_f27_volume_regime_vregm_delta_42d_slope_v065_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_42d_slope_v066_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_42d_slope_v067_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_42d_slope_v068_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_42d_slope_v069_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d energy vregm
def f27vg_f27_volume_regime_vregm_energy_42d_slope_v070_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_42d_slope_v071_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_42d_slope_v072_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_42d_slope_v073_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_42d_slope_v075_signal(volume):
    sig = _volume_regime_ratio(volume, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d level vregm
def f27vg_f27_volume_regime_vregm_level_63d_slope_v076_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d mean vregm
def f27vg_f27_volume_regime_vregm_mean_63d_slope_v077_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d var vregm
def f27vg_f27_volume_regime_vregm_std_63d_slope_v078_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(63, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_63d_slope_v079_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = _z(sig, 63)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d change vregm
def f27vg_f27_volume_regime_vregm_delta_63d_slope_v080_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_63d_slope_v081_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_63d_slope_v082_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_63d_slope_v083_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_63d_slope_v084_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d energy vregm
def f27vg_f27_volume_regime_vregm_energy_63d_slope_v085_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_63d_slope_v086_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_63d_slope_v087_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_63d_slope_v088_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_63d_slope_v090_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d level vregm
def f27vg_f27_volume_regime_vregm_level_84d_slope_v091_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d mean vregm
def f27vg_f27_volume_regime_vregm_mean_84d_slope_v092_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d var vregm
def f27vg_f27_volume_regime_vregm_std_84d_slope_v093_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(84, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_84d_slope_v094_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = _z(sig, 84)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d change vregm
def f27vg_f27_volume_regime_vregm_delta_84d_slope_v095_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_84d_slope_v096_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_84d_slope_v097_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_84d_slope_v098_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_84d_slope_v099_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d energy vregm
def f27vg_f27_volume_regime_vregm_energy_84d_slope_v100_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_84d_slope_v101_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_84d_slope_v102_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_84d_slope_v103_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_84d_slope_v105_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d level vregm
def f27vg_f27_volume_regime_vregm_level_126d_slope_v106_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d mean vregm
def f27vg_f27_volume_regime_vregm_mean_126d_slope_v107_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d var vregm
def f27vg_f27_volume_regime_vregm_std_126d_slope_v108_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(126, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_126d_slope_v109_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = _z(sig, 126)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d change vregm
def f27vg_f27_volume_regime_vregm_delta_126d_slope_v110_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_126d_slope_v111_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_126d_slope_v112_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_126d_slope_v113_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_126d_slope_v114_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d energy vregm
def f27vg_f27_volume_regime_vregm_energy_126d_slope_v115_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_126d_slope_v116_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_126d_slope_v117_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_126d_slope_v118_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_126d_slope_v120_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d level vregm
def f27vg_f27_volume_regime_vregm_level_252d_slope_v121_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d mean vregm
def f27vg_f27_volume_regime_vregm_mean_252d_slope_v122_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d var vregm
def f27vg_f27_volume_regime_vregm_std_252d_slope_v123_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(252, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_252d_slope_v124_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = _z(sig, 252)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d change vregm
def f27vg_f27_volume_regime_vregm_delta_252d_slope_v125_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_252d_slope_v126_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_252d_slope_v127_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_252d_slope_v128_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_252d_slope_v129_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d energy vregm
def f27vg_f27_volume_regime_vregm_energy_252d_slope_v130_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_252d_slope_v131_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_252d_slope_v132_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_252d_slope_v133_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_252d_slope_v135_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d level vregm
def f27vg_f27_volume_regime_vregm_level_504d_slope_v136_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d mean vregm
def f27vg_f27_volume_regime_vregm_mean_504d_slope_v137_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d var vregm
def f27vg_f27_volume_regime_vregm_std_504d_slope_v138_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(504, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_504d_slope_v139_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = _z(sig, 504)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d change vregm
def f27vg_f27_volume_regime_vregm_delta_504d_slope_v140_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d relchg vregm
def f27vg_f27_volume_regime_vregm_pctdelta_504d_slope_v141_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_504d_slope_v142_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_504d_slope_v143_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_504d_slope_v144_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d energy vregm
def f27vg_f27_volume_regime_vregm_energy_504d_slope_v145_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_504d_slope_v146_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_504d_slope_v147_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_504d_slope_v148_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_504d_slope_v150_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['volume'], "func": fn} for fn in [f27vg_f27_volume_regime_vregm_level_5d_slope_v001_signal, f27vg_f27_volume_regime_vregm_mean_5d_slope_v002_signal, f27vg_f27_volume_regime_vregm_std_5d_slope_v003_signal, f27vg_f27_volume_regime_vregm_zscore_5d_slope_v004_signal, f27vg_f27_volume_regime_vregm_delta_5d_slope_v005_signal, f27vg_f27_volume_regime_vregm_pctdelta_5d_slope_v006_signal, f27vg_f27_volume_regime_vregm_upper_gap_5d_slope_v007_signal, f27vg_f27_volume_regime_vregm_lower_gap_5d_slope_v008_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_5d_slope_v009_signal, f27vg_f27_volume_regime_vregm_energy_5d_slope_v010_signal, f27vg_f27_volume_regime_vregm_ewm_gap_5d_slope_v011_signal, f27vg_f27_volume_regime_vregm_tail_relief_5d_slope_v012_signal, f27vg_f27_volume_regime_vregm_peak_fade_5d_slope_v013_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_5d_slope_v015_signal, f27vg_f27_volume_regime_vregm_level_10d_slope_v016_signal, f27vg_f27_volume_regime_vregm_mean_10d_slope_v017_signal, f27vg_f27_volume_regime_vregm_std_10d_slope_v018_signal, f27vg_f27_volume_regime_vregm_zscore_10d_slope_v019_signal, f27vg_f27_volume_regime_vregm_delta_10d_slope_v020_signal, f27vg_f27_volume_regime_vregm_pctdelta_10d_slope_v021_signal, f27vg_f27_volume_regime_vregm_upper_gap_10d_slope_v022_signal, f27vg_f27_volume_regime_vregm_lower_gap_10d_slope_v023_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_10d_slope_v024_signal, f27vg_f27_volume_regime_vregm_energy_10d_slope_v025_signal, f27vg_f27_volume_regime_vregm_ewm_gap_10d_slope_v026_signal, f27vg_f27_volume_regime_vregm_tail_relief_10d_slope_v027_signal, f27vg_f27_volume_regime_vregm_peak_fade_10d_slope_v028_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_10d_slope_v030_signal, f27vg_f27_volume_regime_vregm_level_15d_slope_v031_signal, f27vg_f27_volume_regime_vregm_mean_15d_slope_v032_signal, f27vg_f27_volume_regime_vregm_std_15d_slope_v033_signal, f27vg_f27_volume_regime_vregm_zscore_15d_slope_v034_signal, f27vg_f27_volume_regime_vregm_delta_15d_slope_v035_signal, f27vg_f27_volume_regime_vregm_pctdelta_15d_slope_v036_signal, f27vg_f27_volume_regime_vregm_upper_gap_15d_slope_v037_signal, f27vg_f27_volume_regime_vregm_lower_gap_15d_slope_v038_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_15d_slope_v039_signal, f27vg_f27_volume_regime_vregm_energy_15d_slope_v040_signal, f27vg_f27_volume_regime_vregm_ewm_gap_15d_slope_v041_signal, f27vg_f27_volume_regime_vregm_tail_relief_15d_slope_v042_signal, f27vg_f27_volume_regime_vregm_peak_fade_15d_slope_v043_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_15d_slope_v045_signal, f27vg_f27_volume_regime_vregm_level_21d_slope_v046_signal, f27vg_f27_volume_regime_vregm_mean_21d_slope_v047_signal, f27vg_f27_volume_regime_vregm_std_21d_slope_v048_signal, f27vg_f27_volume_regime_vregm_zscore_21d_slope_v049_signal, f27vg_f27_volume_regime_vregm_delta_21d_slope_v050_signal, f27vg_f27_volume_regime_vregm_pctdelta_21d_slope_v051_signal, f27vg_f27_volume_regime_vregm_upper_gap_21d_slope_v052_signal, f27vg_f27_volume_regime_vregm_lower_gap_21d_slope_v053_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_21d_slope_v054_signal, f27vg_f27_volume_regime_vregm_energy_21d_slope_v055_signal, f27vg_f27_volume_regime_vregm_ewm_gap_21d_slope_v056_signal, f27vg_f27_volume_regime_vregm_tail_relief_21d_slope_v057_signal, f27vg_f27_volume_regime_vregm_peak_fade_21d_slope_v058_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_21d_slope_v060_signal, f27vg_f27_volume_regime_vregm_level_42d_slope_v061_signal, f27vg_f27_volume_regime_vregm_mean_42d_slope_v062_signal, f27vg_f27_volume_regime_vregm_std_42d_slope_v063_signal, f27vg_f27_volume_regime_vregm_zscore_42d_slope_v064_signal, f27vg_f27_volume_regime_vregm_delta_42d_slope_v065_signal, f27vg_f27_volume_regime_vregm_pctdelta_42d_slope_v066_signal, f27vg_f27_volume_regime_vregm_upper_gap_42d_slope_v067_signal, f27vg_f27_volume_regime_vregm_lower_gap_42d_slope_v068_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_42d_slope_v069_signal, f27vg_f27_volume_regime_vregm_energy_42d_slope_v070_signal, f27vg_f27_volume_regime_vregm_ewm_gap_42d_slope_v071_signal, f27vg_f27_volume_regime_vregm_tail_relief_42d_slope_v072_signal, f27vg_f27_volume_regime_vregm_peak_fade_42d_slope_v073_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_42d_slope_v075_signal, f27vg_f27_volume_regime_vregm_level_63d_slope_v076_signal, f27vg_f27_volume_regime_vregm_mean_63d_slope_v077_signal, f27vg_f27_volume_regime_vregm_std_63d_slope_v078_signal, f27vg_f27_volume_regime_vregm_zscore_63d_slope_v079_signal, f27vg_f27_volume_regime_vregm_delta_63d_slope_v080_signal, f27vg_f27_volume_regime_vregm_pctdelta_63d_slope_v081_signal, f27vg_f27_volume_regime_vregm_upper_gap_63d_slope_v082_signal, f27vg_f27_volume_regime_vregm_lower_gap_63d_slope_v083_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_63d_slope_v084_signal, f27vg_f27_volume_regime_vregm_energy_63d_slope_v085_signal, f27vg_f27_volume_regime_vregm_ewm_gap_63d_slope_v086_signal, f27vg_f27_volume_regime_vregm_tail_relief_63d_slope_v087_signal, f27vg_f27_volume_regime_vregm_peak_fade_63d_slope_v088_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_63d_slope_v090_signal, f27vg_f27_volume_regime_vregm_level_84d_slope_v091_signal, f27vg_f27_volume_regime_vregm_mean_84d_slope_v092_signal, f27vg_f27_volume_regime_vregm_std_84d_slope_v093_signal, f27vg_f27_volume_regime_vregm_zscore_84d_slope_v094_signal, f27vg_f27_volume_regime_vregm_delta_84d_slope_v095_signal, f27vg_f27_volume_regime_vregm_pctdelta_84d_slope_v096_signal, f27vg_f27_volume_regime_vregm_upper_gap_84d_slope_v097_signal, f27vg_f27_volume_regime_vregm_lower_gap_84d_slope_v098_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_84d_slope_v099_signal, f27vg_f27_volume_regime_vregm_energy_84d_slope_v100_signal, f27vg_f27_volume_regime_vregm_ewm_gap_84d_slope_v101_signal, f27vg_f27_volume_regime_vregm_tail_relief_84d_slope_v102_signal, f27vg_f27_volume_regime_vregm_peak_fade_84d_slope_v103_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_84d_slope_v105_signal, f27vg_f27_volume_regime_vregm_level_126d_slope_v106_signal, f27vg_f27_volume_regime_vregm_mean_126d_slope_v107_signal, f27vg_f27_volume_regime_vregm_std_126d_slope_v108_signal, f27vg_f27_volume_regime_vregm_zscore_126d_slope_v109_signal, f27vg_f27_volume_regime_vregm_delta_126d_slope_v110_signal, f27vg_f27_volume_regime_vregm_pctdelta_126d_slope_v111_signal, f27vg_f27_volume_regime_vregm_upper_gap_126d_slope_v112_signal, f27vg_f27_volume_regime_vregm_lower_gap_126d_slope_v113_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_126d_slope_v114_signal, f27vg_f27_volume_regime_vregm_energy_126d_slope_v115_signal, f27vg_f27_volume_regime_vregm_ewm_gap_126d_slope_v116_signal, f27vg_f27_volume_regime_vregm_tail_relief_126d_slope_v117_signal, f27vg_f27_volume_regime_vregm_peak_fade_126d_slope_v118_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_126d_slope_v120_signal, f27vg_f27_volume_regime_vregm_level_252d_slope_v121_signal, f27vg_f27_volume_regime_vregm_mean_252d_slope_v122_signal, f27vg_f27_volume_regime_vregm_std_252d_slope_v123_signal, f27vg_f27_volume_regime_vregm_zscore_252d_slope_v124_signal, f27vg_f27_volume_regime_vregm_delta_252d_slope_v125_signal, f27vg_f27_volume_regime_vregm_pctdelta_252d_slope_v126_signal, f27vg_f27_volume_regime_vregm_upper_gap_252d_slope_v127_signal, f27vg_f27_volume_regime_vregm_lower_gap_252d_slope_v128_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_252d_slope_v129_signal, f27vg_f27_volume_regime_vregm_energy_252d_slope_v130_signal, f27vg_f27_volume_regime_vregm_ewm_gap_252d_slope_v131_signal, f27vg_f27_volume_regime_vregm_tail_relief_252d_slope_v132_signal, f27vg_f27_volume_regime_vregm_peak_fade_252d_slope_v133_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_252d_slope_v135_signal, f27vg_f27_volume_regime_vregm_level_504d_slope_v136_signal, f27vg_f27_volume_regime_vregm_mean_504d_slope_v137_signal, f27vg_f27_volume_regime_vregm_std_504d_slope_v138_signal, f27vg_f27_volume_regime_vregm_zscore_504d_slope_v139_signal, f27vg_f27_volume_regime_vregm_delta_504d_slope_v140_signal, f27vg_f27_volume_regime_vregm_pctdelta_504d_slope_v141_signal, f27vg_f27_volume_regime_vregm_upper_gap_504d_slope_v142_signal, f27vg_f27_volume_regime_vregm_lower_gap_504d_slope_v143_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_504d_slope_v144_signal, f27vg_f27_volume_regime_vregm_energy_504d_slope_v145_signal, f27vg_f27_volume_regime_vregm_ewm_gap_504d_slope_v146_signal, f27vg_f27_volume_regime_vregm_tail_relief_504d_slope_v147_signal, f27vg_f27_volume_regime_vregm_peak_fade_504d_slope_v148_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_504d_slope_v150_signal]}
F27_VOLUME_REGIME_REGISTRY_SLOPE = REGISTRY

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
