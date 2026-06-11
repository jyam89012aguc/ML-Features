
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_logdiff_21d_base_v076_signal(transactionvalue, closeadj):
    result = _diff(_log(transactionvalue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_logdiff_63d_base_v077_signal(transactionvalue, closeadj):
    result = _diff(_log(transactionvalue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_logdiff_126d_base_v078_signal(transactionvalue, closeadj):
    result = _diff(_log(transactionvalue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_logdiff_252d_base_v079_signal(transactionvalue, closeadj):
    result = _diff(_log(transactionvalue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_logdiff_504d_base_v080_signal(transactionvalue, closeadj):
    result = _diff(_log(transactionvalue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_cv_21d_base_v081_signal(transactionvalue):
    m = _mean(transactionvalue, 21)
    s = _std(transactionvalue, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_cv_63d_base_v082_signal(transactionvalue):
    m = _mean(transactionvalue, 63)
    s = _std(transactionvalue, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_cv_126d_base_v083_signal(transactionvalue):
    m = _mean(transactionvalue, 126)
    s = _std(transactionvalue, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_cv_252d_base_v084_signal(transactionvalue):
    m = _mean(transactionvalue, 252)
    s = _std(transactionvalue, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_cv_504d_base_v085_signal(transactionvalue):
    m = _mean(transactionvalue, 504)
    s = _std(transactionvalue, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_range_21d_base_v086_signal(transactionvalue):
    hi = transactionvalue.rolling(21).max()
    lo = transactionvalue.rolling(21).min()
    result = _safe_div(hi - lo, _mean(transactionvalue, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_range_63d_base_v087_signal(transactionvalue):
    hi = transactionvalue.rolling(63).max()
    lo = transactionvalue.rolling(63).min()
    result = _safe_div(hi - lo, _mean(transactionvalue, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_range_126d_base_v088_signal(transactionvalue):
    hi = transactionvalue.rolling(126).max()
    lo = transactionvalue.rolling(126).min()
    result = _safe_div(hi - lo, _mean(transactionvalue, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_range_252d_base_v089_signal(transactionvalue):
    hi = transactionvalue.rolling(252).max()
    lo = transactionvalue.rolling(252).min()
    result = _safe_div(hi - lo, _mean(transactionvalue, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_range_504d_base_v090_signal(transactionvalue):
    hi = transactionvalue.rolling(504).max()
    lo = transactionvalue.rolling(504).min()
    result = _safe_div(hi - lo, _mean(transactionvalue, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_mad_21d_base_v091_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 21)
    result = _mean((transactionvalue - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_mad_63d_base_v092_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 63)
    result = _mean((transactionvalue - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_mad_126d_base_v093_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 126)
    result = _mean((transactionvalue - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_mad_252d_base_v094_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 252)
    result = _mean((transactionvalue - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_mad_504d_base_v095_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 504)
    result = _mean((transactionvalue - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_21d_base_v096_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_63d_base_v097_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_126d_base_v098_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_252d_base_v099_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_504d_base_v100_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_std_21d_base_v101_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_std_63d_base_v102_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_std_126d_base_v103_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_std_252d_base_v104_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_ewm_std_504d_base_v105_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_med_21d_base_v106_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_med_63d_base_v107_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_med_126d_base_v108_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_med_252d_base_v109_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_med_504d_base_v110_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sum_21d_base_v111_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sum_63d_base_v112_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sum_126d_base_v113_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sum_252d_base_v114_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sum_504d_base_v115_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sign_21d_base_v116_signal(transactionvalue):
    result = _mean(np.sign(_diff(transactionvalue, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sign_63d_base_v117_signal(transactionvalue):
    result = _mean(np.sign(_diff(transactionvalue, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sign_126d_base_v118_signal(transactionvalue):
    result = _mean(np.sign(_diff(transactionvalue, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sign_252d_base_v119_signal(transactionvalue):
    result = _mean(np.sign(_diff(transactionvalue, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_sign_504d_base_v120_signal(transactionvalue):
    result = _mean(np.sign(_diff(transactionvalue, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_peak_freq_63d_base_v121_signal(transactionvalue):
    is_peak = (transactionvalue == transactionvalue.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_trough_freq_63d_base_v122_signal(transactionvalue):
    is_trough = (transactionvalue == transactionvalue.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_peak_freq_252d_base_v123_signal(transactionvalue):
    is_peak = (transactionvalue == transactionvalue.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of transactionvalue
def gm_f67_biotech_f67_insider_buy_intensity_score_trough_freq_252d_base_v124_signal(transactionvalue):
    is_trough = (transactionvalue == transactionvalue.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_125d_base_v125_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_126d_base_v126_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_127d_base_v127_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_128d_base_v128_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_129d_base_v129_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_130d_base_v130_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_131d_base_v131_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_132d_base_v132_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_133d_base_v133_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_134d_base_v134_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_135d_base_v135_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_136d_base_v136_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_137d_base_v137_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_138d_base_v138_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_139d_base_v139_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_140d_base_v140_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_141d_base_v141_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_142d_base_v142_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_143d_base_v143_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_144d_base_v144_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_145d_base_v145_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_146d_base_v146_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_147d_base_v147_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_148d_base_v148_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_149d_base_v149_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f67_biotech_f67_insider_buy_intensity_score_lag_150d_base_v150_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

