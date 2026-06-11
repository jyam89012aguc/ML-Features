import inspect
import numpy as np
import pandas as pd

def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return (x - m) / s.replace(0, np.nan)

def _volatility_regime_ratio(closeadj, w):
    r = closeadj.pct_change()
    vol = r.rolling(w, min_periods=2).std()
    return vol / vol.rolling(max(3, w//2), min_periods=2).mean().replace(0, np.nan)

# 63d level vreg
def f17vr_f17_volatility_regime_vreg_level_63d_base_v076_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean vreg
def f17vr_f17_volatility_regime_vreg_mean_63d_base_v077_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d var vreg
def f17vr_f17_volatility_regime_vreg_std_63d_base_v078_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig.rolling(63, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d zscore vreg
def f17vr_f17_volatility_regime_vreg_zscore_63d_base_v079_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = _z(sig, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change vreg
def f17vr_f17_volatility_regime_vreg_delta_63d_base_v080_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q75gap vreg
def f17vr_f17_volatility_regime_vreg_upper_gap_63d_base_v082_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d q25gap vreg
def f17vr_f17_volatility_regime_vreg_lower_gap_63d_base_v083_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smean gap vreg
def f17vr_f17_volatility_regime_vreg_short_mean_gap_63d_base_v084_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig.rolling(21, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d energy vreg
def f17vr_f17_volatility_regime_vreg_energy_63d_base_v085_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = (sig * sig).rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d ewm gap vreg
def f17vr_f17_volatility_regime_vreg_ewm_gap_63d_base_v086_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig.ewm(span=21, adjust=False, min_periods=2).mean() - sig.rolling(63, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d tail relief vreg
def f17vr_f17_volatility_regime_vreg_tail_relief_63d_base_v087_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig - sig.rolling(63, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak fade vreg
def f17vr_f17_volatility_regime_vreg_peak_fade_63d_base_v088_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig.rolling(63, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 63d voladj chg vreg
def f17vr_f17_volatility_regime_vreg_vol_adj_delta_63d_base_v090_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 63)
    result = sig.diff(21) / sig.rolling(63, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d level vreg
def f17vr_f17_volatility_regime_vreg_level_84d_base_v091_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d mean vreg
def f17vr_f17_volatility_regime_vreg_mean_84d_base_v092_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d var vreg
def f17vr_f17_volatility_regime_vreg_std_84d_base_v093_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig.rolling(84, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d zscore vreg
def f17vr_f17_volatility_regime_vreg_zscore_84d_base_v094_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = _z(sig, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d change vreg
def f17vr_f17_volatility_regime_vreg_delta_84d_base_v095_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q75gap vreg
def f17vr_f17_volatility_regime_vreg_upper_gap_84d_base_v097_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d q25gap vreg
def f17vr_f17_volatility_regime_vreg_lower_gap_84d_base_v098_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d smean gap vreg
def f17vr_f17_volatility_regime_vreg_short_mean_gap_84d_base_v099_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig.rolling(28, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d energy vreg
def f17vr_f17_volatility_regime_vreg_energy_84d_base_v100_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = (sig * sig).rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d ewm gap vreg
def f17vr_f17_volatility_regime_vreg_ewm_gap_84d_base_v101_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig.ewm(span=28, adjust=False, min_periods=2).mean() - sig.rolling(84, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d tail relief vreg
def f17vr_f17_volatility_regime_vreg_tail_relief_84d_base_v102_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig - sig.rolling(84, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 84d peak fade vreg
def f17vr_f17_volatility_regime_vreg_peak_fade_84d_base_v103_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig.rolling(84, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 84d voladj chg vreg
def f17vr_f17_volatility_regime_vreg_vol_adj_delta_84d_base_v105_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 84)
    result = sig.diff(21) / sig.rolling(84, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d level vreg
def f17vr_f17_volatility_regime_vreg_level_126d_base_v106_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean vreg
def f17vr_f17_volatility_regime_vreg_mean_126d_base_v107_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d var vreg
def f17vr_f17_volatility_regime_vreg_std_126d_base_v108_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig.rolling(126, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d zscore vreg
def f17vr_f17_volatility_regime_vreg_zscore_126d_base_v109_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = _z(sig, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d change vreg
def f17vr_f17_volatility_regime_vreg_delta_126d_base_v110_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q75gap vreg
def f17vr_f17_volatility_regime_vreg_upper_gap_126d_base_v112_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d q25gap vreg
def f17vr_f17_volatility_regime_vreg_lower_gap_126d_base_v113_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d smean gap vreg
def f17vr_f17_volatility_regime_vreg_short_mean_gap_126d_base_v114_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig.rolling(42, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d energy vreg
def f17vr_f17_volatility_regime_vreg_energy_126d_base_v115_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = (sig * sig).rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d ewm gap vreg
def f17vr_f17_volatility_regime_vreg_ewm_gap_126d_base_v116_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig.ewm(span=42, adjust=False, min_periods=2).mean() - sig.rolling(126, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d tail relief vreg
def f17vr_f17_volatility_regime_vreg_tail_relief_126d_base_v117_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig - sig.rolling(126, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 126d peak fade vreg
def f17vr_f17_volatility_regime_vreg_peak_fade_126d_base_v118_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig.rolling(126, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 126d voladj chg vreg
def f17vr_f17_volatility_regime_vreg_vol_adj_delta_126d_base_v120_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 126)
    result = sig.diff(21) / sig.rolling(126, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d level vreg
def f17vr_f17_volatility_regime_vreg_level_252d_base_v121_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean vreg
def f17vr_f17_volatility_regime_vreg_mean_252d_base_v122_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d var vreg
def f17vr_f17_volatility_regime_vreg_std_252d_base_v123_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig.rolling(252, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d zscore vreg
def f17vr_f17_volatility_regime_vreg_zscore_252d_base_v124_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = _z(sig, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change vreg
def f17vr_f17_volatility_regime_vreg_delta_252d_base_v125_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q75gap vreg
def f17vr_f17_volatility_regime_vreg_upper_gap_252d_base_v127_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d q25gap vreg
def f17vr_f17_volatility_regime_vreg_lower_gap_252d_base_v128_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smean gap vreg
def f17vr_f17_volatility_regime_vreg_short_mean_gap_252d_base_v129_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig.rolling(84, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d energy vreg
def f17vr_f17_volatility_regime_vreg_energy_252d_base_v130_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = (sig * sig).rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d ewm gap vreg
def f17vr_f17_volatility_regime_vreg_ewm_gap_252d_base_v131_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig.ewm(span=84, adjust=False, min_periods=2).mean() - sig.rolling(252, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d tail relief vreg
def f17vr_f17_volatility_regime_vreg_tail_relief_252d_base_v132_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig - sig.rolling(252, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak fade vreg
def f17vr_f17_volatility_regime_vreg_peak_fade_252d_base_v133_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig.rolling(252, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 252d voladj chg vreg
def f17vr_f17_volatility_regime_vreg_vol_adj_delta_252d_base_v135_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 252)
    result = sig.diff(21) / sig.rolling(252, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d level vreg
def f17vr_f17_volatility_regime_vreg_level_504d_base_v136_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean vreg
def f17vr_f17_volatility_regime_vreg_mean_504d_base_v137_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d var vreg
def f17vr_f17_volatility_regime_vreg_std_504d_base_v138_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig.rolling(504, min_periods=2).std()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d zscore vreg
def f17vr_f17_volatility_regime_vreg_zscore_504d_base_v139_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = _z(sig, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d change vreg
def f17vr_f17_volatility_regime_vreg_delta_504d_base_v140_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q75gap vreg
def f17vr_f17_volatility_regime_vreg_upper_gap_504d_base_v142_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d q25gap vreg
def f17vr_f17_volatility_regime_vreg_lower_gap_504d_base_v143_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d smean gap vreg
def f17vr_f17_volatility_regime_vreg_short_mean_gap_504d_base_v144_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig.rolling(168, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d energy vreg
def f17vr_f17_volatility_regime_vreg_energy_504d_base_v145_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = (sig * sig).rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d ewm gap vreg
def f17vr_f17_volatility_regime_vreg_ewm_gap_504d_base_v146_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig.ewm(span=168, adjust=False, min_periods=2).mean() - sig.rolling(504, min_periods=2).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d tail relief vreg
def f17vr_f17_volatility_regime_vreg_tail_relief_504d_base_v147_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig - sig.rolling(504, min_periods=2).min()
    return result.replace([np.inf, -np.inf], np.nan)

# 504d peak fade vreg
def f17vr_f17_volatility_regime_vreg_peak_fade_504d_base_v148_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig.rolling(504, min_periods=2).max() - sig
    return result.replace([np.inf, -np.inf], np.nan)

# 504d voladj chg vreg
def f17vr_f17_volatility_regime_vreg_vol_adj_delta_504d_base_v150_signal(closeadj):
    sig = _volatility_regime_ratio(closeadj, 504)
    result = sig.diff(21) / sig.rolling(504, min_periods=2).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [f17vr_f17_volatility_regime_vreg_level_63d_base_v076_signal, f17vr_f17_volatility_regime_vreg_mean_63d_base_v077_signal, f17vr_f17_volatility_regime_vreg_std_63d_base_v078_signal, f17vr_f17_volatility_regime_vreg_zscore_63d_base_v079_signal, f17vr_f17_volatility_regime_vreg_delta_63d_base_v080_signal, f17vr_f17_volatility_regime_vreg_upper_gap_63d_base_v082_signal, f17vr_f17_volatility_regime_vreg_lower_gap_63d_base_v083_signal, f17vr_f17_volatility_regime_vreg_short_mean_gap_63d_base_v084_signal, f17vr_f17_volatility_regime_vreg_energy_63d_base_v085_signal, f17vr_f17_volatility_regime_vreg_ewm_gap_63d_base_v086_signal, f17vr_f17_volatility_regime_vreg_tail_relief_63d_base_v087_signal, f17vr_f17_volatility_regime_vreg_peak_fade_63d_base_v088_signal, f17vr_f17_volatility_regime_vreg_vol_adj_delta_63d_base_v090_signal, f17vr_f17_volatility_regime_vreg_level_84d_base_v091_signal, f17vr_f17_volatility_regime_vreg_mean_84d_base_v092_signal, f17vr_f17_volatility_regime_vreg_std_84d_base_v093_signal, f17vr_f17_volatility_regime_vreg_zscore_84d_base_v094_signal, f17vr_f17_volatility_regime_vreg_delta_84d_base_v095_signal, f17vr_f17_volatility_regime_vreg_upper_gap_84d_base_v097_signal, f17vr_f17_volatility_regime_vreg_lower_gap_84d_base_v098_signal, f17vr_f17_volatility_regime_vreg_short_mean_gap_84d_base_v099_signal, f17vr_f17_volatility_regime_vreg_energy_84d_base_v100_signal, f17vr_f17_volatility_regime_vreg_ewm_gap_84d_base_v101_signal, f17vr_f17_volatility_regime_vreg_tail_relief_84d_base_v102_signal, f17vr_f17_volatility_regime_vreg_peak_fade_84d_base_v103_signal, f17vr_f17_volatility_regime_vreg_vol_adj_delta_84d_base_v105_signal, f17vr_f17_volatility_regime_vreg_level_126d_base_v106_signal, f17vr_f17_volatility_regime_vreg_mean_126d_base_v107_signal, f17vr_f17_volatility_regime_vreg_std_126d_base_v108_signal, f17vr_f17_volatility_regime_vreg_zscore_126d_base_v109_signal, f17vr_f17_volatility_regime_vreg_delta_126d_base_v110_signal, f17vr_f17_volatility_regime_vreg_upper_gap_126d_base_v112_signal, f17vr_f17_volatility_regime_vreg_lower_gap_126d_base_v113_signal, f17vr_f17_volatility_regime_vreg_short_mean_gap_126d_base_v114_signal, f17vr_f17_volatility_regime_vreg_energy_126d_base_v115_signal, f17vr_f17_volatility_regime_vreg_ewm_gap_126d_base_v116_signal, f17vr_f17_volatility_regime_vreg_tail_relief_126d_base_v117_signal, f17vr_f17_volatility_regime_vreg_peak_fade_126d_base_v118_signal, f17vr_f17_volatility_regime_vreg_vol_adj_delta_126d_base_v120_signal, f17vr_f17_volatility_regime_vreg_level_252d_base_v121_signal, f17vr_f17_volatility_regime_vreg_mean_252d_base_v122_signal, f17vr_f17_volatility_regime_vreg_std_252d_base_v123_signal, f17vr_f17_volatility_regime_vreg_zscore_252d_base_v124_signal, f17vr_f17_volatility_regime_vreg_delta_252d_base_v125_signal, f17vr_f17_volatility_regime_vreg_upper_gap_252d_base_v127_signal, f17vr_f17_volatility_regime_vreg_lower_gap_252d_base_v128_signal, f17vr_f17_volatility_regime_vreg_short_mean_gap_252d_base_v129_signal, f17vr_f17_volatility_regime_vreg_energy_252d_base_v130_signal, f17vr_f17_volatility_regime_vreg_ewm_gap_252d_base_v131_signal, f17vr_f17_volatility_regime_vreg_tail_relief_252d_base_v132_signal, f17vr_f17_volatility_regime_vreg_peak_fade_252d_base_v133_signal, f17vr_f17_volatility_regime_vreg_vol_adj_delta_252d_base_v135_signal, f17vr_f17_volatility_regime_vreg_level_504d_base_v136_signal, f17vr_f17_volatility_regime_vreg_mean_504d_base_v137_signal, f17vr_f17_volatility_regime_vreg_std_504d_base_v138_signal, f17vr_f17_volatility_regime_vreg_zscore_504d_base_v139_signal, f17vr_f17_volatility_regime_vreg_delta_504d_base_v140_signal, f17vr_f17_volatility_regime_vreg_upper_gap_504d_base_v142_signal, f17vr_f17_volatility_regime_vreg_lower_gap_504d_base_v143_signal, f17vr_f17_volatility_regime_vreg_short_mean_gap_504d_base_v144_signal, f17vr_f17_volatility_regime_vreg_energy_504d_base_v145_signal, f17vr_f17_volatility_regime_vreg_ewm_gap_504d_base_v146_signal, f17vr_f17_volatility_regime_vreg_tail_relief_504d_base_v147_signal, f17vr_f17_volatility_regime_vreg_peak_fade_504d_base_v148_signal, f17vr_f17_volatility_regime_vreg_vol_adj_delta_504d_base_v150_signal]}
F17_VOLATILITY_REGIME_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    t = pd.Series(np.arange(n, dtype=float))
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0)
    base = pd.Series(40.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.03, n)) + cyc))
    closeadj = base
    funcs = [v["func"] for v in REGISTRY.values()]
    ok_nan = 0
    for func in funcs:
        y1 = func(closeadj)
        y2 = func(closeadj)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        ok_nan += (y1.iloc[504:].isna().mean() < 0.50)
        src = inspect.getsource(func)
        assert "_volatility_regime_ratio" in src
    assert ok_nan >= int(0.80 * len(funcs))
