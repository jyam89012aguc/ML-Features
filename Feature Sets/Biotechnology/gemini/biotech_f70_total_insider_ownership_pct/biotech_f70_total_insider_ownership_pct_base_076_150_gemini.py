
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_std_21d_base_v076_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_std_63d_base_v077_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_std_126d_base_v078_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_std_252d_base_v079_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_std_504d_base_v080_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_logdiff_21d_base_v081_signal(sharesownedfollowingtransaction, closeadj):
    result = _diff(_log(sharesownedfollowingtransaction), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_logdiff_63d_base_v082_signal(sharesownedfollowingtransaction, closeadj):
    result = _diff(_log(sharesownedfollowingtransaction), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_logdiff_126d_base_v083_signal(sharesownedfollowingtransaction, closeadj):
    result = _diff(_log(sharesownedfollowingtransaction), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_logdiff_252d_base_v084_signal(sharesownedfollowingtransaction, closeadj):
    result = _diff(_log(sharesownedfollowingtransaction), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_logdiff_504d_base_v085_signal(sharesownedfollowingtransaction, closeadj):
    result = _diff(_log(sharesownedfollowingtransaction), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_cv_21d_base_v086_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 21)
    s = _std(sharesownedfollowingtransaction, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_cv_63d_base_v087_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 63)
    s = _std(sharesownedfollowingtransaction, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_cv_126d_base_v088_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 126)
    s = _std(sharesownedfollowingtransaction, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_cv_252d_base_v089_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 252)
    s = _std(sharesownedfollowingtransaction, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_cv_504d_base_v090_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 504)
    s = _std(sharesownedfollowingtransaction, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_range_21d_base_v091_signal(sharesownedfollowingtransaction):
    hi = sharesownedfollowingtransaction.rolling(21).max()
    lo = sharesownedfollowingtransaction.rolling(21).min()
    result = _safe_div(hi - lo, _mean(sharesownedfollowingtransaction, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_range_63d_base_v092_signal(sharesownedfollowingtransaction):
    hi = sharesownedfollowingtransaction.rolling(63).max()
    lo = sharesownedfollowingtransaction.rolling(63).min()
    result = _safe_div(hi - lo, _mean(sharesownedfollowingtransaction, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_range_126d_base_v093_signal(sharesownedfollowingtransaction):
    hi = sharesownedfollowingtransaction.rolling(126).max()
    lo = sharesownedfollowingtransaction.rolling(126).min()
    result = _safe_div(hi - lo, _mean(sharesownedfollowingtransaction, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_range_252d_base_v094_signal(sharesownedfollowingtransaction):
    hi = sharesownedfollowingtransaction.rolling(252).max()
    lo = sharesownedfollowingtransaction.rolling(252).min()
    result = _safe_div(hi - lo, _mean(sharesownedfollowingtransaction, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_range_504d_base_v095_signal(sharesownedfollowingtransaction):
    hi = sharesownedfollowingtransaction.rolling(504).max()
    lo = sharesownedfollowingtransaction.rolling(504).min()
    result = _safe_div(hi - lo, _mean(sharesownedfollowingtransaction, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mad_21d_base_v096_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 21)
    result = _mean((sharesownedfollowingtransaction - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mad_63d_base_v097_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 63)
    result = _mean((sharesownedfollowingtransaction - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mad_126d_base_v098_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 126)
    result = _mean((sharesownedfollowingtransaction - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mad_252d_base_v099_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 252)
    result = _mean((sharesownedfollowingtransaction - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_mad_504d_base_v100_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 504)
    result = _mean((sharesownedfollowingtransaction - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_21d_base_v101_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_63d_base_v102_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_126d_base_v103_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_252d_base_v104_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_504d_base_v105_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_std_21d_base_v106_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_std_63d_base_v107_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_std_126d_base_v108_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_std_252d_base_v109_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_ewm_std_504d_base_v110_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_med_21d_base_v111_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_med_63d_base_v112_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_med_126d_base_v113_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_med_252d_base_v114_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_med_504d_base_v115_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sum_21d_base_v116_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sum_63d_base_v117_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sum_126d_base_v118_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sum_252d_base_v119_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sum_504d_base_v120_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sign_21d_base_v121_signal(sharesownedfollowingtransaction):
    result = _mean(np.sign(_diff(sharesownedfollowingtransaction, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sign_63d_base_v122_signal(sharesownedfollowingtransaction):
    result = _mean(np.sign(_diff(sharesownedfollowingtransaction, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sign_126d_base_v123_signal(sharesownedfollowingtransaction):
    result = _mean(np.sign(_diff(sharesownedfollowingtransaction, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sign_252d_base_v124_signal(sharesownedfollowingtransaction):
    result = _mean(np.sign(_diff(sharesownedfollowingtransaction, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_sign_504d_base_v125_signal(sharesownedfollowingtransaction):
    result = _mean(np.sign(_diff(sharesownedfollowingtransaction, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_peak_freq_63d_base_v126_signal(sharesownedfollowingtransaction):
    is_peak = (sharesownedfollowingtransaction == sharesownedfollowingtransaction.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_trough_freq_63d_base_v127_signal(sharesownedfollowingtransaction):
    is_trough = (sharesownedfollowingtransaction == sharesownedfollowingtransaction.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_peak_freq_252d_base_v128_signal(sharesownedfollowingtransaction):
    is_peak = (sharesownedfollowingtransaction == sharesownedfollowingtransaction.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of sharesownedfollowingtransaction
def gm_f70_biotech_f70_total_insider_ownership_pct_trough_freq_252d_base_v129_signal(sharesownedfollowingtransaction):
    is_trough = (sharesownedfollowingtransaction == sharesownedfollowingtransaction.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_130d_base_v130_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_131d_base_v131_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_132d_base_v132_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_133d_base_v133_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_134d_base_v134_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_135d_base_v135_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_136d_base_v136_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_137d_base_v137_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_138d_base_v138_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_139d_base_v139_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_140d_base_v140_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_141d_base_v141_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_142d_base_v142_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_143d_base_v143_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_144d_base_v144_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_145d_base_v145_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_146d_base_v146_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_147d_base_v147_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_148d_base_v148_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_149d_base_v149_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f70_biotech_f70_total_insider_ownership_pct_lag_150d_base_v150_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

