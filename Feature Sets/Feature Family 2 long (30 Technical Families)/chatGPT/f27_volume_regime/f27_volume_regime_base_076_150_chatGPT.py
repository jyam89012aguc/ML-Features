import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _volume_regime_ratio(volume, w):
    v = np.log(volume.replace(0, np.nan))
    return v.rolling(max(2, w//3), min_periods=2).std() / v.rolling(w, min_periods=2).std().replace(0, np.nan)

# 63d level vregm
def f27vg_f27_volume_regime_vregm_level_63d_base_v076_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean vregm
def f27vg_f27_volume_regime_vregm_mean_63d_base_v077_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d var vregm
def f27vg_f27_volume_regime_vregm_std_63d_base_v078_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(63, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_63d_base_v079_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = _z(sig, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change vregm
def f27vg_f27_volume_regime_vregm_delta_63d_base_v080_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_63d_base_v082_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_63d_base_v083_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_63d_base_v084_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d energy vregm
def f27vg_f27_volume_regime_vregm_energy_63d_base_v085_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_63d_base_v086_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_63d_base_v087_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_63d_base_v088_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_63d_base_v090_signal(volume):
    sig = _volume_regime_ratio(volume, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d level vregm
def f27vg_f27_volume_regime_vregm_level_84d_base_v091_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d mean vregm
def f27vg_f27_volume_regime_vregm_mean_84d_base_v092_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d var vregm
def f27vg_f27_volume_regime_vregm_std_84d_base_v093_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(84, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_84d_base_v094_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = _z(sig, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d change vregm
def f27vg_f27_volume_regime_vregm_delta_84d_base_v095_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_84d_base_v097_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_84d_base_v098_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_84d_base_v099_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d energy vregm
def f27vg_f27_volume_regime_vregm_energy_84d_base_v100_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_84d_base_v101_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_84d_base_v102_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_84d_base_v103_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_84d_base_v105_signal(volume):
    sig = _volume_regime_ratio(volume, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level vregm
def f27vg_f27_volume_regime_vregm_level_126d_base_v106_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean vregm
def f27vg_f27_volume_regime_vregm_mean_126d_base_v107_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d var vregm
def f27vg_f27_volume_regime_vregm_std_126d_base_v108_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(126, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_126d_base_v109_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = _z(sig, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d change vregm
def f27vg_f27_volume_regime_vregm_delta_126d_base_v110_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_126d_base_v112_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_126d_base_v113_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_126d_base_v114_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d energy vregm
def f27vg_f27_volume_regime_vregm_energy_126d_base_v115_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_126d_base_v116_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_126d_base_v117_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_126d_base_v118_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_126d_base_v120_signal(volume):
    sig = _volume_regime_ratio(volume, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level vregm
def f27vg_f27_volume_regime_vregm_level_252d_base_v121_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean vregm
def f27vg_f27_volume_regime_vregm_mean_252d_base_v122_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d var vregm
def f27vg_f27_volume_regime_vregm_std_252d_base_v123_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(252, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_252d_base_v124_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = _z(sig, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change vregm
def f27vg_f27_volume_regime_vregm_delta_252d_base_v125_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_252d_base_v127_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_252d_base_v128_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_252d_base_v129_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d energy vregm
def f27vg_f27_volume_regime_vregm_energy_252d_base_v130_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_252d_base_v131_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_252d_base_v132_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_252d_base_v133_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_252d_base_v135_signal(volume):
    sig = _volume_regime_ratio(volume, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level vregm
def f27vg_f27_volume_regime_vregm_level_504d_base_v136_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean vregm
def f27vg_f27_volume_regime_vregm_mean_504d_base_v137_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d var vregm
def f27vg_f27_volume_regime_vregm_std_504d_base_v138_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(504, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d zscore vregm
def f27vg_f27_volume_regime_vregm_zscore_504d_base_v139_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = _z(sig, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d change vregm
def f27vg_f27_volume_regime_vregm_delta_504d_base_v140_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q75gap vregm
def f27vg_f27_volume_regime_vregm_upper_gap_504d_base_v142_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q25gap vregm
def f27vg_f27_volume_regime_vregm_lower_gap_504d_base_v143_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smean gap vregm
def f27vg_f27_volume_regime_vregm_short_mean_gap_504d_base_v144_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d energy vregm
def f27vg_f27_volume_regime_vregm_energy_504d_base_v145_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ewm gap vregm
def f27vg_f27_volume_regime_vregm_ewm_gap_504d_base_v146_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d tail relief vregm
def f27vg_f27_volume_regime_vregm_tail_relief_504d_base_v147_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d peak fade vregm
def f27vg_f27_volume_regime_vregm_peak_fade_504d_base_v148_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d voladj chg vregm
def f27vg_f27_volume_regime_vregm_vol_adj_delta_504d_base_v150_signal(volume):
    sig = _volume_regime_ratio(volume, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['volume'], "func": fn} for fn in [f27vg_f27_volume_regime_vregm_level_63d_base_v076_signal, f27vg_f27_volume_regime_vregm_mean_63d_base_v077_signal, f27vg_f27_volume_regime_vregm_std_63d_base_v078_signal, f27vg_f27_volume_regime_vregm_zscore_63d_base_v079_signal, f27vg_f27_volume_regime_vregm_delta_63d_base_v080_signal, f27vg_f27_volume_regime_vregm_upper_gap_63d_base_v082_signal, f27vg_f27_volume_regime_vregm_lower_gap_63d_base_v083_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_63d_base_v084_signal, f27vg_f27_volume_regime_vregm_energy_63d_base_v085_signal, f27vg_f27_volume_regime_vregm_ewm_gap_63d_base_v086_signal, f27vg_f27_volume_regime_vregm_tail_relief_63d_base_v087_signal, f27vg_f27_volume_regime_vregm_peak_fade_63d_base_v088_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_63d_base_v090_signal, f27vg_f27_volume_regime_vregm_level_84d_base_v091_signal, f27vg_f27_volume_regime_vregm_mean_84d_base_v092_signal, f27vg_f27_volume_regime_vregm_std_84d_base_v093_signal, f27vg_f27_volume_regime_vregm_zscore_84d_base_v094_signal, f27vg_f27_volume_regime_vregm_delta_84d_base_v095_signal, f27vg_f27_volume_regime_vregm_upper_gap_84d_base_v097_signal, f27vg_f27_volume_regime_vregm_lower_gap_84d_base_v098_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_84d_base_v099_signal, f27vg_f27_volume_regime_vregm_energy_84d_base_v100_signal, f27vg_f27_volume_regime_vregm_ewm_gap_84d_base_v101_signal, f27vg_f27_volume_regime_vregm_tail_relief_84d_base_v102_signal, f27vg_f27_volume_regime_vregm_peak_fade_84d_base_v103_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_84d_base_v105_signal, f27vg_f27_volume_regime_vregm_level_126d_base_v106_signal, f27vg_f27_volume_regime_vregm_mean_126d_base_v107_signal, f27vg_f27_volume_regime_vregm_std_126d_base_v108_signal, f27vg_f27_volume_regime_vregm_zscore_126d_base_v109_signal, f27vg_f27_volume_regime_vregm_delta_126d_base_v110_signal, f27vg_f27_volume_regime_vregm_upper_gap_126d_base_v112_signal, f27vg_f27_volume_regime_vregm_lower_gap_126d_base_v113_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_126d_base_v114_signal, f27vg_f27_volume_regime_vregm_energy_126d_base_v115_signal, f27vg_f27_volume_regime_vregm_ewm_gap_126d_base_v116_signal, f27vg_f27_volume_regime_vregm_tail_relief_126d_base_v117_signal, f27vg_f27_volume_regime_vregm_peak_fade_126d_base_v118_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_126d_base_v120_signal, f27vg_f27_volume_regime_vregm_level_252d_base_v121_signal, f27vg_f27_volume_regime_vregm_mean_252d_base_v122_signal, f27vg_f27_volume_regime_vregm_std_252d_base_v123_signal, f27vg_f27_volume_regime_vregm_zscore_252d_base_v124_signal, f27vg_f27_volume_regime_vregm_delta_252d_base_v125_signal, f27vg_f27_volume_regime_vregm_upper_gap_252d_base_v127_signal, f27vg_f27_volume_regime_vregm_lower_gap_252d_base_v128_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_252d_base_v129_signal, f27vg_f27_volume_regime_vregm_energy_252d_base_v130_signal, f27vg_f27_volume_regime_vregm_ewm_gap_252d_base_v131_signal, f27vg_f27_volume_regime_vregm_tail_relief_252d_base_v132_signal, f27vg_f27_volume_regime_vregm_peak_fade_252d_base_v133_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_252d_base_v135_signal, f27vg_f27_volume_regime_vregm_level_504d_base_v136_signal, f27vg_f27_volume_regime_vregm_mean_504d_base_v137_signal, f27vg_f27_volume_regime_vregm_std_504d_base_v138_signal, f27vg_f27_volume_regime_vregm_zscore_504d_base_v139_signal, f27vg_f27_volume_regime_vregm_delta_504d_base_v140_signal, f27vg_f27_volume_regime_vregm_upper_gap_504d_base_v142_signal, f27vg_f27_volume_regime_vregm_lower_gap_504d_base_v143_signal, f27vg_f27_volume_regime_vregm_short_mean_gap_504d_base_v144_signal, f27vg_f27_volume_regime_vregm_energy_504d_base_v145_signal, f27vg_f27_volume_regime_vregm_ewm_gap_504d_base_v146_signal, f27vg_f27_volume_regime_vregm_tail_relief_504d_base_v147_signal, f27vg_f27_volume_regime_vregm_peak_fade_504d_base_v148_signal, f27vg_f27_volume_regime_vregm_vol_adj_delta_504d_base_v150_signal]}
F27_VOLUME_REGIME_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    volume = pd.Series(np.random.lognormal(13.0, 0.9, n) * (1.0 + 0.25 * np.sin(t / 13.0)))
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(volume)
        y2 = func(volume)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_volume_regime_ratio" in src
    assert ok_nan >= int(0.80 * len(funcs))
