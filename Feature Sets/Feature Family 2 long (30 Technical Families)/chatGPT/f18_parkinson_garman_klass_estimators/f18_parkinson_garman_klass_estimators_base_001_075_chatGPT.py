import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _parkinson_gk_estimator(open, high, low, close, w):
    hl = np.log(high / low.replace(0, np.nan)) ** 2
    oc = np.log(close / open.replace(0, np.nan)) ** 2
    est = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * oc
    return est.rolling(w, min_periods=2).mean() + est.diff(max(1, w//5))

# 5d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_5d_base_v001_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_5d_base_v002_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_5d_base_v003_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_5d_base_v004_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = _z(sig, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_5d_base_v005_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_5d_base_v007_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_5d_base_v008_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_5d_base_v009_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_5d_base_v010_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_5d_base_v011_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_5d_base_v012_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_5d_base_v013_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 5d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_5d_base_v014_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 5d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_5d_base_v015_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_10d_base_v016_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_10d_base_v017_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_10d_base_v018_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_10d_base_v019_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = _z(sig, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_10d_base_v020_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_10d_base_v022_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_10d_base_v023_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_10d_base_v024_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_10d_base_v025_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_10d_base_v026_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_10d_base_v027_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_10d_base_v028_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 10d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_10d_base_v029_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 10d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_10d_base_v030_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_15d_base_v031_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_15d_base_v032_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_15d_base_v033_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_15d_base_v034_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = _z(sig, 15)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_15d_base_v035_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_15d_base_v037_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_15d_base_v038_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 15d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_15d_base_v039_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_15d_base_v040_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_15d_base_v041_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_15d_base_v042_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_15d_base_v043_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 15d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_15d_base_v044_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 15d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_15d_base_v045_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_21d_base_v046_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_21d_base_v047_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_21d_base_v048_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_21d_base_v049_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = _z(sig, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_21d_base_v050_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_21d_base_v052_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_21d_base_v053_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_21d_base_v054_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_21d_base_v055_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_21d_base_v056_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_21d_base_v057_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_21d_base_v058_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 21d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_21d_base_v059_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 21d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_21d_base_v060_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_42d_base_v061_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_42d_base_v062_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_42d_base_v063_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_42d_base_v064_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = _z(sig, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_42d_base_v065_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_42d_base_v067_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_42d_base_v068_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_42d_base_v069_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_42d_base_v070_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_42d_base_v071_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_42d_base_v072_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_42d_base_v073_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 42d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_42d_base_v074_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 42d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_42d_base_v075_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['open', 'high', 'low', 'close'], "func": fn} for fn in [f18pg_f18_parkinson_garman_klass_estimators_pgk_level_5d_base_v001_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_5d_base_v002_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_5d_base_v003_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_5d_base_v004_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_5d_base_v005_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_5d_base_v007_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_5d_base_v008_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_5d_base_v009_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_5d_base_v010_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_5d_base_v011_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_5d_base_v012_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_5d_base_v013_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_5d_base_v014_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_5d_base_v015_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_10d_base_v016_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_10d_base_v017_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_10d_base_v018_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_10d_base_v019_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_10d_base_v020_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_10d_base_v022_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_10d_base_v023_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_10d_base_v024_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_10d_base_v025_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_10d_base_v026_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_10d_base_v027_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_10d_base_v028_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_10d_base_v029_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_10d_base_v030_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_15d_base_v031_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_15d_base_v032_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_15d_base_v033_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_15d_base_v034_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_15d_base_v035_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_15d_base_v037_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_15d_base_v038_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_15d_base_v039_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_15d_base_v040_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_15d_base_v041_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_15d_base_v042_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_15d_base_v043_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_15d_base_v044_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_15d_base_v045_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_21d_base_v046_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_21d_base_v047_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_21d_base_v048_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_21d_base_v049_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_21d_base_v050_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_21d_base_v052_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_21d_base_v053_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_21d_base_v054_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_21d_base_v055_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_21d_base_v056_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_21d_base_v057_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_21d_base_v058_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_21d_base_v059_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_21d_base_v060_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_42d_base_v061_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_42d_base_v062_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_42d_base_v063_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_42d_base_v064_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_42d_base_v065_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_42d_base_v067_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_42d_base_v068_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_42d_base_v069_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_42d_base_v070_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_42d_base_v071_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_42d_base_v072_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_42d_base_v073_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_42d_base_v074_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_42d_base_v075_signal]}
F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    open = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    close = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    high = pd.concat([open, close], axis=1).max(axis=1) * (1.0 + pd.Series(np.random.uniform(0.003, 0.05, n)))
    low = pd.concat([open, close], axis=1).min(axis=1) * (1.0 - pd.Series(np.random.uniform(0.003, 0.05, n)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(open, high, low, close)
        y2 = func(open, high, low, close)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_parkinson_gk_estimator" in src
    assert ok_nan >= int(0.80 * len(funcs))
