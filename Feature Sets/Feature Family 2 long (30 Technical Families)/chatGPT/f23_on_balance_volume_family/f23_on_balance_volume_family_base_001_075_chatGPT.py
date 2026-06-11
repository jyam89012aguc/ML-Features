import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _on_balance_volume_line(closeadj, volume, w):
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.diff(w) / volume.rolling(w, min_periods=2).sum().replace(0, np.nan)

# 5d level obv
def f23ob_f23_on_balance_volume_family_obv_level_5d_base_v001_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_5d_base_v002_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d var obv
def f23ob_f23_on_balance_volume_family_obv_std_5d_base_v003_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_5d_base_v004_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = _z(sig, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_5d_base_v005_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_5d_base_v007_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_5d_base_v008_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_5d_base_v009_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_5d_base_v010_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_5d_base_v011_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_5d_base_v012_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_5d_base_v013_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_5d_base_v014_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_5d_base_v015_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d level obv
def f23ob_f23_on_balance_volume_family_obv_level_10d_base_v016_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_10d_base_v017_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d var obv
def f23ob_f23_on_balance_volume_family_obv_std_10d_base_v018_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_10d_base_v019_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = _z(sig, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_10d_base_v020_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_10d_base_v022_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_10d_base_v023_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_10d_base_v024_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_10d_base_v025_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_10d_base_v026_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_10d_base_v027_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_10d_base_v028_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_10d_base_v029_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_10d_base_v030_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d level obv
def f23ob_f23_on_balance_volume_family_obv_level_15d_base_v031_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_15d_base_v032_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d var obv
def f23ob_f23_on_balance_volume_family_obv_std_15d_base_v033_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_15d_base_v034_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = _z(sig, 15)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_15d_base_v035_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_15d_base_v037_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_15d_base_v038_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_15d_base_v039_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_15d_base_v040_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_15d_base_v041_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_15d_base_v042_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_15d_base_v043_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_15d_base_v044_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_15d_base_v045_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level obv
def f23ob_f23_on_balance_volume_family_obv_level_21d_base_v046_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_21d_base_v047_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d var obv
def f23ob_f23_on_balance_volume_family_obv_std_21d_base_v048_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_21d_base_v049_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = _z(sig, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_21d_base_v050_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_21d_base_v052_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_21d_base_v053_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_21d_base_v054_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_21d_base_v055_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_21d_base_v056_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_21d_base_v057_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_21d_base_v058_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_21d_base_v059_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_21d_base_v060_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d level obv
def f23ob_f23_on_balance_volume_family_obv_level_42d_base_v061_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_42d_base_v062_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d var obv
def f23ob_f23_on_balance_volume_family_obv_std_42d_base_v063_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_42d_base_v064_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = _z(sig, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_42d_base_v065_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_42d_base_v067_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_42d_base_v068_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_42d_base_v069_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_42d_base_v070_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_42d_base_v071_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_42d_base_v072_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_42d_base_v073_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_42d_base_v074_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_42d_base_v075_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['closeadj', 'volume'], "func": fn} for fn in [f23ob_f23_on_balance_volume_family_obv_level_5d_base_v001_signal, f23ob_f23_on_balance_volume_family_obv_mean_5d_base_v002_signal, f23ob_f23_on_balance_volume_family_obv_std_5d_base_v003_signal, f23ob_f23_on_balance_volume_family_obv_zscore_5d_base_v004_signal, f23ob_f23_on_balance_volume_family_obv_delta_5d_base_v005_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_5d_base_v007_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_5d_base_v008_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_5d_base_v009_signal, f23ob_f23_on_balance_volume_family_obv_energy_5d_base_v010_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_5d_base_v011_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_5d_base_v012_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_5d_base_v013_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_5d_base_v014_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_5d_base_v015_signal, f23ob_f23_on_balance_volume_family_obv_level_10d_base_v016_signal, f23ob_f23_on_balance_volume_family_obv_mean_10d_base_v017_signal, f23ob_f23_on_balance_volume_family_obv_std_10d_base_v018_signal, f23ob_f23_on_balance_volume_family_obv_zscore_10d_base_v019_signal, f23ob_f23_on_balance_volume_family_obv_delta_10d_base_v020_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_10d_base_v022_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_10d_base_v023_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_10d_base_v024_signal, f23ob_f23_on_balance_volume_family_obv_energy_10d_base_v025_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_10d_base_v026_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_10d_base_v027_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_10d_base_v028_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_10d_base_v029_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_10d_base_v030_signal, f23ob_f23_on_balance_volume_family_obv_level_15d_base_v031_signal, f23ob_f23_on_balance_volume_family_obv_mean_15d_base_v032_signal, f23ob_f23_on_balance_volume_family_obv_std_15d_base_v033_signal, f23ob_f23_on_balance_volume_family_obv_zscore_15d_base_v034_signal, f23ob_f23_on_balance_volume_family_obv_delta_15d_base_v035_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_15d_base_v037_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_15d_base_v038_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_15d_base_v039_signal, f23ob_f23_on_balance_volume_family_obv_energy_15d_base_v040_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_15d_base_v041_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_15d_base_v042_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_15d_base_v043_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_15d_base_v044_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_15d_base_v045_signal, f23ob_f23_on_balance_volume_family_obv_level_21d_base_v046_signal, f23ob_f23_on_balance_volume_family_obv_mean_21d_base_v047_signal, f23ob_f23_on_balance_volume_family_obv_std_21d_base_v048_signal, f23ob_f23_on_balance_volume_family_obv_zscore_21d_base_v049_signal, f23ob_f23_on_balance_volume_family_obv_delta_21d_base_v050_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_21d_base_v052_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_21d_base_v053_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_21d_base_v054_signal, f23ob_f23_on_balance_volume_family_obv_energy_21d_base_v055_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_21d_base_v056_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_21d_base_v057_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_21d_base_v058_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_21d_base_v059_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_21d_base_v060_signal, f23ob_f23_on_balance_volume_family_obv_level_42d_base_v061_signal, f23ob_f23_on_balance_volume_family_obv_mean_42d_base_v062_signal, f23ob_f23_on_balance_volume_family_obv_std_42d_base_v063_signal, f23ob_f23_on_balance_volume_family_obv_zscore_42d_base_v064_signal, f23ob_f23_on_balance_volume_family_obv_delta_42d_base_v065_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_42d_base_v067_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_42d_base_v068_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_42d_base_v069_signal, f23ob_f23_on_balance_volume_family_obv_energy_42d_base_v070_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_42d_base_v071_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_42d_base_v072_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_42d_base_v073_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_42d_base_v074_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_42d_base_v075_signal]}
F23_ON_BALANCE_VOLUME_FAMILY_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    closeadj = base
    volume = pd.Series(np.random.lognormal(13.0, 0.9, n) * (1.0 + 0.25 * np.sin(t / 13.0)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(closeadj, volume)
        y2 = func(closeadj, volume)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_on_balance_volume_line" in src
    assert ok_nan >= int(0.80 * len(funcs))
