
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


# 21d rolling autocorr of assets
def gm_f08_biotech_f08_tangible_book_value_autocorr_21d_base_v076_signal(assets):
    result = _autocorr(assets, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling autocorr of assets
def gm_f08_biotech_f08_tangible_book_value_autocorr_63d_base_v077_signal(assets):
    result = _autocorr(assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling autocorr of assets
def gm_f08_biotech_f08_tangible_book_value_autocorr_126d_base_v078_signal(assets):
    result = _autocorr(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling autocorr of assets
def gm_f08_biotech_f08_tangible_book_value_autocorr_252d_base_v079_signal(assets):
    result = _autocorr(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling autocorr of assets
def gm_f08_biotech_f08_tangible_book_value_autocorr_504d_base_v080_signal(assets):
    result = _autocorr(assets, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling std of assets
def gm_f08_biotech_f08_tangible_book_value_std_21d_base_v081_signal(assets, closeadj):
    result = _std(assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling std of assets
def gm_f08_biotech_f08_tangible_book_value_std_63d_base_v082_signal(assets, closeadj):
    result = _std(assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling std of assets
def gm_f08_biotech_f08_tangible_book_value_std_126d_base_v083_signal(assets, closeadj):
    result = _std(assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling std of assets
def gm_f08_biotech_f08_tangible_book_value_std_252d_base_v084_signal(assets, closeadj):
    result = _std(assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling std of assets
def gm_f08_biotech_f08_tangible_book_value_std_504d_base_v085_signal(assets, closeadj):
    result = _std(assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d log-diff of assets
def gm_f08_biotech_f08_tangible_book_value_logdiff_21d_base_v086_signal(assets, closeadj):
    result = _diff(_log(assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d log-diff of assets
def gm_f08_biotech_f08_tangible_book_value_logdiff_63d_base_v087_signal(assets, closeadj):
    result = _diff(_log(assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d log-diff of assets
def gm_f08_biotech_f08_tangible_book_value_logdiff_126d_base_v088_signal(assets, closeadj):
    result = _diff(_log(assets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d log-diff of assets
def gm_f08_biotech_f08_tangible_book_value_logdiff_252d_base_v089_signal(assets, closeadj):
    result = _diff(_log(assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d log-diff of assets
def gm_f08_biotech_f08_tangible_book_value_logdiff_504d_base_v090_signal(assets, closeadj):
    result = _diff(_log(assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d coef of variation of assets
def gm_f08_biotech_f08_tangible_book_value_cv_21d_base_v091_signal(assets):
    m = _mean(assets, 21)
    s = _std(assets, 21)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d coef of variation of assets
def gm_f08_biotech_f08_tangible_book_value_cv_63d_base_v092_signal(assets):
    m = _mean(assets, 63)
    s = _std(assets, 63)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d coef of variation of assets
def gm_f08_biotech_f08_tangible_book_value_cv_126d_base_v093_signal(assets):
    m = _mean(assets, 126)
    s = _std(assets, 126)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d coef of variation of assets
def gm_f08_biotech_f08_tangible_book_value_cv_252d_base_v094_signal(assets):
    m = _mean(assets, 252)
    s = _std(assets, 252)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d coef of variation of assets
def gm_f08_biotech_f08_tangible_book_value_cv_504d_base_v095_signal(assets):
    m = _mean(assets, 504)
    s = _std(assets, 504)
    result = _safe_div(s, m.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d hi-lo range of assets
def gm_f08_biotech_f08_tangible_book_value_range_21d_base_v096_signal(assets):
    hi = assets.rolling(21).max()
    lo = assets.rolling(21).min()
    result = _safe_div(hi - lo, _mean(assets, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 63d hi-lo range of assets
def gm_f08_biotech_f08_tangible_book_value_range_63d_base_v097_signal(assets):
    hi = assets.rolling(63).max()
    lo = assets.rolling(63).min()
    result = _safe_div(hi - lo, _mean(assets, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 126d hi-lo range of assets
def gm_f08_biotech_f08_tangible_book_value_range_126d_base_v098_signal(assets):
    hi = assets.rolling(126).max()
    lo = assets.rolling(126).min()
    result = _safe_div(hi - lo, _mean(assets, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 252d hi-lo range of assets
def gm_f08_biotech_f08_tangible_book_value_range_252d_base_v099_signal(assets):
    hi = assets.rolling(252).max()
    lo = assets.rolling(252).min()
    result = _safe_div(hi - lo, _mean(assets, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 504d hi-lo range of assets
def gm_f08_biotech_f08_tangible_book_value_range_504d_base_v100_signal(assets):
    hi = assets.rolling(504).max()
    lo = assets.rolling(504).min()
    result = _safe_div(hi - lo, _mean(assets, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean absolute deviation of assets
def gm_f08_biotech_f08_tangible_book_value_mad_21d_base_v101_signal(assets, closeadj):
    m = _mean(assets, 21)
    result = _mean((assets - m).abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean absolute deviation of assets
def gm_f08_biotech_f08_tangible_book_value_mad_63d_base_v102_signal(assets, closeadj):
    m = _mean(assets, 63)
    result = _mean((assets - m).abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean absolute deviation of assets
def gm_f08_biotech_f08_tangible_book_value_mad_126d_base_v103_signal(assets, closeadj):
    m = _mean(assets, 126)
    result = _mean((assets - m).abs(), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean absolute deviation of assets
def gm_f08_biotech_f08_tangible_book_value_mad_252d_base_v104_signal(assets, closeadj):
    m = _mean(assets, 252)
    result = _mean((assets - m).abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean absolute deviation of assets
def gm_f08_biotech_f08_tangible_book_value_mad_504d_base_v105_signal(assets, closeadj):
    m = _mean(assets, 504)
    result = _mean((assets - m).abs(), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_21d_base_v106_signal(assets, closeadj):
    result = assets.ewm(span=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_63d_base_v107_signal(assets, closeadj):
    result = assets.ewm(span=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_126d_base_v108_signal(assets, closeadj):
    result = assets.ewm(span=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_252d_base_v109_signal(assets, closeadj):
    result = assets.ewm(span=252).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_504d_base_v110_signal(assets, closeadj):
    result = assets.ewm(span=504).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d EWM std of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_std_21d_base_v111_signal(assets, closeadj):
    result = assets.ewm(span=21).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d EWM std of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_std_63d_base_v112_signal(assets, closeadj):
    result = assets.ewm(span=63).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d EWM std of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_std_126d_base_v113_signal(assets, closeadj):
    result = assets.ewm(span=126).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d EWM std of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_std_252d_base_v114_signal(assets, closeadj):
    result = assets.ewm(span=252).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d EWM std of assets
def gm_f08_biotech_f08_tangible_book_value_ewm_std_504d_base_v115_signal(assets, closeadj):
    result = assets.ewm(span=504).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling median of assets
def gm_f08_biotech_f08_tangible_book_value_med_21d_base_v116_signal(assets, closeadj):
    result = assets.rolling(21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of assets
def gm_f08_biotech_f08_tangible_book_value_med_63d_base_v117_signal(assets, closeadj):
    result = assets.rolling(63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling median of assets
def gm_f08_biotech_f08_tangible_book_value_med_126d_base_v118_signal(assets, closeadj):
    result = assets.rolling(126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of assets
def gm_f08_biotech_f08_tangible_book_value_med_252d_base_v119_signal(assets, closeadj):
    result = assets.rolling(252).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of assets
def gm_f08_biotech_f08_tangible_book_value_med_504d_base_v120_signal(assets, closeadj):
    result = assets.rolling(504).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d rolling sum of assets
def gm_f08_biotech_f08_tangible_book_value_sum_21d_base_v121_signal(assets, closeadj):
    result = assets.rolling(21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling sum of assets
def gm_f08_biotech_f08_tangible_book_value_sum_63d_base_v122_signal(assets, closeadj):
    result = assets.rolling(63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d rolling sum of assets
def gm_f08_biotech_f08_tangible_book_value_sum_126d_base_v123_signal(assets, closeadj):
    result = assets.rolling(126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling sum of assets
def gm_f08_biotech_f08_tangible_book_value_sum_252d_base_v124_signal(assets, closeadj):
    result = assets.rolling(252).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling sum of assets
def gm_f08_biotech_f08_tangible_book_value_sum_504d_base_v125_signal(assets, closeadj):
    result = assets.rolling(504).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d sign of change of assets
def gm_f08_biotech_f08_tangible_book_value_sign_21d_base_v126_signal(assets):
    result = _mean(np.sign(_diff(assets, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d sign of change of assets
def gm_f08_biotech_f08_tangible_book_value_sign_63d_base_v127_signal(assets):
    result = _mean(np.sign(_diff(assets, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d sign of change of assets
def gm_f08_biotech_f08_tangible_book_value_sign_126d_base_v128_signal(assets):
    result = _mean(np.sign(_diff(assets, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d sign of change of assets
def gm_f08_biotech_f08_tangible_book_value_sign_252d_base_v129_signal(assets):
    result = _mean(np.sign(_diff(assets, 252)), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 504d sign of change of assets
def gm_f08_biotech_f08_tangible_book_value_sign_504d_base_v130_signal(assets):
    result = _mean(np.sign(_diff(assets, 504)), 504)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d peak frequency of assets
def gm_f08_biotech_f08_tangible_book_value_peak_freq_63d_base_v131_signal(assets):
    is_peak = (assets == assets.rolling(63).max()).astype(float)
    result = _mean(is_peak, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d trough frequency of assets
def gm_f08_biotech_f08_tangible_book_value_trough_freq_63d_base_v132_signal(assets):
    is_trough = (assets == assets.rolling(63).min()).astype(float)
    result = _mean(is_trough, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d peak frequency of assets
def gm_f08_biotech_f08_tangible_book_value_peak_freq_252d_base_v133_signal(assets):
    is_peak = (assets == assets.rolling(252).max()).astype(float)
    result = _mean(is_peak, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d trough frequency of assets
def gm_f08_biotech_f08_tangible_book_value_trough_freq_252d_base_v134_signal(assets):
    is_trough = (assets == assets.rolling(252).min()).astype(float)
    result = _mean(is_trough, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 135
def gm_f08_biotech_f08_tangible_book_value_lag_135d_base_v135_signal(assets, closeadj):
    result = assets.shift(135) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 136
def gm_f08_biotech_f08_tangible_book_value_lag_136d_base_v136_signal(assets, closeadj):
    result = assets.shift(136) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 137
def gm_f08_biotech_f08_tangible_book_value_lag_137d_base_v137_signal(assets, closeadj):
    result = assets.shift(137) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 138
def gm_f08_biotech_f08_tangible_book_value_lag_138d_base_v138_signal(assets, closeadj):
    result = assets.shift(138) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 139
def gm_f08_biotech_f08_tangible_book_value_lag_139d_base_v139_signal(assets, closeadj):
    result = assets.shift(139) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 140
def gm_f08_biotech_f08_tangible_book_value_lag_140d_base_v140_signal(assets, closeadj):
    result = assets.shift(140) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 141
def gm_f08_biotech_f08_tangible_book_value_lag_141d_base_v141_signal(assets, closeadj):
    result = assets.shift(141) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 142
def gm_f08_biotech_f08_tangible_book_value_lag_142d_base_v142_signal(assets, closeadj):
    result = assets.shift(142) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 143
def gm_f08_biotech_f08_tangible_book_value_lag_143d_base_v143_signal(assets, closeadj):
    result = assets.shift(143) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 144
def gm_f08_biotech_f08_tangible_book_value_lag_144d_base_v144_signal(assets, closeadj):
    result = assets.shift(144) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 145
def gm_f08_biotech_f08_tangible_book_value_lag_145d_base_v145_signal(assets, closeadj):
    result = assets.shift(145) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 146
def gm_f08_biotech_f08_tangible_book_value_lag_146d_base_v146_signal(assets, closeadj):
    result = assets.shift(146) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 147
def gm_f08_biotech_f08_tangible_book_value_lag_147d_base_v147_signal(assets, closeadj):
    result = assets.shift(147) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 148
def gm_f08_biotech_f08_tangible_book_value_lag_148d_base_v148_signal(assets, closeadj):
    result = assets.shift(148) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 149
def gm_f08_biotech_f08_tangible_book_value_lag_149d_base_v149_signal(assets, closeadj):
    result = assets.shift(149) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# Lag 150
def gm_f08_biotech_f08_tangible_book_value_lag_150d_base_v150_signal(assets, closeadj):
    result = assets.shift(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

