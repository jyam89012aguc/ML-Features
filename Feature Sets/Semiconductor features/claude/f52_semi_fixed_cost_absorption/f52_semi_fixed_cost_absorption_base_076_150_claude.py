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
def _f52_fca(ox, rev):
    return ox / rev.replace(0, np.nan)


def _f52_abs_scale(ox, rev):
    return (ox / rev.replace(0, np.nan)) * np.log(rev.replace(0, np.nan).abs())


# level of fixed cost absorption scaled by log revenue (21d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_21d_base_v076_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level of fixed cost absorption scaled by log revenue (63d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_63d_base_v077_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level of fixed cost absorption scaled by log revenue (126d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_126d_base_v078_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level of fixed cost absorption scaled by log revenue (252d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_252d_base_v079_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level of fixed cost absorption scaled by log revenue (504d mean-centered)
def f52fca_semi_fixed_cost_absorption_fcascl_level_504d_base_v080_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_21d_base_v081_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_63d_base_v082_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_126d_base_v083_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_252d_base_v084_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_z_504d_base_v085_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of fixed cost absorption scaled by log revenue (median/MAD)
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_21d_base_v086_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(21, min_periods=11).median()
    mad = (m - med).abs().rolling(21, min_periods=11).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of fixed cost absorption scaled by log revenue (median/MAD)
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_63d_base_v087_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of fixed cost absorption scaled by log revenue (median/MAD)
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_126d_base_v088_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(126, min_periods=63).median()
    mad = (m - med).abs().rolling(126, min_periods=63).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of fixed cost absorption scaled by log revenue (median/MAD)
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_252d_base_v089_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(252, min_periods=126).median()
    mad = (m - med).abs().rolling(252, min_periods=126).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of fixed cost absorption scaled by log revenue (median/MAD)
def f52fca_semi_fixed_cost_absorption_fcascl_robustz_504d_base_v090_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    med = m.rolling(504, min_periods=252).median()
    mad = (m - med).abs().rolling(504, min_periods=252).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling max of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_max_21d_base_v091_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling max of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_max_63d_base_v092_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling max of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_max_126d_base_v093_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling max of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_max_252d_base_v094_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling max of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_max_504d_base_v095_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling min of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_min_21d_base_v096_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling min of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_min_63d_base_v097_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling min of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_min_126d_base_v098_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling min of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_min_252d_base_v099_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling min of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_min_504d_base_v100_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of fixed cost absorption scaled by log revenue (max - min)
def f52fca_semi_fixed_cost_absorption_fcascl_rng_21d_base_v101_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 21) - _min(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of fixed cost absorption scaled by log revenue (max - min)
def f52fca_semi_fixed_cost_absorption_fcascl_rng_63d_base_v102_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 63) - _min(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of fixed cost absorption scaled by log revenue (max - min)
def f52fca_semi_fixed_cost_absorption_fcascl_rng_126d_base_v103_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 126) - _min(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of fixed cost absorption scaled by log revenue (max - min)
def f52fca_semi_fixed_cost_absorption_fcascl_rng_252d_base_v104_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 252) - _min(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of fixed cost absorption scaled by log revenue (max - min)
def f52fca_semi_fixed_cost_absorption_fcascl_rng_504d_base_v105_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _max(m, 504) - _min(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of fixed cost absorption scaled by log revenue in its rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_21d_base_v106_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 21)
    hi = _max(m, 21)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of fixed cost absorption scaled by log revenue in its rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_63d_base_v107_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of fixed cost absorption scaled by log revenue in its rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_126d_base_v108_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 126)
    hi = _max(m, 126)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of fixed cost absorption scaled by log revenue in its rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_252d_base_v109_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 252)
    hi = _max(m, 252)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of fixed cost absorption scaled by log revenue in its rolling range
