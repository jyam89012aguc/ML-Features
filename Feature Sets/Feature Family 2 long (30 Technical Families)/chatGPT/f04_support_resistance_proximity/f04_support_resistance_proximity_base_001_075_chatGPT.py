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

# 5d level sr
def f04sr_f04_support_resistance_proximity_sr_level_5d_base_v001_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_5d_base_v002_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d var sr
def f04sr_f04_support_resistance_proximity_sr_std_5d_base_v003_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(5, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_5d_base_v004_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = _z(sig, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_5d_base_v005_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_5d_base_v007_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_5d_base_v008_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_5d_base_v009_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_5d_base_v010_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_5d_base_v011_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_5d_base_v012_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_5d_base_v013_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_5d_base_v014_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_5d_base_v015_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d level sr
def f04sr_f04_support_resistance_proximity_sr_level_10d_base_v016_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_10d_base_v017_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d var sr
def f04sr_f04_support_resistance_proximity_sr_std_10d_base_v018_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(10, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_10d_base_v019_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = _z(sig, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_10d_base_v020_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_10d_base_v022_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_10d_base_v023_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_10d_base_v024_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_10d_base_v025_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_10d_base_v026_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_10d_base_v027_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_10d_base_v028_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_10d_base_v029_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_10d_base_v030_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d level sr
def f04sr_f04_support_resistance_proximity_sr_level_15d_base_v031_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_15d_base_v032_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d var sr
def f04sr_f04_support_resistance_proximity_sr_std_15d_base_v033_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(15, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_15d_base_v034_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = _z(sig, 15)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_15d_base_v035_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_15d_base_v037_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_15d_base_v038_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_15d_base_v039_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_15d_base_v040_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_15d_base_v041_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_15d_base_v042_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_15d_base_v043_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_15d_base_v044_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_15d_base_v045_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level sr
def f04sr_f04_support_resistance_proximity_sr_level_21d_base_v046_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_21d_base_v047_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d var sr
def f04sr_f04_support_resistance_proximity_sr_std_21d_base_v048_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(21, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_21d_base_v049_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = _z(sig, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_21d_base_v050_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_21d_base_v052_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_21d_base_v053_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_21d_base_v054_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_21d_base_v055_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_21d_base_v056_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_21d_base_v057_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_21d_base_v058_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_21d_base_v059_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_21d_base_v060_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d level sr
def f04sr_f04_support_resistance_proximity_sr_level_42d_base_v061_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d mean sr
def f04sr_f04_support_resistance_proximity_sr_mean_42d_base_v062_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d var sr
def f04sr_f04_support_resistance_proximity_sr_std_42d_base_v063_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(42, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d zscore sr
def f04sr_f04_support_resistance_proximity_sr_zscore_42d_base_v064_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = _z(sig, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d change sr
def f04sr_f04_support_resistance_proximity_sr_delta_42d_base_v065_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q75gap sr
def f04sr_f04_support_resistance_proximity_sr_upper_gap_42d_base_v067_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q25gap sr
def f04sr_f04_support_resistance_proximity_sr_lower_gap_42d_base_v068_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d smean gap sr
def f04sr_f04_support_resistance_proximity_sr_short_mean_gap_42d_base_v069_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d energy sr
def f04sr_f04_support_resistance_proximity_sr_energy_42d_base_v070_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d ewm gap sr
def f04sr_f04_support_resistance_proximity_sr_ewm_gap_42d_base_v071_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d tail relief sr
def f04sr_f04_support_resistance_proximity_sr_tail_relief_42d_base_v072_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d peak fade sr
def f04sr_f04_support_resistance_proximity_sr_peak_fade_42d_base_v073_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d absmean sr
def f04sr_f04_support_resistance_proximity_sr_mean_abs_42d_base_v074_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d voladj chg sr
def f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_42d_base_v075_signal(closeadj):
    sig = _support_resistance_proximity(closeadj, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [f04sr_f04_support_resistance_proximity_sr_level_5d_base_v001_signal, f04sr_f04_support_resistance_proximity_sr_mean_5d_base_v002_signal, f04sr_f04_support_resistance_proximity_sr_std_5d_base_v003_signal, f04sr_f04_support_resistance_proximity_sr_zscore_5d_base_v004_signal, f04sr_f04_support_resistance_proximity_sr_delta_5d_base_v005_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_5d_base_v007_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_5d_base_v008_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_5d_base_v009_signal, f04sr_f04_support_resistance_proximity_sr_energy_5d_base_v010_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_5d_base_v011_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_5d_base_v012_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_5d_base_v013_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_5d_base_v014_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_5d_base_v015_signal, f04sr_f04_support_resistance_proximity_sr_level_10d_base_v016_signal, f04sr_f04_support_resistance_proximity_sr_mean_10d_base_v017_signal, f04sr_f04_support_resistance_proximity_sr_std_10d_base_v018_signal, f04sr_f04_support_resistance_proximity_sr_zscore_10d_base_v019_signal, f04sr_f04_support_resistance_proximity_sr_delta_10d_base_v020_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_10d_base_v022_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_10d_base_v023_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_10d_base_v024_signal, f04sr_f04_support_resistance_proximity_sr_energy_10d_base_v025_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_10d_base_v026_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_10d_base_v027_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_10d_base_v028_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_10d_base_v029_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_10d_base_v030_signal, f04sr_f04_support_resistance_proximity_sr_level_15d_base_v031_signal, f04sr_f04_support_resistance_proximity_sr_mean_15d_base_v032_signal, f04sr_f04_support_resistance_proximity_sr_std_15d_base_v033_signal, f04sr_f04_support_resistance_proximity_sr_zscore_15d_base_v034_signal, f04sr_f04_support_resistance_proximity_sr_delta_15d_base_v035_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_15d_base_v037_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_15d_base_v038_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_15d_base_v039_signal, f04sr_f04_support_resistance_proximity_sr_energy_15d_base_v040_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_15d_base_v041_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_15d_base_v042_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_15d_base_v043_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_15d_base_v044_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_15d_base_v045_signal, f04sr_f04_support_resistance_proximity_sr_level_21d_base_v046_signal, f04sr_f04_support_resistance_proximity_sr_mean_21d_base_v047_signal, f04sr_f04_support_resistance_proximity_sr_std_21d_base_v048_signal, f04sr_f04_support_resistance_proximity_sr_zscore_21d_base_v049_signal, f04sr_f04_support_resistance_proximity_sr_delta_21d_base_v050_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_21d_base_v052_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_21d_base_v053_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_21d_base_v054_signal, f04sr_f04_support_resistance_proximity_sr_energy_21d_base_v055_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_21d_base_v056_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_21d_base_v057_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_21d_base_v058_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_21d_base_v059_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_21d_base_v060_signal, f04sr_f04_support_resistance_proximity_sr_level_42d_base_v061_signal, f04sr_f04_support_resistance_proximity_sr_mean_42d_base_v062_signal, f04sr_f04_support_resistance_proximity_sr_std_42d_base_v063_signal, f04sr_f04_support_resistance_proximity_sr_zscore_42d_base_v064_signal, f04sr_f04_support_resistance_proximity_sr_delta_42d_base_v065_signal, f04sr_f04_support_resistance_proximity_sr_upper_gap_42d_base_v067_signal, f04sr_f04_support_resistance_proximity_sr_lower_gap_42d_base_v068_signal, f04sr_f04_support_resistance_proximity_sr_short_mean_gap_42d_base_v069_signal, f04sr_f04_support_resistance_proximity_sr_energy_42d_base_v070_signal, f04sr_f04_support_resistance_proximity_sr_ewm_gap_42d_base_v071_signal, f04sr_f04_support_resistance_proximity_sr_tail_relief_42d_base_v072_signal, f04sr_f04_support_resistance_proximity_sr_peak_fade_42d_base_v073_signal, f04sr_f04_support_resistance_proximity_sr_mean_abs_42d_base_v074_signal, f04sr_f04_support_resistance_proximity_sr_vol_adj_delta_42d_base_v075_signal]}
F04_SUPPORT_RESISTANCE_PROXIMITY_REGISTRY_001_075 = REGISTRY

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
