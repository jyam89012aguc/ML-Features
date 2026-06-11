
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_logdiff_21d_base_v076_signal(ncff, closeadj):
    result = _diff(_log(ncff), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_logdiff_63d_base_v077_signal(ncff, closeadj):
    result = _diff(_log(ncff), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_logdiff_126d_base_v078_signal(ncff, closeadj):
    result = _diff(_log(ncff), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_logdiff_252d_base_v079_signal(ncff, closeadj):
    result = _diff(_log(ncff), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_logdiff_504d_base_v080_signal(ncff, closeadj):
    result = _diff(_log(ncff), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_cv_21d_base_v081_signal(ncff):
    m = _mean(ncff, 21)
    s = _std(ncff, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_cv_63d_base_v082_signal(ncff):
    m = _mean(ncff, 63)
    s = _std(ncff, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_cv_126d_base_v083_signal(ncff):
    m = _mean(ncff, 126)
    s = _std(ncff, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_cv_252d_base_v084_signal(ncff):
    m = _mean(ncff, 252)
    s = _std(ncff, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_cv_504d_base_v085_signal(ncff):
    m = _mean(ncff, 504)
    s = _std(ncff, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_range_21d_base_v086_signal(ncff):
    hi = ncff.rolling(21).max()
    lo = ncff.rolling(21).min()
    result = _safe_div(hi - lo, _mean(ncff, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_range_63d_base_v087_signal(ncff):
    hi = ncff.rolling(63).max()
    lo = ncff.rolling(63).min()
    result = _safe_div(hi - lo, _mean(ncff, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_range_126d_base_v088_signal(ncff):
    hi = ncff.rolling(126).max()
    lo = ncff.rolling(126).min()
    result = _safe_div(hi - lo, _mean(ncff, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_range_252d_base_v089_signal(ncff):
    hi = ncff.rolling(252).max()
    lo = ncff.rolling(252).min()
    result = _safe_div(hi - lo, _mean(ncff, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_range_504d_base_v090_signal(ncff):
    hi = ncff.rolling(504).max()
    lo = ncff.rolling(504).min()
    result = _safe_div(hi - lo, _mean(ncff, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mad_21d_base_v091_signal(ncff, closeadj):
    m = _mean(ncff, 21)
    result = _mean((ncff - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mad_63d_base_v092_signal(ncff, closeadj):
    m = _mean(ncff, 63)
    result = _mean((ncff - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mad_126d_base_v093_signal(ncff, closeadj):
    m = _mean(ncff, 126)
    result = _mean((ncff - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mad_252d_base_v094_signal(ncff, closeadj):
    m = _mean(ncff, 252)
    result = _mean((ncff - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_mad_504d_base_v095_signal(ncff, closeadj):
    m = _mean(ncff, 504)
    result = _mean((ncff - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_21d_base_v096_signal(ncff, closeadj):
    result = ncff.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_63d_base_v097_signal(ncff, closeadj):
    result = ncff.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_126d_base_v098_signal(ncff, closeadj):
    result = ncff.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_252d_base_v099_signal(ncff, closeadj):
    result = ncff.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_504d_base_v100_signal(ncff, closeadj):
    result = ncff.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_std_21d_base_v101_signal(ncff, closeadj):
    result = ncff.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_std_63d_base_v102_signal(ncff, closeadj):
    result = ncff.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_std_126d_base_v103_signal(ncff, closeadj):
    result = ncff.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_std_252d_base_v104_signal(ncff, closeadj):
    result = ncff.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_ewm_std_504d_base_v105_signal(ncff, closeadj):
    result = ncff.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_med_21d_base_v106_signal(ncff, closeadj):
    result = ncff.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_med_63d_base_v107_signal(ncff, closeadj):
    result = ncff.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_med_126d_base_v108_signal(ncff, closeadj):
    result = ncff.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_med_252d_base_v109_signal(ncff, closeadj):
    result = ncff.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_med_504d_base_v110_signal(ncff, closeadj):
    result = ncff.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sum_21d_base_v111_signal(ncff, closeadj):
    result = ncff.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sum_63d_base_v112_signal(ncff, closeadj):
    result = ncff.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sum_126d_base_v113_signal(ncff, closeadj):
    result = ncff.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sum_252d_base_v114_signal(ncff, closeadj):
    result = ncff.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sum_504d_base_v115_signal(ncff, closeadj):
    result = ncff.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sign_21d_base_v116_signal(ncff):
    result = _mean(np.sign(_diff(ncff, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sign_63d_base_v117_signal(ncff):
    result = _mean(np.sign(_diff(ncff, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sign_126d_base_v118_signal(ncff):
    result = _mean(np.sign(_diff(ncff, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sign_252d_base_v119_signal(ncff):
    result = _mean(np.sign(_diff(ncff, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_sign_504d_base_v120_signal(ncff):
    result = _mean(np.sign(_diff(ncff, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_peak_freq_63d_base_v121_signal(ncff):
    is_peak = (ncff == ncff.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_trough_freq_63d_base_v122_signal(ncff):
    is_trough = (ncff == ncff.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_peak_freq_252d_base_v123_signal(ncff):
    is_peak = (ncff == ncff.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of ncff
def gm_f17_biotech_f17_financing_cash_flow_dependence_trough_freq_252d_base_v124_signal(ncff):
    is_trough = (ncff == ncff.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_125d_base_v125_signal(ncff, closeadj):
    result = ncff.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_126d_base_v126_signal(ncff, closeadj):
    result = ncff.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_127d_base_v127_signal(ncff, closeadj):
    result = ncff.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_128d_base_v128_signal(ncff, closeadj):
    result = ncff.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_129d_base_v129_signal(ncff, closeadj):
    result = ncff.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_130d_base_v130_signal(ncff, closeadj):
    result = ncff.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_131d_base_v131_signal(ncff, closeadj):
    result = ncff.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_132d_base_v132_signal(ncff, closeadj):
    result = ncff.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_133d_base_v133_signal(ncff, closeadj):
    result = ncff.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_134d_base_v134_signal(ncff, closeadj):
    result = ncff.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_135d_base_v135_signal(ncff, closeadj):
    result = ncff.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_136d_base_v136_signal(ncff, closeadj):
    result = ncff.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_137d_base_v137_signal(ncff, closeadj):
    result = ncff.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_138d_base_v138_signal(ncff, closeadj):
    result = ncff.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_139d_base_v139_signal(ncff, closeadj):
    result = ncff.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_140d_base_v140_signal(ncff, closeadj):
    result = ncff.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_141d_base_v141_signal(ncff, closeadj):
    result = ncff.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_142d_base_v142_signal(ncff, closeadj):
    result = ncff.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_143d_base_v143_signal(ncff, closeadj):
    result = ncff.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_144d_base_v144_signal(ncff, closeadj):
    result = ncff.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_145d_base_v145_signal(ncff, closeadj):
    result = ncff.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_146d_base_v146_signal(ncff, closeadj):
    result = ncff.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_147d_base_v147_signal(ncff, closeadj):
    result = ncff.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_148d_base_v148_signal(ncff, closeadj):
    result = ncff.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_149d_base_v149_signal(ncff, closeadj):
    result = ncff.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f17_biotech_f17_financing_cash_flow_dependence_lag_150d_base_v150_signal(ncff, closeadj):
    result = ncff.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

