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

# 63d level gap
def f07gb_f07_gap_behavior_gap_level_63d_base_v076_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean gap
def f07gb_f07_gap_behavior_gap_mean_63d_base_v077_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d var gap
def f07gb_f07_gap_behavior_gap_std_63d_base_v078_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.rolling(63, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_63d_base_v079_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = _z(sig, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change gap
def f07gb_f07_gap_behavior_gap_delta_63d_base_v080_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_63d_base_v082_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_63d_base_v083_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_63d_base_v084_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d energy gap
def f07gb_f07_gap_behavior_gap_energy_63d_base_v085_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_63d_base_v086_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_63d_base_v087_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_63d_base_v088_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_63d_base_v089_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_63d_base_v090_signal(open, close):
    sig = _gap_open_prior_close(open, close, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d level gap
def f07gb_f07_gap_behavior_gap_level_84d_base_v091_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d mean gap
def f07gb_f07_gap_behavior_gap_mean_84d_base_v092_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d var gap
def f07gb_f07_gap_behavior_gap_std_84d_base_v093_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.rolling(84, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_84d_base_v094_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = _z(sig, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d change gap
def f07gb_f07_gap_behavior_gap_delta_84d_base_v095_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_84d_base_v097_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_84d_base_v098_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_84d_base_v099_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d energy gap
def f07gb_f07_gap_behavior_gap_energy_84d_base_v100_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_84d_base_v101_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_84d_base_v102_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_84d_base_v103_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_84d_base_v104_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_84d_base_v105_signal(open, close):
    sig = _gap_open_prior_close(open, close, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level gap
def f07gb_f07_gap_behavior_gap_level_126d_base_v106_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean gap
def f07gb_f07_gap_behavior_gap_mean_126d_base_v107_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d var gap
def f07gb_f07_gap_behavior_gap_std_126d_base_v108_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.rolling(126, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_126d_base_v109_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = _z(sig, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d change gap
def f07gb_f07_gap_behavior_gap_delta_126d_base_v110_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_126d_base_v112_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_126d_base_v113_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_126d_base_v114_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d energy gap
def f07gb_f07_gap_behavior_gap_energy_126d_base_v115_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_126d_base_v116_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_126d_base_v117_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_126d_base_v118_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_126d_base_v119_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_126d_base_v120_signal(open, close):
    sig = _gap_open_prior_close(open, close, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level gap
def f07gb_f07_gap_behavior_gap_level_252d_base_v121_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean gap
def f07gb_f07_gap_behavior_gap_mean_252d_base_v122_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d var gap
def f07gb_f07_gap_behavior_gap_std_252d_base_v123_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.rolling(252, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_252d_base_v124_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = _z(sig, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change gap
def f07gb_f07_gap_behavior_gap_delta_252d_base_v125_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_252d_base_v127_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_252d_base_v128_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_252d_base_v129_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d energy gap
def f07gb_f07_gap_behavior_gap_energy_252d_base_v130_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_252d_base_v131_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_252d_base_v132_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_252d_base_v133_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_252d_base_v134_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_252d_base_v135_signal(open, close):
    sig = _gap_open_prior_close(open, close, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level gap
def f07gb_f07_gap_behavior_gap_level_504d_base_v136_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean gap
def f07gb_f07_gap_behavior_gap_mean_504d_base_v137_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d var gap
def f07gb_f07_gap_behavior_gap_std_504d_base_v138_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.rolling(504, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d zscore gap
def f07gb_f07_gap_behavior_gap_zscore_504d_base_v139_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = _z(sig, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d change gap
def f07gb_f07_gap_behavior_gap_delta_504d_base_v140_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q75gap gap
def f07gb_f07_gap_behavior_gap_upper_gap_504d_base_v142_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q25gap gap
def f07gb_f07_gap_behavior_gap_lower_gap_504d_base_v143_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smean gap gap
def f07gb_f07_gap_behavior_gap_short_mean_gap_504d_base_v144_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d energy gap
def f07gb_f07_gap_behavior_gap_energy_504d_base_v145_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ewm gap gap
def f07gb_f07_gap_behavior_gap_ewm_gap_504d_base_v146_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d tail relief gap
def f07gb_f07_gap_behavior_gap_tail_relief_504d_base_v147_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d peak fade gap
def f07gb_f07_gap_behavior_gap_peak_fade_504d_base_v148_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d absmean gap
def f07gb_f07_gap_behavior_gap_mean_abs_504d_base_v149_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d voladj chg gap
def f07gb_f07_gap_behavior_gap_vol_adj_delta_504d_base_v150_signal(open, close):
    sig = _gap_open_prior_close(open, close, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['open', 'close'], "func": fn} for fn in [f07gb_f07_gap_behavior_gap_level_63d_base_v076_signal, f07gb_f07_gap_behavior_gap_mean_63d_base_v077_signal, f07gb_f07_gap_behavior_gap_std_63d_base_v078_signal, f07gb_f07_gap_behavior_gap_zscore_63d_base_v079_signal, f07gb_f07_gap_behavior_gap_delta_63d_base_v080_signal, f07gb_f07_gap_behavior_gap_upper_gap_63d_base_v082_signal, f07gb_f07_gap_behavior_gap_lower_gap_63d_base_v083_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_63d_base_v084_signal, f07gb_f07_gap_behavior_gap_energy_63d_base_v085_signal, f07gb_f07_gap_behavior_gap_ewm_gap_63d_base_v086_signal, f07gb_f07_gap_behavior_gap_tail_relief_63d_base_v087_signal, f07gb_f07_gap_behavior_gap_peak_fade_63d_base_v088_signal, f07gb_f07_gap_behavior_gap_mean_abs_63d_base_v089_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_63d_base_v090_signal, f07gb_f07_gap_behavior_gap_level_84d_base_v091_signal, f07gb_f07_gap_behavior_gap_mean_84d_base_v092_signal, f07gb_f07_gap_behavior_gap_std_84d_base_v093_signal, f07gb_f07_gap_behavior_gap_zscore_84d_base_v094_signal, f07gb_f07_gap_behavior_gap_delta_84d_base_v095_signal, f07gb_f07_gap_behavior_gap_upper_gap_84d_base_v097_signal, f07gb_f07_gap_behavior_gap_lower_gap_84d_base_v098_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_84d_base_v099_signal, f07gb_f07_gap_behavior_gap_energy_84d_base_v100_signal, f07gb_f07_gap_behavior_gap_ewm_gap_84d_base_v101_signal, f07gb_f07_gap_behavior_gap_tail_relief_84d_base_v102_signal, f07gb_f07_gap_behavior_gap_peak_fade_84d_base_v103_signal, f07gb_f07_gap_behavior_gap_mean_abs_84d_base_v104_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_84d_base_v105_signal, f07gb_f07_gap_behavior_gap_level_126d_base_v106_signal, f07gb_f07_gap_behavior_gap_mean_126d_base_v107_signal, f07gb_f07_gap_behavior_gap_std_126d_base_v108_signal, f07gb_f07_gap_behavior_gap_zscore_126d_base_v109_signal, f07gb_f07_gap_behavior_gap_delta_126d_base_v110_signal, f07gb_f07_gap_behavior_gap_upper_gap_126d_base_v112_signal, f07gb_f07_gap_behavior_gap_lower_gap_126d_base_v113_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_126d_base_v114_signal, f07gb_f07_gap_behavior_gap_energy_126d_base_v115_signal, f07gb_f07_gap_behavior_gap_ewm_gap_126d_base_v116_signal, f07gb_f07_gap_behavior_gap_tail_relief_126d_base_v117_signal, f07gb_f07_gap_behavior_gap_peak_fade_126d_base_v118_signal, f07gb_f07_gap_behavior_gap_mean_abs_126d_base_v119_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_126d_base_v120_signal, f07gb_f07_gap_behavior_gap_level_252d_base_v121_signal, f07gb_f07_gap_behavior_gap_mean_252d_base_v122_signal, f07gb_f07_gap_behavior_gap_std_252d_base_v123_signal, f07gb_f07_gap_behavior_gap_zscore_252d_base_v124_signal, f07gb_f07_gap_behavior_gap_delta_252d_base_v125_signal, f07gb_f07_gap_behavior_gap_upper_gap_252d_base_v127_signal, f07gb_f07_gap_behavior_gap_lower_gap_252d_base_v128_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_252d_base_v129_signal, f07gb_f07_gap_behavior_gap_energy_252d_base_v130_signal, f07gb_f07_gap_behavior_gap_ewm_gap_252d_base_v131_signal, f07gb_f07_gap_behavior_gap_tail_relief_252d_base_v132_signal, f07gb_f07_gap_behavior_gap_peak_fade_252d_base_v133_signal, f07gb_f07_gap_behavior_gap_mean_abs_252d_base_v134_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_252d_base_v135_signal, f07gb_f07_gap_behavior_gap_level_504d_base_v136_signal, f07gb_f07_gap_behavior_gap_mean_504d_base_v137_signal, f07gb_f07_gap_behavior_gap_std_504d_base_v138_signal, f07gb_f07_gap_behavior_gap_zscore_504d_base_v139_signal, f07gb_f07_gap_behavior_gap_delta_504d_base_v140_signal, f07gb_f07_gap_behavior_gap_upper_gap_504d_base_v142_signal, f07gb_f07_gap_behavior_gap_lower_gap_504d_base_v143_signal, f07gb_f07_gap_behavior_gap_short_mean_gap_504d_base_v144_signal, f07gb_f07_gap_behavior_gap_energy_504d_base_v145_signal, f07gb_f07_gap_behavior_gap_ewm_gap_504d_base_v146_signal, f07gb_f07_gap_behavior_gap_tail_relief_504d_base_v147_signal, f07gb_f07_gap_behavior_gap_peak_fade_504d_base_v148_signal, f07gb_f07_gap_behavior_gap_mean_abs_504d_base_v149_signal, f07gb_f07_gap_behavior_gap_vol_adj_delta_504d_base_v150_signal]}
F07_GAP_BEHAVIOR_REGISTRY_076_150 = REGISTRY

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
