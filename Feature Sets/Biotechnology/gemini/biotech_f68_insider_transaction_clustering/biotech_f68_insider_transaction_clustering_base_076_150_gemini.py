
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_logdiff_21d_base_v076_signal(ownername, closeadj):
    result = _diff(_log(ownername), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_logdiff_63d_base_v077_signal(ownername, closeadj):
    result = _diff(_log(ownername), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_logdiff_126d_base_v078_signal(ownername, closeadj):
    result = _diff(_log(ownername), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_logdiff_252d_base_v079_signal(ownername, closeadj):
    result = _diff(_log(ownername), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_logdiff_504d_base_v080_signal(ownername, closeadj):
    result = _diff(_log(ownername), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_cv_21d_base_v081_signal(ownername):
    m = _mean(ownername, 21)
    s = _std(ownername, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_cv_63d_base_v082_signal(ownername):
    m = _mean(ownername, 63)
    s = _std(ownername, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_cv_126d_base_v083_signal(ownername):
    m = _mean(ownername, 126)
    s = _std(ownername, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_cv_252d_base_v084_signal(ownername):
    m = _mean(ownername, 252)
    s = _std(ownername, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_cv_504d_base_v085_signal(ownername):
    m = _mean(ownername, 504)
    s = _std(ownername, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_range_21d_base_v086_signal(ownername):
    hi = ownername.rolling(21).max()
    lo = ownername.rolling(21).min()
    result = _safe_div(hi - lo, _mean(ownername, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_range_63d_base_v087_signal(ownername):
    hi = ownername.rolling(63).max()
    lo = ownername.rolling(63).min()
    result = _safe_div(hi - lo, _mean(ownername, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_range_126d_base_v088_signal(ownername):
    hi = ownername.rolling(126).max()
    lo = ownername.rolling(126).min()
    result = _safe_div(hi - lo, _mean(ownername, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_range_252d_base_v089_signal(ownername):
    hi = ownername.rolling(252).max()
    lo = ownername.rolling(252).min()
    result = _safe_div(hi - lo, _mean(ownername, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_range_504d_base_v090_signal(ownername):
    hi = ownername.rolling(504).max()
    lo = ownername.rolling(504).min()
    result = _safe_div(hi - lo, _mean(ownername, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mad_21d_base_v091_signal(ownername, closeadj):
    m = _mean(ownername, 21)
    result = _mean((ownername - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mad_63d_base_v092_signal(ownername, closeadj):
    m = _mean(ownername, 63)
    result = _mean((ownername - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mad_126d_base_v093_signal(ownername, closeadj):
    m = _mean(ownername, 126)
    result = _mean((ownername - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mad_252d_base_v094_signal(ownername, closeadj):
    m = _mean(ownername, 252)
    result = _mean((ownername - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_mad_504d_base_v095_signal(ownername, closeadj):
    m = _mean(ownername, 504)
    result = _mean((ownername - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_21d_base_v096_signal(ownername, closeadj):
    result = ownername.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_63d_base_v097_signal(ownername, closeadj):
    result = ownername.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_126d_base_v098_signal(ownername, closeadj):
    result = ownername.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_252d_base_v099_signal(ownername, closeadj):
    result = ownername.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_504d_base_v100_signal(ownername, closeadj):
    result = ownername.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_std_21d_base_v101_signal(ownername, closeadj):
    result = ownername.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_std_63d_base_v102_signal(ownername, closeadj):
    result = ownername.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_std_126d_base_v103_signal(ownername, closeadj):
    result = ownername.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_std_252d_base_v104_signal(ownername, closeadj):
    result = ownername.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_ewm_std_504d_base_v105_signal(ownername, closeadj):
    result = ownername.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_med_21d_base_v106_signal(ownername, closeadj):
    result = ownername.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_med_63d_base_v107_signal(ownername, closeadj):
    result = ownername.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_med_126d_base_v108_signal(ownername, closeadj):
    result = ownername.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_med_252d_base_v109_signal(ownername, closeadj):
    result = ownername.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_med_504d_base_v110_signal(ownername, closeadj):
    result = ownername.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sum_21d_base_v111_signal(ownername, closeadj):
    result = ownername.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sum_63d_base_v112_signal(ownername, closeadj):
    result = ownername.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sum_126d_base_v113_signal(ownername, closeadj):
    result = ownername.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sum_252d_base_v114_signal(ownername, closeadj):
    result = ownername.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sum_504d_base_v115_signal(ownername, closeadj):
    result = ownername.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sign_21d_base_v116_signal(ownername):
    result = _mean(np.sign(_diff(ownername, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sign_63d_base_v117_signal(ownername):
    result = _mean(np.sign(_diff(ownername, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sign_126d_base_v118_signal(ownername):
    result = _mean(np.sign(_diff(ownername, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sign_252d_base_v119_signal(ownername):
    result = _mean(np.sign(_diff(ownername, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_sign_504d_base_v120_signal(ownername):
    result = _mean(np.sign(_diff(ownername, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_peak_freq_63d_base_v121_signal(ownername):
    is_peak = (ownername == ownername.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_trough_freq_63d_base_v122_signal(ownername):
    is_trough = (ownername == ownername.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_peak_freq_252d_base_v123_signal(ownername):
    is_peak = (ownername == ownername.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of ownername
def gm_f68_biotech_f68_insider_transaction_clustering_trough_freq_252d_base_v124_signal(ownername):
    is_trough = (ownername == ownername.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f68_biotech_f68_insider_transaction_clustering_lag_125d_base_v125_signal(ownername, closeadj):
    result = ownername.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f68_biotech_f68_insider_transaction_clustering_lag_126d_base_v126_signal(ownername, closeadj):
    result = ownername.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f68_biotech_f68_insider_transaction_clustering_lag_127d_base_v127_signal(ownername, closeadj):
    result = ownername.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f68_biotech_f68_insider_transaction_clustering_lag_128d_base_v128_signal(ownername, closeadj):
    result = ownername.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f68_biotech_f68_insider_transaction_clustering_lag_129d_base_v129_signal(ownername, closeadj):
    result = ownername.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f68_biotech_f68_insider_transaction_clustering_lag_130d_base_v130_signal(ownername, closeadj):
    result = ownername.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f68_biotech_f68_insider_transaction_clustering_lag_131d_base_v131_signal(ownername, closeadj):
    result = ownername.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f68_biotech_f68_insider_transaction_clustering_lag_132d_base_v132_signal(ownername, closeadj):
    result = ownername.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f68_biotech_f68_insider_transaction_clustering_lag_133d_base_v133_signal(ownername, closeadj):
    result = ownername.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f68_biotech_f68_insider_transaction_clustering_lag_134d_base_v134_signal(ownername, closeadj):
    result = ownername.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f68_biotech_f68_insider_transaction_clustering_lag_135d_base_v135_signal(ownername, closeadj):
    result = ownername.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f68_biotech_f68_insider_transaction_clustering_lag_136d_base_v136_signal(ownername, closeadj):
    result = ownername.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f68_biotech_f68_insider_transaction_clustering_lag_137d_base_v137_signal(ownername, closeadj):
    result = ownername.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f68_biotech_f68_insider_transaction_clustering_lag_138d_base_v138_signal(ownername, closeadj):
    result = ownername.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f68_biotech_f68_insider_transaction_clustering_lag_139d_base_v139_signal(ownername, closeadj):
    result = ownername.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f68_biotech_f68_insider_transaction_clustering_lag_140d_base_v140_signal(ownername, closeadj):
    result = ownername.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f68_biotech_f68_insider_transaction_clustering_lag_141d_base_v141_signal(ownername, closeadj):
    result = ownername.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f68_biotech_f68_insider_transaction_clustering_lag_142d_base_v142_signal(ownername, closeadj):
    result = ownername.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f68_biotech_f68_insider_transaction_clustering_lag_143d_base_v143_signal(ownername, closeadj):
    result = ownername.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f68_biotech_f68_insider_transaction_clustering_lag_144d_base_v144_signal(ownername, closeadj):
    result = ownername.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f68_biotech_f68_insider_transaction_clustering_lag_145d_base_v145_signal(ownername, closeadj):
    result = ownername.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f68_biotech_f68_insider_transaction_clustering_lag_146d_base_v146_signal(ownername, closeadj):
    result = ownername.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f68_biotech_f68_insider_transaction_clustering_lag_147d_base_v147_signal(ownername, closeadj):
    result = ownername.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f68_biotech_f68_insider_transaction_clustering_lag_148d_base_v148_signal(ownername, closeadj):
    result = ownername.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f68_biotech_f68_insider_transaction_clustering_lag_149d_base_v149_signal(ownername, closeadj):
    result = ownername.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f68_biotech_f68_insider_transaction_clustering_lag_150d_base_v150_signal(ownername, closeadj):
    result = ownername.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

