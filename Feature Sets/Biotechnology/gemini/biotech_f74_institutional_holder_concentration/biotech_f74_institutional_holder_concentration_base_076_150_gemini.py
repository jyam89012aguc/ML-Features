
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of units
def gm_f74_biotech_f74_institutional_holder_concentration_logdiff_21d_base_v076_signal(units, closeadj):
    result = _diff(_log(units), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of units
def gm_f74_biotech_f74_institutional_holder_concentration_logdiff_63d_base_v077_signal(units, closeadj):
    result = _diff(_log(units), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of units
def gm_f74_biotech_f74_institutional_holder_concentration_logdiff_126d_base_v078_signal(units, closeadj):
    result = _diff(_log(units), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of units
def gm_f74_biotech_f74_institutional_holder_concentration_logdiff_252d_base_v079_signal(units, closeadj):
    result = _diff(_log(units), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of units
def gm_f74_biotech_f74_institutional_holder_concentration_logdiff_504d_base_v080_signal(units, closeadj):
    result = _diff(_log(units), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of units
def gm_f74_biotech_f74_institutional_holder_concentration_cv_21d_base_v081_signal(units):
    m = _mean(units, 21)
    s = _std(units, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of units
def gm_f74_biotech_f74_institutional_holder_concentration_cv_63d_base_v082_signal(units):
    m = _mean(units, 63)
    s = _std(units, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of units
def gm_f74_biotech_f74_institutional_holder_concentration_cv_126d_base_v083_signal(units):
    m = _mean(units, 126)
    s = _std(units, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of units
def gm_f74_biotech_f74_institutional_holder_concentration_cv_252d_base_v084_signal(units):
    m = _mean(units, 252)
    s = _std(units, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of units
def gm_f74_biotech_f74_institutional_holder_concentration_cv_504d_base_v085_signal(units):
    m = _mean(units, 504)
    s = _std(units, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of units
def gm_f74_biotech_f74_institutional_holder_concentration_range_21d_base_v086_signal(units):
    hi = units.rolling(21).max()
    lo = units.rolling(21).min()
    result = _safe_div(hi - lo, _mean(units, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of units
def gm_f74_biotech_f74_institutional_holder_concentration_range_63d_base_v087_signal(units):
    hi = units.rolling(63).max()
    lo = units.rolling(63).min()
    result = _safe_div(hi - lo, _mean(units, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of units
def gm_f74_biotech_f74_institutional_holder_concentration_range_126d_base_v088_signal(units):
    hi = units.rolling(126).max()
    lo = units.rolling(126).min()
    result = _safe_div(hi - lo, _mean(units, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of units
def gm_f74_biotech_f74_institutional_holder_concentration_range_252d_base_v089_signal(units):
    hi = units.rolling(252).max()
    lo = units.rolling(252).min()
    result = _safe_div(hi - lo, _mean(units, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of units
def gm_f74_biotech_f74_institutional_holder_concentration_range_504d_base_v090_signal(units):
    hi = units.rolling(504).max()
    lo = units.rolling(504).min()
    result = _safe_div(hi - lo, _mean(units, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of units
def gm_f74_biotech_f74_institutional_holder_concentration_mad_21d_base_v091_signal(units, closeadj):
    m = _mean(units, 21)
    result = _mean((units - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of units
def gm_f74_biotech_f74_institutional_holder_concentration_mad_63d_base_v092_signal(units, closeadj):
    m = _mean(units, 63)
    result = _mean((units - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of units
def gm_f74_biotech_f74_institutional_holder_concentration_mad_126d_base_v093_signal(units, closeadj):
    m = _mean(units, 126)
    result = _mean((units - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of units
def gm_f74_biotech_f74_institutional_holder_concentration_mad_252d_base_v094_signal(units, closeadj):
    m = _mean(units, 252)
    result = _mean((units - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of units
def gm_f74_biotech_f74_institutional_holder_concentration_mad_504d_base_v095_signal(units, closeadj):
    m = _mean(units, 504)
    result = _mean((units - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_21d_base_v096_signal(units, closeadj):
    result = units.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_63d_base_v097_signal(units, closeadj):
    result = units.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_126d_base_v098_signal(units, closeadj):
    result = units.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_252d_base_v099_signal(units, closeadj):
    result = units.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_504d_base_v100_signal(units, closeadj):
    result = units.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_std_21d_base_v101_signal(units, closeadj):
    result = units.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_std_63d_base_v102_signal(units, closeadj):
    result = units.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_std_126d_base_v103_signal(units, closeadj):
    result = units.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_std_252d_base_v104_signal(units, closeadj):
    result = units.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of units
def gm_f74_biotech_f74_institutional_holder_concentration_ewm_std_504d_base_v105_signal(units, closeadj):
    result = units.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of units
def gm_f74_biotech_f74_institutional_holder_concentration_med_21d_base_v106_signal(units, closeadj):
    result = units.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of units
def gm_f74_biotech_f74_institutional_holder_concentration_med_63d_base_v107_signal(units, closeadj):
    result = units.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of units
def gm_f74_biotech_f74_institutional_holder_concentration_med_126d_base_v108_signal(units, closeadj):
    result = units.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of units
def gm_f74_biotech_f74_institutional_holder_concentration_med_252d_base_v109_signal(units, closeadj):
    result = units.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of units
def gm_f74_biotech_f74_institutional_holder_concentration_med_504d_base_v110_signal(units, closeadj):
    result = units.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of units
def gm_f74_biotech_f74_institutional_holder_concentration_sum_21d_base_v111_signal(units, closeadj):
    result = units.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of units
def gm_f74_biotech_f74_institutional_holder_concentration_sum_63d_base_v112_signal(units, closeadj):
    result = units.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of units
def gm_f74_biotech_f74_institutional_holder_concentration_sum_126d_base_v113_signal(units, closeadj):
    result = units.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of units
def gm_f74_biotech_f74_institutional_holder_concentration_sum_252d_base_v114_signal(units, closeadj):
    result = units.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of units
def gm_f74_biotech_f74_institutional_holder_concentration_sum_504d_base_v115_signal(units, closeadj):
    result = units.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of units
def gm_f74_biotech_f74_institutional_holder_concentration_sign_21d_base_v116_signal(units):
    result = _mean(np.sign(_diff(units, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of units
def gm_f74_biotech_f74_institutional_holder_concentration_sign_63d_base_v117_signal(units):
    result = _mean(np.sign(_diff(units, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of units
def gm_f74_biotech_f74_institutional_holder_concentration_sign_126d_base_v118_signal(units):
    result = _mean(np.sign(_diff(units, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of units
def gm_f74_biotech_f74_institutional_holder_concentration_sign_252d_base_v119_signal(units):
    result = _mean(np.sign(_diff(units, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of units
def gm_f74_biotech_f74_institutional_holder_concentration_sign_504d_base_v120_signal(units):
    result = _mean(np.sign(_diff(units, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of units
def gm_f74_biotech_f74_institutional_holder_concentration_peak_freq_63d_base_v121_signal(units):
    is_peak = (units == units.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of units
def gm_f74_biotech_f74_institutional_holder_concentration_trough_freq_63d_base_v122_signal(units):
    is_trough = (units == units.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of units
def gm_f74_biotech_f74_institutional_holder_concentration_peak_freq_252d_base_v123_signal(units):
    is_peak = (units == units.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of units
def gm_f74_biotech_f74_institutional_holder_concentration_trough_freq_252d_base_v124_signal(units):
    is_trough = (units == units.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f74_biotech_f74_institutional_holder_concentration_lag_125d_base_v125_signal(units, closeadj):
    result = units.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f74_biotech_f74_institutional_holder_concentration_lag_126d_base_v126_signal(units, closeadj):
    result = units.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f74_biotech_f74_institutional_holder_concentration_lag_127d_base_v127_signal(units, closeadj):
    result = units.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f74_biotech_f74_institutional_holder_concentration_lag_128d_base_v128_signal(units, closeadj):
    result = units.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f74_biotech_f74_institutional_holder_concentration_lag_129d_base_v129_signal(units, closeadj):
    result = units.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f74_biotech_f74_institutional_holder_concentration_lag_130d_base_v130_signal(units, closeadj):
    result = units.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f74_biotech_f74_institutional_holder_concentration_lag_131d_base_v131_signal(units, closeadj):
    result = units.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f74_biotech_f74_institutional_holder_concentration_lag_132d_base_v132_signal(units, closeadj):
    result = units.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f74_biotech_f74_institutional_holder_concentration_lag_133d_base_v133_signal(units, closeadj):
    result = units.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f74_biotech_f74_institutional_holder_concentration_lag_134d_base_v134_signal(units, closeadj):
    result = units.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f74_biotech_f74_institutional_holder_concentration_lag_135d_base_v135_signal(units, closeadj):
    result = units.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f74_biotech_f74_institutional_holder_concentration_lag_136d_base_v136_signal(units, closeadj):
    result = units.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f74_biotech_f74_institutional_holder_concentration_lag_137d_base_v137_signal(units, closeadj):
    result = units.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f74_biotech_f74_institutional_holder_concentration_lag_138d_base_v138_signal(units, closeadj):
    result = units.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f74_biotech_f74_institutional_holder_concentration_lag_139d_base_v139_signal(units, closeadj):
    result = units.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f74_biotech_f74_institutional_holder_concentration_lag_140d_base_v140_signal(units, closeadj):
    result = units.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f74_biotech_f74_institutional_holder_concentration_lag_141d_base_v141_signal(units, closeadj):
    result = units.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f74_biotech_f74_institutional_holder_concentration_lag_142d_base_v142_signal(units, closeadj):
    result = units.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f74_biotech_f74_institutional_holder_concentration_lag_143d_base_v143_signal(units, closeadj):
    result = units.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f74_biotech_f74_institutional_holder_concentration_lag_144d_base_v144_signal(units, closeadj):
    result = units.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f74_biotech_f74_institutional_holder_concentration_lag_145d_base_v145_signal(units, closeadj):
    result = units.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f74_biotech_f74_institutional_holder_concentration_lag_146d_base_v146_signal(units, closeadj):
    result = units.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f74_biotech_f74_institutional_holder_concentration_lag_147d_base_v147_signal(units, closeadj):
    result = units.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f74_biotech_f74_institutional_holder_concentration_lag_148d_base_v148_signal(units, closeadj):
    result = units.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f74_biotech_f74_institutional_holder_concentration_lag_149d_base_v149_signal(units, closeadj):
    result = units.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f74_biotech_f74_institutional_holder_concentration_lag_150d_base_v150_signal(units, closeadj):
    result = units.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

