
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_logdiff_21d_base_v076_signal(ncfcommon, closeadj):
    result = _diff(_log(ncfcommon), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_logdiff_63d_base_v077_signal(ncfcommon, closeadj):
    result = _diff(_log(ncfcommon), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_logdiff_126d_base_v078_signal(ncfcommon, closeadj):
    result = _diff(_log(ncfcommon), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_logdiff_252d_base_v079_signal(ncfcommon, closeadj):
    result = _diff(_log(ncfcommon), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_logdiff_504d_base_v080_signal(ncfcommon, closeadj):
    result = _diff(_log(ncfcommon), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_cv_21d_base_v081_signal(ncfcommon):
    m = _mean(ncfcommon, 21)
    s = _std(ncfcommon, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_cv_63d_base_v082_signal(ncfcommon):
    m = _mean(ncfcommon, 63)
    s = _std(ncfcommon, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_cv_126d_base_v083_signal(ncfcommon):
    m = _mean(ncfcommon, 126)
    s = _std(ncfcommon, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_cv_252d_base_v084_signal(ncfcommon):
    m = _mean(ncfcommon, 252)
    s = _std(ncfcommon, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_cv_504d_base_v085_signal(ncfcommon):
    m = _mean(ncfcommon, 504)
    s = _std(ncfcommon, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_range_21d_base_v086_signal(ncfcommon):
    hi = ncfcommon.rolling(21).max()
    lo = ncfcommon.rolling(21).min()
    result = _safe_div(hi - lo, _mean(ncfcommon, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_range_63d_base_v087_signal(ncfcommon):
    hi = ncfcommon.rolling(63).max()
    lo = ncfcommon.rolling(63).min()
    result = _safe_div(hi - lo, _mean(ncfcommon, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_range_126d_base_v088_signal(ncfcommon):
    hi = ncfcommon.rolling(126).max()
    lo = ncfcommon.rolling(126).min()
    result = _safe_div(hi - lo, _mean(ncfcommon, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_range_252d_base_v089_signal(ncfcommon):
    hi = ncfcommon.rolling(252).max()
    lo = ncfcommon.rolling(252).min()
    result = _safe_div(hi - lo, _mean(ncfcommon, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_range_504d_base_v090_signal(ncfcommon):
    hi = ncfcommon.rolling(504).max()
    lo = ncfcommon.rolling(504).min()
    result = _safe_div(hi - lo, _mean(ncfcommon, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mad_21d_base_v091_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 21)
    result = _mean((ncfcommon - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mad_63d_base_v092_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 63)
    result = _mean((ncfcommon - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mad_126d_base_v093_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 126)
    result = _mean((ncfcommon - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mad_252d_base_v094_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 252)
    result = _mean((ncfcommon - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_mad_504d_base_v095_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 504)
    result = _mean((ncfcommon - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_21d_base_v096_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_63d_base_v097_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_126d_base_v098_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_252d_base_v099_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_504d_base_v100_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_std_21d_base_v101_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_std_63d_base_v102_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_std_126d_base_v103_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_std_252d_base_v104_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_ewm_std_504d_base_v105_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_med_21d_base_v106_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_med_63d_base_v107_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_med_126d_base_v108_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_med_252d_base_v109_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_med_504d_base_v110_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sum_21d_base_v111_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sum_63d_base_v112_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sum_126d_base_v113_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sum_252d_base_v114_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sum_504d_base_v115_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sign_21d_base_v116_signal(ncfcommon):
    result = _mean(np.sign(_diff(ncfcommon, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sign_63d_base_v117_signal(ncfcommon):
    result = _mean(np.sign(_diff(ncfcommon, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sign_126d_base_v118_signal(ncfcommon):
    result = _mean(np.sign(_diff(ncfcommon, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sign_252d_base_v119_signal(ncfcommon):
    result = _mean(np.sign(_diff(ncfcommon, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_sign_504d_base_v120_signal(ncfcommon):
    result = _mean(np.sign(_diff(ncfcommon, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_peak_freq_63d_base_v121_signal(ncfcommon):
    is_peak = (ncfcommon == ncfcommon.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_trough_freq_63d_base_v122_signal(ncfcommon):
    is_trough = (ncfcommon == ncfcommon.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_peak_freq_252d_base_v123_signal(ncfcommon):
    is_peak = (ncfcommon == ncfcommon.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of ncfcommon
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_trough_freq_252d_base_v124_signal(ncfcommon):
    is_trough = (ncfcommon == ncfcommon.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_125d_base_v125_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_126d_base_v126_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_127d_base_v127_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_128d_base_v128_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_129d_base_v129_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_130d_base_v130_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_131d_base_v131_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_132d_base_v132_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_133d_base_v133_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_134d_base_v134_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_135d_base_v135_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_136d_base_v136_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_137d_base_v137_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_138d_base_v138_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_139d_base_v139_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_140d_base_v140_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_141d_base_v141_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_142d_base_v142_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_143d_base_v143_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_144d_base_v144_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_145d_base_v145_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_146d_base_v146_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_147d_base_v147_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_148d_base_v148_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_149d_base_v149_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f32_biotech_f32_common_stock_issuance_cash_flow_lag_150d_base_v150_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

