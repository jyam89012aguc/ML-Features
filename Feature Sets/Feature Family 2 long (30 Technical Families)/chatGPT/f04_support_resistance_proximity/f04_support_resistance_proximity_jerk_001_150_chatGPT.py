import inspect
import numpy as np
import pandas as pd


def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _support_resistance_proximity(closeadj, w):
    support = closeadj.rolling(w, min_periods=2).min().shift(1)
    resistance = closeadj.rolling(w, min_periods=2).max().shift(1)
    return ((closeadj - support) / support.abs().replace(0, np.nan)) - ((resistance - closeadj) / resistance.abs().replace(0, np.nan))

# jk5 5d level sr
def f04sr_f04_support_resistance_proximity_sr_level_5d_jerk_v001_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_5d_jerk_v002_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d var sr
def f04sr_f04_support_resistance_proximity_sr_std_5d_jerk_v003_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(5, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_5d_jerk_v004_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = _z(sig, 5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_5d_jerk_v005_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_5d_jerk_v006_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_5d_jerk_v007_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_5d_jerk_v008_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_5d_jerk_v009_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_5d_jerk_v010_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_5d_jerk_v011_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_5d_jerk_v012_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_5d_jerk_v013_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_5d_jerk_v014_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_5d_jerk_v015_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d level sr
def f04sr_f04_support_resistance_proximity_sr_level_10d_jerk_v016_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_10d_jerk_v017_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d var sr
def f04sr_f04_support_resistance_proximity_sr_std_10d_jerk_v018_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(10, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_10d_jerk_v019_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = _z(sig, 10)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_10d_jerk_v020_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_10d_jerk_v021_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_10d_jerk_v022_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_10d_jerk_v023_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_10d_jerk_v024_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_10d_jerk_v025_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_10d_jerk_v026_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_10d_jerk_v027_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_10d_jerk_v028_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_10d_jerk_v029_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_10d_jerk_v030_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d level sr
def f04sr_f04_support_resistance_proximity_sr_level_15d_jerk_v031_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_15d_jerk_v032_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d var sr
def f04sr_f04_support_resistance_proximity_sr_std_15d_jerk_v033_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(15, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_15d_jerk_v034_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = _z(sig, 15)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_15d_jerk_v035_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_15d_jerk_v036_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_15d_jerk_v037_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_15d_jerk_v038_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_15d_jerk_v039_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_15d_jerk_v040_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_15d_jerk_v041_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_15d_jerk_v042_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_15d_jerk_v043_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_15d_jerk_v044_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_15d_jerk_v045_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d level sr
def f04sr_f04_support_resistance_proximity_sr_level_21d_jerk_v046_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_21d_jerk_v047_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d var sr
def f04sr_f04_support_resistance_proximity_sr_std_21d_jerk_v048_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(21, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_21d_jerk_v049_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = _z(sig, 21)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_21d_jerk_v050_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_21d_jerk_v051_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_21d_jerk_v052_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_21d_jerk_v053_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_21d_jerk_v054_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_21d_jerk_v055_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_21d_jerk_v056_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_21d_jerk_v057_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_21d_jerk_v058_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_21d_jerk_v059_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_21d_jerk_v060_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d level sr
def f04sr_f04_support_resistance_proximity_sr_level_42d_jerk_v061_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_42d_jerk_v062_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d var sr
def f04sr_f04_support_resistance_proximity_sr_std_42d_jerk_v063_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(42, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_42d_jerk_v064_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = _z(sig, 42)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_42d_jerk_v065_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_42d_jerk_v066_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_42d_jerk_v067_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_42d_jerk_v068_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_42d_jerk_v069_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_42d_jerk_v070_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_42d_jerk_v071_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_42d_jerk_v072_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_42d_jerk_v073_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_42d_jerk_v074_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_42d_jerk_v075_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d level sr
def f04sr_f04_support_resistance_proximity_sr_level_63d_jerk_v076_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_63d_jerk_v077_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d var sr
def f04sr_f04_support_resistance_proximity_sr_std_63d_jerk_v078_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.rolling(63, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_63d_jerk_v079_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = _z(sig, 63)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_63d_jerk_v080_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_63d_jerk_v081_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_63d_jerk_v082_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_63d_jerk_v083_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_63d_jerk_v084_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_63d_jerk_v085_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_63d_jerk_v086_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_63d_jerk_v087_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_63d_jerk_v088_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_63d_jerk_v089_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_63d_jerk_v090_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d level sr
def f04sr_f04_support_resistance_proximity_sr_level_84d_jerk_v091_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_84d_jerk_v092_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d var sr
def f04sr_f04_support_resistance_proximity_sr_std_84d_jerk_v093_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.rolling(84, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_84d_jerk_v094_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = _z(sig, 84)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_84d_jerk_v095_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_84d_jerk_v096_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_84d_jerk_v097_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_84d_jerk_v098_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_84d_jerk_v099_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_84d_jerk_v100_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_84d_jerk_v101_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_84d_jerk_v102_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_84d_jerk_v103_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_84d_jerk_v104_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_84d_jerk_v105_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d level sr
def f04sr_f04_support_resistance_proximity_sr_level_126d_jerk_v106_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_126d_jerk_v107_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d var sr
def f04sr_f04_support_resistance_proximity_sr_std_126d_jerk_v108_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.rolling(126, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_126d_jerk_v109_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = _z(sig, 126)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_126d_jerk_v110_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_126d_jerk_v111_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_126d_jerk_v112_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_126d_jerk_v113_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_126d_jerk_v114_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_126d_jerk_v115_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_126d_jerk_v116_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_126d_jerk_v117_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_126d_jerk_v118_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_126d_jerk_v119_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_126d_jerk_v120_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d level sr
def f04sr_f04_support_resistance_proximity_sr_level_252d_jerk_v121_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_252d_jerk_v122_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d var sr
def f04sr_f04_support_resistance_proximity_sr_std_252d_jerk_v123_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.rolling(252, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_252d_jerk_v124_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = _z(sig, 252)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_252d_jerk_v125_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_252d_jerk_v126_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_252d_jerk_v127_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_252d_jerk_v128_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_252d_jerk_v129_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_252d_jerk_v130_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_252d_jerk_v131_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_252d_jerk_v132_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_252d_jerk_v133_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_252d_jerk_v134_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_252d_jerk_v135_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d level sr
def f04sr_f04_support_resistance_proximity_sr_level_504d_jerk_v136_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_504d_jerk_v137_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d var sr
def f04sr_f04_support_resistance_proximity_sr_std_504d_jerk_v138_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.rolling(504, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_504d_jerk_v139_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = _z(sig, 504)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_504d_jerk_v140_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d relchg sr
def f04sr_f04_support_resistance_proximity_sr_pctdelta_504d_jerk_v141_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_504d_jerk_v142_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_504d_jerk_v143_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_504d_jerk_v144_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_504d_jerk_v145_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_504d_jerk_v146_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_504d_jerk_v147_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_504d_jerk_v148_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_504d_jerk_v149_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_504d_jerk_v150_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [f04sr_f04_support_resistance_proximity_sr_level_5d_jerk_v001_signal, f04sr_f04_support_resistance_proximity_sr_mean_5d_jerk_v002_signal, f04sr_f04_support_resistance_proximity_sr_std_5d_jerk_v003_signal, f04sr_f04_support_resistance_proximity_sr_zscore_5d_jerk_v004_signal, f04sr_f04_support_resistance_proximity_sr_delta_5d_jerk_v005_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_5d_jerk_v006_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_5d_jerk_v007_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_5d_jerk_v008_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_5d_jerk_v009_signal, f04sr_f04_support_resistance_proximity_sr_energy_5d_jerk_v010_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_5d_jerk_v011_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_5d_jerk_v012_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_5d_jerk_v013_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_5d_jerk_v014_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_5d_jerk_v015_signal, f04sr_f04_support_resistance_proximity_sr_level_10d_jerk_v016_signal, f04sr_f04_support_resistance_proximity_sr_mean_10d_jerk_v017_signal, f04sr_f04_support_resistance_proximity_sr_std_10d_jerk_v018_signal, f04sr_f04_support_resistance_proximity_sr_zscore_10d_jerk_v019_signal, f04sr_f04_support_resistance_proximity_sr_delta_10d_jerk_v020_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_10d_jerk_v021_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_10d_jerk_v022_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_10d_jerk_v023_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_10d_jerk_v024_signal, f04sr_f04_support_resistance_proximity_sr_energy_10d_jerk_v025_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_10d_jerk_v026_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_10d_jerk_v027_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_10d_jerk_v028_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_10d_jerk_v029_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_10d_jerk_v030_signal, f04sr_f04_support_resistance_proximity_sr_level_15d_jerk_v031_signal, f04sr_f04_support_resistance_proximity_sr_mean_15d_jerk_v032_signal, f04sr_f04_support_resistance_proximity_sr_std_15d_jerk_v033_signal, f04sr_f04_support_resistance_proximity_sr_zscore_15d_jerk_v034_signal, f04sr_f04_support_resistance_proximity_sr_delta_15d_jerk_v035_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_15d_jerk_v036_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_15d_jerk_v037_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_15d_jerk_v038_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_15d_jerk_v039_signal, f04sr_f04_support_resistance_proximity_sr_energy_15d_jerk_v040_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_15d_jerk_v041_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_15d_jerk_v042_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_15d_jerk_v043_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_15d_jerk_v044_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_15d_jerk_v045_signal, f04sr_f04_support_resistance_proximity_sr_level_21d_jerk_v046_signal, f04sr_f04_support_resistance_proximity_sr_mean_21d_jerk_v047_signal, f04sr_f04_support_resistance_proximity_sr_std_21d_jerk_v048_signal, f04sr_f04_support_resistance_proximity_sr_zscore_21d_jerk_v049_signal, f04sr_f04_support_resistance_proximity_sr_delta_21d_jerk_v050_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_21d_jerk_v051_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_21d_jerk_v052_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_21d_jerk_v053_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_21d_jerk_v054_signal, f04sr_f04_support_resistance_proximity_sr_energy_21d_jerk_v055_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_21d_jerk_v056_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_21d_jerk_v057_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_21d_jerk_v058_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_21d_jerk_v059_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_21d_jerk_v060_signal, f04sr_f04_support_resistance_proximity_sr_level_42d_jerk_v061_signal, f04sr_f04_support_resistance_proximity_sr_mean_42d_jerk_v062_signal, f04sr_f04_support_resistance_proximity_sr_std_42d_jerk_v063_signal, f04sr_f04_support_resistance_proximity_sr_zscore_42d_jerk_v064_signal, f04sr_f04_support_resistance_proximity_sr_delta_42d_jerk_v065_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_42d_jerk_v066_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_42d_jerk_v067_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_42d_jerk_v068_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_42d_jerk_v069_signal, f04sr_f04_support_resistance_proximity_sr_energy_42d_jerk_v070_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_42d_jerk_v071_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_42d_jerk_v072_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_42d_jerk_v073_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_42d_jerk_v074_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_42d_jerk_v075_signal, f04sr_f04_support_resistance_proximity_sr_level_63d_jerk_v076_signal, f04sr_f04_support_resistance_proximity_sr_mean_63d_jerk_v077_signal, f04sr_f04_support_resistance_proximity_sr_std_63d_jerk_v078_signal, f04sr_f04_support_resistance_proximity_sr_zscore_63d_jerk_v079_signal, f04sr_f04_support_resistance_proximity_sr_delta_63d_jerk_v080_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_63d_jerk_v081_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_63d_jerk_v082_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_63d_jerk_v083_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_63d_jerk_v084_signal, f04sr_f04_support_resistance_proximity_sr_energy_63d_jerk_v085_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_63d_jerk_v086_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_63d_jerk_v087_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_63d_jerk_v088_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_63d_jerk_v089_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_63d_jerk_v090_signal, f04sr_f04_support_resistance_proximity_sr_level_84d_jerk_v091_signal, f04sr_f04_support_resistance_proximity_sr_mean_84d_jerk_v092_signal, f04sr_f04_support_resistance_proximity_sr_std_84d_jerk_v093_signal, f04sr_f04_support_resistance_proximity_sr_zscore_84d_jerk_v094_signal, f04sr_f04_support_resistance_proximity_sr_delta_84d_jerk_v095_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_84d_jerk_v096_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_84d_jerk_v097_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_84d_jerk_v098_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_84d_jerk_v099_signal, f04sr_f04_support_resistance_proximity_sr_energy_84d_jerk_v100_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_84d_jerk_v101_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_84d_jerk_v102_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_84d_jerk_v103_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_84d_jerk_v104_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_84d_jerk_v105_signal, f04sr_f04_support_resistance_proximity_sr_level_126d_jerk_v106_signal, f04sr_f04_support_resistance_proximity_sr_mean_126d_jerk_v107_signal, f04sr_f04_support_resistance_proximity_sr_std_126d_jerk_v108_signal, f04sr_f04_support_resistance_proximity_sr_zscore_126d_jerk_v109_signal, f04sr_f04_support_resistance_proximity_sr_delta_126d_jerk_v110_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_126d_jerk_v111_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_126d_jerk_v112_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_126d_jerk_v113_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_126d_jerk_v114_signal, f04sr_f04_support_resistance_proximity_sr_energy_126d_jerk_v115_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_126d_jerk_v116_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_126d_jerk_v117_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_126d_jerk_v118_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_126d_jerk_v119_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_126d_jerk_v120_signal, f04sr_f04_support_resistance_proximity_sr_level_252d_jerk_v121_signal, f04sr_f04_support_resistance_proximity_sr_mean_252d_jerk_v122_signal, f04sr_f04_support_resistance_proximity_sr_std_252d_jerk_v123_signal, f04sr_f04_support_resistance_proximity_sr_zscore_252d_jerk_v124_signal, f04sr_f04_support_resistance_proximity_sr_delta_252d_jerk_v125_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_252d_jerk_v126_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_252d_jerk_v127_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_252d_jerk_v128_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_252d_jerk_v129_signal, f04sr_f04_support_resistance_proximity_sr_energy_252d_jerk_v130_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_252d_jerk_v131_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_252d_jerk_v132_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_252d_jerk_v133_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_252d_jerk_v134_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_252d_jerk_v135_signal, f04sr_f04_support_resistance_proximity_sr_level_504d_jerk_v136_signal, f04sr_f04_support_resistance_proximity_sr_mean_504d_jerk_v137_signal, f04sr_f04_support_resistance_proximity_sr_std_504d_jerk_v138_signal, f04sr_f04_support_resistance_proximity_sr_zscore_504d_jerk_v139_signal, f04sr_f04_support_resistance_proximity_sr_delta_504d_jerk_v140_signal, f04sr_f04_support_resistance_proximity_sr_pctdelta_504d_jerk_v141_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_504d_jerk_v142_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_504d_jerk_v143_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_504d_jerk_v144_signal, f04sr_f04_support_resistance_proximity_sr_energy_504d_jerk_v145_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_504d_jerk_v146_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_504d_jerk_v147_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_504d_jerk_v148_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_504d_jerk_v149_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_504d_jerk_v150_signal]}
F04_SUPPORT_RESISTANCE_PROXIMITY_REGISTRY_JERK = REGISTRY


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
        assert "_support_resistance_proximity" in src
    assert ok_nan >= int(0.80 * len(funcs))
