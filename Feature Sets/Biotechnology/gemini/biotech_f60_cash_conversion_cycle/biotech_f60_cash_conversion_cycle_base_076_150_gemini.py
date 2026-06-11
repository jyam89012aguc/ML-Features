
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling kurtosis of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_kurt_21d_base_v076_signal(receivables):
    result = _kurt(receivables, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling kurtosis of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_kurt_63d_base_v077_signal(receivables):
    result = _kurt(receivables, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling kurtosis of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_kurt_126d_base_v078_signal(receivables):
    result = _kurt(receivables, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling kurtosis of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_kurt_252d_base_v079_signal(receivables):
    result = _kurt(receivables, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling kurtosis of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_kurt_504d_base_v080_signal(receivables):
    result = _kurt(receivables, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling rank of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_rank_21d_base_v081_signal(receivables, closeadj):
    result = _rank(receivables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling rank of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_rank_63d_base_v082_signal(receivables, closeadj):
    result = _rank(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling rank of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_rank_126d_base_v083_signal(receivables, closeadj):
    result = _rank(receivables, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling rank of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_rank_252d_base_v084_signal(receivables, closeadj):
    result = _rank(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling rank of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_rank_504d_base_v085_signal(receivables, closeadj):
    result = _rank(receivables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling autocorr of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_autocorr_21d_base_v086_signal(receivables):
    result = _autocorr(receivables, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_autocorr_63d_base_v087_signal(receivables):
    result = _autocorr(receivables, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_autocorr_126d_base_v088_signal(receivables):
    result = _autocorr(receivables, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_autocorr_252d_base_v089_signal(receivables):
    result = _autocorr(receivables, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_autocorr_504d_base_v090_signal(receivables):
    result = _autocorr(receivables, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_std_21d_base_v091_signal(receivables, closeadj):
    result = _std(receivables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_std_63d_base_v092_signal(receivables, closeadj):
    result = _std(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_std_126d_base_v093_signal(receivables, closeadj):
    result = _std(receivables, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_std_252d_base_v094_signal(receivables, closeadj):
    result = _std(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_std_504d_base_v095_signal(receivables, closeadj):
    result = _std(receivables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_logdiff_21d_base_v096_signal(receivables, closeadj):
    result = _diff(_log(receivables), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_logdiff_63d_base_v097_signal(receivables, closeadj):
    result = _diff(_log(receivables), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_logdiff_126d_base_v098_signal(receivables, closeadj):
    result = _diff(_log(receivables), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_logdiff_252d_base_v099_signal(receivables, closeadj):
    result = _diff(_log(receivables), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_logdiff_504d_base_v100_signal(receivables, closeadj):
    result = _diff(_log(receivables), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_cv_21d_base_v101_signal(receivables):
    m = _mean(receivables, 21)
    s = _std(receivables, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_cv_63d_base_v102_signal(receivables):
    m = _mean(receivables, 63)
    s = _std(receivables, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_cv_126d_base_v103_signal(receivables):
    m = _mean(receivables, 126)
    s = _std(receivables, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_cv_252d_base_v104_signal(receivables):
    m = _mean(receivables, 252)
    s = _std(receivables, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_cv_504d_base_v105_signal(receivables):
    m = _mean(receivables, 504)
    s = _std(receivables, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_range_21d_base_v106_signal(receivables):
    hi = receivables.rolling(21).max()
    lo = receivables.rolling(21).min()
    result = _safe_div(hi - lo, _mean(receivables, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_range_63d_base_v107_signal(receivables):
    hi = receivables.rolling(63).max()
    lo = receivables.rolling(63).min()
    result = _safe_div(hi - lo, _mean(receivables, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_range_126d_base_v108_signal(receivables):
    hi = receivables.rolling(126).max()
    lo = receivables.rolling(126).min()
    result = _safe_div(hi - lo, _mean(receivables, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_range_252d_base_v109_signal(receivables):
    hi = receivables.rolling(252).max()
    lo = receivables.rolling(252).min()
    result = _safe_div(hi - lo, _mean(receivables, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_range_504d_base_v110_signal(receivables):
    hi = receivables.rolling(504).max()
    lo = receivables.rolling(504).min()
    result = _safe_div(hi - lo, _mean(receivables, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_mad_21d_base_v111_signal(receivables, closeadj):
    m = _mean(receivables, 21)
    result = _mean((receivables - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_mad_63d_base_v112_signal(receivables, closeadj):
    m = _mean(receivables, 63)
    result = _mean((receivables - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_mad_126d_base_v113_signal(receivables, closeadj):
    m = _mean(receivables, 126)
    result = _mean((receivables - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_mad_252d_base_v114_signal(receivables, closeadj):
    m = _mean(receivables, 252)
    result = _mean((receivables - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_mad_504d_base_v115_signal(receivables, closeadj):
    m = _mean(receivables, 504)
    result = _mean((receivables - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_21d_base_v116_signal(receivables, closeadj):
    result = receivables.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_63d_base_v117_signal(receivables, closeadj):
    result = receivables.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_126d_base_v118_signal(receivables, closeadj):
    result = receivables.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_252d_base_v119_signal(receivables, closeadj):
    result = receivables.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_504d_base_v120_signal(receivables, closeadj):
    result = receivables.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_std_21d_base_v121_signal(receivables, closeadj):
    result = receivables.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_std_63d_base_v122_signal(receivables, closeadj):
    result = receivables.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_std_126d_base_v123_signal(receivables, closeadj):
    result = receivables.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_std_252d_base_v124_signal(receivables, closeadj):
    result = receivables.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_ewm_std_504d_base_v125_signal(receivables, closeadj):
    result = receivables.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_med_21d_base_v126_signal(receivables, closeadj):
    result = receivables.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_med_63d_base_v127_signal(receivables, closeadj):
    result = receivables.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_med_126d_base_v128_signal(receivables, closeadj):
    result = receivables.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_med_252d_base_v129_signal(receivables, closeadj):
    result = receivables.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_med_504d_base_v130_signal(receivables, closeadj):
    result = receivables.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sum_21d_base_v131_signal(receivables, closeadj):
    result = receivables.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sum_63d_base_v132_signal(receivables, closeadj):
    result = receivables.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sum_126d_base_v133_signal(receivables, closeadj):
    result = receivables.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sum_252d_base_v134_signal(receivables, closeadj):
    result = receivables.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sum_504d_base_v135_signal(receivables, closeadj):
    result = receivables.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sign_21d_base_v136_signal(receivables):
    result = _mean(np.sign(_diff(receivables, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sign_63d_base_v137_signal(receivables):
    result = _mean(np.sign(_diff(receivables, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sign_126d_base_v138_signal(receivables):
    result = _mean(np.sign(_diff(receivables, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sign_252d_base_v139_signal(receivables):
    result = _mean(np.sign(_diff(receivables, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_sign_504d_base_v140_signal(receivables):
    result = _mean(np.sign(_diff(receivables, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_peak_freq_63d_base_v141_signal(receivables):
    is_peak = (receivables == receivables.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_trough_freq_63d_base_v142_signal(receivables):
    is_trough = (receivables == receivables.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_peak_freq_252d_base_v143_signal(receivables):
    is_peak = (receivables == receivables.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of receivables
def gm_f60_biotech_f60_cash_conversion_cycle_trough_freq_252d_base_v144_signal(receivables):
    is_trough = (receivables == receivables.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f60_biotech_f60_cash_conversion_cycle_lag_145d_base_v145_signal(receivables, closeadj):
    result = receivables.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f60_biotech_f60_cash_conversion_cycle_lag_146d_base_v146_signal(receivables, closeadj):
    result = receivables.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f60_biotech_f60_cash_conversion_cycle_lag_147d_base_v147_signal(receivables, closeadj):
    result = receivables.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f60_biotech_f60_cash_conversion_cycle_lag_148d_base_v148_signal(receivables, closeadj):
    result = receivables.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f60_biotech_f60_cash_conversion_cycle_lag_149d_base_v149_signal(receivables, closeadj):
    result = receivables.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f60_biotech_f60_cash_conversion_cycle_lag_150d_base_v150_signal(receivables, closeadj):
    result = receivables.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

