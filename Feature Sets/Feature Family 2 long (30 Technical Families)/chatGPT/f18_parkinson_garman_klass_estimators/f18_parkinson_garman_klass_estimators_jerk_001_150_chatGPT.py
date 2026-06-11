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

# jk5 5d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_5d_jerk_v001_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_5d_jerk_v002_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_5d_jerk_v003_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_5d_jerk_v004_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = _z(sig, 5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_5d_jerk_v005_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_5d_jerk_v006_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_5d_jerk_v007_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_5d_jerk_v008_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_5d_jerk_v009_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(2, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_5d_jerk_v010_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = (sig * sig).rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_5d_jerk_v011_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.ewm(span=2, adjust=False, min_periods=2).mean() - sig.rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_5d_jerk_v012_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig - sig.rolling(5, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_5d_jerk_v013_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.rolling(5, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_5d_jerk_v014_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.abs().rolling(5, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 5d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_5d_jerk_v015_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 5)
    result = sig.diff(5) / sig.rolling(5, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_10d_jerk_v016_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_10d_jerk_v017_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_10d_jerk_v018_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_10d_jerk_v019_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = _z(sig, 10)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_10d_jerk_v020_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_10d_jerk_v021_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_10d_jerk_v022_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_10d_jerk_v023_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_10d_jerk_v024_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(3, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_10d_jerk_v025_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = (sig * sig).rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_10d_jerk_v026_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.ewm(span=3, adjust=False, min_periods=2).mean() - sig.rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_10d_jerk_v027_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig - sig.rolling(10, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_10d_jerk_v028_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.rolling(10, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_10d_jerk_v029_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.abs().rolling(10, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 10d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_10d_jerk_v030_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 10)
    result = sig.diff(5) / sig.rolling(10, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_15d_jerk_v031_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_15d_jerk_v032_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_15d_jerk_v033_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_15d_jerk_v034_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = _z(sig, 15)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_15d_jerk_v035_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_15d_jerk_v036_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_15d_jerk_v037_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_15d_jerk_v038_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_15d_jerk_v039_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(5, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_15d_jerk_v040_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = (sig * sig).rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_15d_jerk_v041_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.ewm(span=5, adjust=False, min_periods=2).mean() - sig.rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_15d_jerk_v042_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig - sig.rolling(15, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_15d_jerk_v043_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.rolling(15, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_15d_jerk_v044_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.abs().rolling(15, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 15d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_15d_jerk_v045_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 15)
    result = sig.diff(5) / sig.rolling(15, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_21d_jerk_v046_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_21d_jerk_v047_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_21d_jerk_v048_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).std()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_21d_jerk_v049_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = _z(sig, 21)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_21d_jerk_v050_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.diff(5)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_21d_jerk_v051_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.diff(5) / sig.abs().shift(5).replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_21d_jerk_v052_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.75)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_21d_jerk_v053_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).quantile(0.25)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_21d_jerk_v054_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(7, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_21d_jerk_v055_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = (sig * sig).rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_21d_jerk_v056_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.ewm(span=7, adjust=False, min_periods=2).mean() - sig.rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_21d_jerk_v057_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig - sig.rolling(21, min_periods=2).min()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_21d_jerk_v058_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.rolling(21, min_periods=2).max() - sig
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_21d_jerk_v059_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.abs().rolling(21, min_periods=2).mean()
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk5 21d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_21d_jerk_v060_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 21)
    result = sig.diff(5) / sig.rolling(21, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(5) / result.abs().shift(5).replace(0, np.nan)
    result = slope.diff(5)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_42d_jerk_v061_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_42d_jerk_v062_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_42d_jerk_v063_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_42d_jerk_v064_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = _z(sig, 42)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_42d_jerk_v065_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_42d_jerk_v066_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_42d_jerk_v067_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_42d_jerk_v068_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_42d_jerk_v069_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(14, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_42d_jerk_v070_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = (sig * sig).rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_42d_jerk_v071_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.ewm(span=14, adjust=False, min_periods=2).mean() - sig.rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_42d_jerk_v072_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig - sig.rolling(42, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_42d_jerk_v073_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.rolling(42, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_42d_jerk_v074_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.abs().rolling(42, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 42d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_42d_jerk_v075_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 42)
    result = sig.diff(21) / sig.rolling(42, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_63d_jerk_v076_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_63d_jerk_v077_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_63d_jerk_v078_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_63d_jerk_v079_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = _z(sig, 63)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_63d_jerk_v080_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_63d_jerk_v081_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_63d_jerk_v082_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_63d_jerk_v083_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_63d_jerk_v084_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_63d_jerk_v085_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_63d_jerk_v086_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_63d_jerk_v087_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_63d_jerk_v088_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_63d_jerk_v089_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 63d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_63d_jerk_v090_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_84d_jerk_v091_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_84d_jerk_v092_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_84d_jerk_v093_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_84d_jerk_v094_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = _z(sig, 84)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_84d_jerk_v095_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_84d_jerk_v096_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_84d_jerk_v097_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_84d_jerk_v098_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_84d_jerk_v099_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_84d_jerk_v100_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_84d_jerk_v101_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_84d_jerk_v102_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_84d_jerk_v103_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_84d_jerk_v104_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 84d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_84d_jerk_v105_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_126d_jerk_v106_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_126d_jerk_v107_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_126d_jerk_v108_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_126d_jerk_v109_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = _z(sig, 126)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_126d_jerk_v110_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_126d_jerk_v111_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_126d_jerk_v112_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_126d_jerk_v113_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_126d_jerk_v114_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_126d_jerk_v115_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_126d_jerk_v116_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_126d_jerk_v117_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_126d_jerk_v118_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_126d_jerk_v119_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 126d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_126d_jerk_v120_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_252d_jerk_v121_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_252d_jerk_v122_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_252d_jerk_v123_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_252d_jerk_v124_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = _z(sig, 252)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_252d_jerk_v125_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_252d_jerk_v126_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_252d_jerk_v127_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_252d_jerk_v128_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_252d_jerk_v129_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_252d_jerk_v130_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_252d_jerk_v131_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_252d_jerk_v132_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_252d_jerk_v133_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_252d_jerk_v134_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 252d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_252d_jerk_v135_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_504d_jerk_v136_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_504d_jerk_v137_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_504d_jerk_v138_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).std()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_504d_jerk_v139_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = _z(sig, 504)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_504d_jerk_v140_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.diff(21)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d relchg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_504d_jerk_v141_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.diff(21) / sig.abs().shift(21).replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_504d_jerk_v142_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_504d_jerk_v143_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_504d_jerk_v144_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_504d_jerk_v145_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_504d_jerk_v146_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_504d_jerk_v147_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_504d_jerk_v148_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_504d_jerk_v149_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# jk21 504d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_504d_jerk_v150_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    slope = result.diff(21) / result.abs().shift(21).replace(0, np.nan)
    result = slope.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


REGISTRY = {fn.__name__: {"inputs": ['open', 'high', 'low', 'close'], "func": fn} for fn in [f18pg_f18_parkinson_garman_klass_estimators_pgk_level_5d_jerk_v001_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_5d_jerk_v002_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_5d_jerk_v003_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_5d_jerk_v004_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_5d_jerk_v005_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_5d_jerk_v006_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_5d_jerk_v007_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_5d_jerk_v008_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_5d_jerk_v009_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_5d_jerk_v010_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_5d_jerk_v011_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_5d_jerk_v012_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_5d_jerk_v013_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_5d_jerk_v014_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_5d_jerk_v015_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_10d_jerk_v016_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_10d_jerk_v017_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_10d_jerk_v018_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_10d_jerk_v019_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_10d_jerk_v020_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_10d_jerk_v021_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_10d_jerk_v022_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_10d_jerk_v023_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_10d_jerk_v024_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_10d_jerk_v025_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_10d_jerk_v026_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_10d_jerk_v027_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_10d_jerk_v028_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_10d_jerk_v029_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_10d_jerk_v030_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_15d_jerk_v031_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_15d_jerk_v032_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_15d_jerk_v033_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_15d_jerk_v034_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_15d_jerk_v035_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_15d_jerk_v036_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_15d_jerk_v037_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_15d_jerk_v038_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_15d_jerk_v039_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_15d_jerk_v040_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_15d_jerk_v041_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_15d_jerk_v042_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_15d_jerk_v043_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_15d_jerk_v044_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_15d_jerk_v045_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_21d_jerk_v046_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_21d_jerk_v047_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_21d_jerk_v048_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_21d_jerk_v049_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_21d_jerk_v050_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_21d_jerk_v051_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_21d_jerk_v052_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_21d_jerk_v053_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_21d_jerk_v054_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_21d_jerk_v055_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_21d_jerk_v056_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_21d_jerk_v057_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_21d_jerk_v058_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_21d_jerk_v059_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_21d_jerk_v060_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_42d_jerk_v061_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_42d_jerk_v062_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_42d_jerk_v063_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_42d_jerk_v064_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_42d_jerk_v065_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_42d_jerk_v066_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_42d_jerk_v067_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_42d_jerk_v068_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_42d_jerk_v069_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_42d_jerk_v070_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_42d_jerk_v071_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_42d_jerk_v072_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_42d_jerk_v073_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_42d_jerk_v074_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_42d_jerk_v075_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_63d_jerk_v076_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_63d_jerk_v077_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_63d_jerk_v078_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_63d_jerk_v079_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_63d_jerk_v080_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_63d_jerk_v081_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_63d_jerk_v082_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_63d_jerk_v083_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_63d_jerk_v084_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_63d_jerk_v085_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_63d_jerk_v086_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_63d_jerk_v087_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_63d_jerk_v088_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_63d_jerk_v089_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_63d_jerk_v090_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_84d_jerk_v091_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_84d_jerk_v092_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_84d_jerk_v093_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_84d_jerk_v094_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_84d_jerk_v095_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_84d_jerk_v096_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_84d_jerk_v097_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_84d_jerk_v098_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_84d_jerk_v099_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_84d_jerk_v100_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_84d_jerk_v101_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_84d_jerk_v102_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_84d_jerk_v103_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_84d_jerk_v104_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_84d_jerk_v105_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_126d_jerk_v106_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_126d_jerk_v107_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_126d_jerk_v108_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_126d_jerk_v109_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_126d_jerk_v110_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_126d_jerk_v111_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_126d_jerk_v112_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_126d_jerk_v113_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_126d_jerk_v114_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_126d_jerk_v115_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_126d_jerk_v116_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_126d_jerk_v117_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_126d_jerk_v118_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_126d_jerk_v119_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_126d_jerk_v120_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_252d_jerk_v121_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_252d_jerk_v122_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_252d_jerk_v123_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_252d_jerk_v124_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_252d_jerk_v125_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_252d_jerk_v126_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_252d_jerk_v127_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_252d_jerk_v128_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_252d_jerk_v129_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_252d_jerk_v130_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_252d_jerk_v131_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_252d_jerk_v132_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_252d_jerk_v133_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_252d_jerk_v134_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_252d_jerk_v135_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_504d_jerk_v136_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_504d_jerk_v137_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_504d_jerk_v138_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_504d_jerk_v139_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_504d_jerk_v140_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_pctdelta_504d_jerk_v141_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_504d_jerk_v142_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_504d_jerk_v143_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_504d_jerk_v144_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_504d_jerk_v145_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_504d_jerk_v146_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_504d_jerk_v147_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_504d_jerk_v148_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_504d_jerk_v149_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_504d_jerk_v150_signal]}
F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_JERK = REGISTRY


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
