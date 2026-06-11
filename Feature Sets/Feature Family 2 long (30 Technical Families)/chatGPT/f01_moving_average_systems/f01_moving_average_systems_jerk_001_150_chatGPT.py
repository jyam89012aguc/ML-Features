import inspect
import numpy as np
import pandas as pd


def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _ma_system_spread(closeadj, w):
    fast = closeadj.rolling(max(2, w//3), min_periods=2).mean()
    slow = closeadj.rolling(w, min_periods=2).mean()
    return (fast - slow) / slow.abs().replace(0, np.nan)

# jk5 5d level ma
def f01ma_f01_moving_average_systems_ma_level_5d_jerk_v001_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d mean ma
def f01ma_f01_moving_average_systems_ma_mean_5d_jerk_v002_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d var ma
def f01ma_f01_moving_average_systems_ma_std_5d_jerk_v003_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.rolling(5, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_5d_jerk_v004_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = _z(sig, 5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d change ma
def f01ma_f01_moving_average_systems_ma_delta_5d_jerk_v005_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_5d_jerk_v006_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_5d_jerk_v007_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_5d_jerk_v008_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_5d_jerk_v009_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d energy ma
def f01ma_f01_moving_average_systems_ma_energy_5d_jerk_v010_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_5d_jerk_v011_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_5d_jerk_v012_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_5d_jerk_v013_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_5d_jerk_v014_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_5d_jerk_v015_signal(closeadj):
    sig = _ma_system_spread(closeadj, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d level ma
def f01ma_f01_moving_average_systems_ma_level_10d_jerk_v016_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d mean ma
def f01ma_f01_moving_average_systems_ma_mean_10d_jerk_v017_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d var ma
def f01ma_f01_moving_average_systems_ma_std_10d_jerk_v018_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.rolling(10, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_10d_jerk_v019_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = _z(sig, 10)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d change ma
def f01ma_f01_moving_average_systems_ma_delta_10d_jerk_v020_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_10d_jerk_v021_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_10d_jerk_v022_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_10d_jerk_v023_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_10d_jerk_v024_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d energy ma
def f01ma_f01_moving_average_systems_ma_energy_10d_jerk_v025_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_10d_jerk_v026_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_10d_jerk_v027_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_10d_jerk_v028_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_10d_jerk_v029_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_10d_jerk_v030_signal(closeadj):
    sig = _ma_system_spread(closeadj, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d level ma
def f01ma_f01_moving_average_systems_ma_level_15d_jerk_v031_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d mean ma
def f01ma_f01_moving_average_systems_ma_mean_15d_jerk_v032_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d var ma
def f01ma_f01_moving_average_systems_ma_std_15d_jerk_v033_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.rolling(15, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_15d_jerk_v034_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = _z(sig, 15)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d change ma
def f01ma_f01_moving_average_systems_ma_delta_15d_jerk_v035_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_15d_jerk_v036_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_15d_jerk_v037_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_15d_jerk_v038_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_15d_jerk_v039_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d energy ma
def f01ma_f01_moving_average_systems_ma_energy_15d_jerk_v040_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_15d_jerk_v041_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_15d_jerk_v042_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_15d_jerk_v043_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_15d_jerk_v044_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_15d_jerk_v045_signal(closeadj):
    sig = _ma_system_spread(closeadj, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d level ma
def f01ma_f01_moving_average_systems_ma_level_21d_jerk_v046_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d mean ma
def f01ma_f01_moving_average_systems_ma_mean_21d_jerk_v047_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d var ma
def f01ma_f01_moving_average_systems_ma_std_21d_jerk_v048_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.rolling(21, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_21d_jerk_v049_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = _z(sig, 21)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d change ma
def f01ma_f01_moving_average_systems_ma_delta_21d_jerk_v050_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_21d_jerk_v051_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_21d_jerk_v052_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_21d_jerk_v053_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_21d_jerk_v054_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d energy ma
def f01ma_f01_moving_average_systems_ma_energy_21d_jerk_v055_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_21d_jerk_v056_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_21d_jerk_v057_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_21d_jerk_v058_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_21d_jerk_v059_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_21d_jerk_v060_signal(closeadj):
    sig = _ma_system_spread(closeadj, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d level ma
def f01ma_f01_moving_average_systems_ma_level_42d_jerk_v061_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d mean ma
def f01ma_f01_moving_average_systems_ma_mean_42d_jerk_v062_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d var ma
def f01ma_f01_moving_average_systems_ma_std_42d_jerk_v063_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.rolling(42, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_42d_jerk_v064_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = _z(sig, 42)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d change ma
def f01ma_f01_moving_average_systems_ma_delta_42d_jerk_v065_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_42d_jerk_v066_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_42d_jerk_v067_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_42d_jerk_v068_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_42d_jerk_v069_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d energy ma
def f01ma_f01_moving_average_systems_ma_energy_42d_jerk_v070_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_42d_jerk_v071_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_42d_jerk_v072_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_42d_jerk_v073_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_42d_jerk_v074_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_42d_jerk_v075_signal(closeadj):
    sig = _ma_system_spread(closeadj, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d level ma
def f01ma_f01_moving_average_systems_ma_level_63d_jerk_v076_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d mean ma
def f01ma_f01_moving_average_systems_ma_mean_63d_jerk_v077_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d var ma
def f01ma_f01_moving_average_systems_ma_std_63d_jerk_v078_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.rolling(63, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_63d_jerk_v079_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = _z(sig, 63)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d change ma
def f01ma_f01_moving_average_systems_ma_delta_63d_jerk_v080_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_63d_jerk_v081_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_63d_jerk_v082_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_63d_jerk_v083_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_63d_jerk_v084_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d energy ma
def f01ma_f01_moving_average_systems_ma_energy_63d_jerk_v085_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_63d_jerk_v086_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_63d_jerk_v087_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_63d_jerk_v088_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_63d_jerk_v089_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_63d_jerk_v090_signal(closeadj):
    sig = _ma_system_spread(closeadj, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d level ma
def f01ma_f01_moving_average_systems_ma_level_84d_jerk_v091_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d mean ma
def f01ma_f01_moving_average_systems_ma_mean_84d_jerk_v092_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d var ma
def f01ma_f01_moving_average_systems_ma_std_84d_jerk_v093_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.rolling(84, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_84d_jerk_v094_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = _z(sig, 84)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d change ma
def f01ma_f01_moving_average_systems_ma_delta_84d_jerk_v095_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_84d_jerk_v096_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_84d_jerk_v097_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_84d_jerk_v098_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_84d_jerk_v099_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d energy ma
def f01ma_f01_moving_average_systems_ma_energy_84d_jerk_v100_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_84d_jerk_v101_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_84d_jerk_v102_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_84d_jerk_v103_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_84d_jerk_v104_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_84d_jerk_v105_signal(closeadj):
    sig = _ma_system_spread(closeadj, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d level ma
def f01ma_f01_moving_average_systems_ma_level_126d_jerk_v106_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d mean ma
def f01ma_f01_moving_average_systems_ma_mean_126d_jerk_v107_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d var ma
def f01ma_f01_moving_average_systems_ma_std_126d_jerk_v108_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.rolling(126, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_126d_jerk_v109_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = _z(sig, 126)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d change ma
def f01ma_f01_moving_average_systems_ma_delta_126d_jerk_v110_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_126d_jerk_v111_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_126d_jerk_v112_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_126d_jerk_v113_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_126d_jerk_v114_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d energy ma
def f01ma_f01_moving_average_systems_ma_energy_126d_jerk_v115_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_126d_jerk_v116_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_126d_jerk_v117_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_126d_jerk_v118_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_126d_jerk_v119_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_126d_jerk_v120_signal(closeadj):
    sig = _ma_system_spread(closeadj, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d level ma
def f01ma_f01_moving_average_systems_ma_level_252d_jerk_v121_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d mean ma
def f01ma_f01_moving_average_systems_ma_mean_252d_jerk_v122_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d var ma
def f01ma_f01_moving_average_systems_ma_std_252d_jerk_v123_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.rolling(252, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_252d_jerk_v124_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = _z(sig, 252)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d change ma
def f01ma_f01_moving_average_systems_ma_delta_252d_jerk_v125_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_252d_jerk_v126_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_252d_jerk_v127_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_252d_jerk_v128_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_252d_jerk_v129_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d energy ma
def f01ma_f01_moving_average_systems_ma_energy_252d_jerk_v130_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_252d_jerk_v131_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_252d_jerk_v132_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_252d_jerk_v133_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_252d_jerk_v134_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_252d_jerk_v135_signal(closeadj):
    sig = _ma_system_spread(closeadj, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d level ma
def f01ma_f01_moving_average_systems_ma_level_504d_jerk_v136_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d mean ma
def f01ma_f01_moving_average_systems_ma_mean_504d_jerk_v137_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d var ma
def f01ma_f01_moving_average_systems_ma_std_504d_jerk_v138_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.rolling(504, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d zscore ma
def f01ma_f01_moving_average_systems_ma_zscore_504d_jerk_v139_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = _z(sig, 504)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d change ma
def f01ma_f01_moving_average_systems_ma_delta_504d_jerk_v140_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d relchg ma
def f01ma_f01_moving_average_systems_ma_pctdelta_504d_jerk_v141_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q75gap ma
def f01ma_f01_moving_average_systems_ma_upper_gap_504d_jerk_v142_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q25gap ma
def f01ma_f01_moving_average_systems_ma_lower_gap_504d_jerk_v143_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d smean gap ma
def f01ma_f01_moving_average_systems_ma_short_mean_gap_504d_jerk_v144_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d energy ma
def f01ma_f01_moving_average_systems_ma_energy_504d_jerk_v145_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d ewm gap ma
def f01ma_f01_moving_average_systems_ma_ewm_gap_504d_jerk_v146_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d tail relief ma
def f01ma_f01_moving_average_systems_ma_tail_relief_504d_jerk_v147_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d peak fade ma
def f01ma_f01_moving_average_systems_ma_peak_fade_504d_jerk_v148_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d absmean ma
def f01ma_f01_moving_average_systems_ma_mean_abs_504d_jerk_v149_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d voladj chg ma
def f01ma_f01_moving_average_systems_ma_vol_adj_delta_504d_jerk_v150_signal(closeadj):
    sig = _ma_system_spread(closeadj, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [f01ma_f01_moving_average_systems_ma_level_5d_jerk_v001_signal, f01ma_f01_moving_average_systems_ma_mean_5d_jerk_v002_signal, f01ma_f01_moving_average_systems_ma_std_5d_jerk_v003_signal, f01ma_f01_moving_average_systems_ma_zscore_5d_jerk_v004_signal, f01ma_f01_moving_average_systems_ma_delta_5d_jerk_v005_signal, f01ma_f01_moving_average_systems_ma_pctdelta_5d_jerk_v006_signal, f01ma_f01_moving_average_systems_ma_upper_gap_5d_jerk_v007_signal, f01ma_f01_moving_average_systems_ma_lower_gap_5d_jerk_v008_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_5d_jerk_v009_signal, f01ma_f01_moving_average_systems_ma_energy_5d_jerk_v010_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_5d_jerk_v011_signal, f01ma_f01_moving_average_systems_ma_tail_relief_5d_jerk_v012_signal, f01ma_f01_moving_average_systems_ma_peak_fade_5d_jerk_v013_signal, f01ma_f01_moving_average_systems_ma_mean_abs_5d_jerk_v014_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_5d_jerk_v015_signal, f01ma_f01_moving_average_systems_ma_level_10d_jerk_v016_signal, f01ma_f01_moving_average_systems_ma_mean_10d_jerk_v017_signal, f01ma_f01_moving_average_systems_ma_std_10d_jerk_v018_signal, f01ma_f01_moving_average_systems_ma_zscore_10d_jerk_v019_signal, f01ma_f01_moving_average_systems_ma_delta_10d_jerk_v020_signal, f01ma_f01_moving_average_systems_ma_pctdelta_10d_jerk_v021_signal, f01ma_f01_moving_average_systems_ma_upper_gap_10d_jerk_v022_signal, f01ma_f01_moving_average_systems_ma_lower_gap_10d_jerk_v023_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_10d_jerk_v024_signal, f01ma_f01_moving_average_systems_ma_energy_10d_jerk_v025_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_10d_jerk_v026_signal, f01ma_f01_moving_average_systems_ma_tail_relief_10d_jerk_v027_signal, f01ma_f01_moving_average_systems_ma_peak_fade_10d_jerk_v028_signal, f01ma_f01_moving_average_systems_ma_mean_abs_10d_jerk_v029_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_10d_jerk_v030_signal, f01ma_f01_moving_average_systems_ma_level_15d_jerk_v031_signal, f01ma_f01_moving_average_systems_ma_mean_15d_jerk_v032_signal, f01ma_f01_moving_average_systems_ma_std_15d_jerk_v033_signal, f01ma_f01_moving_average_systems_ma_zscore_15d_jerk_v034_signal, f01ma_f01_moving_average_systems_ma_delta_15d_jerk_v035_signal, f01ma_f01_moving_average_systems_ma_pctdelta_15d_jerk_v036_signal, f01ma_f01_moving_average_systems_ma_upper_gap_15d_jerk_v037_signal, f01ma_f01_moving_average_systems_ma_lower_gap_15d_jerk_v038_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_15d_jerk_v039_signal, f01ma_f01_moving_average_systems_ma_energy_15d_jerk_v040_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_15d_jerk_v041_signal, f01ma_f01_moving_average_systems_ma_tail_relief_15d_jerk_v042_signal, f01ma_f01_moving_average_systems_ma_peak_fade_15d_jerk_v043_signal, f01ma_f01_moving_average_systems_ma_mean_abs_15d_jerk_v044_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_15d_jerk_v045_signal, f01ma_f01_moving_average_systems_ma_level_21d_jerk_v046_signal, f01ma_f01_moving_average_systems_ma_mean_21d_jerk_v047_signal, f01ma_f01_moving_average_systems_ma_std_21d_jerk_v048_signal, f01ma_f01_moving_average_systems_ma_zscore_21d_jerk_v049_signal, f01ma_f01_moving_average_systems_ma_delta_21d_jerk_v050_signal, f01ma_f01_moving_average_systems_ma_pctdelta_21d_jerk_v051_signal, f01ma_f01_moving_average_systems_ma_upper_gap_21d_jerk_v052_signal, f01ma_f01_moving_average_systems_ma_lower_gap_21d_jerk_v053_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_21d_jerk_v054_signal, f01ma_f01_moving_average_systems_ma_energy_21d_jerk_v055_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_21d_jerk_v056_signal, f01ma_f01_moving_average_systems_ma_tail_relief_21d_jerk_v057_signal, f01ma_f01_moving_average_systems_ma_peak_fade_21d_jerk_v058_signal, f01ma_f01_moving_average_systems_ma_mean_abs_21d_jerk_v059_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_21d_jerk_v060_signal, f01ma_f01_moving_average_systems_ma_level_42d_jerk_v061_signal, f01ma_f01_moving_average_systems_ma_mean_42d_jerk_v062_signal, f01ma_f01_moving_average_systems_ma_std_42d_jerk_v063_signal, f01ma_f01_moving_average_systems_ma_zscore_42d_jerk_v064_signal, f01ma_f01_moving_average_systems_ma_delta_42d_jerk_v065_signal, f01ma_f01_moving_average_systems_ma_pctdelta_42d_jerk_v066_signal, f01ma_f01_moving_average_systems_ma_upper_gap_42d_jerk_v067_signal, f01ma_f01_moving_average_systems_ma_lower_gap_42d_jerk_v068_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_42d_jerk_v069_signal, f01ma_f01_moving_average_systems_ma_energy_42d_jerk_v070_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_42d_jerk_v071_signal, f01ma_f01_moving_average_systems_ma_tail_relief_42d_jerk_v072_signal, f01ma_f01_moving_average_systems_ma_peak_fade_42d_jerk_v073_signal, f01ma_f01_moving_average_systems_ma_mean_abs_42d_jerk_v074_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_42d_jerk_v075_signal, f01ma_f01_moving_average_systems_ma_level_63d_jerk_v076_signal, f01ma_f01_moving_average_systems_ma_mean_63d_jerk_v077_signal, f01ma_f01_moving_average_systems_ma_std_63d_jerk_v078_signal, f01ma_f01_moving_average_systems_ma_zscore_63d_jerk_v079_signal, f01ma_f01_moving_average_systems_ma_delta_63d_jerk_v080_signal, f01ma_f01_moving_average_systems_ma_pctdelta_63d_jerk_v081_signal, f01ma_f01_moving_average_systems_ma_upper_gap_63d_jerk_v082_signal, f01ma_f01_moving_average_systems_ma_lower_gap_63d_jerk_v083_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_63d_jerk_v084_signal, f01ma_f01_moving_average_systems_ma_energy_63d_jerk_v085_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_63d_jerk_v086_signal, f01ma_f01_moving_average_systems_ma_tail_relief_63d_jerk_v087_signal, f01ma_f01_moving_average_systems_ma_peak_fade_63d_jerk_v088_signal, f01ma_f01_moving_average_systems_ma_mean_abs_63d_jerk_v089_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_63d_jerk_v090_signal, f01ma_f01_moving_average_systems_ma_level_84d_jerk_v091_signal, f01ma_f01_moving_average_systems_ma_mean_84d_jerk_v092_signal, f01ma_f01_moving_average_systems_ma_std_84d_jerk_v093_signal, f01ma_f01_moving_average_systems_ma_zscore_84d_jerk_v094_signal, f01ma_f01_moving_average_systems_ma_delta_84d_jerk_v095_signal, f01ma_f01_moving_average_systems_ma_pctdelta_84d_jerk_v096_signal, f01ma_f01_moving_average_systems_ma_upper_gap_84d_jerk_v097_signal, f01ma_f01_moving_average_systems_ma_lower_gap_84d_jerk_v098_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_84d_jerk_v099_signal, f01ma_f01_moving_average_systems_ma_energy_84d_jerk_v100_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_84d_jerk_v101_signal, f01ma_f01_moving_average_systems_ma_tail_relief_84d_jerk_v102_signal, f01ma_f01_moving_average_systems_ma_peak_fade_84d_jerk_v103_signal, f01ma_f01_moving_average_systems_ma_mean_abs_84d_jerk_v104_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_84d_jerk_v105_signal, f01ma_f01_moving_average_systems_ma_level_126d_jerk_v106_signal, f01ma_f01_moving_average_systems_ma_mean_126d_jerk_v107_signal, f01ma_f01_moving_average_systems_ma_std_126d_jerk_v108_signal, f01ma_f01_moving_average_systems_ma_zscore_126d_jerk_v109_signal, f01ma_f01_moving_average_systems_ma_delta_126d_jerk_v110_signal, f01ma_f01_moving_average_systems_ma_pctdelta_126d_jerk_v111_signal, f01ma_f01_moving_average_systems_ma_upper_gap_126d_jerk_v112_signal, f01ma_f01_moving_average_systems_ma_lower_gap_126d_jerk_v113_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_126d_jerk_v114_signal, f01ma_f01_moving_average_systems_ma_energy_126d_jerk_v115_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_126d_jerk_v116_signal, f01ma_f01_moving_average_systems_ma_tail_relief_126d_jerk_v117_signal, f01ma_f01_moving_average_systems_ma_peak_fade_126d_jerk_v118_signal, f01ma_f01_moving_average_systems_ma_mean_abs_126d_jerk_v119_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_126d_jerk_v120_signal, f01ma_f01_moving_average_systems_ma_level_252d_jerk_v121_signal, f01ma_f01_moving_average_systems_ma_mean_252d_jerk_v122_signal, f01ma_f01_moving_average_systems_ma_std_252d_jerk_v123_signal, f01ma_f01_moving_average_systems_ma_zscore_252d_jerk_v124_signal, f01ma_f01_moving_average_systems_ma_delta_252d_jerk_v125_signal, f01ma_f01_moving_average_systems_ma_pctdelta_252d_jerk_v126_signal, f01ma_f01_moving_average_systems_ma_upper_gap_252d_jerk_v127_signal, f01ma_f01_moving_average_systems_ma_lower_gap_252d_jerk_v128_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_252d_jerk_v129_signal, f01ma_f01_moving_average_systems_ma_energy_252d_jerk_v130_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_252d_jerk_v131_signal, f01ma_f01_moving_average_systems_ma_tail_relief_252d_jerk_v132_signal, f01ma_f01_moving_average_systems_ma_peak_fade_252d_jerk_v133_signal, f01ma_f01_moving_average_systems_ma_mean_abs_252d_jerk_v134_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_252d_jerk_v135_signal, f01ma_f01_moving_average_systems_ma_level_504d_jerk_v136_signal, f01ma_f01_moving_average_systems_ma_mean_504d_jerk_v137_signal, f01ma_f01_moving_average_systems_ma_std_504d_jerk_v138_signal, f01ma_f01_moving_average_systems_ma_zscore_504d_jerk_v139_signal, f01ma_f01_moving_average_systems_ma_delta_504d_jerk_v140_signal, f01ma_f01_moving_average_systems_ma_pctdelta_504d_jerk_v141_signal, f01ma_f01_moving_average_systems_ma_upper_gap_504d_jerk_v142_signal, f01ma_f01_moving_average_systems_ma_lower_gap_504d_jerk_v143_signal, f01ma_f01_moving_average_systems_ma_short_mean_gap_504d_jerk_v144_signal, f01ma_f01_moving_average_systems_ma_energy_504d_jerk_v145_signal, f01ma_f01_moving_average_systems_ma_ewm_gap_504d_jerk_v146_signal, f01ma_f01_moving_average_systems_ma_tail_relief_504d_jerk_v147_signal, f01ma_f01_moving_average_systems_ma_peak_fade_504d_jerk_v148_signal, f01ma_f01_moving_average_systems_ma_mean_abs_504d_jerk_v149_signal, f01ma_f01_moving_average_systems_ma_vol_adj_delta_504d_jerk_v150_signal]}
F01_MOVING_AVERAGE_SYSTEMS_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    closeadj = base
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(closeadj)
        y2 = func(closeadj)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_ma_system_spread" in src
    assert ok_nan >= int(0.80 * len(funcs))
