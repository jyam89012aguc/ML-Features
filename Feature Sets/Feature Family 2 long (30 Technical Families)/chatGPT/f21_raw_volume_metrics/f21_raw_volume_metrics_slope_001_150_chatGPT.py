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

# sl5 5d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_5d_slope_v001_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_5d_slope_v002_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_5d_slope_v003_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(5, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_5d_slope_v004_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = _z(sig, 5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_5d_slope_v005_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_5d_slope_v006_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_5d_slope_v007_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_5d_slope_v008_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_5d_slope_v009_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_5d_slope_v010_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_5d_slope_v011_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_5d_slope_v012_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_5d_slope_v013_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 5d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_5d_slope_v015_signal(volume):
    sig = _raw_volume_metric(volume, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_10d_slope_v016_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_10d_slope_v017_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_10d_slope_v018_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(10, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_10d_slope_v019_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = _z(sig, 10)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_10d_slope_v020_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_10d_slope_v021_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_10d_slope_v022_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_10d_slope_v023_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_10d_slope_v024_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_10d_slope_v025_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_10d_slope_v026_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_10d_slope_v027_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_10d_slope_v028_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 10d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_10d_slope_v030_signal(volume):
    sig = _raw_volume_metric(volume, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_15d_slope_v031_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_15d_slope_v032_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_15d_slope_v033_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(15, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_15d_slope_v034_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = _z(sig, 15)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_15d_slope_v035_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_15d_slope_v036_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_15d_slope_v037_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_15d_slope_v038_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_15d_slope_v039_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_15d_slope_v040_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_15d_slope_v041_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_15d_slope_v042_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_15d_slope_v043_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 15d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_15d_slope_v045_signal(volume):
    sig = _raw_volume_metric(volume, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_21d_slope_v046_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_21d_slope_v047_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_21d_slope_v048_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(21, min_periods=2).std()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_21d_slope_v049_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = _z(sig, 21)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_21d_slope_v050_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.diff(5)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_21d_slope_v051_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_21d_slope_v052_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_21d_slope_v053_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_21d_slope_v054_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_21d_slope_v055_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_21d_slope_v056_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_21d_slope_v057_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_21d_slope_v058_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl5 21d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_21d_slope_v060_signal(volume):
    sig = _raw_volume_metric(volume, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    result = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_42d_slope_v061_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_42d_slope_v062_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_42d_slope_v063_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(42, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_42d_slope_v064_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = _z(sig, 42)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_42d_slope_v065_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_42d_slope_v066_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_42d_slope_v067_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_42d_slope_v068_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_42d_slope_v069_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_42d_slope_v070_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_42d_slope_v071_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_42d_slope_v072_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_42d_slope_v073_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 42d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_42d_slope_v075_signal(volume):
    sig = _raw_volume_metric(volume, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_63d_slope_v076_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_63d_slope_v077_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_63d_slope_v078_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.rolling(63, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_63d_slope_v079_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = _z(sig, 63)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_63d_slope_v080_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_63d_slope_v081_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_63d_slope_v082_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_63d_slope_v083_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_63d_slope_v084_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_63d_slope_v085_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_63d_slope_v086_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_63d_slope_v087_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_63d_slope_v088_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 63d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_63d_slope_v090_signal(volume):
    sig = _raw_volume_metric(volume, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_84d_slope_v091_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_84d_slope_v092_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_84d_slope_v093_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.rolling(84, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_84d_slope_v094_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = _z(sig, 84)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_84d_slope_v095_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_84d_slope_v096_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_84d_slope_v097_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_84d_slope_v098_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_84d_slope_v099_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_84d_slope_v100_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_84d_slope_v101_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_84d_slope_v102_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_84d_slope_v103_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 84d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_84d_slope_v105_signal(volume):
    sig = _raw_volume_metric(volume, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_126d_slope_v106_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_126d_slope_v107_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_126d_slope_v108_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.rolling(126, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_126d_slope_v109_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = _z(sig, 126)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_126d_slope_v110_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_126d_slope_v111_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_126d_slope_v112_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_126d_slope_v113_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_126d_slope_v114_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_126d_slope_v115_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_126d_slope_v116_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_126d_slope_v117_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_126d_slope_v118_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 126d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_126d_slope_v120_signal(volume):
    sig = _raw_volume_metric(volume, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_252d_slope_v121_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_252d_slope_v122_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_252d_slope_v123_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.rolling(252, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_252d_slope_v124_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = _z(sig, 252)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_252d_slope_v125_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_252d_slope_v126_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_252d_slope_v127_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_252d_slope_v128_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_252d_slope_v129_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_252d_slope_v130_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_252d_slope_v131_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_252d_slope_v132_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_252d_slope_v133_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 252d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_252d_slope_v135_signal(volume):
    sig = _raw_volume_metric(volume, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d level rvol
def f21rvv_f21_raw_volume_metrics_rvol_level_504d_slope_v136_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d mean rvol
def f21rvv_f21_raw_volume_metrics_rvol_mean_504d_slope_v137_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d var rvol
def f21rvv_f21_raw_volume_metrics_rvol_std_504d_slope_v138_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.rolling(504, min_periods=2).std()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d zscore rvol
def f21rvv_f21_raw_volume_metrics_rvol_zscore_504d_slope_v139_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = _z(sig, 504)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d change rvol
def f21rvv_f21_raw_volume_metrics_rvol_delta_504d_slope_v140_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.diff(21)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d relchg rvol
def f21rvv_f21_raw_volume_metrics_rvol_pctdelta_504d_slope_v141_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q75gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_upper_gap_504d_slope_v142_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d q25gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_lower_gap_504d_slope_v143_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d smean gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_504d_slope_v144_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d energy rvol
def f21rvv_f21_raw_volume_metrics_rvol_energy_504d_slope_v145_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d ewm gap rvol
def f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_504d_slope_v146_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d tail relief rvol
def f21rvv_f21_raw_volume_metrics_rvol_tail_relief_504d_slope_v147_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d peak fade rvol
def f21rvv_f21_raw_volume_metrics_rvol_peak_fade_504d_slope_v148_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# sl21 504d voladj chg rvol
def f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_504d_slope_v150_signal(volume):
    sig = _raw_volume_metric(volume, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    result = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['volume'], "func": fn} for fn in [f21rvv_f21_raw_volume_metrics_rvol_level_5d_slope_v001_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_5d_slope_v002_signal, f21rvv_f21_raw_volume_metrics_rvol_std_5d_slope_v003_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_5d_slope_v004_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_5d_slope_v005_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_5d_slope_v006_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_5d_slope_v007_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_5d_slope_v008_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_5d_slope_v009_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_5d_slope_v010_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_5d_slope_v011_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_5d_slope_v012_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_5d_slope_v013_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_5d_slope_v015_signal, f21rvv_f21_raw_volume_metrics_rvol_level_10d_slope_v016_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_10d_slope_v017_signal, f21rvv_f21_raw_volume_metrics_rvol_std_10d_slope_v018_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_10d_slope_v019_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_10d_slope_v020_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_10d_slope_v021_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_10d_slope_v022_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_10d_slope_v023_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_10d_slope_v024_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_10d_slope_v025_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_10d_slope_v026_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_10d_slope_v027_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_10d_slope_v028_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_10d_slope_v030_signal, f21rvv_f21_raw_volume_metrics_rvol_level_15d_slope_v031_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_15d_slope_v032_signal, f21rvv_f21_raw_volume_metrics_rvol_std_15d_slope_v033_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_15d_slope_v034_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_15d_slope_v035_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_15d_slope_v036_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_15d_slope_v037_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_15d_slope_v038_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_15d_slope_v039_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_15d_slope_v040_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_15d_slope_v041_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_15d_slope_v042_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_15d_slope_v043_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_15d_slope_v045_signal, f21rvv_f21_raw_volume_metrics_rvol_level_21d_slope_v046_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_21d_slope_v047_signal, f21rvv_f21_raw_volume_metrics_rvol_std_21d_slope_v048_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_21d_slope_v049_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_21d_slope_v050_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_21d_slope_v051_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_21d_slope_v052_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_21d_slope_v053_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_21d_slope_v054_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_21d_slope_v055_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_21d_slope_v056_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_21d_slope_v057_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_21d_slope_v058_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_21d_slope_v060_signal, f21rvv_f21_raw_volume_metrics_rvol_level_42d_slope_v061_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_42d_slope_v062_signal, f21rvv_f21_raw_volume_metrics_rvol_std_42d_slope_v063_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_42d_slope_v064_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_42d_slope_v065_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_42d_slope_v066_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_42d_slope_v067_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_42d_slope_v068_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_42d_slope_v069_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_42d_slope_v070_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_42d_slope_v071_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_42d_slope_v072_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_42d_slope_v073_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_42d_slope_v075_signal, f21rvv_f21_raw_volume_metrics_rvol_level_63d_slope_v076_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_63d_slope_v077_signal, f21rvv_f21_raw_volume_metrics_rvol_std_63d_slope_v078_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_63d_slope_v079_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_63d_slope_v080_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_63d_slope_v081_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_63d_slope_v082_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_63d_slope_v083_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_63d_slope_v084_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_63d_slope_v085_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_63d_slope_v086_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_63d_slope_v087_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_63d_slope_v088_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_63d_slope_v090_signal, f21rvv_f21_raw_volume_metrics_rvol_level_84d_slope_v091_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_84d_slope_v092_signal, f21rvv_f21_raw_volume_metrics_rvol_std_84d_slope_v093_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_84d_slope_v094_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_84d_slope_v095_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_84d_slope_v096_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_84d_slope_v097_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_84d_slope_v098_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_84d_slope_v099_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_84d_slope_v100_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_84d_slope_v101_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_84d_slope_v102_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_84d_slope_v103_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_84d_slope_v105_signal, f21rvv_f21_raw_volume_metrics_rvol_level_126d_slope_v106_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_126d_slope_v107_signal, f21rvv_f21_raw_volume_metrics_rvol_std_126d_slope_v108_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_126d_slope_v109_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_126d_slope_v110_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_126d_slope_v111_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_126d_slope_v112_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_126d_slope_v113_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_126d_slope_v114_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_126d_slope_v115_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_126d_slope_v116_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_126d_slope_v117_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_126d_slope_v118_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_126d_slope_v120_signal, f21rvv_f21_raw_volume_metrics_rvol_level_252d_slope_v121_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_252d_slope_v122_signal, f21rvv_f21_raw_volume_metrics_rvol_std_252d_slope_v123_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_252d_slope_v124_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_252d_slope_v125_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_252d_slope_v126_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_252d_slope_v127_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_252d_slope_v128_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_252d_slope_v129_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_252d_slope_v130_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_252d_slope_v131_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_252d_slope_v132_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_252d_slope_v133_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_252d_slope_v135_signal, f21rvv_f21_raw_volume_metrics_rvol_level_504d_slope_v136_signal, f21rvv_f21_raw_volume_metrics_rvol_mean_504d_slope_v137_signal, f21rvv_f21_raw_volume_metrics_rvol_std_504d_slope_v138_signal, f21rvv_f21_raw_volume_metrics_rvol_zscore_504d_slope_v139_signal, f21rvv_f21_raw_volume_metrics_rvol_delta_504d_slope_v140_signal, f21rvv_f21_raw_volume_metrics_rvol_pctdelta_504d_slope_v141_signal, f21rvv_f21_raw_volume_metrics_rvol_upper_gap_504d_slope_v142_signal, f21rvv_f21_raw_volume_metrics_rvol_lower_gap_504d_slope_v143_signal, f21rvv_f21_raw_volume_metrics_rvol_short_mean_gap_504d_slope_v144_signal, f21rvv_f21_raw_volume_metrics_rvol_energy_504d_slope_v145_signal, f21rvv_f21_raw_volume_metrics_rvol_ewm_gap_504d_slope_v146_signal, f21rvv_f21_raw_volume_metrics_rvol_tail_relief_504d_slope_v147_signal, f21rvv_f21_raw_volume_metrics_rvol_peak_fade_504d_slope_v148_signal, f21rvv_f21_raw_volume_metrics_rvol_vol_adj_delta_504d_slope_v150_signal]}
F21_RAW_VOLUME_METRICS_REGISTRY_SLOPE = REGISTRY

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