def f52fca_semi_fixed_cost_absorption_fcascl_pos_504d_base_v110_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    lo = _min(m, 504)
    hi = _max(m, 504)
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of fixed cost absorption scaled by log revenue from rolling peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_21d_base_v111_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 21)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of fixed cost absorption scaled by log revenue from rolling peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_63d_base_v112_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 63)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of fixed cost absorption scaled by log revenue from rolling peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_126d_base_v113_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 126)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of fixed cost absorption scaled by log revenue from rolling peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_252d_base_v114_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 252)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of fixed cost absorption scaled by log revenue from rolling peak
def f52fca_semi_fixed_cost_absorption_fcascl_dd_504d_base_v115_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    peak = _max(m, 504)
    result = m - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of fixed cost absorption scaled by log revenue above rolling trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_21d_base_v116_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 21)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of fixed cost absorption scaled by log revenue above rolling trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_63d_base_v117_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 63)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of fixed cost absorption scaled by log revenue above rolling trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_126d_base_v118_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 126)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of fixed cost absorption scaled by log revenue above rolling trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_252d_base_v119_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 252)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of fixed cost absorption scaled by log revenue above rolling trough
def f52fca_semi_fixed_cost_absorption_fcascl_up_504d_base_v120_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    trough = _min(m, 504)
    result = m - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of fixed cost absorption scaled by log revenue (volatility)
def f52fca_semi_fixed_cost_absorption_fcascl_std_21d_base_v121_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _std(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of fixed cost absorption scaled by log revenue (volatility)
def f52fca_semi_fixed_cost_absorption_fcascl_std_63d_base_v122_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _std(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of fixed cost absorption scaled by log revenue (volatility)
def f52fca_semi_fixed_cost_absorption_fcascl_std_126d_base_v123_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _std(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of fixed cost absorption scaled by log revenue (volatility)
def f52fca_semi_fixed_cost_absorption_fcascl_std_252d_base_v124_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _std(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of fixed cost absorption scaled by log revenue (volatility)
def f52fca_semi_fixed_cost_absorption_fcascl_std_504d_base_v125_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = _std(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_21d_base_v126_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_63d_base_v127_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_126d_base_v128_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_252d_base_v129_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_skew_504d_base_v130_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_kurt_21d_base_v131_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_kurt_63d_base_v132_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_kurt_126d_base_v133_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_kurt_252d_base_v134_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_kurt_504d_base_v135_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_21d_base_v136_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = (m.diff() > 0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_63d_base_v137_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_126d_base_v138_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = (m.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_252d_base_v139_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = (m.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit-ratio of positive fixed cost absorption scaled by log revenue changes
def f52fca_semi_fixed_cost_absorption_fcascl_hit_504d_base_v140_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = (m.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_21d_base_v141_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_63d_base_v142_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_126d_base_v143_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_252d_base_v144_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative changes of fixed cost absorption scaled by log revenue
def f52fca_semi_fixed_cost_absorption_fcascl_cumsign_504d_base_v145_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = pd.Series(np.sign(m.diff()), index=m.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA-crossover of fixed cost absorption scaled by log revenue (fast vs slow)
def f52fca_semi_fixed_cost_absorption_fcascl_ema_21d_base_v146_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.ewm(span=max(2, 21//4), adjust=False).mean() - m.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA-crossover of fixed cost absorption scaled by log revenue (fast vs slow)
def f52fca_semi_fixed_cost_absorption_fcascl_ema_63d_base_v147_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA-crossover of fixed cost absorption scaled by log revenue (fast vs slow)
def f52fca_semi_fixed_cost_absorption_fcascl_ema_126d_base_v148_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.ewm(span=max(2, 126//4), adjust=False).mean() - m.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA-crossover of fixed cost absorption scaled by log revenue (fast vs slow)
def f52fca_semi_fixed_cost_absorption_fcascl_ema_252d_base_v149_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.ewm(span=max(2, 252//4), adjust=False).mean() - m.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA-crossover of fixed cost absorption scaled by log revenue (fast vs slow)
def f52fca_semi_fixed_cost_absorption_fcascl_ema_504d_base_v150_signal(opex, revenue, closeadj):
    m = _f52_abs_scale(opex, revenue)
    result = m.ewm(span=max(2, 504//4), adjust=False).mean() - m.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
