
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_std_21d_base_v076_signal(netinc, closeadj):
    result = _std(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_std_63d_base_v077_signal(netinc, closeadj):
    result = _std(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_std_126d_base_v078_signal(netinc, closeadj):
    result = _std(netinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_std_252d_base_v079_signal(netinc, closeadj):
    result = _std(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_std_504d_base_v080_signal(netinc, closeadj):
    result = _std(netinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_logdiff_21d_base_v081_signal(netinc, closeadj):
    result = _diff(_log(netinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_logdiff_63d_base_v082_signal(netinc, closeadj):
    result = _diff(_log(netinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_logdiff_126d_base_v083_signal(netinc, closeadj):
    result = _diff(_log(netinc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_logdiff_252d_base_v084_signal(netinc, closeadj):
    result = _diff(_log(netinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_logdiff_504d_base_v085_signal(netinc, closeadj):
    result = _diff(_log(netinc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_cv_21d_base_v086_signal(netinc):
    m = _mean(netinc, 21)
    s = _std(netinc, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_cv_63d_base_v087_signal(netinc):
    m = _mean(netinc, 63)
    s = _std(netinc, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_cv_126d_base_v088_signal(netinc):
    m = _mean(netinc, 126)
    s = _std(netinc, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_cv_252d_base_v089_signal(netinc):
    m = _mean(netinc, 252)
    s = _std(netinc, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_cv_504d_base_v090_signal(netinc):
    m = _mean(netinc, 504)
    s = _std(netinc, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_range_21d_base_v091_signal(netinc):
    hi = netinc.rolling(21).max()
    lo = netinc.rolling(21).min()
    result = _safe_div(hi - lo, _mean(netinc, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_range_63d_base_v092_signal(netinc):
    hi = netinc.rolling(63).max()
    lo = netinc.rolling(63).min()
    result = _safe_div(hi - lo, _mean(netinc, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_range_126d_base_v093_signal(netinc):
    hi = netinc.rolling(126).max()
    lo = netinc.rolling(126).min()
    result = _safe_div(hi - lo, _mean(netinc, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_range_252d_base_v094_signal(netinc):
    hi = netinc.rolling(252).max()
    lo = netinc.rolling(252).min()
    result = _safe_div(hi - lo, _mean(netinc, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_range_504d_base_v095_signal(netinc):
    hi = netinc.rolling(504).max()
    lo = netinc.rolling(504).min()
    result = _safe_div(hi - lo, _mean(netinc, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_mad_21d_base_v096_signal(netinc, closeadj):
    m = _mean(netinc, 21)
    result = _mean((netinc - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_mad_63d_base_v097_signal(netinc, closeadj):
    m = _mean(netinc, 63)
    result = _mean((netinc - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_mad_126d_base_v098_signal(netinc, closeadj):
    m = _mean(netinc, 126)
    result = _mean((netinc - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_mad_252d_base_v099_signal(netinc, closeadj):
    m = _mean(netinc, 252)
    result = _mean((netinc - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_mad_504d_base_v100_signal(netinc, closeadj):
    m = _mean(netinc, 504)
    result = _mean((netinc - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_21d_base_v101_signal(netinc, closeadj):
    result = netinc.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_63d_base_v102_signal(netinc, closeadj):
    result = netinc.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_126d_base_v103_signal(netinc, closeadj):
    result = netinc.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_252d_base_v104_signal(netinc, closeadj):
    result = netinc.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_504d_base_v105_signal(netinc, closeadj):
    result = netinc.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_std_21d_base_v106_signal(netinc, closeadj):
    result = netinc.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_std_63d_base_v107_signal(netinc, closeadj):
    result = netinc.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_std_126d_base_v108_signal(netinc, closeadj):
    result = netinc.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_std_252d_base_v109_signal(netinc, closeadj):
    result = netinc.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_ewm_std_504d_base_v110_signal(netinc, closeadj):
    result = netinc.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_med_21d_base_v111_signal(netinc, closeadj):
    result = netinc.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_med_63d_base_v112_signal(netinc, closeadj):
    result = netinc.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_med_126d_base_v113_signal(netinc, closeadj):
    result = netinc.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_med_252d_base_v114_signal(netinc, closeadj):
    result = netinc.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_med_504d_base_v115_signal(netinc, closeadj):
    result = netinc.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sum_21d_base_v116_signal(netinc, closeadj):
    result = netinc.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sum_63d_base_v117_signal(netinc, closeadj):
    result = netinc.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sum_126d_base_v118_signal(netinc, closeadj):
    result = netinc.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sum_252d_base_v119_signal(netinc, closeadj):
    result = netinc.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sum_504d_base_v120_signal(netinc, closeadj):
    result = netinc.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sign_21d_base_v121_signal(netinc):
    result = _mean(np.sign(_diff(netinc, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sign_63d_base_v122_signal(netinc):
    result = _mean(np.sign(_diff(netinc, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sign_126d_base_v123_signal(netinc):
    result = _mean(np.sign(_diff(netinc, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sign_252d_base_v124_signal(netinc):
    result = _mean(np.sign(_diff(netinc, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_sign_504d_base_v125_signal(netinc):
    result = _mean(np.sign(_diff(netinc, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_peak_freq_63d_base_v126_signal(netinc):
    is_peak = (netinc == netinc.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_trough_freq_63d_base_v127_signal(netinc):
    is_trough = (netinc == netinc.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_peak_freq_252d_base_v128_signal(netinc):
    is_peak = (netinc == netinc.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of netinc
def gm_f53_biotech_f53_return_on_equity_profitability_trough_freq_252d_base_v129_signal(netinc):
    is_trough = (netinc == netinc.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f53_biotech_f53_return_on_equity_profitability_lag_130d_base_v130_signal(netinc, closeadj):
    result = netinc.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f53_biotech_f53_return_on_equity_profitability_lag_131d_base_v131_signal(netinc, closeadj):
    result = netinc.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f53_biotech_f53_return_on_equity_profitability_lag_132d_base_v132_signal(netinc, closeadj):
    result = netinc.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f53_biotech_f53_return_on_equity_profitability_lag_133d_base_v133_signal(netinc, closeadj):
    result = netinc.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f53_biotech_f53_return_on_equity_profitability_lag_134d_base_v134_signal(netinc, closeadj):
    result = netinc.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f53_biotech_f53_return_on_equity_profitability_lag_135d_base_v135_signal(netinc, closeadj):
    result = netinc.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f53_biotech_f53_return_on_equity_profitability_lag_136d_base_v136_signal(netinc, closeadj):
    result = netinc.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f53_biotech_f53_return_on_equity_profitability_lag_137d_base_v137_signal(netinc, closeadj):
    result = netinc.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f53_biotech_f53_return_on_equity_profitability_lag_138d_base_v138_signal(netinc, closeadj):
    result = netinc.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f53_biotech_f53_return_on_equity_profitability_lag_139d_base_v139_signal(netinc, closeadj):
    result = netinc.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f53_biotech_f53_return_on_equity_profitability_lag_140d_base_v140_signal(netinc, closeadj):
    result = netinc.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f53_biotech_f53_return_on_equity_profitability_lag_141d_base_v141_signal(netinc, closeadj):
    result = netinc.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f53_biotech_f53_return_on_equity_profitability_lag_142d_base_v142_signal(netinc, closeadj):
    result = netinc.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f53_biotech_f53_return_on_equity_profitability_lag_143d_base_v143_signal(netinc, closeadj):
    result = netinc.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f53_biotech_f53_return_on_equity_profitability_lag_144d_base_v144_signal(netinc, closeadj):
    result = netinc.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f53_biotech_f53_return_on_equity_profitability_lag_145d_base_v145_signal(netinc, closeadj):
    result = netinc.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f53_biotech_f53_return_on_equity_profitability_lag_146d_base_v146_signal(netinc, closeadj):
    result = netinc.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f53_biotech_f53_return_on_equity_profitability_lag_147d_base_v147_signal(netinc, closeadj):
    result = netinc.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f53_biotech_f53_return_on_equity_profitability_lag_148d_base_v148_signal(netinc, closeadj):
    result = netinc.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f53_biotech_f53_return_on_equity_profitability_lag_149d_base_v149_signal(netinc, closeadj):
    result = netinc.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f53_biotech_f53_return_on_equity_profitability_lag_150d_base_v150_signal(netinc, closeadj):
    result = netinc.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

