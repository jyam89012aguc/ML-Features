
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_std_21d_base_v076_signal(marketcap, closeadj):
    result = _std(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_std_63d_base_v077_signal(marketcap, closeadj):
    result = _std(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_std_126d_base_v078_signal(marketcap, closeadj):
    result = _std(marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_std_252d_base_v079_signal(marketcap, closeadj):
    result = _std(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_std_504d_base_v080_signal(marketcap, closeadj):
    result = _std(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_logdiff_21d_base_v081_signal(marketcap, closeadj):
    result = _diff(_log(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_logdiff_63d_base_v082_signal(marketcap, closeadj):
    result = _diff(_log(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_logdiff_126d_base_v083_signal(marketcap, closeadj):
    result = _diff(_log(marketcap), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_logdiff_252d_base_v084_signal(marketcap, closeadj):
    result = _diff(_log(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_logdiff_504d_base_v085_signal(marketcap, closeadj):
    result = _diff(_log(marketcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_cv_21d_base_v086_signal(marketcap):
    m = _mean(marketcap, 21)
    s = _std(marketcap, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_cv_63d_base_v087_signal(marketcap):
    m = _mean(marketcap, 63)
    s = _std(marketcap, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_cv_126d_base_v088_signal(marketcap):
    m = _mean(marketcap, 126)
    s = _std(marketcap, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_cv_252d_base_v089_signal(marketcap):
    m = _mean(marketcap, 252)
    s = _std(marketcap, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_cv_504d_base_v090_signal(marketcap):
    m = _mean(marketcap, 504)
    s = _std(marketcap, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_range_21d_base_v091_signal(marketcap):
    hi = marketcap.rolling(21).max()
    lo = marketcap.rolling(21).min()
    result = _safe_div(hi - lo, _mean(marketcap, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_range_63d_base_v092_signal(marketcap):
    hi = marketcap.rolling(63).max()
    lo = marketcap.rolling(63).min()
    result = _safe_div(hi - lo, _mean(marketcap, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_range_126d_base_v093_signal(marketcap):
    hi = marketcap.rolling(126).max()
    lo = marketcap.rolling(126).min()
    result = _safe_div(hi - lo, _mean(marketcap, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_range_252d_base_v094_signal(marketcap):
    hi = marketcap.rolling(252).max()
    lo = marketcap.rolling(252).min()
    result = _safe_div(hi - lo, _mean(marketcap, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_range_504d_base_v095_signal(marketcap):
    hi = marketcap.rolling(504).max()
    lo = marketcap.rolling(504).min()
    result = _safe_div(hi - lo, _mean(marketcap, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_mad_21d_base_v096_signal(marketcap, closeadj):
    m = _mean(marketcap, 21)
    result = _mean((marketcap - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_mad_63d_base_v097_signal(marketcap, closeadj):
    m = _mean(marketcap, 63)
    result = _mean((marketcap - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_mad_126d_base_v098_signal(marketcap, closeadj):
    m = _mean(marketcap, 126)
    result = _mean((marketcap - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_mad_252d_base_v099_signal(marketcap, closeadj):
    m = _mean(marketcap, 252)
    result = _mean((marketcap - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_mad_504d_base_v100_signal(marketcap, closeadj):
    m = _mean(marketcap, 504)
    result = _mean((marketcap - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_21d_base_v101_signal(marketcap, closeadj):
    result = marketcap.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_63d_base_v102_signal(marketcap, closeadj):
    result = marketcap.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_126d_base_v103_signal(marketcap, closeadj):
    result = marketcap.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_252d_base_v104_signal(marketcap, closeadj):
    result = marketcap.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_504d_base_v105_signal(marketcap, closeadj):
    result = marketcap.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_std_21d_base_v106_signal(marketcap, closeadj):
    result = marketcap.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_std_63d_base_v107_signal(marketcap, closeadj):
    result = marketcap.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_std_126d_base_v108_signal(marketcap, closeadj):
    result = marketcap.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_std_252d_base_v109_signal(marketcap, closeadj):
    result = marketcap.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_ewm_std_504d_base_v110_signal(marketcap, closeadj):
    result = marketcap.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_med_21d_base_v111_signal(marketcap, closeadj):
    result = marketcap.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_med_63d_base_v112_signal(marketcap, closeadj):
    result = marketcap.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_med_126d_base_v113_signal(marketcap, closeadj):
    result = marketcap.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_med_252d_base_v114_signal(marketcap, closeadj):
    result = marketcap.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_med_504d_base_v115_signal(marketcap, closeadj):
    result = marketcap.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sum_21d_base_v116_signal(marketcap, closeadj):
    result = marketcap.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sum_63d_base_v117_signal(marketcap, closeadj):
    result = marketcap.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sum_126d_base_v118_signal(marketcap, closeadj):
    result = marketcap.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sum_252d_base_v119_signal(marketcap, closeadj):
    result = marketcap.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sum_504d_base_v120_signal(marketcap, closeadj):
    result = marketcap.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sign_21d_base_v121_signal(marketcap):
    result = _mean(np.sign(_diff(marketcap, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sign_63d_base_v122_signal(marketcap):
    result = _mean(np.sign(_diff(marketcap, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sign_126d_base_v123_signal(marketcap):
    result = _mean(np.sign(_diff(marketcap, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sign_252d_base_v124_signal(marketcap):
    result = _mean(np.sign(_diff(marketcap, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_sign_504d_base_v125_signal(marketcap):
    result = _mean(np.sign(_diff(marketcap, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_peak_freq_63d_base_v126_signal(marketcap):
    is_peak = (marketcap == marketcap.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_trough_freq_63d_base_v127_signal(marketcap):
    is_trough = (marketcap == marketcap.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_peak_freq_252d_base_v128_signal(marketcap):
    is_peak = (marketcap == marketcap.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of marketcap
def gm_f83_biotech_f83_price_to_sales_ratio_trough_freq_252d_base_v129_signal(marketcap):
    is_trough = (marketcap == marketcap.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 130
def gm_f83_biotech_f83_price_to_sales_ratio_lag_130d_base_v130_signal(marketcap, closeadj):
    result = marketcap.shift(130) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 131
def gm_f83_biotech_f83_price_to_sales_ratio_lag_131d_base_v131_signal(marketcap, closeadj):
    result = marketcap.shift(131) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 132
def gm_f83_biotech_f83_price_to_sales_ratio_lag_132d_base_v132_signal(marketcap, closeadj):
    result = marketcap.shift(132) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 133
def gm_f83_biotech_f83_price_to_sales_ratio_lag_133d_base_v133_signal(marketcap, closeadj):
    result = marketcap.shift(133) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 134
def gm_f83_biotech_f83_price_to_sales_ratio_lag_134d_base_v134_signal(marketcap, closeadj):
    result = marketcap.shift(134) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f83_biotech_f83_price_to_sales_ratio_lag_135d_base_v135_signal(marketcap, closeadj):
    result = marketcap.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f83_biotech_f83_price_to_sales_ratio_lag_136d_base_v136_signal(marketcap, closeadj):
    result = marketcap.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f83_biotech_f83_price_to_sales_ratio_lag_137d_base_v137_signal(marketcap, closeadj):
    result = marketcap.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f83_biotech_f83_price_to_sales_ratio_lag_138d_base_v138_signal(marketcap, closeadj):
    result = marketcap.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f83_biotech_f83_price_to_sales_ratio_lag_139d_base_v139_signal(marketcap, closeadj):
    result = marketcap.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f83_biotech_f83_price_to_sales_ratio_lag_140d_base_v140_signal(marketcap, closeadj):
    result = marketcap.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f83_biotech_f83_price_to_sales_ratio_lag_141d_base_v141_signal(marketcap, closeadj):
    result = marketcap.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f83_biotech_f83_price_to_sales_ratio_lag_142d_base_v142_signal(marketcap, closeadj):
    result = marketcap.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f83_biotech_f83_price_to_sales_ratio_lag_143d_base_v143_signal(marketcap, closeadj):
    result = marketcap.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f83_biotech_f83_price_to_sales_ratio_lag_144d_base_v144_signal(marketcap, closeadj):
    result = marketcap.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f83_biotech_f83_price_to_sales_ratio_lag_145d_base_v145_signal(marketcap, closeadj):
    result = marketcap.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f83_biotech_f83_price_to_sales_ratio_lag_146d_base_v146_signal(marketcap, closeadj):
    result = marketcap.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f83_biotech_f83_price_to_sales_ratio_lag_147d_base_v147_signal(marketcap, closeadj):
    result = marketcap.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f83_biotech_f83_price_to_sales_ratio_lag_148d_base_v148_signal(marketcap, closeadj):
    result = marketcap.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f83_biotech_f83_price_to_sales_ratio_lag_149d_base_v149_signal(marketcap, closeadj):
    result = marketcap.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f83_biotech_f83_price_to_sales_ratio_lag_150d_base_v150_signal(marketcap, closeadj):
    result = marketcap.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

