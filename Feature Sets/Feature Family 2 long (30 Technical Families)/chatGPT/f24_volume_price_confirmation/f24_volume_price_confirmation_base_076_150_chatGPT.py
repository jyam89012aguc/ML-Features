import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _volume_price_confirmation(closeadj, volume, w):
    return closeadj.pct_change(w) * (volume / volume.rolling(w, min_periods=2).mean().replace(0, np.nan))

# 63d level vpc
def f24vp_f24_volume_price_confirmation_vpc_level_63d_base_v076_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_63d_base_v077_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d var vpc
def f24vp_f24_volume_price_confirmation_vpc_std_63d_base_v078_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.rolling(63, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d zscore vpc
def f24vp_f24_volume_price_confirmation_vpc_zscore_63d_base_v079_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = _z(sig, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change vpc
def f24vp_f24_volume_price_confirmation_vpc_delta_63d_base_v080_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q75gap vpc
def f24vp_f24_volume_price_confirmation_vpc_upper_gap_63d_base_v082_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q25gap vpc
def f24vp_f24_volume_price_confirmation_vpc_lower_gap_63d_base_v083_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smean gap vpc
def f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_63d_base_v084_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d energy vpc
def f24vp_f24_volume_price_confirmation_vpc_energy_63d_base_v085_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ewm gap vpc
def f24vp_f24_volume_price_confirmation_vpc_ewm_gap_63d_base_v086_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d tail relief vpc
def f24vp_f24_volume_price_confirmation_vpc_tail_relief_63d_base_v087_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak fade vpc
def f24vp_f24_volume_price_confirmation_vpc_peak_fade_63d_base_v088_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d absmean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_abs_63d_base_v089_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.abs().rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d voladj chg vpc
def f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_63d_base_v090_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d level vpc
def f24vp_f24_volume_price_confirmation_vpc_level_84d_base_v091_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d mean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_84d_base_v092_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d var vpc
def f24vp_f24_volume_price_confirmation_vpc_std_84d_base_v093_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.rolling(84, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d zscore vpc
def f24vp_f24_volume_price_confirmation_vpc_zscore_84d_base_v094_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = _z(sig, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d change vpc
def f24vp_f24_volume_price_confirmation_vpc_delta_84d_base_v095_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q75gap vpc
def f24vp_f24_volume_price_confirmation_vpc_upper_gap_84d_base_v097_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q25gap vpc
def f24vp_f24_volume_price_confirmation_vpc_lower_gap_84d_base_v098_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d smean gap vpc
def f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_84d_base_v099_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d energy vpc
def f24vp_f24_volume_price_confirmation_vpc_energy_84d_base_v100_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d ewm gap vpc
def f24vp_f24_volume_price_confirmation_vpc_ewm_gap_84d_base_v101_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d tail relief vpc
def f24vp_f24_volume_price_confirmation_vpc_tail_relief_84d_base_v102_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d peak fade vpc
def f24vp_f24_volume_price_confirmation_vpc_peak_fade_84d_base_v103_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d absmean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_abs_84d_base_v104_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.abs().rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d voladj chg vpc
def f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_84d_base_v105_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level vpc
def f24vp_f24_volume_price_confirmation_vpc_level_126d_base_v106_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_126d_base_v107_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d var vpc
def f24vp_f24_volume_price_confirmation_vpc_std_126d_base_v108_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.rolling(126, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d zscore vpc
def f24vp_f24_volume_price_confirmation_vpc_zscore_126d_base_v109_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = _z(sig, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d change vpc
def f24vp_f24_volume_price_confirmation_vpc_delta_126d_base_v110_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q75gap vpc
def f24vp_f24_volume_price_confirmation_vpc_upper_gap_126d_base_v112_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q25gap vpc
def f24vp_f24_volume_price_confirmation_vpc_lower_gap_126d_base_v113_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smean gap vpc
def f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_126d_base_v114_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d energy vpc
def f24vp_f24_volume_price_confirmation_vpc_energy_126d_base_v115_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ewm gap vpc
def f24vp_f24_volume_price_confirmation_vpc_ewm_gap_126d_base_v116_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d tail relief vpc
def f24vp_f24_volume_price_confirmation_vpc_tail_relief_126d_base_v117_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d peak fade vpc
def f24vp_f24_volume_price_confirmation_vpc_peak_fade_126d_base_v118_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d absmean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_abs_126d_base_v119_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.abs().rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d voladj chg vpc
def f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_126d_base_v120_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level vpc
def f24vp_f24_volume_price_confirmation_vpc_level_252d_base_v121_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_252d_base_v122_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d var vpc
def f24vp_f24_volume_price_confirmation_vpc_std_252d_base_v123_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.rolling(252, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d zscore vpc
def f24vp_f24_volume_price_confirmation_vpc_zscore_252d_base_v124_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = _z(sig, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change vpc
def f24vp_f24_volume_price_confirmation_vpc_delta_252d_base_v125_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q75gap vpc
def f24vp_f24_volume_price_confirmation_vpc_upper_gap_252d_base_v127_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q25gap vpc
def f24vp_f24_volume_price_confirmation_vpc_lower_gap_252d_base_v128_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smean gap vpc
def f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_252d_base_v129_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d energy vpc
def f24vp_f24_volume_price_confirmation_vpc_energy_252d_base_v130_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ewm gap vpc
def f24vp_f24_volume_price_confirmation_vpc_ewm_gap_252d_base_v131_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d tail relief vpc
def f24vp_f24_volume_price_confirmation_vpc_tail_relief_252d_base_v132_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak fade vpc
def f24vp_f24_volume_price_confirmation_vpc_peak_fade_252d_base_v133_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d absmean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_abs_252d_base_v134_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.abs().rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d voladj chg vpc
def f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_252d_base_v135_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level vpc
def f24vp_f24_volume_price_confirmation_vpc_level_504d_base_v136_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_504d_base_v137_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d var vpc
def f24vp_f24_volume_price_confirmation_vpc_std_504d_base_v138_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.rolling(504, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d zscore vpc
def f24vp_f24_volume_price_confirmation_vpc_zscore_504d_base_v139_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = _z(sig, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d change vpc
def f24vp_f24_volume_price_confirmation_vpc_delta_504d_base_v140_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q75gap vpc
def f24vp_f24_volume_price_confirmation_vpc_upper_gap_504d_base_v142_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q25gap vpc
def f24vp_f24_volume_price_confirmation_vpc_lower_gap_504d_base_v143_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smean gap vpc
def f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_504d_base_v144_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d energy vpc
def f24vp_f24_volume_price_confirmation_vpc_energy_504d_base_v145_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ewm gap vpc
def f24vp_f24_volume_price_confirmation_vpc_ewm_gap_504d_base_v146_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d tail relief vpc
def f24vp_f24_volume_price_confirmation_vpc_tail_relief_504d_base_v147_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d peak fade vpc
def f24vp_f24_volume_price_confirmation_vpc_peak_fade_504d_base_v148_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d absmean vpc
def f24vp_f24_volume_price_confirmation_vpc_mean_abs_504d_base_v149_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.abs().rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d voladj chg vpc
def f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_504d_base_v150_signal(closeadj, volume):
    sig = _volume_price_confirmation(closeadj, volume, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['closeadj', 'volume'], "func": fn} for fn in [f24vp_f24_volume_price_confirmation_vpc_level_63d_base_v076_signal, f24vp_f24_volume_price_confirmation_vpc_mean_63d_base_v077_signal, f24vp_f24_volume_price_confirmation_vpc_std_63d_base_v078_signal, f24vp_f24_volume_price_confirmation_vpc_zscore_63d_base_v079_signal, f24vp_f24_volume_price_confirmation_vpc_delta_63d_base_v080_signal, f24vp_f24_volume_price_confirmation_vpc_upper_gap_63d_base_v082_signal, f24vp_f24_volume_price_confirmation_vpc_lower_gap_63d_base_v083_signal, f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_63d_base_v084_signal, f24vp_f24_volume_price_confirmation_vpc_energy_63d_base_v085_signal, f24vp_f24_volume_price_confirmation_vpc_ewm_gap_63d_base_v086_signal, f24vp_f24_volume_price_confirmation_vpc_tail_relief_63d_base_v087_signal, f24vp_f24_volume_price_confirmation_vpc_peak_fade_63d_base_v088_signal, f24vp_f24_volume_price_confirmation_vpc_mean_abs_63d_base_v089_signal, f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_63d_base_v090_signal, f24vp_f24_volume_price_confirmation_vpc_level_84d_base_v091_signal, f24vp_f24_volume_price_confirmation_vpc_mean_84d_base_v092_signal, f24vp_f24_volume_price_confirmation_vpc_std_84d_base_v093_signal, f24vp_f24_volume_price_confirmation_vpc_zscore_84d_base_v094_signal, f24vp_f24_volume_price_confirmation_vpc_delta_84d_base_v095_signal, f24vp_f24_volume_price_confirmation_vpc_upper_gap_84d_base_v097_signal, f24vp_f24_volume_price_confirmation_vpc_lower_gap_84d_base_v098_signal, f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_84d_base_v099_signal, f24vp_f24_volume_price_confirmation_vpc_energy_84d_base_v100_signal, f24vp_f24_volume_price_confirmation_vpc_ewm_gap_84d_base_v101_signal, f24vp_f24_volume_price_confirmation_vpc_tail_relief_84d_base_v102_signal, f24vp_f24_volume_price_confirmation_vpc_peak_fade_84d_base_v103_signal, f24vp_f24_volume_price_confirmation_vpc_mean_abs_84d_base_v104_signal, f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_84d_base_v105_signal, f24vp_f24_volume_price_confirmation_vpc_level_126d_base_v106_signal, f24vp_f24_volume_price_confirmation_vpc_mean_126d_base_v107_signal, f24vp_f24_volume_price_confirmation_vpc_std_126d_base_v108_signal, f24vp_f24_volume_price_confirmation_vpc_zscore_126d_base_v109_signal, f24vp_f24_volume_price_confirmation_vpc_delta_126d_base_v110_signal, f24vp_f24_volume_price_confirmation_vpc_upper_gap_126d_base_v112_signal, f24vp_f24_volume_price_confirmation_vpc_lower_gap_126d_base_v113_signal, f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_126d_base_v114_signal, f24vp_f24_volume_price_confirmation_vpc_energy_126d_base_v115_signal, f24vp_f24_volume_price_confirmation_vpc_ewm_gap_126d_base_v116_signal, f24vp_f24_volume_price_confirmation_vpc_tail_relief_126d_base_v117_signal, f24vp_f24_volume_price_confirmation_vpc_peak_fade_126d_base_v118_signal, f24vp_f24_volume_price_confirmation_vpc_mean_abs_126d_base_v119_signal, f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_126d_base_v120_signal, f24vp_f24_volume_price_confirmation_vpc_level_252d_base_v121_signal, f24vp_f24_volume_price_confirmation_vpc_mean_252d_base_v122_signal, f24vp_f24_volume_price_confirmation_vpc_std_252d_base_v123_signal, f24vp_f24_volume_price_confirmation_vpc_zscore_252d_base_v124_signal, f24vp_f24_volume_price_confirmation_vpc_delta_252d_base_v125_signal, f24vp_f24_volume_price_confirmation_vpc_upper_gap_252d_base_v127_signal, f24vp_f24_volume_price_confirmation_vpc_lower_gap_252d_base_v128_signal, f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_252d_base_v129_signal, f24vp_f24_volume_price_confirmation_vpc_energy_252d_base_v130_signal, f24vp_f24_volume_price_confirmation_vpc_ewm_gap_252d_base_v131_signal, f24vp_f24_volume_price_confirmation_vpc_tail_relief_252d_base_v132_signal, f24vp_f24_volume_price_confirmation_vpc_peak_fade_252d_base_v133_signal, f24vp_f24_volume_price_confirmation_vpc_mean_abs_252d_base_v134_signal, f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_252d_base_v135_signal, f24vp_f24_volume_price_confirmation_vpc_level_504d_base_v136_signal, f24vp_f24_volume_price_confirmation_vpc_mean_504d_base_v137_signal, f24vp_f24_volume_price_confirmation_vpc_std_504d_base_v138_signal, f24vp_f24_volume_price_confirmation_vpc_zscore_504d_base_v139_signal, f24vp_f24_volume_price_confirmation_vpc_delta_504d_base_v140_signal, f24vp_f24_volume_price_confirmation_vpc_upper_gap_504d_base_v142_signal, f24vp_f24_volume_price_confirmation_vpc_lower_gap_504d_base_v143_signal, f24vp_f24_volume_price_confirmation_vpc_short_mean_gap_504d_base_v144_signal, f24vp_f24_volume_price_confirmation_vpc_energy_504d_base_v145_signal, f24vp_f24_volume_price_confirmation_vpc_ewm_gap_504d_base_v146_signal, f24vp_f24_volume_price_confirmation_vpc_tail_relief_504d_base_v147_signal, f24vp_f24_volume_price_confirmation_vpc_peak_fade_504d_base_v148_signal, f24vp_f24_volume_price_confirmation_vpc_mean_abs_504d_base_v149_signal, f24vp_f24_volume_price_confirmation_vpc_vol_adj_delta_504d_base_v150_signal]}
F24_VOLUME_PRICE_CONFIRMATION_REGISTRY_076_150 = REGISTRY

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
        assert "_volume_price_confirmation" in src
    assert ok_nan >= int(0.80 * len(funcs))
