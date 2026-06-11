
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling autocorr of ebit
def gm_f54_biotech_f54_return_on_invested_capital_autocorr_21d_base_v076_signal(ebit):
    result = _autocorr(ebit, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of ebit
def gm_f54_biotech_f54_return_on_invested_capital_autocorr_63d_base_v077_signal(ebit):
    result = _autocorr(ebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of ebit
def gm_f54_biotech_f54_return_on_invested_capital_autocorr_126d_base_v078_signal(ebit):
    result = _autocorr(ebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of ebit
def gm_f54_biotech_f54_return_on_invested_capital_autocorr_252d_base_v079_signal(ebit):
    result = _autocorr(ebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of ebit
def gm_f54_biotech_f54_return_on_invested_capital_autocorr_504d_base_v080_signal(ebit):
    result = _autocorr(ebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_std_21d_base_v081_signal(ebit, closeadj):
    result = _std(ebit, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_std_63d_base_v082_signal(ebit, closeadj):
    result = _std(ebit, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_std_126d_base_v083_signal(ebit, closeadj):
    result = _std(ebit, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_std_252d_base_v084_signal(ebit, closeadj):
    result = _std(ebit, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_std_504d_base_v085_signal(ebit, closeadj):
    result = _std(ebit, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of ebit
def gm_f54_biotech_f54_return_on_invested_capital_logdiff_21d_base_v086_signal(ebit, closeadj):
    result = _diff(_log(ebit), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of ebit
def gm_f54_biotech_f54_return_on_invested_capital_logdiff_63d_base_v087_signal(ebit, closeadj):
    result = _diff(_log(ebit), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of ebit
def gm_f54_biotech_f54_return_on_invested_capital_logdiff_126d_base_v088_signal(ebit, closeadj):
    result = _diff(_log(ebit), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of ebit
def gm_f54_biotech_f54_return_on_invested_capital_logdiff_252d_base_v089_signal(ebit, closeadj):
    result = _diff(_log(ebit), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of ebit
def gm_f54_biotech_f54_return_on_invested_capital_logdiff_504d_base_v090_signal(ebit, closeadj):
    result = _diff(_log(ebit), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_cv_21d_base_v091_signal(ebit):
    m = _mean(ebit, 21)
    s = _std(ebit, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_cv_63d_base_v092_signal(ebit):
    m = _mean(ebit, 63)
    s = _std(ebit, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_cv_126d_base_v093_signal(ebit):
    m = _mean(ebit, 126)
    s = _std(ebit, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_cv_252d_base_v094_signal(ebit):
    m = _mean(ebit, 252)
    s = _std(ebit, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_cv_504d_base_v095_signal(ebit):
    m = _mean(ebit, 504)
    s = _std(ebit, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of ebit
def gm_f54_biotech_f54_return_on_invested_capital_range_21d_base_v096_signal(ebit):
    hi = ebit.rolling(21).max()
    lo = ebit.rolling(21).min()
    result = _safe_div(hi - lo, _mean(ebit, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of ebit
def gm_f54_biotech_f54_return_on_invested_capital_range_63d_base_v097_signal(ebit):
    hi = ebit.rolling(63).max()
    lo = ebit.rolling(63).min()
    result = _safe_div(hi - lo, _mean(ebit, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of ebit
def gm_f54_biotech_f54_return_on_invested_capital_range_126d_base_v098_signal(ebit):
    hi = ebit.rolling(126).max()
    lo = ebit.rolling(126).min()
    result = _safe_div(hi - lo, _mean(ebit, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of ebit
def gm_f54_biotech_f54_return_on_invested_capital_range_252d_base_v099_signal(ebit):
    hi = ebit.rolling(252).max()
    lo = ebit.rolling(252).min()
    result = _safe_div(hi - lo, _mean(ebit, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of ebit
def gm_f54_biotech_f54_return_on_invested_capital_range_504d_base_v100_signal(ebit):
    hi = ebit.rolling(504).max()
    lo = ebit.rolling(504).min()
    result = _safe_div(hi - lo, _mean(ebit, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_mad_21d_base_v101_signal(ebit, closeadj):
    m = _mean(ebit, 21)
    result = _mean((ebit - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_mad_63d_base_v102_signal(ebit, closeadj):
    m = _mean(ebit, 63)
    result = _mean((ebit - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_mad_126d_base_v103_signal(ebit, closeadj):
    m = _mean(ebit, 126)
    result = _mean((ebit - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_mad_252d_base_v104_signal(ebit, closeadj):
    m = _mean(ebit, 252)
    result = _mean((ebit - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of ebit
def gm_f54_biotech_f54_return_on_invested_capital_mad_504d_base_v105_signal(ebit, closeadj):
    m = _mean(ebit, 504)
    result = _mean((ebit - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_21d_base_v106_signal(ebit, closeadj):
    result = ebit.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_63d_base_v107_signal(ebit, closeadj):
    result = ebit.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_126d_base_v108_signal(ebit, closeadj):
    result = ebit.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_252d_base_v109_signal(ebit, closeadj):
    result = ebit.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_504d_base_v110_signal(ebit, closeadj):
    result = ebit.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_std_21d_base_v111_signal(ebit, closeadj):
    result = ebit.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_std_63d_base_v112_signal(ebit, closeadj):
    result = ebit.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_std_126d_base_v113_signal(ebit, closeadj):
    result = ebit.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_std_252d_base_v114_signal(ebit, closeadj):
    result = ebit.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of ebit
def gm_f54_biotech_f54_return_on_invested_capital_ewm_std_504d_base_v115_signal(ebit, closeadj):
    result = ebit.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of ebit
def gm_f54_biotech_f54_return_on_invested_capital_med_21d_base_v116_signal(ebit, closeadj):
    result = ebit.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ebit
def gm_f54_biotech_f54_return_on_invested_capital_med_63d_base_v117_signal(ebit, closeadj):
    result = ebit.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of ebit
def gm_f54_biotech_f54_return_on_invested_capital_med_126d_base_v118_signal(ebit, closeadj):
    result = ebit.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ebit
def gm_f54_biotech_f54_return_on_invested_capital_med_252d_base_v119_signal(ebit, closeadj):
    result = ebit.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ebit
def gm_f54_biotech_f54_return_on_invested_capital_med_504d_base_v120_signal(ebit, closeadj):
    result = ebit.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sum_21d_base_v121_signal(ebit, closeadj):
    result = ebit.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sum_63d_base_v122_signal(ebit, closeadj):
    result = ebit.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sum_126d_base_v123_signal(ebit, closeadj):
    result = ebit.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sum_252d_base_v124_signal(ebit, closeadj):
    result = ebit.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sum_504d_base_v125_signal(ebit, closeadj):
    result = ebit.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sign_21d_base_v126_signal(ebit):
    result = _mean(np.sign(_diff(ebit, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sign_63d_base_v127_signal(ebit):
    result = _mean(np.sign(_diff(ebit, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sign_126d_base_v128_signal(ebit):
    result = _mean(np.sign(_diff(ebit, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sign_252d_base_v129_signal(ebit):
    result = _mean(np.sign(_diff(ebit, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of ebit
def gm_f54_biotech_f54_return_on_invested_capital_sign_504d_base_v130_signal(ebit):
    result = _mean(np.sign(_diff(ebit, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of ebit
def gm_f54_biotech_f54_return_on_invested_capital_peak_freq_63d_base_v131_signal(ebit):
    is_peak = (ebit == ebit.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of ebit
def gm_f54_biotech_f54_return_on_invested_capital_trough_freq_63d_base_v132_signal(ebit):
    is_trough = (ebit == ebit.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of ebit
def gm_f54_biotech_f54_return_on_invested_capital_peak_freq_252d_base_v133_signal(ebit):
    is_peak = (ebit == ebit.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of ebit
def gm_f54_biotech_f54_return_on_invested_capital_trough_freq_252d_base_v134_signal(ebit):
    is_trough = (ebit == ebit.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f54_biotech_f54_return_on_invested_capital_lag_135d_base_v135_signal(ebit, closeadj):
    result = ebit.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f54_biotech_f54_return_on_invested_capital_lag_136d_base_v136_signal(ebit, closeadj):
    result = ebit.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f54_biotech_f54_return_on_invested_capital_lag_137d_base_v137_signal(ebit, closeadj):
    result = ebit.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f54_biotech_f54_return_on_invested_capital_lag_138d_base_v138_signal(ebit, closeadj):
    result = ebit.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f54_biotech_f54_return_on_invested_capital_lag_139d_base_v139_signal(ebit, closeadj):
    result = ebit.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f54_biotech_f54_return_on_invested_capital_lag_140d_base_v140_signal(ebit, closeadj):
    result = ebit.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f54_biotech_f54_return_on_invested_capital_lag_141d_base_v141_signal(ebit, closeadj):
    result = ebit.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f54_biotech_f54_return_on_invested_capital_lag_142d_base_v142_signal(ebit, closeadj):
    result = ebit.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f54_biotech_f54_return_on_invested_capital_lag_143d_base_v143_signal(ebit, closeadj):
    result = ebit.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f54_biotech_f54_return_on_invested_capital_lag_144d_base_v144_signal(ebit, closeadj):
    result = ebit.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f54_biotech_f54_return_on_invested_capital_lag_145d_base_v145_signal(ebit, closeadj):
    result = ebit.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f54_biotech_f54_return_on_invested_capital_lag_146d_base_v146_signal(ebit, closeadj):
    result = ebit.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f54_biotech_f54_return_on_invested_capital_lag_147d_base_v147_signal(ebit, closeadj):
    result = ebit.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f54_biotech_f54_return_on_invested_capital_lag_148d_base_v148_signal(ebit, closeadj):
    result = ebit.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f54_biotech_f54_return_on_invested_capital_lag_149d_base_v149_signal(ebit, closeadj):
    result = ebit.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f54_biotech_f54_return_on_invested_capital_lag_150d_base_v150_signal(ebit, closeadj):
    result = ebit.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

