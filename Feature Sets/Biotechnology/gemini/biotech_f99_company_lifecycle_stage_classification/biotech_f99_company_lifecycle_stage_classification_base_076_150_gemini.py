
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling autocorr of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_autocorr_21d_base_v076_signal(revenue):
    result = _autocorr(revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_autocorr_63d_base_v077_signal(revenue):
    result = _autocorr(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_autocorr_126d_base_v078_signal(revenue):
    result = _autocorr(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_autocorr_252d_base_v079_signal(revenue):
    result = _autocorr(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_autocorr_504d_base_v080_signal(revenue):
    result = _autocorr(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_std_21d_base_v081_signal(revenue, closeadj):
    result = _std(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_std_63d_base_v082_signal(revenue, closeadj):
    result = _std(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_std_126d_base_v083_signal(revenue, closeadj):
    result = _std(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_std_252d_base_v084_signal(revenue, closeadj):
    result = _std(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_std_504d_base_v085_signal(revenue, closeadj):
    result = _std(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_logdiff_21d_base_v086_signal(revenue, closeadj):
    result = _diff(_log(revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_logdiff_63d_base_v087_signal(revenue, closeadj):
    result = _diff(_log(revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_logdiff_126d_base_v088_signal(revenue, closeadj):
    result = _diff(_log(revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_logdiff_252d_base_v089_signal(revenue, closeadj):
    result = _diff(_log(revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_logdiff_504d_base_v090_signal(revenue, closeadj):
    result = _diff(_log(revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_cv_21d_base_v091_signal(revenue):
    m = _mean(revenue, 21)
    s = _std(revenue, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_cv_63d_base_v092_signal(revenue):
    m = _mean(revenue, 63)
    s = _std(revenue, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_cv_126d_base_v093_signal(revenue):
    m = _mean(revenue, 126)
    s = _std(revenue, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_cv_252d_base_v094_signal(revenue):
    m = _mean(revenue, 252)
    s = _std(revenue, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_cv_504d_base_v095_signal(revenue):
    m = _mean(revenue, 504)
    s = _std(revenue, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_range_21d_base_v096_signal(revenue):
    hi = revenue.rolling(21).max()
    lo = revenue.rolling(21).min()
    result = _safe_div(hi - lo, _mean(revenue, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_range_63d_base_v097_signal(revenue):
    hi = revenue.rolling(63).max()
    lo = revenue.rolling(63).min()
    result = _safe_div(hi - lo, _mean(revenue, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_range_126d_base_v098_signal(revenue):
    hi = revenue.rolling(126).max()
    lo = revenue.rolling(126).min()
    result = _safe_div(hi - lo, _mean(revenue, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_range_252d_base_v099_signal(revenue):
    hi = revenue.rolling(252).max()
    lo = revenue.rolling(252).min()
    result = _safe_div(hi - lo, _mean(revenue, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_range_504d_base_v100_signal(revenue):
    hi = revenue.rolling(504).max()
    lo = revenue.rolling(504).min()
    result = _safe_div(hi - lo, _mean(revenue, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mad_21d_base_v101_signal(revenue, closeadj):
    m = _mean(revenue, 21)
    result = _mean((revenue - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mad_63d_base_v102_signal(revenue, closeadj):
    m = _mean(revenue, 63)
    result = _mean((revenue - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mad_126d_base_v103_signal(revenue, closeadj):
    m = _mean(revenue, 126)
    result = _mean((revenue - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mad_252d_base_v104_signal(revenue, closeadj):
    m = _mean(revenue, 252)
    result = _mean((revenue - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_mad_504d_base_v105_signal(revenue, closeadj):
    m = _mean(revenue, 504)
    result = _mean((revenue - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_21d_base_v106_signal(revenue, closeadj):
    result = revenue.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_63d_base_v107_signal(revenue, closeadj):
    result = revenue.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_126d_base_v108_signal(revenue, closeadj):
    result = revenue.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_252d_base_v109_signal(revenue, closeadj):
    result = revenue.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_504d_base_v110_signal(revenue, closeadj):
    result = revenue.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_std_21d_base_v111_signal(revenue, closeadj):
    result = revenue.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_std_63d_base_v112_signal(revenue, closeadj):
    result = revenue.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_std_126d_base_v113_signal(revenue, closeadj):
    result = revenue.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_std_252d_base_v114_signal(revenue, closeadj):
    result = revenue.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_ewm_std_504d_base_v115_signal(revenue, closeadj):
    result = revenue.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_med_21d_base_v116_signal(revenue, closeadj):
    result = revenue.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_med_63d_base_v117_signal(revenue, closeadj):
    result = revenue.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_med_126d_base_v118_signal(revenue, closeadj):
    result = revenue.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_med_252d_base_v119_signal(revenue, closeadj):
    result = revenue.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_med_504d_base_v120_signal(revenue, closeadj):
    result = revenue.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sum_21d_base_v121_signal(revenue, closeadj):
    result = revenue.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sum_63d_base_v122_signal(revenue, closeadj):
    result = revenue.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sum_126d_base_v123_signal(revenue, closeadj):
    result = revenue.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sum_252d_base_v124_signal(revenue, closeadj):
    result = revenue.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sum_504d_base_v125_signal(revenue, closeadj):
    result = revenue.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sign_21d_base_v126_signal(revenue):
    result = _mean(np.sign(_diff(revenue, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sign_63d_base_v127_signal(revenue):
    result = _mean(np.sign(_diff(revenue, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sign_126d_base_v128_signal(revenue):
    result = _mean(np.sign(_diff(revenue, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sign_252d_base_v129_signal(revenue):
    result = _mean(np.sign(_diff(revenue, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_sign_504d_base_v130_signal(revenue):
    result = _mean(np.sign(_diff(revenue, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_peak_freq_63d_base_v131_signal(revenue):
    is_peak = (revenue == revenue.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_trough_freq_63d_base_v132_signal(revenue):
    is_trough = (revenue == revenue.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_peak_freq_252d_base_v133_signal(revenue):
    is_peak = (revenue == revenue.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of revenue
def gm_f99_biotech_f99_company_lifecycle_stage_classification_trough_freq_252d_base_v134_signal(revenue):
    is_trough = (revenue == revenue.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_135d_base_v135_signal(revenue, closeadj):
    result = revenue.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_136d_base_v136_signal(revenue, closeadj):
    result = revenue.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_137d_base_v137_signal(revenue, closeadj):
    result = revenue.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_138d_base_v138_signal(revenue, closeadj):
    result = revenue.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_139d_base_v139_signal(revenue, closeadj):
    result = revenue.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_140d_base_v140_signal(revenue, closeadj):
    result = revenue.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_141d_base_v141_signal(revenue, closeadj):
    result = revenue.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_142d_base_v142_signal(revenue, closeadj):
    result = revenue.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_143d_base_v143_signal(revenue, closeadj):
    result = revenue.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_144d_base_v144_signal(revenue, closeadj):
    result = revenue.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_145d_base_v145_signal(revenue, closeadj):
    result = revenue.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_146d_base_v146_signal(revenue, closeadj):
    result = revenue.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_147d_base_v147_signal(revenue, closeadj):
    result = revenue.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_148d_base_v148_signal(revenue, closeadj):
    result = revenue.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_149d_base_v149_signal(revenue, closeadj):
    result = revenue.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f99_biotech_f99_company_lifecycle_stage_classification_lag_150d_base_v150_signal(revenue, closeadj):
    result = revenue.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

