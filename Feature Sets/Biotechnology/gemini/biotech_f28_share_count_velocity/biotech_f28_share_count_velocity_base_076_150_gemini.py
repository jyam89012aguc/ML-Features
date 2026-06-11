
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of sharesbas
def gm_f28_biotech_f28_share_count_velocity_logdiff_21d_base_v076_signal(sharesbas, closeadj):
    result = _diff(_log(sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of sharesbas
def gm_f28_biotech_f28_share_count_velocity_logdiff_63d_base_v077_signal(sharesbas, closeadj):
    result = _diff(_log(sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of sharesbas
def gm_f28_biotech_f28_share_count_velocity_logdiff_126d_base_v078_signal(sharesbas, closeadj):
    result = _diff(_log(sharesbas), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of sharesbas
def gm_f28_biotech_f28_share_count_velocity_logdiff_252d_base_v079_signal(sharesbas, closeadj):
    result = _diff(_log(sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of sharesbas
def gm_f28_biotech_f28_share_count_velocity_logdiff_504d_base_v080_signal(sharesbas, closeadj):
    result = _diff(_log(sharesbas), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_cv_21d_base_v081_signal(sharesbas):
    m = _mean(sharesbas, 21)
    s = _std(sharesbas, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_cv_63d_base_v082_signal(sharesbas):
    m = _mean(sharesbas, 63)
    s = _std(sharesbas, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_cv_126d_base_v083_signal(sharesbas):
    m = _mean(sharesbas, 126)
    s = _std(sharesbas, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_cv_252d_base_v084_signal(sharesbas):
    m = _mean(sharesbas, 252)
    s = _std(sharesbas, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_cv_504d_base_v085_signal(sharesbas):
    m = _mean(sharesbas, 504)
    s = _std(sharesbas, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of sharesbas
def gm_f28_biotech_f28_share_count_velocity_range_21d_base_v086_signal(sharesbas):
    hi = sharesbas.rolling(21).max()
    lo = sharesbas.rolling(21).min()
    result = _safe_div(hi - lo, _mean(sharesbas, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of sharesbas
def gm_f28_biotech_f28_share_count_velocity_range_63d_base_v087_signal(sharesbas):
    hi = sharesbas.rolling(63).max()
    lo = sharesbas.rolling(63).min()
    result = _safe_div(hi - lo, _mean(sharesbas, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of sharesbas
def gm_f28_biotech_f28_share_count_velocity_range_126d_base_v088_signal(sharesbas):
    hi = sharesbas.rolling(126).max()
    lo = sharesbas.rolling(126).min()
    result = _safe_div(hi - lo, _mean(sharesbas, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of sharesbas
def gm_f28_biotech_f28_share_count_velocity_range_252d_base_v089_signal(sharesbas):
    hi = sharesbas.rolling(252).max()
    lo = sharesbas.rolling(252).min()
    result = _safe_div(hi - lo, _mean(sharesbas, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of sharesbas
def gm_f28_biotech_f28_share_count_velocity_range_504d_base_v090_signal(sharesbas):
    hi = sharesbas.rolling(504).max()
    lo = sharesbas.rolling(504).min()
    result = _safe_div(hi - lo, _mean(sharesbas, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mad_21d_base_v091_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 21)
    result = _mean((sharesbas - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mad_63d_base_v092_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 63)
    result = _mean((sharesbas - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mad_126d_base_v093_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 126)
    result = _mean((sharesbas - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mad_252d_base_v094_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 252)
    result = _mean((sharesbas - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of sharesbas
def gm_f28_biotech_f28_share_count_velocity_mad_504d_base_v095_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 504)
    result = _mean((sharesbas - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_21d_base_v096_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_63d_base_v097_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_126d_base_v098_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_252d_base_v099_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_504d_base_v100_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_std_21d_base_v101_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_std_63d_base_v102_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_std_126d_base_v103_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_std_252d_base_v104_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of sharesbas
def gm_f28_biotech_f28_share_count_velocity_ewm_std_504d_base_v105_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of sharesbas
def gm_f28_biotech_f28_share_count_velocity_med_21d_base_v106_signal(sharesbas, closeadj):
    result = sharesbas.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesbas
def gm_f28_biotech_f28_share_count_velocity_med_63d_base_v107_signal(sharesbas, closeadj):
    result = sharesbas.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of sharesbas
def gm_f28_biotech_f28_share_count_velocity_med_126d_base_v108_signal(sharesbas, closeadj):
    result = sharesbas.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesbas
def gm_f28_biotech_f28_share_count_velocity_med_252d_base_v109_signal(sharesbas, closeadj):
    result = sharesbas.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesbas
def gm_f28_biotech_f28_share_count_velocity_med_504d_base_v110_signal(sharesbas, closeadj):
    result = sharesbas.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sum_21d_base_v111_signal(sharesbas, closeadj):
    result = sharesbas.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sum_63d_base_v112_signal(sharesbas, closeadj):
    result = sharesbas.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sum_126d_base_v113_signal(sharesbas, closeadj):
    result = sharesbas.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sum_252d_base_v114_signal(sharesbas, closeadj):
    result = sharesbas.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sum_504d_base_v115_signal(sharesbas, closeadj):
    result = sharesbas.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sign_21d_base_v116_signal(sharesbas):
    result = _mean(np.sign(_diff(sharesbas, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sign_63d_base_v117_signal(sharesbas):
    result = _mean(np.sign(_diff(sharesbas, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sign_126d_base_v118_signal(sharesbas):
    result = _mean(np.sign(_diff(sharesbas, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sign_252d_base_v119_signal(sharesbas):
    result = _mean(np.sign(_diff(sharesbas, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of sharesbas
def gm_f28_biotech_f28_share_count_velocity_sign_504d_base_v120_signal(sharesbas):
    result = _mean(np.sign(_diff(sharesbas, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of sharesbas
def gm_f28_biotech_f28_share_count_velocity_peak_freq_63d_base_v121_signal(sharesbas):
    is_peak = (sharesbas == sharesbas.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of sharesbas
def gm_f28_biotech_f28_share_count_velocity_trough_freq_63d_base_v122_signal(sharesbas):
    is_trough = (sharesbas == sharesbas.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of sharesbas
def gm_f28_biotech_f28_share_count_velocity_peak_freq_252d_base_v123_signal(sharesbas):
    is_peak = (sharesbas == sharesbas.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of sharesbas
def gm_f28_biotech_f28_share_count_velocity_trough_freq_252d_base_v124_signal(sharesbas):
    is_trough = (sharesbas == sharesbas.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f28_biotech_f28_share_count_velocity_lag_125d_base_v125_signal(sharesbas, closeadj):
    result = sharesbas.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f28_biotech_f28_share_count_velocity_lag_126d_base_v126_signal(sharesbas, closeadj):
    result = sharesbas.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f28_biotech_f28_share_count_velocity_lag_127d_base_v127_signal(sharesbas, closeadj):
    result = sharesbas.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f28_biotech_f28_share_count_velocity_lag_128d_base_v128_signal(sharesbas, closeadj):
    result = sharesbas.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f28_biotech_f28_share_count_velocity_lag_129d_base_v129_signal(sharesbas, closeadj):
    result = sharesbas.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f28_biotech_f28_share_count_velocity_lag_130d_base_v130_signal(sharesbas, closeadj):
    result = sharesbas.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f28_biotech_f28_share_count_velocity_lag_131d_base_v131_signal(sharesbas, closeadj):
    result = sharesbas.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f28_biotech_f28_share_count_velocity_lag_132d_base_v132_signal(sharesbas, closeadj):
    result = sharesbas.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f28_biotech_f28_share_count_velocity_lag_133d_base_v133_signal(sharesbas, closeadj):
    result = sharesbas.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f28_biotech_f28_share_count_velocity_lag_134d_base_v134_signal(sharesbas, closeadj):
    result = sharesbas.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f28_biotech_f28_share_count_velocity_lag_135d_base_v135_signal(sharesbas, closeadj):
    result = sharesbas.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f28_biotech_f28_share_count_velocity_lag_136d_base_v136_signal(sharesbas, closeadj):
    result = sharesbas.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f28_biotech_f28_share_count_velocity_lag_137d_base_v137_signal(sharesbas, closeadj):
    result = sharesbas.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f28_biotech_f28_share_count_velocity_lag_138d_base_v138_signal(sharesbas, closeadj):
    result = sharesbas.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f28_biotech_f28_share_count_velocity_lag_139d_base_v139_signal(sharesbas, closeadj):
    result = sharesbas.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f28_biotech_f28_share_count_velocity_lag_140d_base_v140_signal(sharesbas, closeadj):
    result = sharesbas.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f28_biotech_f28_share_count_velocity_lag_141d_base_v141_signal(sharesbas, closeadj):
    result = sharesbas.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f28_biotech_f28_share_count_velocity_lag_142d_base_v142_signal(sharesbas, closeadj):
    result = sharesbas.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f28_biotech_f28_share_count_velocity_lag_143d_base_v143_signal(sharesbas, closeadj):
    result = sharesbas.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f28_biotech_f28_share_count_velocity_lag_144d_base_v144_signal(sharesbas, closeadj):
    result = sharesbas.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f28_biotech_f28_share_count_velocity_lag_145d_base_v145_signal(sharesbas, closeadj):
    result = sharesbas.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f28_biotech_f28_share_count_velocity_lag_146d_base_v146_signal(sharesbas, closeadj):
    result = sharesbas.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f28_biotech_f28_share_count_velocity_lag_147d_base_v147_signal(sharesbas, closeadj):
    result = sharesbas.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f28_biotech_f28_share_count_velocity_lag_148d_base_v148_signal(sharesbas, closeadj):
    result = sharesbas.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f28_biotech_f28_share_count_velocity_lag_149d_base_v149_signal(sharesbas, closeadj):
    result = sharesbas.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f28_biotech_f28_share_count_velocity_lag_150d_base_v150_signal(sharesbas, closeadj):
    result = sharesbas.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

