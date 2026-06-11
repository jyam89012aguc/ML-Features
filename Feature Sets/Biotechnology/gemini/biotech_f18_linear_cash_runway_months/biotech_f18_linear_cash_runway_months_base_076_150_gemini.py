
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_std_21d_base_v076_signal(cashneq, closeadj):
    result = _std(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_std_63d_base_v077_signal(cashneq, closeadj):
    result = _std(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_std_126d_base_v078_signal(cashneq, closeadj):
    result = _std(cashneq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_std_252d_base_v079_signal(cashneq, closeadj):
    result = _std(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_std_504d_base_v080_signal(cashneq, closeadj):
    result = _std(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_logdiff_21d_base_v081_signal(cashneq, closeadj):
    result = _diff(_log(cashneq), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_logdiff_63d_base_v082_signal(cashneq, closeadj):
    result = _diff(_log(cashneq), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_logdiff_126d_base_v083_signal(cashneq, closeadj):
    result = _diff(_log(cashneq), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_logdiff_252d_base_v084_signal(cashneq, closeadj):
    result = _diff(_log(cashneq), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_logdiff_504d_base_v085_signal(cashneq, closeadj):
    result = _diff(_log(cashneq), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_cv_21d_base_v086_signal(cashneq):
    m = _mean(cashneq, 21)
    s = _std(cashneq, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_cv_63d_base_v087_signal(cashneq):
    m = _mean(cashneq, 63)
    s = _std(cashneq, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_cv_126d_base_v088_signal(cashneq):
    m = _mean(cashneq, 126)
    s = _std(cashneq, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_cv_252d_base_v089_signal(cashneq):
    m = _mean(cashneq, 252)
    s = _std(cashneq, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_cv_504d_base_v090_signal(cashneq):
    m = _mean(cashneq, 504)
    s = _std(cashneq, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_range_21d_base_v091_signal(cashneq):
    hi = cashneq.rolling(21).max()
    lo = cashneq.rolling(21).min()
    result = _safe_div(hi - lo, _mean(cashneq, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_range_63d_base_v092_signal(cashneq):
    hi = cashneq.rolling(63).max()
    lo = cashneq.rolling(63).min()
    result = _safe_div(hi - lo, _mean(cashneq, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_range_126d_base_v093_signal(cashneq):
    hi = cashneq.rolling(126).max()
    lo = cashneq.rolling(126).min()
    result = _safe_div(hi - lo, _mean(cashneq, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_range_252d_base_v094_signal(cashneq):
    hi = cashneq.rolling(252).max()
    lo = cashneq.rolling(252).min()
    result = _safe_div(hi - lo, _mean(cashneq, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_range_504d_base_v095_signal(cashneq):
    hi = cashneq.rolling(504).max()
    lo = cashneq.rolling(504).min()
    result = _safe_div(hi - lo, _mean(cashneq, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mad_21d_base_v096_signal(cashneq, closeadj):
    m = _mean(cashneq, 21)
    result = _mean((cashneq - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mad_63d_base_v097_signal(cashneq, closeadj):
    m = _mean(cashneq, 63)
    result = _mean((cashneq - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mad_126d_base_v098_signal(cashneq, closeadj):
    m = _mean(cashneq, 126)
    result = _mean((cashneq - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mad_252d_base_v099_signal(cashneq, closeadj):
    m = _mean(cashneq, 252)
    result = _mean((cashneq - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_mad_504d_base_v100_signal(cashneq, closeadj):
    m = _mean(cashneq, 504)
    result = _mean((cashneq - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_21d_base_v101_signal(cashneq, closeadj):
    result = cashneq.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_63d_base_v102_signal(cashneq, closeadj):
    result = cashneq.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_126d_base_v103_signal(cashneq, closeadj):
    result = cashneq.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_252d_base_v104_signal(cashneq, closeadj):
    result = cashneq.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_504d_base_v105_signal(cashneq, closeadj):
    result = cashneq.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_std_21d_base_v106_signal(cashneq, closeadj):
    result = cashneq.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_std_63d_base_v107_signal(cashneq, closeadj):
    result = cashneq.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_std_126d_base_v108_signal(cashneq, closeadj):
    result = cashneq.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_std_252d_base_v109_signal(cashneq, closeadj):
    result = cashneq.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_ewm_std_504d_base_v110_signal(cashneq, closeadj):
    result = cashneq.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_med_21d_base_v111_signal(cashneq, closeadj):
    result = cashneq.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_med_63d_base_v112_signal(cashneq, closeadj):
    result = cashneq.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_med_126d_base_v113_signal(cashneq, closeadj):
    result = cashneq.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_med_252d_base_v114_signal(cashneq, closeadj):
    result = cashneq.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_med_504d_base_v115_signal(cashneq, closeadj):
    result = cashneq.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sum_21d_base_v116_signal(cashneq, closeadj):
    result = cashneq.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sum_63d_base_v117_signal(cashneq, closeadj):
    result = cashneq.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sum_126d_base_v118_signal(cashneq, closeadj):
    result = cashneq.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sum_252d_base_v119_signal(cashneq, closeadj):
    result = cashneq.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sum_504d_base_v120_signal(cashneq, closeadj):
    result = cashneq.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sign_21d_base_v121_signal(cashneq):
    result = _mean(np.sign(_diff(cashneq, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sign_63d_base_v122_signal(cashneq):
    result = _mean(np.sign(_diff(cashneq, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sign_126d_base_v123_signal(cashneq):
    result = _mean(np.sign(_diff(cashneq, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sign_252d_base_v124_signal(cashneq):
    result = _mean(np.sign(_diff(cashneq, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_sign_504d_base_v125_signal(cashneq):
    result = _mean(np.sign(_diff(cashneq, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_peak_freq_63d_base_v126_signal(cashneq):
    is_peak = (cashneq == cashneq.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_trough_freq_63d_base_v127_signal(cashneq):
    is_trough = (cashneq == cashneq.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_peak_freq_252d_base_v128_signal(cashneq):
    is_peak = (cashneq == cashneq.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of cashneq
def gm_f18_biotech_f18_linear_cash_runway_months_trough_freq_252d_base_v129_signal(cashneq):
    is_trough = (cashneq == cashneq.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f18_biotech_f18_linear_cash_runway_months_lag_130d_base_v130_signal(cashneq, closeadj):
    result = cashneq.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f18_biotech_f18_linear_cash_runway_months_lag_131d_base_v131_signal(cashneq, closeadj):
    result = cashneq.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f18_biotech_f18_linear_cash_runway_months_lag_132d_base_v132_signal(cashneq, closeadj):
    result = cashneq.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f18_biotech_f18_linear_cash_runway_months_lag_133d_base_v133_signal(cashneq, closeadj):
    result = cashneq.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f18_biotech_f18_linear_cash_runway_months_lag_134d_base_v134_signal(cashneq, closeadj):
    result = cashneq.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f18_biotech_f18_linear_cash_runway_months_lag_135d_base_v135_signal(cashneq, closeadj):
    result = cashneq.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f18_biotech_f18_linear_cash_runway_months_lag_136d_base_v136_signal(cashneq, closeadj):
    result = cashneq.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f18_biotech_f18_linear_cash_runway_months_lag_137d_base_v137_signal(cashneq, closeadj):
    result = cashneq.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f18_biotech_f18_linear_cash_runway_months_lag_138d_base_v138_signal(cashneq, closeadj):
    result = cashneq.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f18_biotech_f18_linear_cash_runway_months_lag_139d_base_v139_signal(cashneq, closeadj):
    result = cashneq.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f18_biotech_f18_linear_cash_runway_months_lag_140d_base_v140_signal(cashneq, closeadj):
    result = cashneq.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f18_biotech_f18_linear_cash_runway_months_lag_141d_base_v141_signal(cashneq, closeadj):
    result = cashneq.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f18_biotech_f18_linear_cash_runway_months_lag_142d_base_v142_signal(cashneq, closeadj):
    result = cashneq.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f18_biotech_f18_linear_cash_runway_months_lag_143d_base_v143_signal(cashneq, closeadj):
    result = cashneq.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f18_biotech_f18_linear_cash_runway_months_lag_144d_base_v144_signal(cashneq, closeadj):
    result = cashneq.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f18_biotech_f18_linear_cash_runway_months_lag_145d_base_v145_signal(cashneq, closeadj):
    result = cashneq.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f18_biotech_f18_linear_cash_runway_months_lag_146d_base_v146_signal(cashneq, closeadj):
    result = cashneq.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f18_biotech_f18_linear_cash_runway_months_lag_147d_base_v147_signal(cashneq, closeadj):
    result = cashneq.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f18_biotech_f18_linear_cash_runway_months_lag_148d_base_v148_signal(cashneq, closeadj):
    result = cashneq.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f18_biotech_f18_linear_cash_runway_months_lag_149d_base_v149_signal(cashneq, closeadj):
    result = cashneq.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f18_biotech_f18_linear_cash_runway_months_lag_150d_base_v150_signal(cashneq, closeadj):
    result = cashneq.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

