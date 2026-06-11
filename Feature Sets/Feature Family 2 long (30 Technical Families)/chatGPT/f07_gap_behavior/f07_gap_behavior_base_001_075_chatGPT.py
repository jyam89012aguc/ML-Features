import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _gap_open_prior_close(open, close, w):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    return gap.rolling(w, min_periods=2).mean()

# 5d level gap
def f07gb_f07_gap_behavior_gap_level_5d_base_v001_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean gap
def f07gb_f07_gap_behavior_gap_mean_5d_base_v002_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d var gap
def f07gb_f07_gap_behavior_gap_std_5d_base_v003_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.rolling(5, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_5d_base_v004_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = _z(sig, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d change gap
def f07gb_f07_gap_behavior_gap_delta_5d_base_v005_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_5d_base_v007_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_5d_base_v008_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_5d_base_v009_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d energy gap
def f07gb_f07_gap_behavior_gap_energy_5d_base_v010_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_5d_base_v011_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_5d_base_v012_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_5d_base_v013_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_5d_base_v014_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_5d_base_v015_signal(open, close):
    sig = _gap_open_prior_close(open, close, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d level gap
def f07gb_f07_gap_behavior_gap_level_10d_base_v016_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d mean gap
def f07gb_f07_gap_behavior_gap_mean_10d_base_v017_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d var gap
def f07gb_f07_gap_behavior_gap_std_10d_base_v018_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.rolling(10, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_10d_base_v019_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = _z(sig, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d change gap
def f07gb_f07_gap_behavior_gap_delta_10d_base_v020_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_10d_base_v022_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_10d_base_v023_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_10d_base_v024_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d energy gap
def f07gb_f07_gap_behavior_gap_energy_10d_base_v025_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_10d_base_v026_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_10d_base_v027_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_10d_base_v028_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_10d_base_v029_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_10d_base_v030_signal(open, close):
    sig = _gap_open_prior_close(open, close, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d level gap
def f07gb_f07_gap_behavior_gap_level_15d_base_v031_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d mean gap
def f07gb_f07_gap_behavior_gap_mean_15d_base_v032_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d var gap
def f07gb_f07_gap_behavior_gap_std_15d_base_v033_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.rolling(15, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_15d_base_v034_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = _z(sig, 15)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d change gap
def f07gb_f07_gap_behavior_gap_delta_15d_base_v035_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_15d_base_v037_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_15d_base_v038_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_15d_base_v039_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d energy gap
def f07gb_f07_gap_behavior_gap_energy_15d_base_v040_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_15d_base_v041_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_15d_base_v042_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_15d_base_v043_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_15d_base_v044_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_15d_base_v045_signal(open, close):
    sig = _gap_open_prior_close(open, close, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level gap
def f07gb_f07_gap_behavior_gap_level_21d_base_v046_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean gap
def f07gb_f07_gap_behavior_gap_mean_21d_base_v047_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d var gap
def f07gb_f07_gap_behavior_gap_std_21d_base_v048_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.rolling(21, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_21d_base_v049_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = _z(sig, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d change gap
def f07gb_f07_gap_behavior_gap_delta_21d_base_v050_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_21d_base_v052_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_21d_base_v053_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_21d_base_v054_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d energy gap
def f07gb_f07_gap_behavior_gap_energy_21d_base_v055_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_21d_base_v056_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_21d_base_v057_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_21d_base_v058_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_21d_base_v059_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_21d_base_v060_signal(open, close):
    sig = _gap_open_prior_close(open, close, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d level gap
def f07gb_f07_gap_behavior_gap_level_42d_base_v061_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d mean gap
def f07gb_f07_gap_behavior_gap_mean_42d_base_v062_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d var gap
def f07gb_f07_gap_behavior_gap_std_42d_base_v063_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.rolling(42, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_42d_base_v064_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = _z(sig, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d change gap
def f07gb_f07_gap_behavior_gap_delta_42d_base_v065_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_42d_base_v067_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_42d_base_v068_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_42d_base_v069_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d energy gap
def f07gb_f07_gap_behavior_gap_energy_42d_base_v070_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_42d_base_v071_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_42d_base_v072_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_42d_base_v073_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_42d_base_v074_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_42d_base_v075_signal(open, close):
    sig = _gap_open_prior_close(open, close, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['open', 'close'], "func": fn} for fn in [f07gb_f07_gap_behavior_gap_level_5d_base_v001_signal, f07gb_f07_gap_behavior_gap_mean_5d_base_v002_signal, f07gb_f07_gap_behavior_gap_std_5d_base_v003_signal, f07gb_f07_gap_behavior_gap_zscore_5d_base_v004_signal, f07gb_f07_gap_behavior_gap_delta_5d_base_v005_signal, f07gb_f07_gap_behavior_gap_upper_gap_5d_base_v007_signal, f07gb_f07_gap_behavior_gap_lower_gap_5d_base_v008_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_5d_base_v009_signal, f07gb_f07_gap_behavior_gap_energy_5d_base_v010_signal, f07gb_f07_gap_behavior_gap_ewm_gap_5d_base_v011_signal, f07gb_f07_gap_behavior_gap_tail_relief_5d_base_v012_signal, f07gb_f07_gap_behavior_gap_peak_fade_5d_base_v013_signal, f07gb_f07_gap_behavior_gap_mean_abs_5d_base_v014_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_5d_base_v015_signal, f07gb_f07_gap_behavior_gap_level_10d_base_v016_signal, f07gb_f07_gap_behavior_gap_mean_10d_base_v017_signal, f07gb_f07_gap_behavior_gap_std_10d_base_v018_signal, f07gb_f07_gap_behavior_gap_zscore_10d_base_v019_signal, f07gb_f07_gap_behavior_gap_delta_10d_base_v020_signal, f07gb_f07_gap_behavior_gap_upper_gap_10d_base_v022_signal, f07gb_f07_gap_behavior_gap_lower_gap_10d_base_v023_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_10d_base_v024_signal, f07gb_f07_gap_behavior_gap_energy_10d_base_v025_signal, f07gb_f07_gap_behavior_gap_ewm_gap_10d_base_v026_signal, f07gb_f07_gap_behavior_gap_tail_relief_10d_base_v027_signal, f07gb_f07_gap_behavior_gap_peak_fade_10d_base_v028_signal, f07gb_f07_gap_behavior_gap_mean_abs_10d_base_v029_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_10d_base_v030_signal, f07gb_f07_gap_behavior_gap_level_15d_base_v031_signal, f07gb_f07_gap_behavior_gap_mean_15d_base_v032_signal, f07gb_f07_gap_behavior_gap_std_15d_base_v033_signal, f07gb_f07_gap_behavior_gap_zscore_15d_base_v034_signal, f07gb_f07_gap_behavior_gap_delta_15d_base_v035_signal, f07gb_f07_gap_behavior_gap_upper_gap_15d_base_v037_signal, f07gb_f07_gap_behavior_gap_lower_gap_15d_base_v038_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_15d_base_v039_signal, f07gb_f07_gap_behavior_gap_energy_15d_base_v040_signal, f07gb_f07_gap_behavior_gap_ewm_gap_15d_base_v041_signal, f07gb_f07_gap_behavior_gap_tail_relief_15d_base_v042_signal, f07gb_f07_gap_behavior_gap_peak_fade_15d_base_v043_signal, f07gb_f07_gap_behavior_gap_mean_abs_15d_base_v044_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_15d_base_v045_signal, f07gb_f07_gap_behavior_gap_level_21d_base_v046_signal, f07gb_f07_gap_behavior_gap_mean_21d_base_v047_signal, f07gb_f07_gap_behavior_gap_std_21d_base_v048_signal, f07gb_f07_gap_behavior_gap_zscore_21d_base_v049_signal, f07gb_f07_gap_behavior_gap_delta_21d_base_v050_signal, f07gb_f07_gap_behavior_gap_upper_gap_21d_base_v052_signal, f07gb_f07_gap_behavior_gap_lower_gap_21d_base_v053_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_21d_base_v054_signal, f07gb_f07_gap_behavior_gap_energy_21d_base_v055_signal, f07gb_f07_gap_behavior_gap_ewm_gap_21d_base_v056_signal, f07gb_f07_gap_behavior_gap_tail_relief_21d_base_v057_signal, f07gb_f07_gap_behavior_gap_peak_fade_21d_base_v058_signal, f07gb_f07_gap_behavior_gap_mean_abs_21d_base_v059_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_21d_base_v060_signal, f07gb_f07_gap_behavior_gap_level_42d_base_v061_signal, f07gb_f07_gap_behavior_gap_mean_42d_base_v062_signal, f07gb_f07_gap_behavior_gap_std_42d_base_v063_signal, f07gb_f07_gap_behavior_gap_zscore_42d_base_v064_signal, f07gb_f07_gap_behavior_gap_delta_42d_base_v065_signal, f07gb_f07_gap_behavior_gap_upper_gap_42d_base_v067_signal, f07gb_f07_gap_behavior_gap_lower_gap_42d_base_v068_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_42d_base_v069_signal, f07gb_f07_gap_behavior_gap_energy_42d_base_v070_signal, f07gb_f07_gap_behavior_gap_ewm_gap_42d_base_v071_signal, f07gb_f07_gap_behavior_gap_tail_relief_42d_base_v072_signal, f07gb_f07_gap_behavior_gap_peak_fade_42d_base_v073_signal, f07gb_f07_gap_behavior_gap_mean_abs_42d_base_v074_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_42d_base_v075_signal]}
F07_GAP_BEHAVIOR_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    open = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    close = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(open, close)
        y2 = func(open, close)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_gap_open_prior_close" in src
    assert ok_nan >= int(0.80 * len(funcs))
