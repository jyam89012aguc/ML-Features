
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d log-diff of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_logdiff_21d_base_v076_signal(invcap, closeadj):
    result = _diff(_log(invcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_logdiff_63d_base_v077_signal(invcap, closeadj):
    result = _diff(_log(invcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_logdiff_126d_base_v078_signal(invcap, closeadj):
    result = _diff(_log(invcap), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_logdiff_252d_base_v079_signal(invcap, closeadj):
    result = _diff(_log(invcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_logdiff_504d_base_v080_signal(invcap, closeadj):
    result = _diff(_log(invcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_cv_21d_base_v081_signal(invcap):
    m = _mean(invcap, 21)
    s = _std(invcap, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_cv_63d_base_v082_signal(invcap):
    m = _mean(invcap, 63)
    s = _std(invcap, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_cv_126d_base_v083_signal(invcap):
    m = _mean(invcap, 126)
    s = _std(invcap, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_cv_252d_base_v084_signal(invcap):
    m = _mean(invcap, 252)
    s = _std(invcap, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_cv_504d_base_v085_signal(invcap):
    m = _mean(invcap, 504)
    s = _std(invcap, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_range_21d_base_v086_signal(invcap):
    hi = invcap.rolling(21).max()
    lo = invcap.rolling(21).min()
    result = _safe_div(hi - lo, _mean(invcap, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_range_63d_base_v087_signal(invcap):
    hi = invcap.rolling(63).max()
    lo = invcap.rolling(63).min()
    result = _safe_div(hi - lo, _mean(invcap, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_range_126d_base_v088_signal(invcap):
    hi = invcap.rolling(126).max()
    lo = invcap.rolling(126).min()
    result = _safe_div(hi - lo, _mean(invcap, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_range_252d_base_v089_signal(invcap):
    hi = invcap.rolling(252).max()
    lo = invcap.rolling(252).min()
    result = _safe_div(hi - lo, _mean(invcap, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_range_504d_base_v090_signal(invcap):
    hi = invcap.rolling(504).max()
    lo = invcap.rolling(504).min()
    result = _safe_div(hi - lo, _mean(invcap, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mad_21d_base_v091_signal(invcap, closeadj):
    m = _mean(invcap, 21)
    result = _mean((invcap - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mad_63d_base_v092_signal(invcap, closeadj):
    m = _mean(invcap, 63)
    result = _mean((invcap - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mad_126d_base_v093_signal(invcap, closeadj):
    m = _mean(invcap, 126)
    result = _mean((invcap - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mad_252d_base_v094_signal(invcap, closeadj):
    m = _mean(invcap, 252)
    result = _mean((invcap - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_mad_504d_base_v095_signal(invcap, closeadj):
    m = _mean(invcap, 504)
    result = _mean((invcap - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_21d_base_v096_signal(invcap, closeadj):
    result = invcap.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_63d_base_v097_signal(invcap, closeadj):
    result = invcap.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_126d_base_v098_signal(invcap, closeadj):
    result = invcap.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_252d_base_v099_signal(invcap, closeadj):
    result = invcap.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_504d_base_v100_signal(invcap, closeadj):
    result = invcap.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_std_21d_base_v101_signal(invcap, closeadj):
    result = invcap.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_std_63d_base_v102_signal(invcap, closeadj):
    result = invcap.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_std_126d_base_v103_signal(invcap, closeadj):
    result = invcap.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_std_252d_base_v104_signal(invcap, closeadj):
    result = invcap.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_ewm_std_504d_base_v105_signal(invcap, closeadj):
    result = invcap.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_med_21d_base_v106_signal(invcap, closeadj):
    result = invcap.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_med_63d_base_v107_signal(invcap, closeadj):
    result = invcap.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_med_126d_base_v108_signal(invcap, closeadj):
    result = invcap.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_med_252d_base_v109_signal(invcap, closeadj):
    result = invcap.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_med_504d_base_v110_signal(invcap, closeadj):
    result = invcap.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sum_21d_base_v111_signal(invcap, closeadj):
    result = invcap.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sum_63d_base_v112_signal(invcap, closeadj):
    result = invcap.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sum_126d_base_v113_signal(invcap, closeadj):
    result = invcap.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sum_252d_base_v114_signal(invcap, closeadj):
    result = invcap.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sum_504d_base_v115_signal(invcap, closeadj):
    result = invcap.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sign_21d_base_v116_signal(invcap):
    result = _mean(np.sign(_diff(invcap, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sign_63d_base_v117_signal(invcap):
    result = _mean(np.sign(_diff(invcap, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sign_126d_base_v118_signal(invcap):
    result = _mean(np.sign(_diff(invcap, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sign_252d_base_v119_signal(invcap):
    result = _mean(np.sign(_diff(invcap, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_sign_504d_base_v120_signal(invcap):
    result = _mean(np.sign(_diff(invcap, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_peak_freq_63d_base_v121_signal(invcap):
    is_peak = (invcap == invcap.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_trough_freq_63d_base_v122_signal(invcap):
    is_trough = (invcap == invcap.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_peak_freq_252d_base_v123_signal(invcap):
    is_peak = (invcap == invcap.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of invcap
def gm_f55_biotech_f55_invested_capital_growth_rate_trough_freq_252d_base_v124_signal(invcap):
    is_trough = (invcap == invcap.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 125
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_125d_base_v125_signal(invcap, closeadj):
    result = invcap.shift(125) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 126
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_126d_base_v126_signal(invcap, closeadj):
    result = invcap.shift(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 127
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_127d_base_v127_signal(invcap, closeadj):
    result = invcap.shift(127) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 128
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_128d_base_v128_signal(invcap, closeadj):
    result = invcap.shift(128) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 129
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_129d_base_v129_signal(invcap, closeadj):
    result = invcap.shift(129) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_130d_base_v130_signal(invcap, closeadj):
    result = invcap.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_131d_base_v131_signal(invcap, closeadj):
    result = invcap.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_132d_base_v132_signal(invcap, closeadj):
    result = invcap.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_133d_base_v133_signal(invcap, closeadj):
    result = invcap.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_134d_base_v134_signal(invcap, closeadj):
    result = invcap.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_135d_base_v135_signal(invcap, closeadj):
    result = invcap.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_136d_base_v136_signal(invcap, closeadj):
    result = invcap.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_137d_base_v137_signal(invcap, closeadj):
    result = invcap.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_138d_base_v138_signal(invcap, closeadj):
    result = invcap.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_139d_base_v139_signal(invcap, closeadj):
    result = invcap.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_140d_base_v140_signal(invcap, closeadj):
    result = invcap.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_141d_base_v141_signal(invcap, closeadj):
    result = invcap.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_142d_base_v142_signal(invcap, closeadj):
    result = invcap.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_143d_base_v143_signal(invcap, closeadj):
    result = invcap.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_144d_base_v144_signal(invcap, closeadj):
    result = invcap.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_145d_base_v145_signal(invcap, closeadj):
    result = invcap.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_146d_base_v146_signal(invcap, closeadj):
    result = invcap.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_147d_base_v147_signal(invcap, closeadj):
    result = invcap.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_148d_base_v148_signal(invcap, closeadj):
    result = invcap.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_149d_base_v149_signal(invcap, closeadj):
    result = invcap.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f55_biotech_f55_invested_capital_growth_rate_lag_150d_base_v150_signal(invcap, closeadj):
    result = invcap.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

