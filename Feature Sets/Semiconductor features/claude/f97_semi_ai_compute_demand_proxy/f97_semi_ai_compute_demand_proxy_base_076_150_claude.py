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
def _f97ai_log_ratio(rev, hyp):
    return np.log(rev.replace(0, np.nan).abs() / hyp.replace(0, np.nan).abs())


def _f97ai_ratio(rev, hyp):
    return rev / hyp.replace(0, np.nan)


def _f97ai_log_diff(s, n):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f97ai_roll_corr(a, b, w):
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


def _f97ai_roll_beta(a, b, w):
    cov = a.rolling(w, min_periods=max(2, w // 2)).cov(b)
    var = b.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


# 21d drawdown of mindshare log ratio from its rolling peak
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_21d_base_v076_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of mindshare log ratio from its rolling peak
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_63d_base_v077_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of mindshare log ratio from its rolling peak
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_126d_base_v078_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of mindshare log ratio from its rolling peak
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_252d_base_v079_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of mindshare log ratio from its rolling peak
def f97ai_f97_semi_ai_compute_demand_proxy_ratiodd_504d_base_v080_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of mindshare log ratio above rolling trough
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_21d_base_v081_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of mindshare log ratio above rolling trough
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_63d_base_v082_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of mindshare log ratio above rolling trough
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_126d_base_v083_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of mindshare log ratio above rolling trough
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_252d_base_v084_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of mindshare log ratio above rolling trough
def f97ai_f97_semi_ai_compute_demand_proxy_ratioup_504d_base_v085_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = r - _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_21d_base_v086_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 21) - _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_63d_base_v087_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 63) - _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_126d_base_v088_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 126) - _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_252d_base_v089_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 252) - _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiorng_504d_base_v090_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 504) - _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of mindshare log ratio in its rolling range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_21d_base_v091_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 21)
    hi = _max(r, 21)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of mindshare log ratio in its rolling range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_63d_base_v092_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 63)
    hi = _max(r, 63)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of mindshare log ratio in its rolling range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_126d_base_v093_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 126)
    hi = _max(r, 126)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of mindshare log ratio in its rolling range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_252d_base_v094_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 252)
    hi = _max(r, 252)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of mindshare log ratio in its rolling range
