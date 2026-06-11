import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _high_low_range_ratio(high, low, close, w):
    rng = (high - low) / close.abs().replace(0, np.nan)
    return rng.rolling(w, min_periods=2).mean() + rng.diff(max(1, w//5))

# 63d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_63d_base_v076_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_63d_base_v077_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_63d_base_v078_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(63, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_63d_base_v079_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = _z(sig, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_63d_base_v080_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_63d_base_v082_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_63d_base_v083_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_63d_base_v084_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_63d_base_v085_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_63d_base_v086_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_63d_base_v087_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_63d_base_v088_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_63d_base_v089_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_63d_base_v090_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_84d_base_v091_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_84d_base_v092_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_84d_base_v093_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(84, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_84d_base_v094_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = _z(sig, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_84d_base_v095_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_84d_base_v097_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_84d_base_v098_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_84d_base_v099_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_84d_base_v100_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_84d_base_v101_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_84d_base_v102_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_84d_base_v103_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_84d_base_v104_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_84d_base_v105_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_126d_base_v106_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_126d_base_v107_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_126d_base_v108_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(126, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_126d_base_v109_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = _z(sig, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_126d_base_v110_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_126d_base_v112_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_126d_base_v113_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_126d_base_v114_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_126d_base_v115_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_126d_base_v116_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_126d_base_v117_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_126d_base_v118_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_126d_base_v119_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_126d_base_v120_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_252d_base_v121_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_252d_base_v122_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_252d_base_v123_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(252, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_252d_base_v124_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = _z(sig, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_252d_base_v125_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_252d_base_v127_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_252d_base_v128_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_252d_base_v129_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_252d_base_v130_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_252d_base_v131_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_252d_base_v132_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_252d_base_v133_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_252d_base_v134_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_252d_base_v135_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_level_504d_base_v136_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_504d_base_v137_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d var hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_std_504d_base_v138_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(504, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d zscore hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_zscore_504d_base_v139_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = _z(sig, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d change hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_delta_504d_base_v140_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q75gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_504d_base_v142_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q25gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_504d_base_v143_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smean gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_504d_base_v144_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d energy hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_energy_504d_base_v145_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ewm gap hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_504d_base_v146_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d tail relief hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_504d_base_v147_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d peak fade hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_504d_base_v148_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d absmean hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_504d_base_v149_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d voladj chg hlrng
def f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_504d_base_v150_signal(high, low, close):
    sig = _high_low_range_ratio(high, low, close, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['high', 'low', 'close'], "func": fn} for fn in [f08hl_f08_high_low_range_dynamics_hlrng_level_63d_base_v076_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_63d_base_v077_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_63d_base_v078_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_63d_base_v079_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_63d_base_v080_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_63d_base_v082_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_63d_base_v083_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_63d_base_v084_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_63d_base_v085_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_63d_base_v086_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_63d_base_v087_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_63d_base_v088_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_63d_base_v089_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_63d_base_v090_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_84d_base_v091_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_84d_base_v092_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_84d_base_v093_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_84d_base_v094_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_84d_base_v095_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_84d_base_v097_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_84d_base_v098_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_84d_base_v099_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_84d_base_v100_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_84d_base_v101_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_84d_base_v102_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_84d_base_v103_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_84d_base_v104_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_84d_base_v105_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_126d_base_v106_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_126d_base_v107_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_126d_base_v108_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_126d_base_v109_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_126d_base_v110_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_126d_base_v112_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_126d_base_v113_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_126d_base_v114_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_126d_base_v115_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_126d_base_v116_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_126d_base_v117_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_126d_base_v118_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_126d_base_v119_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_126d_base_v120_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_252d_base_v121_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_252d_base_v122_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_252d_base_v123_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_252d_base_v124_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_252d_base_v125_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_252d_base_v127_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_252d_base_v128_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_252d_base_v129_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_252d_base_v130_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_252d_base_v131_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_252d_base_v132_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_252d_base_v133_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_252d_base_v134_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_252d_base_v135_signal, f08hl_f08_high_low_range_dynamics_hlrng_level_504d_base_v136_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_504d_base_v137_signal, f08hl_f08_high_low_range_dynamics_hlrng_std_504d_base_v138_signal, f08hl_f08_high_low_range_dynamics_hlrng_zscore_504d_base_v139_signal, f08hl_f08_high_low_range_dynamics_hlrng_delta_504d_base_v140_signal, f08hl_f08_high_low_range_dynamics_hlrng_upper_gap_504d_base_v142_signal, f08hl_f08_high_low_range_dynamics_hlrng_lower_gap_504d_base_v143_signal, f08hl_f08_high_low_range_dynamics_hlrng_short_mean_gap_504d_base_v144_signal, f08hl_f08_high_low_range_dynamics_hlrng_energy_504d_base_v145_signal, f08hl_f08_high_low_range_dynamics_hlrng_ewm_gap_504d_base_v146_signal, f08hl_f08_high_low_range_dynamics_hlrng_tail_relief_504d_base_v147_signal, f08hl_f08_high_low_range_dynamics_hlrng_peak_fade_504d_base_v148_signal, f08hl_f08_high_low_range_dynamics_hlrng_mean_abs_504d_base_v149_signal, f08hl_f08_high_low_range_dynamics_hlrng_vol_adj_delta_504d_base_v150_signal]}
F08_HIGH_LOW_RANGE_DYNAMICS_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    close = base * (1.0 + pd.Series(np.random.normal(0.0, 0.01, n)))
    high = close * (1.0 + pd.Series(np.random.uniform(0.003, 0.05, n)))
    low = close * (1.0 - pd.Series(np.random.uniform(0.003, 0.05, n)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(high, low, close)
        y2 = func(high, low, close)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_high_low_range_ratio" in src
    assert ok_nan >= int(0.80 * len(funcs))
