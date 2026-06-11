import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f51_sga_rev(s, rev):
    return s / rev.replace(0, np.nan)


def _f51_sga_rev_log(s, rev):
    return np.log(s.replace(0, np.nan).abs() / rev.replace(0, np.nan).abs())


# level of log SG&A intensity (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_21d_base_v076_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level of log SG&A intensity (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_63d_base_v077_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level of log SG&A intensity (126d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_126d_base_v078_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level of log SG&A intensity (252d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_252d_base_v079_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level of log SG&A intensity (504d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_504d_base_v080_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_21d_base_v081_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_63d_base_v082_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_126d_base_v083_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_252d_base_v084_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_504d_base_v085_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of log SG&A intensity (median/MAD)
def f51sga_semi_sga_to_revenue_sgarlog_robustz_21d_base_v086_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(21, min_periods=11).median()
    mad = (m - med).abs().rolling(21, min_periods=11).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of log SG&A intensity (median/MAD)
def f51sga_semi_sga_to_revenue_sgarlog_robustz_63d_base_v087_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of log SG&A intensity (median/MAD)
def f51sga_semi_sga_to_revenue_sgarlog_robustz_126d_base_v088_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(126, min_periods=63).median()
    mad = (m - med).abs().rolling(126, min_periods=63).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of log SG&A intensity (median/MAD)
def f51sga_semi_sga_to_revenue_sgarlog_robustz_252d_base_v089_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(252, min_periods=126).median()
    mad = (m - med).abs().rolling(252, min_periods=126).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of log SG&A intensity (median/MAD)
def f51sga_semi_sga_to_revenue_sgarlog_robustz_504d_base_v090_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(504, min_periods=252).median()
    mad = (m - med).abs().rolling(504, min_periods=252).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling max of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_max_21d_base_v091_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling max of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_max_63d_base_v092_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling max of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_max_126d_base_v093_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling max of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_max_252d_base_v094_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling max of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_max_504d_base_v095_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling min of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_min_21d_base_v096_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling min of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_min_63d_base_v097_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling min of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_min_126d_base_v098_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling min of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_min_252d_base_v099_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling min of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_min_504d_base_v100_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of log SG&A intensity (max - min)
def f51sga_semi_sga_to_revenue_sgarlog_rng_21d_base_v101_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of log SG&A intensity (max - min)
def f51sga_semi_sga_to_revenue_sgarlog_rng_63d_base_v102_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of log SG&A intensity (max - min)
def f51sga_semi_sga_to_revenue_sgarlog_rng_126d_base_v103_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of log SG&A intensity (max - min)
def f51sga_semi_sga_to_revenue_sgarlog_rng_252d_base_v104_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of log SG&A intensity (max - min)
def f51sga_semi_sga_to_revenue_sgarlog_rng_504d_base_v105_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of log SG&A intensity in its rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_21d_base_v106_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of log SG&A intensity in its rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_63d_base_v107_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of log SG&A intensity in its rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_126d_base_v108_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of log SG&A intensity in its rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_252d_base_v109_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of log SG&A intensity in its rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_504d_base_v110_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of log SG&A intensity from rolling peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_21d_base_v111_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of log SG&A intensity from rolling peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_63d_base_v112_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of log SG&A intensity from rolling peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_126d_base_v113_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of log SG&A intensity from rolling peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_252d_base_v114_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 252)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of log SG&A intensity from rolling peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_504d_base_v115_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 504)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of log SG&A intensity above rolling trough
def f51sga_semi_sga_to_revenue_sgarlog_up_21d_base_v116_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 21)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of log SG&A intensity above rolling trough
def f51sga_semi_sga_to_revenue_sgarlog_up_63d_base_v117_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 63)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of log SG&A intensity above rolling trough
def f51sga_semi_sga_to_revenue_sgarlog_up_126d_base_v118_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 126)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of log SG&A intensity above rolling trough
def f51sga_semi_sga_to_revenue_sgarlog_up_252d_base_v119_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 252)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of log SG&A intensity above rolling trough
def f51sga_semi_sga_to_revenue_sgarlog_up_504d_base_v120_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 504)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of log SG&A intensity (volatility)
def f51sga_semi_sga_to_revenue_sgarlog_std_21d_base_v121_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _std(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of log SG&A intensity (volatility)
def f51sga_semi_sga_to_revenue_sgarlog_std_63d_base_v122_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _std(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of log SG&A intensity (volatility)
def f51sga_semi_sga_to_revenue_sgarlog_std_126d_base_v123_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of log SG&A intensity (volatility)
def f51sga_semi_sga_to_revenue_sgarlog_std_252d_base_v124_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _std(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of log SG&A intensity (volatility)
def f51sga_semi_sga_to_revenue_sgarlog_std_504d_base_v125_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = _std(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_21d_base_v126_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_63d_base_v127_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_126d_base_v128_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_252d_base_v129_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_504d_base_v130_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_kurt_21d_base_v131_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_kurt_63d_base_v132_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_kurt_126d_base_v133_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_kurt_252d_base_v134_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_kurt_504d_base_v135_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_21d_base_v136_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = (m.diff() > 0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_63d_base_v137_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_126d_base_v138_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = (m.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_252d_base_v139_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = (m.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_504d_base_v140_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = (m.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_21d_base_v141_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_63d_base_v142_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_126d_base_v143_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_252d_base_v144_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_504d_base_v145_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA-crossover of log SG&A intensity (fast vs slow)
def f51sga_semi_sga_to_revenue_sgarlog_ema_21d_base_v146_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.ewm(span=max(2, 21//4), adjust=False).mean() - m.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA-crossover of log SG&A intensity (fast vs slow)
def f51sga_semi_sga_to_revenue_sgarlog_ema_63d_base_v147_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA-crossover of log SG&A intensity (fast vs slow)
def f51sga_semi_sga_to_revenue_sgarlog_ema_126d_base_v148_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.ewm(span=max(2, 126//4), adjust=False).mean() - m.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA-crossover of log SG&A intensity (fast vs slow)
def f51sga_semi_sga_to_revenue_sgarlog_ema_252d_base_v149_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.ewm(span=max(2, 252//4), adjust=False).mean() - m.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA-crossover of log SG&A intensity (fast vs slow)
def f51sga_semi_sga_to_revenue_sgarlog_ema_504d_base_v150_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    result = m.ewm(span=max(2, 504//4), adjust=False).mean() - m.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
