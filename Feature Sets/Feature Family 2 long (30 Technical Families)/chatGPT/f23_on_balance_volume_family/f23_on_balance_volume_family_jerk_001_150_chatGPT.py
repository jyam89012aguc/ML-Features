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

# jk5 5d level obv
def f23ob_f23_on_balance_volume_family_obv_level_5d_jerk_v001_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_5d_jerk_v002_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d var obv
def f23ob_f23_on_balance_volume_family_obv_std_5d_jerk_v003_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_5d_jerk_v004_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = _z(sig, 5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_5d_jerk_v005_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_5d_jerk_v007_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_5d_jerk_v008_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_5d_jerk_v009_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_5d_jerk_v010_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_5d_jerk_v011_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_5d_jerk_v012_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_5d_jerk_v013_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_5d_jerk_v014_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_5d_jerk_v015_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d level obv
def f23ob_f23_on_balance_volume_family_obv_level_10d_jerk_v016_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_10d_jerk_v017_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d var obv
def f23ob_f23_on_balance_volume_family_obv_std_10d_jerk_v018_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_10d_jerk_v019_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = _z(sig, 10)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_10d_jerk_v020_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_10d_jerk_v021_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_10d_jerk_v022_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_10d_jerk_v023_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_10d_jerk_v024_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_10d_jerk_v025_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_10d_jerk_v026_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_10d_jerk_v027_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_10d_jerk_v028_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_10d_jerk_v029_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_10d_jerk_v030_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d level obv
def f23ob_f23_on_balance_volume_family_obv_level_15d_jerk_v031_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_15d_jerk_v032_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d var obv
def f23ob_f23_on_balance_volume_family_obv_std_15d_jerk_v033_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_15d_jerk_v034_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = _z(sig, 15)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_15d_jerk_v035_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_15d_jerk_v036_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_15d_jerk_v037_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_15d_jerk_v038_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_15d_jerk_v039_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_15d_jerk_v040_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_15d_jerk_v041_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_15d_jerk_v042_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_15d_jerk_v043_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_15d_jerk_v044_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_15d_jerk_v045_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d level obv
def f23ob_f23_on_balance_volume_family_obv_level_21d_jerk_v046_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_21d_jerk_v047_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d var obv
def f23ob_f23_on_balance_volume_family_obv_std_21d_jerk_v048_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_21d_jerk_v049_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = _z(sig, 21)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_21d_jerk_v050_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_21d_jerk_v051_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_21d_jerk_v052_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_21d_jerk_v053_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_21d_jerk_v054_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_21d_jerk_v055_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_21d_jerk_v056_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_21d_jerk_v057_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_21d_jerk_v058_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_21d_jerk_v059_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_21d_jerk_v060_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d level obv
def f23ob_f23_on_balance_volume_family_obv_level_42d_jerk_v061_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_42d_jerk_v062_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d var obv
def f23ob_f23_on_balance_volume_family_obv_std_42d_jerk_v063_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_42d_jerk_v064_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = _z(sig, 42)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_42d_jerk_v065_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_42d_jerk_v066_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_42d_jerk_v067_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_42d_jerk_v068_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_42d_jerk_v069_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_42d_jerk_v070_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_42d_jerk_v071_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_42d_jerk_v072_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_42d_jerk_v073_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_42d_jerk_v074_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_42d_jerk_v075_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d level obv
def f23ob_f23_on_balance_volume_family_obv_level_63d_jerk_v076_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_63d_jerk_v077_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d var obv
def f23ob_f23_on_balance_volume_family_obv_std_63d_jerk_v078_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.rolling(63, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_63d_jerk_v079_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = _z(sig, 63)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_63d_jerk_v080_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_63d_jerk_v081_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_63d_jerk_v082_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_63d_jerk_v083_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_63d_jerk_v084_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_63d_jerk_v085_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_63d_jerk_v086_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_63d_jerk_v087_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_63d_jerk_v088_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_63d_jerk_v089_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_63d_jerk_v090_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d level obv
def f23ob_f23_on_balance_volume_family_obv_level_84d_jerk_v091_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_84d_jerk_v092_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d var obv
def f23ob_f23_on_balance_volume_family_obv_std_84d_jerk_v093_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.rolling(84, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_84d_jerk_v094_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = _z(sig, 84)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_84d_jerk_v095_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_84d_jerk_v096_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_84d_jerk_v097_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_84d_jerk_v098_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_84d_jerk_v099_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_84d_jerk_v100_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_84d_jerk_v101_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_84d_jerk_v102_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_84d_jerk_v103_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_84d_jerk_v104_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_84d_jerk_v105_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d level obv
def f23ob_f23_on_balance_volume_family_obv_level_126d_jerk_v106_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_126d_jerk_v107_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d var obv
def f23ob_f23_on_balance_volume_family_obv_std_126d_jerk_v108_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.rolling(126, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_126d_jerk_v109_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = _z(sig, 126)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_126d_jerk_v110_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_126d_jerk_v111_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_126d_jerk_v112_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_126d_jerk_v113_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_126d_jerk_v114_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_126d_jerk_v115_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_126d_jerk_v116_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_126d_jerk_v117_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_126d_jerk_v118_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_126d_jerk_v119_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_126d_jerk_v120_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d level obv
def f23ob_f23_on_balance_volume_family_obv_level_252d_jerk_v121_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_252d_jerk_v122_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d var obv
def f23ob_f23_on_balance_volume_family_obv_std_252d_jerk_v123_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.rolling(252, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_252d_jerk_v124_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = _z(sig, 252)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_252d_jerk_v125_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_252d_jerk_v126_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_252d_jerk_v127_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_252d_jerk_v128_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_252d_jerk_v129_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_252d_jerk_v130_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_252d_jerk_v131_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_252d_jerk_v132_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_252d_jerk_v133_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_252d_jerk_v134_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_252d_jerk_v135_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d level obv
def f23ob_f23_on_balance_volume_family_obv_level_504d_jerk_v136_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d mean obv
def f23ob_f23_on_balance_volume_family_obv_mean_504d_jerk_v137_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d var obv
def f23ob_f23_on_balance_volume_family_obv_std_504d_jerk_v138_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.rolling(504, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d zscore obv
def f23ob_f23_on_balance_volume_family_obv_zscore_504d_jerk_v139_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = _z(sig, 504)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d change obv
def f23ob_f23_on_balance_volume_family_obv_delta_504d_jerk_v140_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d relchg obv
def f23ob_f23_on_balance_volume_family_obv_pctdelta_504d_jerk_v141_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q75gap obv
def f23ob_f23_on_balance_volume_family_obv_upper_gap_504d_jerk_v142_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q25gap obv
def f23ob_f23_on_balance_volume_family_obv_lower_gap_504d_jerk_v143_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d smean gap obv
def f23ob_f23_on_balance_volume_family_obv_short_mean_gap_504d_jerk_v144_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d energy obv
def f23ob_f23_on_balance_volume_family_obv_energy_504d_jerk_v145_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d ewm gap obv
def f23ob_f23_on_balance_volume_family_obv_ewm_gap_504d_jerk_v146_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d tail relief obv
def f23ob_f23_on_balance_volume_family_obv_tail_relief_504d_jerk_v147_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d peak fade obv
def f23ob_f23_on_balance_volume_family_obv_peak_fade_504d_jerk_v148_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d absmean obv
def f23ob_f23_on_balance_volume_family_obv_mean_abs_504d_jerk_v149_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d voladj chg obv
def f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_504d_jerk_v150_signal(closeadj, volume):
    sig = _on_balance_volume_line(closeadj, volume, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['closeadj', 'volume'], "func": fn} for fn in [f23ob_f23_on_balance_volume_family_obv_level_5d_jerk_v001_signal, f23ob_f23_on_balance_volume_family_obv_mean_5d_jerk_v002_signal, f23ob_f23_on_balance_volume_family_obv_std_5d_jerk_v003_signal, f23ob_f23_on_balance_volume_family_obv_zscore_5d_jerk_v004_signal, f23ob_f23_on_balance_volume_family_obv_delta_5d_jerk_v005_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_5d_jerk_v007_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_5d_jerk_v008_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_5d_jerk_v009_signal, f23ob_f23_on_balance_volume_family_obv_energy_5d_jerk_v010_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_5d_jerk_v011_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_5d_jerk_v012_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_5d_jerk_v013_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_5d_jerk_v014_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_5d_jerk_v015_signal, f23ob_f23_on_balance_volume_family_obv_level_10d_jerk_v016_signal, f23ob_f23_on_balance_volume_family_obv_mean_10d_jerk_v017_signal, f23ob_f23_on_balance_volume_family_obv_std_10d_jerk_v018_signal, f23ob_f23_on_balance_volume_family_obv_zscore_10d_jerk_v019_signal, f23ob_f23_on_balance_volume_family_obv_delta_10d_jerk_v020_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_10d_jerk_v021_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_10d_jerk_v022_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_10d_jerk_v023_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_10d_jerk_v024_signal, f23ob_f23_on_balance_volume_family_obv_energy_10d_jerk_v025_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_10d_jerk_v026_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_10d_jerk_v027_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_10d_jerk_v028_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_10d_jerk_v029_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_10d_jerk_v030_signal, f23ob_f23_on_balance_volume_family_obv_level_15d_jerk_v031_signal, f23ob_f23_on_balance_volume_family_obv_mean_15d_jerk_v032_signal, f23ob_f23_on_balance_volume_family_obv_std_15d_jerk_v033_signal, f23ob_f23_on_balance_volume_family_obv_zscore_15d_jerk_v034_signal, f23ob_f23_on_balance_volume_family_obv_delta_15d_jerk_v035_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_15d_jerk_v036_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_15d_jerk_v037_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_15d_jerk_v038_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_15d_jerk_v039_signal, f23ob_f23_on_balance_volume_family_obv_energy_15d_jerk_v040_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_15d_jerk_v041_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_15d_jerk_v042_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_15d_jerk_v043_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_15d_jerk_v044_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_15d_jerk_v045_signal, f23ob_f23_on_balance_volume_family_obv_level_21d_jerk_v046_signal, f23ob_f23_on_balance_volume_family_obv_mean_21d_jerk_v047_signal, f23ob_f23_on_balance_volume_family_obv_std_21d_jerk_v048_signal, f23ob_f23_on_balance_volume_family_obv_zscore_21d_jerk_v049_signal, f23ob_f23_on_balance_volume_family_obv_delta_21d_jerk_v050_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_21d_jerk_v051_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_21d_jerk_v052_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_21d_jerk_v053_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_21d_jerk_v054_signal, f23ob_f23_on_balance_volume_family_obv_energy_21d_jerk_v055_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_21d_jerk_v056_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_21d_jerk_v057_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_21d_jerk_v058_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_21d_jerk_v059_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_21d_jerk_v060_signal, f23ob_f23_on_balance_volume_family_obv_level_42d_jerk_v061_signal, f23ob_f23_on_balance_volume_family_obv_mean_42d_jerk_v062_signal, f23ob_f23_on_balance_volume_family_obv_std_42d_jerk_v063_signal, f23ob_f23_on_balance_volume_family_obv_zscore_42d_jerk_v064_signal, f23ob_f23_on_balance_volume_family_obv_delta_42d_jerk_v065_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_42d_jerk_v066_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_42d_jerk_v067_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_42d_jerk_v068_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_42d_jerk_v069_signal, f23ob_f23_on_balance_volume_family_obv_energy_42d_jerk_v070_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_42d_jerk_v071_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_42d_jerk_v072_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_42d_jerk_v073_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_42d_jerk_v074_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_42d_jerk_v075_signal, f23ob_f23_on_balance_volume_family_obv_level_63d_jerk_v076_signal, f23ob_f23_on_balance_volume_family_obv_mean_63d_jerk_v077_signal, f23ob_f23_on_balance_volume_family_obv_std_63d_jerk_v078_signal, f23ob_f23_on_balance_volume_family_obv_zscore_63d_jerk_v079_signal, f23ob_f23_on_balance_volume_family_obv_delta_63d_jerk_v080_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_63d_jerk_v081_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_63d_jerk_v082_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_63d_jerk_v083_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_63d_jerk_v084_signal, f23ob_f23_on_balance_volume_family_obv_energy_63d_jerk_v085_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_63d_jerk_v086_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_63d_jerk_v087_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_63d_jerk_v088_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_63d_jerk_v089_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_63d_jerk_v090_signal, f23ob_f23_on_balance_volume_family_obv_level_84d_jerk_v091_signal, f23ob_f23_on_balance_volume_family_obv_mean_84d_jerk_v092_signal, f23ob_f23_on_balance_volume_family_obv_std_84d_jerk_v093_signal, f23ob_f23_on_balance_volume_family_obv_zscore_84d_jerk_v094_signal, f23ob_f23_on_balance_volume_family_obv_delta_84d_jerk_v095_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_84d_jerk_v096_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_84d_jerk_v097_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_84d_jerk_v098_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_84d_jerk_v099_signal, f23ob_f23_on_balance_volume_family_obv_energy_84d_jerk_v100_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_84d_jerk_v101_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_84d_jerk_v102_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_84d_jerk_v103_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_84d_jerk_v104_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_84d_jerk_v105_signal, f23ob_f23_on_balance_volume_family_obv_level_126d_jerk_v106_signal, f23ob_f23_on_balance_volume_family_obv_mean_126d_jerk_v107_signal, f23ob_f23_on_balance_volume_family_obv_std_126d_jerk_v108_signal, f23ob_f23_on_balance_volume_family_obv_zscore_126d_jerk_v109_signal, f23ob_f23_on_balance_volume_family_obv_delta_126d_jerk_v110_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_126d_jerk_v111_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_126d_jerk_v112_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_126d_jerk_v113_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_126d_jerk_v114_signal, f23ob_f23_on_balance_volume_family_obv_energy_126d_jerk_v115_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_126d_jerk_v116_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_126d_jerk_v117_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_126d_jerk_v118_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_126d_jerk_v119_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_126d_jerk_v120_signal, f23ob_f23_on_balance_volume_family_obv_level_252d_jerk_v121_signal, f23ob_f23_on_balance_volume_family_obv_mean_252d_jerk_v122_signal, f23ob_f23_on_balance_volume_family_obv_std_252d_jerk_v123_signal, f23ob_f23_on_balance_volume_family_obv_zscore_252d_jerk_v124_signal, f23ob_f23_on_balance_volume_family_obv_delta_252d_jerk_v125_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_252d_jerk_v126_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_252d_jerk_v127_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_252d_jerk_v128_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_252d_jerk_v129_signal, f23ob_f23_on_balance_volume_family_obv_energy_252d_jerk_v130_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_252d_jerk_v131_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_252d_jerk_v132_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_252d_jerk_v133_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_252d_jerk_v134_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_252d_jerk_v135_signal, f23ob_f23_on_balance_volume_family_obv_level_504d_jerk_v136_signal, f23ob_f23_on_balance_volume_family_obv_mean_504d_jerk_v137_signal, f23ob_f23_on_balance_volume_family_obv_std_504d_jerk_v138_signal, f23ob_f23_on_balance_volume_family_obv_zscore_504d_jerk_v139_signal, f23ob_f23_on_balance_volume_family_obv_delta_504d_jerk_v140_signal, f23ob_f23_on_balance_volume_family_obv_pctdelta_504d_jerk_v141_signal, f23ob_f23_on_balance_volume_family_obv_upper_gap_504d_jerk_v142_signal, f23ob_f23_on_balance_volume_family_obv_lower_gap_504d_jerk_v143_signal, f23ob_f23_on_balance_volume_family_obv_short_mean_gap_504d_jerk_v144_signal, f23ob_f23_on_balance_volume_family_obv_energy_504d_jerk_v145_signal, f23ob_f23_on_balance_volume_family_obv_ewm_gap_504d_jerk_v146_signal, f23ob_f23_on_balance_volume_family_obv_tail_relief_504d_jerk_v147_signal, f23ob_f23_on_balance_volume_family_obv_peak_fade_504d_jerk_v148_signal, f23ob_f23_on_balance_volume_family_obv_mean_abs_504d_jerk_v149_signal, f23ob_f23_on_balance_volume_family_obv_vol_adj_delta_504d_jerk_v150_signal]}
F23_ON_BALANCE_VOLUME_FAMILY_REGISTRY_JERK = REGISTRY

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
