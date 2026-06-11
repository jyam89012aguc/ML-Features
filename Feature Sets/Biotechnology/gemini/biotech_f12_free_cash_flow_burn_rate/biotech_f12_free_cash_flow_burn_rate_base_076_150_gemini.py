
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_logdiff_21d_base_v076_signal(fcf, closeadj):
    result = _diff(_log(fcf), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_logdiff_63d_base_v077_signal(fcf, closeadj):
    result = _diff(_log(fcf), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_logdiff_126d_base_v078_signal(fcf, closeadj):
    result = _diff(_log(fcf), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_logdiff_252d_base_v079_signal(fcf, closeadj):
    result = _diff(_log(fcf), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_logdiff_504d_base_v080_signal(fcf, closeadj):
    result = _diff(_log(fcf), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_cv_21d_base_v081_signal(fcf):
    m = _mean(fcf, 21)
    s = _std(fcf, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_cv_63d_base_v082_signal(fcf):
    m = _mean(fcf, 63)
    s = _std(fcf, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_cv_126d_base_v083_signal(fcf):
    m = _mean(fcf, 126)
    s = _std(fcf, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_cv_252d_base_v084_signal(fcf):
    m = _mean(fcf, 252)
    s = _std(fcf, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_cv_504d_base_v085_signal(fcf):
    m = _mean(fcf, 504)
    s = _std(fcf, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_range_21d_base_v086_signal(fcf):
    hi = fcf.rolling(21).max()
    lo = fcf.rolling(21).min()
    result = _safe_div(hi - lo, _mean(fcf, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_range_63d_base_v087_signal(fcf):
    hi = fcf.rolling(63).max()
    lo = fcf.rolling(63).min()
    result = _safe_div(hi - lo, _mean(fcf, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_range_126d_base_v088_signal(fcf):
    hi = fcf.rolling(126).max()
    lo = fcf.rolling(126).min()
    result = _safe_div(hi - lo, _mean(fcf, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_range_252d_base_v089_signal(fcf):
    hi = fcf.rolling(252).max()
    lo = fcf.rolling(252).min()
    result = _safe_div(hi - lo, _mean(fcf, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_range_504d_base_v090_signal(fcf):
    hi = fcf.rolling(504).max()
    lo = fcf.rolling(504).min()
    result = _safe_div(hi - lo, _mean(fcf, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mad_21d_base_v091_signal(fcf, closeadj):
    m = _mean(fcf, 21)
    result = _mean((fcf - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mad_63d_base_v092_signal(fcf, closeadj):
    m = _mean(fcf, 63)
    result = _mean((fcf - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mad_126d_base_v093_signal(fcf, closeadj):
    m = _mean(fcf, 126)
    result = _mean((fcf - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mad_252d_base_v094_signal(fcf, closeadj):
    m = _mean(fcf, 252)
    result = _mean((fcf - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_mad_504d_base_v095_signal(fcf, closeadj):
    m = _mean(fcf, 504)
    result = _mean((fcf - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_21d_base_v096_signal(fcf, closeadj):
    result = fcf.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_63d_base_v097_signal(fcf, closeadj):
    result = fcf.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_126d_base_v098_signal(fcf, closeadj):
    result = fcf.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_252d_base_v099_signal(fcf, closeadj):
    result = fcf.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_504d_base_v100_signal(fcf, closeadj):
    result = fcf.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_std_21d_base_v101_signal(fcf, closeadj):
    result = fcf.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_std_63d_base_v102_signal(fcf, closeadj):
    result = fcf.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_std_126d_base_v103_signal(fcf, closeadj):
    result = fcf.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_std_252d_base_v104_signal(fcf, closeadj):
    result = fcf.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_ewm_std_504d_base_v105_signal(fcf, closeadj):
    result = fcf.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_med_21d_base_v106_signal(fcf, closeadj):
    result = fcf.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_med_63d_base_v107_signal(fcf, closeadj):
    result = fcf.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_med_126d_base_v108_signal(fcf, closeadj):
    result = fcf.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_med_252d_base_v109_signal(fcf, closeadj):
    result = fcf.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_med_504d_base_v110_signal(fcf, closeadj):
    result = fcf.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sum_21d_base_v111_signal(fcf, closeadj):
    result = fcf.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sum_63d_base_v112_signal(fcf, closeadj):
    result = fcf.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sum_126d_base_v113_signal(fcf, closeadj):
    result = fcf.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sum_252d_base_v114_signal(fcf, closeadj):
    result = fcf.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sum_504d_base_v115_signal(fcf, closeadj):
    result = fcf.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sign_21d_base_v116_signal(fcf):
    result = _mean(np.sign(_diff(fcf, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sign_63d_base_v117_signal(fcf):
    result = _mean(np.sign(_diff(fcf, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sign_126d_base_v118_signal(fcf):
    result = _mean(np.sign(_diff(fcf, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sign_252d_base_v119_signal(fcf):
    result = _mean(np.sign(_diff(fcf, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_sign_504d_base_v120_signal(fcf):
    result = _mean(np.sign(_diff(fcf, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_peak_freq_63d_base_v121_signal(fcf):
    is_peak = (fcf == fcf.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_trough_freq_63d_base_v122_signal(fcf):
    is_trough = (fcf == fcf.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_peak_freq_252d_base_v123_signal(fcf):
    is_peak = (fcf == fcf.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of fcf
def gm_f12_biotech_f12_free_cash_flow_burn_rate_trough_freq_252d_base_v124_signal(fcf):
    is_trough = (fcf == fcf.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_125d_base_v125_signal(fcf, closeadj):
    result = fcf.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_126d_base_v126_signal(fcf, closeadj):
    result = fcf.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_127d_base_v127_signal(fcf, closeadj):
    result = fcf.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_128d_base_v128_signal(fcf, closeadj):
    result = fcf.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_129d_base_v129_signal(fcf, closeadj):
    result = fcf.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_130d_base_v130_signal(fcf, closeadj):
    result = fcf.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_131d_base_v131_signal(fcf, closeadj):
    result = fcf.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_132d_base_v132_signal(fcf, closeadj):
    result = fcf.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_133d_base_v133_signal(fcf, closeadj):
    result = fcf.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_134d_base_v134_signal(fcf, closeadj):
    result = fcf.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_135d_base_v135_signal(fcf, closeadj):
    result = fcf.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_136d_base_v136_signal(fcf, closeadj):
    result = fcf.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_137d_base_v137_signal(fcf, closeadj):
    result = fcf.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_138d_base_v138_signal(fcf, closeadj):
    result = fcf.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_139d_base_v139_signal(fcf, closeadj):
    result = fcf.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_140d_base_v140_signal(fcf, closeadj):
    result = fcf.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_141d_base_v141_signal(fcf, closeadj):
    result = fcf.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_142d_base_v142_signal(fcf, closeadj):
    result = fcf.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_143d_base_v143_signal(fcf, closeadj):
    result = fcf.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_144d_base_v144_signal(fcf, closeadj):
    result = fcf.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_145d_base_v145_signal(fcf, closeadj):
    result = fcf.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_146d_base_v146_signal(fcf, closeadj):
    result = fcf.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_147d_base_v147_signal(fcf, closeadj):
    result = fcf.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_148d_base_v148_signal(fcf, closeadj):
    result = fcf.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_149d_base_v149_signal(fcf, closeadj):
    result = fcf.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f12_biotech_f12_free_cash_flow_burn_rate_lag_150d_base_v150_signal(fcf, closeadj):
    result = fcf.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

