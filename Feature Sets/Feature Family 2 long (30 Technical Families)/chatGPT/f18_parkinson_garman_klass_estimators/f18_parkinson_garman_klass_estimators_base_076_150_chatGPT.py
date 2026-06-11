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

# 63d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_63d_base_v076_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_63d_base_v077_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_63d_base_v078_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_63d_base_v079_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = _z(sig, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_63d_base_v080_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_63d_base_v082_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_63d_base_v083_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_63d_base_v084_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_63d_base_v085_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_63d_base_v086_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_63d_base_v087_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_63d_base_v088_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_63d_base_v089_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_63d_base_v090_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_84d_base_v091_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_84d_base_v092_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_84d_base_v093_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_84d_base_v094_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = _z(sig, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_84d_base_v095_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_84d_base_v097_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_84d_base_v098_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_84d_base_v099_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_84d_base_v100_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_84d_base_v101_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_84d_base_v102_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_84d_base_v103_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_84d_base_v104_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_84d_base_v105_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_126d_base_v106_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_126d_base_v107_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_126d_base_v108_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_126d_base_v109_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = _z(sig, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_126d_base_v110_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_126d_base_v112_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_126d_base_v113_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_126d_base_v114_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_126d_base_v115_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_126d_base_v116_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_126d_base_v117_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_126d_base_v118_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_126d_base_v119_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_126d_base_v120_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_252d_base_v121_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_252d_base_v122_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_252d_base_v123_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_252d_base_v124_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = _z(sig, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_252d_base_v125_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_252d_base_v127_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_252d_base_v128_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_252d_base_v129_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_252d_base_v130_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_252d_base_v131_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_252d_base_v132_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_252d_base_v133_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_252d_base_v134_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_252d_base_v135_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_level_504d_base_v136_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_504d_base_v137_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d var pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_std_504d_base_v138_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d zscore pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_504d_base_v139_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = _z(sig, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d change pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_504d_base_v140_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q75gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_504d_base_v142_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q25gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_504d_base_v143_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smean gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_504d_base_v144_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d energy pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_504d_base_v145_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ewm gap pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_504d_base_v146_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d tail relief pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_504d_base_v147_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d peak fade pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_504d_base_v148_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d absmean pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_504d_base_v149_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d voladj chg pgk
def f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_504d_base_v150_signal(open, high, low, close):
    sig = _parkinson_gk_estimator(open, high, low, close, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['open', 'high', 'low', 'close'], "func": fn} for fn in [f18pg_f18_parkinson_garman_klass_estimators_pgk_level_63d_base_v076_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_63d_base_v077_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_63d_base_v078_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_63d_base_v079_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_63d_base_v080_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_63d_base_v082_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_63d_base_v083_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_63d_base_v084_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_63d_base_v085_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_63d_base_v086_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_63d_base_v087_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_63d_base_v088_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_63d_base_v089_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_63d_base_v090_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_84d_base_v091_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_84d_base_v092_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_84d_base_v093_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_84d_base_v094_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_84d_base_v095_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_84d_base_v097_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_84d_base_v098_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_84d_base_v099_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_84d_base_v100_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_84d_base_v101_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_84d_base_v102_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_84d_base_v103_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_84d_base_v104_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_84d_base_v105_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_126d_base_v106_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_126d_base_v107_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_126d_base_v108_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_126d_base_v109_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_126d_base_v110_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_126d_base_v112_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_126d_base_v113_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_126d_base_v114_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_126d_base_v115_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_126d_base_v116_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_126d_base_v117_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_126d_base_v118_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_126d_base_v119_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_126d_base_v120_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_252d_base_v121_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_252d_base_v122_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_252d_base_v123_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_252d_base_v124_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_252d_base_v125_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_252d_base_v127_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_252d_base_v128_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_252d_base_v129_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_252d_base_v130_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_252d_base_v131_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_252d_base_v132_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_252d_base_v133_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_252d_base_v134_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_252d_base_v135_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_level_504d_base_v136_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_504d_base_v137_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_std_504d_base_v138_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_zscore_504d_base_v139_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_delta_504d_base_v140_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_upper_gap_504d_base_v142_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_lower_gap_504d_base_v143_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_short_mean_gap_504d_base_v144_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_energy_504d_base_v145_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_ewm_gap_504d_base_v146_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_tail_relief_504d_base_v147_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_peak_fade_504d_base_v148_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_mean_abs_504d_base_v149_signal, f18pg_f18_parkinson_garman_klass_estimators_pgk_vol_adj_delta_504d_base_v150_signal]}
F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_REGISTRY_076_150 = REGISTRY

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