def f97ai_f97_semi_ai_compute_demand_proxy_ratiopos_504d_base_v095_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    lo = _min(r, 504)
    hi = _max(r, 504)
    result = (r - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling max of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_21d_base_v096_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling max of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_63d_base_v097_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling max of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_126d_base_v098_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling max of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_252d_base_v099_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling max of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomax_504d_base_v100_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling min of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_21d_base_v101_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling min of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_63d_base_v102_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling min of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_126d_base_v103_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling min of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_252d_base_v104_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling min of mindshare log ratio
def f97ai_f97_semi_ai_compute_demand_proxy_ratiomin_504d_base_v105_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    result = _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of mindshare log ratio first differences (tracking volatility)
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_21d_base_v106_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    result = _std(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of mindshare log ratio first differences (tracking volatility)
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_63d_base_v107_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    result = _std(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of mindshare log ratio first differences (tracking volatility)
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_126d_base_v108_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    result = _std(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of mindshare log ratio first differences (tracking volatility)
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_252d_base_v109_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    result = _std(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of mindshare log ratio first differences (tracking volatility)
def f97ai_f97_semi_ai_compute_demand_proxy_ratiostd_504d_base_v110_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index).diff()
    result = _std(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue deviation from rolling mean of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_21d_base_v111_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 21)
    result = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue deviation from rolling mean of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_63d_base_v112_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 63)
    result = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue deviation from rolling mean of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_126d_base_v113_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 126)
    result = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue deviation from rolling mean of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_252d_base_v114_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 252)
    result = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue deviation from rolling mean of hyperscaler index
def f97ai_f97_semi_ai_compute_demand_proxy_revhypdev_504d_base_v115_signal(revenue, hyperscaler_capex_index, closeadj):
    base = _mean(hyperscaler_capex_index, 504)
    result = np.log(revenue.replace(0, np.nan).abs() / base.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative difference of log changes (rev vs hyper)
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_21d_base_v116_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    result = diff.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative difference of log changes (rev vs hyper)
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_63d_base_v117_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    result = diff.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative difference of log changes (rev vs hyper)
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_126d_base_v118_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    result = diff.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative difference of log changes (rev vs hyper)
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_252d_base_v119_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    result = diff.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative difference of log changes (rev vs hyper)
def f97ai_f97_semi_ai_compute_demand_proxy_cumretdiff_504d_base_v120_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = revenue.pct_change() - hyperscaler_capex_index.pct_change()
    result = diff.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d tracking error of revenue vs hyperscaler index log differences
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_21d_base_v121_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    result = _std(diff, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tracking error of revenue vs hyperscaler index log differences
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_63d_base_v122_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    result = _std(diff, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d tracking error of revenue vs hyperscaler index log differences
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_126d_base_v123_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    result = _std(diff, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tracking error of revenue vs hyperscaler index log differences
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_252d_base_v124_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    result = _std(diff, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tracking error of revenue vs hyperscaler index log differences
def f97ai_f97_semi_ai_compute_demand_proxy_trackerr_504d_base_v125_signal(revenue, hyperscaler_capex_index, closeadj):
    diff = _f97ai_log_diff(revenue, 1) - _f97ai_log_diff(hyperscaler_capex_index, 1)
    result = _std(diff, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr trend (current 21d corr minus 63d trailing corr mean)
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_21d_base_v126_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 21)
    result = c - _mean(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr trend (current 63d corr minus 126d trailing corr mean)
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_63d_base_v127_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 63)
    result = c - _mean(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr trend (current 126d corr minus 252d trailing corr mean)
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_126d_base_v128_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 126)
    result = c - _mean(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr trend (current 252d corr minus 504d trailing corr mean)
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_252d_base_v129_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 252)
    result = c - _mean(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr trend (current 504d corr minus 756d trailing corr mean)
def f97ai_f97_semi_ai_compute_demand_proxy_corrdiff_504d_base_v130_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 504)
    result = c - _mean(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite signal: z-score of corr plus z-score of beta
def f97ai_f97_semi_ai_compute_demand_proxy_composite_21d_base_v131_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 21)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 21)
    result = _z(c, 252) + _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite signal: z-score of corr plus z-score of beta
def f97ai_f97_semi_ai_compute_demand_proxy_composite_63d_base_v132_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 63)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 63)
    result = _z(c, 252) + _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite signal: z-score of corr plus z-score of beta
def f97ai_f97_semi_ai_compute_demand_proxy_composite_126d_base_v133_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 126)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 126)
    result = _z(c, 252) + _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite signal: z-score of corr plus z-score of beta
def f97ai_f97_semi_ai_compute_demand_proxy_composite_252d_base_v134_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 252)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 252)
    result = _z(c, 504) + _z(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite signal: z-score of corr plus z-score of beta
def f97ai_f97_semi_ai_compute_demand_proxy_composite_504d_base_v135_signal(revenue, hyperscaler_capex_index, closeadj):
    c = _f97ai_roll_corr(revenue, hyperscaler_capex_index, 504)
    b = _f97ai_roll_beta(revenue, hyperscaler_capex_index, 504)
    result = _z(c, 504) + _z(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of mindshare log ratio (median/MAD)
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_21d_base_v136_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(21, min_periods=11).median()
    mad = (r - med).abs().rolling(21, min_periods=11).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of mindshare log ratio (median/MAD)
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_63d_base_v137_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(63, min_periods=32).median()
    mad = (r - med).abs().rolling(63, min_periods=32).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of mindshare log ratio (median/MAD)
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_126d_base_v138_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(126, min_periods=63).median()
    mad = (r - med).abs().rolling(126, min_periods=63).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of mindshare log ratio (median/MAD)
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_252d_base_v139_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(252, min_periods=126).median()
    mad = (r - med).abs().rolling(252, min_periods=126).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of mindshare log ratio (median/MAD)
def f97ai_f97_semi_ai_compute_demand_proxy_robustz_504d_base_v140_signal(revenue, hyperscaler_capex_index, closeadj):
    r = _f97ai_log_ratio(revenue, hyperscaler_capex_index)
    med = r.rolling(504, min_periods=252).median()
    mad = (r - med).abs().rolling(504, min_periods=252).median()
    result = (r - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed YoY-comovement count (sign of rev YoY times sign of hyper YoY)
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_21d_base_v141_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    result = s.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed YoY-comovement count (sign of rev YoY times sign of hyper YoY)
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_63d_base_v142_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    result = s.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed YoY-comovement count (sign of rev YoY times sign of hyper YoY)
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_126d_base_v143_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    result = s.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed YoY-comovement count (sign of rev YoY times sign of hyper YoY)
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_252d_base_v144_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    result = s.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed YoY-comovement count (sign of rev YoY times sign of hyper YoY)
def f97ai_f97_semi_ai_compute_demand_proxy_yoysigncum_504d_base_v145_signal(revenue, hyperscaler_capex_index, closeadj):
    rv = _f97ai_log_diff(revenue, 252)
    hv = _f97ai_log_diff(hyperscaler_capex_index, 252)
    s = pd.Series(np.sign(rv) * np.sign(hv), index=rv.index)
    result = s.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue z-score (own series) interacted with hyperscaler regime tag z-score
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_21d_base_v146_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 21)
    zh = _z(hyperscaler_capex_index, 21)
    result = zr * zh
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue z-score interacted with hyperscaler regime tag z-score
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_63d_base_v147_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 63)
    zh = _z(hyperscaler_capex_index, 63)
    result = zr * zh
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue z-score interacted with hyperscaler regime tag z-score
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_126d_base_v148_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 126)
    zh = _z(hyperscaler_capex_index, 126)
    result = zr * zh
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue z-score interacted with hyperscaler regime tag z-score
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_252d_base_v149_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 252)
    zh = _z(hyperscaler_capex_index, 252)
    result = zr * zh
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue z-score interacted with hyperscaler regime tag z-score
def f97ai_f97_semi_ai_compute_demand_proxy_regimex_504d_base_v150_signal(revenue, hyperscaler_capex_index, closeadj):
    zr = _z(revenue, 504)
    zh = _z(hyperscaler_capex_index, 504)
    result = zr * zh
    return result.replace([np.inf, -np.inf], np.nan)
