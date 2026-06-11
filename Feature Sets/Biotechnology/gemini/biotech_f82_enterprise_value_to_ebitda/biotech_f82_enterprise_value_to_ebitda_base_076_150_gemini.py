
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_std_21d_base_v076_signal(ev, closeadj):
    result = _std(ev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_std_63d_base_v077_signal(ev, closeadj):
    result = _std(ev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_std_126d_base_v078_signal(ev, closeadj):
    result = _std(ev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_std_252d_base_v079_signal(ev, closeadj):
    result = _std(ev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_std_504d_base_v080_signal(ev, closeadj):
    result = _std(ev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_logdiff_21d_base_v081_signal(ev, closeadj):
    result = _diff(_log(ev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_logdiff_63d_base_v082_signal(ev, closeadj):
    result = _diff(_log(ev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_logdiff_126d_base_v083_signal(ev, closeadj):
    result = _diff(_log(ev), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_logdiff_252d_base_v084_signal(ev, closeadj):
    result = _diff(_log(ev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_logdiff_504d_base_v085_signal(ev, closeadj):
    result = _diff(_log(ev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_cv_21d_base_v086_signal(ev):
    m = _mean(ev, 21)
    s = _std(ev, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_cv_63d_base_v087_signal(ev):
    m = _mean(ev, 63)
    s = _std(ev, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_cv_126d_base_v088_signal(ev):
    m = _mean(ev, 126)
    s = _std(ev, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_cv_252d_base_v089_signal(ev):
    m = _mean(ev, 252)
    s = _std(ev, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_cv_504d_base_v090_signal(ev):
    m = _mean(ev, 504)
    s = _std(ev, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_range_21d_base_v091_signal(ev):
    hi = ev.rolling(21).max()
    lo = ev.rolling(21).min()
    result = _safe_div(hi - lo, _mean(ev, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_range_63d_base_v092_signal(ev):
    hi = ev.rolling(63).max()
    lo = ev.rolling(63).min()
    result = _safe_div(hi - lo, _mean(ev, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_range_126d_base_v093_signal(ev):
    hi = ev.rolling(126).max()
    lo = ev.rolling(126).min()
    result = _safe_div(hi - lo, _mean(ev, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_range_252d_base_v094_signal(ev):
    hi = ev.rolling(252).max()
    lo = ev.rolling(252).min()
    result = _safe_div(hi - lo, _mean(ev, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_range_504d_base_v095_signal(ev):
    hi = ev.rolling(504).max()
    lo = ev.rolling(504).min()
    result = _safe_div(hi - lo, _mean(ev, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mad_21d_base_v096_signal(ev, closeadj):
    m = _mean(ev, 21)
    result = _mean((ev - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mad_63d_base_v097_signal(ev, closeadj):
    m = _mean(ev, 63)
    result = _mean((ev - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mad_126d_base_v098_signal(ev, closeadj):
    m = _mean(ev, 126)
    result = _mean((ev - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mad_252d_base_v099_signal(ev, closeadj):
    m = _mean(ev, 252)
    result = _mean((ev - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_mad_504d_base_v100_signal(ev, closeadj):
    m = _mean(ev, 504)
    result = _mean((ev - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_21d_base_v101_signal(ev, closeadj):
    result = ev.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_63d_base_v102_signal(ev, closeadj):
    result = ev.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_126d_base_v103_signal(ev, closeadj):
    result = ev.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_252d_base_v104_signal(ev, closeadj):
    result = ev.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_504d_base_v105_signal(ev, closeadj):
    result = ev.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_std_21d_base_v106_signal(ev, closeadj):
    result = ev.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_std_63d_base_v107_signal(ev, closeadj):
    result = ev.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_std_126d_base_v108_signal(ev, closeadj):
    result = ev.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_std_252d_base_v109_signal(ev, closeadj):
    result = ev.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_ewm_std_504d_base_v110_signal(ev, closeadj):
    result = ev.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_med_21d_base_v111_signal(ev, closeadj):
    result = ev.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_med_63d_base_v112_signal(ev, closeadj):
    result = ev.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_med_126d_base_v113_signal(ev, closeadj):
    result = ev.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_med_252d_base_v114_signal(ev, closeadj):
    result = ev.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_med_504d_base_v115_signal(ev, closeadj):
    result = ev.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sum_21d_base_v116_signal(ev, closeadj):
    result = ev.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sum_63d_base_v117_signal(ev, closeadj):
    result = ev.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sum_126d_base_v118_signal(ev, closeadj):
    result = ev.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sum_252d_base_v119_signal(ev, closeadj):
    result = ev.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sum_504d_base_v120_signal(ev, closeadj):
    result = ev.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sign_21d_base_v121_signal(ev):
    result = _mean(np.sign(_diff(ev, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sign_63d_base_v122_signal(ev):
    result = _mean(np.sign(_diff(ev, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sign_126d_base_v123_signal(ev):
    result = _mean(np.sign(_diff(ev, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sign_252d_base_v124_signal(ev):
    result = _mean(np.sign(_diff(ev, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_sign_504d_base_v125_signal(ev):
    result = _mean(np.sign(_diff(ev, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_peak_freq_63d_base_v126_signal(ev):
    is_peak = (ev == ev.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_trough_freq_63d_base_v127_signal(ev):
    is_trough = (ev == ev.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_peak_freq_252d_base_v128_signal(ev):
    is_peak = (ev == ev.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of ev
def gm_f82_biotech_f82_enterprise_value_to_ebitda_trough_freq_252d_base_v129_signal(ev):
    is_trough = (ev == ev.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_130d_base_v130_signal(ev, closeadj):
    result = ev.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_131d_base_v131_signal(ev, closeadj):
    result = ev.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_132d_base_v132_signal(ev, closeadj):
    result = ev.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_133d_base_v133_signal(ev, closeadj):
    result = ev.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_134d_base_v134_signal(ev, closeadj):
    result = ev.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_135d_base_v135_signal(ev, closeadj):
    result = ev.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_136d_base_v136_signal(ev, closeadj):
    result = ev.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_137d_base_v137_signal(ev, closeadj):
    result = ev.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_138d_base_v138_signal(ev, closeadj):
    result = ev.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_139d_base_v139_signal(ev, closeadj):
    result = ev.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_140d_base_v140_signal(ev, closeadj):
    result = ev.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_141d_base_v141_signal(ev, closeadj):
    result = ev.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_142d_base_v142_signal(ev, closeadj):
    result = ev.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_143d_base_v143_signal(ev, closeadj):
    result = ev.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_144d_base_v144_signal(ev, closeadj):
    result = ev.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_145d_base_v145_signal(ev, closeadj):
    result = ev.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_146d_base_v146_signal(ev, closeadj):
    result = ev.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_147d_base_v147_signal(ev, closeadj):
    result = ev.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_148d_base_v148_signal(ev, closeadj):
    result = ev.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_149d_base_v149_signal(ev, closeadj):
    result = ev.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f82_biotech_f82_enterprise_value_to_ebitda_lag_150d_base_v150_signal(ev, closeadj):
    result = ev.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

