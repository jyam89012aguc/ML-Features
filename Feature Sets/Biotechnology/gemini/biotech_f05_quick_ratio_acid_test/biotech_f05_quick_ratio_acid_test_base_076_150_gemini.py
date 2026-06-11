
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling autocorr of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_autocorr_21d_base_v076_signal(assetsc):
    result = _autocorr(assetsc, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_autocorr_63d_base_v077_signal(assetsc):
    result = _autocorr(assetsc, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_autocorr_126d_base_v078_signal(assetsc):
    result = _autocorr(assetsc, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_autocorr_252d_base_v079_signal(assetsc):
    result = _autocorr(assetsc, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_autocorr_504d_base_v080_signal(assetsc):
    result = _autocorr(assetsc, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_std_21d_base_v081_signal(assetsc, closeadj):
    result = _std(assetsc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_std_63d_base_v082_signal(assetsc, closeadj):
    result = _std(assetsc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_std_126d_base_v083_signal(assetsc, closeadj):
    result = _std(assetsc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_std_252d_base_v084_signal(assetsc, closeadj):
    result = _std(assetsc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_std_504d_base_v085_signal(assetsc, closeadj):
    result = _std(assetsc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_logdiff_21d_base_v086_signal(assetsc, closeadj):
    result = _diff(_log(assetsc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_logdiff_63d_base_v087_signal(assetsc, closeadj):
    result = _diff(_log(assetsc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_logdiff_126d_base_v088_signal(assetsc, closeadj):
    result = _diff(_log(assetsc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_logdiff_252d_base_v089_signal(assetsc, closeadj):
    result = _diff(_log(assetsc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_logdiff_504d_base_v090_signal(assetsc, closeadj):
    result = _diff(_log(assetsc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_cv_21d_base_v091_signal(assetsc):
    m = _mean(assetsc, 21)
    s = _std(assetsc, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_cv_63d_base_v092_signal(assetsc):
    m = _mean(assetsc, 63)
    s = _std(assetsc, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_cv_126d_base_v093_signal(assetsc):
    m = _mean(assetsc, 126)
    s = _std(assetsc, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_cv_252d_base_v094_signal(assetsc):
    m = _mean(assetsc, 252)
    s = _std(assetsc, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_cv_504d_base_v095_signal(assetsc):
    m = _mean(assetsc, 504)
    s = _std(assetsc, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_range_21d_base_v096_signal(assetsc):
    hi = assetsc.rolling(21).max()
    lo = assetsc.rolling(21).min()
    result = _safe_div(hi - lo, _mean(assetsc, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_range_63d_base_v097_signal(assetsc):
    hi = assetsc.rolling(63).max()
    lo = assetsc.rolling(63).min()
    result = _safe_div(hi - lo, _mean(assetsc, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_range_126d_base_v098_signal(assetsc):
    hi = assetsc.rolling(126).max()
    lo = assetsc.rolling(126).min()
    result = _safe_div(hi - lo, _mean(assetsc, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_range_252d_base_v099_signal(assetsc):
    hi = assetsc.rolling(252).max()
    lo = assetsc.rolling(252).min()
    result = _safe_div(hi - lo, _mean(assetsc, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_range_504d_base_v100_signal(assetsc):
    hi = assetsc.rolling(504).max()
    lo = assetsc.rolling(504).min()
    result = _safe_div(hi - lo, _mean(assetsc, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_mad_21d_base_v101_signal(assetsc, closeadj):
    m = _mean(assetsc, 21)
    result = _mean((assetsc - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_mad_63d_base_v102_signal(assetsc, closeadj):
    m = _mean(assetsc, 63)
    result = _mean((assetsc - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_mad_126d_base_v103_signal(assetsc, closeadj):
    m = _mean(assetsc, 126)
    result = _mean((assetsc - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_mad_252d_base_v104_signal(assetsc, closeadj):
    m = _mean(assetsc, 252)
    result = _mean((assetsc - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_mad_504d_base_v105_signal(assetsc, closeadj):
    m = _mean(assetsc, 504)
    result = _mean((assetsc - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_21d_base_v106_signal(assetsc, closeadj):
    result = assetsc.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_63d_base_v107_signal(assetsc, closeadj):
    result = assetsc.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_126d_base_v108_signal(assetsc, closeadj):
    result = assetsc.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_252d_base_v109_signal(assetsc, closeadj):
    result = assetsc.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_504d_base_v110_signal(assetsc, closeadj):
    result = assetsc.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_std_21d_base_v111_signal(assetsc, closeadj):
    result = assetsc.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_std_63d_base_v112_signal(assetsc, closeadj):
    result = assetsc.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_std_126d_base_v113_signal(assetsc, closeadj):
    result = assetsc.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_std_252d_base_v114_signal(assetsc, closeadj):
    result = assetsc.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_ewm_std_504d_base_v115_signal(assetsc, closeadj):
    result = assetsc.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_med_21d_base_v116_signal(assetsc, closeadj):
    result = assetsc.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_med_63d_base_v117_signal(assetsc, closeadj):
    result = assetsc.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_med_126d_base_v118_signal(assetsc, closeadj):
    result = assetsc.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_med_252d_base_v119_signal(assetsc, closeadj):
    result = assetsc.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_med_504d_base_v120_signal(assetsc, closeadj):
    result = assetsc.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sum_21d_base_v121_signal(assetsc, closeadj):
    result = assetsc.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sum_63d_base_v122_signal(assetsc, closeadj):
    result = assetsc.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sum_126d_base_v123_signal(assetsc, closeadj):
    result = assetsc.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sum_252d_base_v124_signal(assetsc, closeadj):
    result = assetsc.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sum_504d_base_v125_signal(assetsc, closeadj):
    result = assetsc.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sign_21d_base_v126_signal(assetsc):
    result = _mean(np.sign(_diff(assetsc, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sign_63d_base_v127_signal(assetsc):
    result = _mean(np.sign(_diff(assetsc, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sign_126d_base_v128_signal(assetsc):
    result = _mean(np.sign(_diff(assetsc, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sign_252d_base_v129_signal(assetsc):
    result = _mean(np.sign(_diff(assetsc, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_sign_504d_base_v130_signal(assetsc):
    result = _mean(np.sign(_diff(assetsc, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_peak_freq_63d_base_v131_signal(assetsc):
    is_peak = (assetsc == assetsc.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_trough_freq_63d_base_v132_signal(assetsc):
    is_trough = (assetsc == assetsc.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_peak_freq_252d_base_v133_signal(assetsc):
    is_peak = (assetsc == assetsc.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of assetsc
def gm_f05_biotech_f05_quick_ratio_acid_test_trough_freq_252d_base_v134_signal(assetsc):
    is_trough = (assetsc == assetsc.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_135d_base_v135_signal(assetsc, closeadj):
    result = assetsc.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_136d_base_v136_signal(assetsc, closeadj):
    result = assetsc.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_137d_base_v137_signal(assetsc, closeadj):
    result = assetsc.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_138d_base_v138_signal(assetsc, closeadj):
    result = assetsc.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_139d_base_v139_signal(assetsc, closeadj):
    result = assetsc.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_140d_base_v140_signal(assetsc, closeadj):
    result = assetsc.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_141d_base_v141_signal(assetsc, closeadj):
    result = assetsc.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_142d_base_v142_signal(assetsc, closeadj):
    result = assetsc.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_143d_base_v143_signal(assetsc, closeadj):
    result = assetsc.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_144d_base_v144_signal(assetsc, closeadj):
    result = assetsc.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_145d_base_v145_signal(assetsc, closeadj):
    result = assetsc.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_146d_base_v146_signal(assetsc, closeadj):
    result = assetsc.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_147d_base_v147_signal(assetsc, closeadj):
    result = assetsc.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_148d_base_v148_signal(assetsc, closeadj):
    result = assetsc.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_149d_base_v149_signal(assetsc, closeadj):
    result = assetsc.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f05_biotech_f05_quick_ratio_acid_test_lag_150d_base_v150_signal(assetsc, closeadj):
    result = assetsc.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

