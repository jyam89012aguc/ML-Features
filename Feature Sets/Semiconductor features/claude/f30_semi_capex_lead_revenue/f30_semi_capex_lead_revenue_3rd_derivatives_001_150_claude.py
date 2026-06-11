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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f30_daily(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f30_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f30_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


def _f30_corr(a, b, w):
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


def _f30_beta(y, x, w):
    cov = y.rolling(w, min_periods=max(2, w // 2)).cov(x)
    var = x.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


# 21d curvature of 21d rolling corr capex(t-21) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_21d_curv_v001_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(21), rv, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_21d_curv_v002_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(21), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_21d_curv_v003_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(21)), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_21d_curv_v004_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(21), rv), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_21d_curv_v005_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _max(_f30_log_ratio(rv, cx.shift(21)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d log-ratio revenue vs capex(t-21) level rel to 21d mean
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrlvl_21d_curv_v006_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _mean(_f30_log_ratio(rv, cx.shift(21)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling corr capex(t-21) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_63d_curv_v007_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(21), rv, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_63d_curv_v008_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(21), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_63d_curv_v009_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(21)), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_63d_curv_v010_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(21), rv), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_63d_curv_v011_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _max(_f30_log_ratio(rv, cx.shift(21)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d log-ratio revenue vs capex(t-21) level rel to 63d mean
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrlvl_63d_curv_v012_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _mean(_f30_log_ratio(rv, cx.shift(21)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling corr capex(t-21) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_126d_curv_v013_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(21), rv, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_126d_curv_v014_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(21), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_126d_curv_v015_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(21)), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_126d_curv_v016_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(21), rv), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_126d_curv_v017_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _max(_f30_log_ratio(rv, cx.shift(21)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d log-ratio revenue vs capex(t-21) level rel to 126d mean
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrlvl_126d_curv_v018_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _mean(_f30_log_ratio(rv, cx.shift(21)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling corr capex(t-21) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_252d_curv_v019_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(21), rv, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_252d_curv_v020_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(21), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_252d_curv_v021_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(21)), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_252d_curv_v022_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(21), rv), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_252d_curv_v023_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _max(_f30_log_ratio(rv, cx.shift(21)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d log-ratio revenue vs capex(t-21) level rel to 252d mean
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrlvl_252d_curv_v024_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _mean(_f30_log_ratio(rv, cx.shift(21)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling corr capex(t-21) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_504d_curv_v025_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(21), rv, 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_504d_curv_v026_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(21), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_504d_curv_v027_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(21)), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_504d_curv_v028_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(21), rv), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_504d_curv_v029_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _max(_f30_log_ratio(rv, cx.shift(21)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d log-ratio revenue vs capex(t-21) level rel to 504d mean
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrlvl_504d_curv_v030_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(21)) - _mean(_f30_log_ratio(rv, cx.shift(21)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling corr capex(t-63) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_21d_curv_v031_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(63), rv, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_21d_curv_v032_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(63), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_21d_curv_v033_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(63)), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_21d_curv_v034_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(63), rv), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_21d_curv_v035_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _max(_f30_log_ratio(rv, cx.shift(63)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d log-ratio revenue vs capex(t-63) level rel to 21d mean
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrlvl_21d_curv_v036_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _mean(_f30_log_ratio(rv, cx.shift(63)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling corr capex(t-63) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_63d_curv_v037_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(63), rv, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_63d_curv_v038_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(63), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_63d_curv_v039_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(63)), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_63d_curv_v040_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(63), rv), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_63d_curv_v041_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _max(_f30_log_ratio(rv, cx.shift(63)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d log-ratio revenue vs capex(t-63) level rel to 63d mean
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrlvl_63d_curv_v042_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _mean(_f30_log_ratio(rv, cx.shift(63)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling corr capex(t-63) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_126d_curv_v043_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(63), rv, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_126d_curv_v044_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(63), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_126d_curv_v045_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(63)), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_126d_curv_v046_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(63), rv), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_126d_curv_v047_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _max(_f30_log_ratio(rv, cx.shift(63)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d log-ratio revenue vs capex(t-63) level rel to 126d mean
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrlvl_126d_curv_v048_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _mean(_f30_log_ratio(rv, cx.shift(63)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling corr capex(t-63) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_252d_curv_v049_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(63), rv, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_252d_curv_v050_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(63), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_252d_curv_v051_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(63)), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_252d_curv_v052_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(63), rv), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_252d_curv_v053_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _max(_f30_log_ratio(rv, cx.shift(63)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d log-ratio revenue vs capex(t-63) level rel to 252d mean
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrlvl_252d_curv_v054_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _mean(_f30_log_ratio(rv, cx.shift(63)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling corr capex(t-63) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_504d_curv_v055_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(63), rv, 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_504d_curv_v056_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(63), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_504d_curv_v057_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(63)), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_504d_curv_v058_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(63), rv), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_504d_curv_v059_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _max(_f30_log_ratio(rv, cx.shift(63)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d log-ratio revenue vs capex(t-63) level rel to 504d mean
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrlvl_504d_curv_v060_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(63)) - _mean(_f30_log_ratio(rv, cx.shift(63)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling corr capex(t-126) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_21d_curv_v061_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(126), rv, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_21d_curv_v062_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(126), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_21d_curv_v063_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(126)), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_21d_curv_v064_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(126), rv), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_21d_curv_v065_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _max(_f30_log_ratio(rv, cx.shift(126)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d log-ratio revenue vs capex(t-126) level rel to 21d mean
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrlvl_21d_curv_v066_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _mean(_f30_log_ratio(rv, cx.shift(126)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling corr capex(t-126) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_63d_curv_v067_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(126), rv, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_63d_curv_v068_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(126), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_63d_curv_v069_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(126)), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_63d_curv_v070_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(126), rv), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_63d_curv_v071_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _max(_f30_log_ratio(rv, cx.shift(126)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d log-ratio revenue vs capex(t-126) level rel to 63d mean
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrlvl_63d_curv_v072_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _mean(_f30_log_ratio(rv, cx.shift(126)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling corr capex(t-126) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_126d_curv_v073_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(126), rv, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_126d_curv_v074_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(126), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_126d_curv_v075_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(126)), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_126d_curv_v076_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(126), rv), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_126d_curv_v077_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _max(_f30_log_ratio(rv, cx.shift(126)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d log-ratio revenue vs capex(t-126) level rel to 126d mean
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrlvl_126d_curv_v078_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _mean(_f30_log_ratio(rv, cx.shift(126)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling corr capex(t-126) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_252d_curv_v079_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(126), rv, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_252d_curv_v080_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(126), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_252d_curv_v081_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(126)), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_252d_curv_v082_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(126), rv), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_252d_curv_v083_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _max(_f30_log_ratio(rv, cx.shift(126)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d log-ratio revenue vs capex(t-126) level rel to 252d mean
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrlvl_252d_curv_v084_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _mean(_f30_log_ratio(rv, cx.shift(126)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling corr capex(t-126) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_504d_curv_v085_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(126), rv, 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_504d_curv_v086_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(126), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_504d_curv_v087_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(126)), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_504d_curv_v088_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(126), rv), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_504d_curv_v089_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _max(_f30_log_ratio(rv, cx.shift(126)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d log-ratio revenue vs capex(t-126) level rel to 504d mean
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrlvl_504d_curv_v090_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(126)) - _mean(_f30_log_ratio(rv, cx.shift(126)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling corr capex(t-252) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_21d_curv_v091_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(252), rv, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_21d_curv_v092_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(252), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_21d_curv_v093_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(252)), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_21d_curv_v094_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(252), rv), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_21d_curv_v095_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _max(_f30_log_ratio(rv, cx.shift(252)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d log-ratio revenue vs capex(t-252) level rel to 21d mean
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrlvl_21d_curv_v096_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _mean(_f30_log_ratio(rv, cx.shift(252)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling corr capex(t-252) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_63d_curv_v097_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(252), rv, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_63d_curv_v098_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(252), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_63d_curv_v099_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(252)), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_63d_curv_v100_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(252), rv), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_63d_curv_v101_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _max(_f30_log_ratio(rv, cx.shift(252)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d log-ratio revenue vs capex(t-252) level rel to 63d mean
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrlvl_63d_curv_v102_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _mean(_f30_log_ratio(rv, cx.shift(252)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling corr capex(t-252) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_126d_curv_v103_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(252), rv, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_126d_curv_v104_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(252), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_126d_curv_v105_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(252)), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_126d_curv_v106_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(252), rv), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_126d_curv_v107_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _max(_f30_log_ratio(rv, cx.shift(252)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d log-ratio revenue vs capex(t-252) level rel to 126d mean
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrlvl_126d_curv_v108_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _mean(_f30_log_ratio(rv, cx.shift(252)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling corr capex(t-252) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_252d_curv_v109_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(252), rv, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_252d_curv_v110_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(252), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_252d_curv_v111_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(252)), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_252d_curv_v112_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(252), rv), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_252d_curv_v113_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _max(_f30_log_ratio(rv, cx.shift(252)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d log-ratio revenue vs capex(t-252) level rel to 252d mean
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrlvl_252d_curv_v114_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _mean(_f30_log_ratio(rv, cx.shift(252)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling corr capex(t-252) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_504d_curv_v115_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(252), rv, 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_504d_curv_v116_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(252), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_504d_curv_v117_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(252)), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_504d_curv_v118_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(252), rv), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_504d_curv_v119_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _max(_f30_log_ratio(rv, cx.shift(252)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d log-ratio revenue vs capex(t-252) level rel to 504d mean
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrlvl_504d_curv_v120_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(252)) - _mean(_f30_log_ratio(rv, cx.shift(252)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling corr capex(t-504) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_21d_curv_v121_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(504), rv, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_21d_curv_v122_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(504), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_21d_curv_v123_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(504)), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_21d_curv_v124_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(504), rv), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_21d_curv_v125_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _max(_f30_log_ratio(rv, cx.shift(504)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d curvature of 21d log-ratio revenue vs capex(t-504) level rel to 21d mean
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrlvl_21d_curv_v126_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _mean(_f30_log_ratio(rv, cx.shift(504)), 21))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling corr capex(t-504) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_63d_curv_v127_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(504), rv, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_63d_curv_v128_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(504), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_63d_curv_v129_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(504)), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_63d_curv_v130_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(504), rv), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_63d_curv_v131_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _max(_f30_log_ratio(rv, cx.shift(504)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d curvature of 63d log-ratio revenue vs capex(t-504) level rel to 63d mean
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrlvl_63d_curv_v132_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _mean(_f30_log_ratio(rv, cx.shift(504)), 63))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling corr capex(t-504) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_126d_curv_v133_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(504), rv, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_126d_curv_v134_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(504), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_126d_curv_v135_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(504)), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_126d_curv_v136_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(504), rv), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_126d_curv_v137_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _max(_f30_log_ratio(rv, cx.shift(504)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d curvature of 126d log-ratio revenue vs capex(t-504) level rel to 126d mean
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrlvl_126d_curv_v138_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _mean(_f30_log_ratio(rv, cx.shift(504)), 126))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling corr capex(t-504) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_252d_curv_v139_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(504), rv, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_252d_curv_v140_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(504), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_252d_curv_v141_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(504)), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_252d_curv_v142_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(504), rv), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_252d_curv_v143_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _max(_f30_log_ratio(rv, cx.shift(504)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d curvature of 252d log-ratio revenue vs capex(t-504) level rel to 252d mean
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrlvl_252d_curv_v144_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _mean(_f30_log_ratio(rv, cx.shift(504)), 252))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling corr capex(t-504) vs revenue
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_504d_curv_v145_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_corr(cx.shift(504), rv, 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_504d_curv_v146_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _f30_beta(rv, cx.shift(504), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_504d_curv_v147_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _z(_f30_log_ratio(rv, cx.shift(504)), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_504d_curv_v148_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = _mean(_f30_ratio(cx.shift(504), rv), 504)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_504d_curv_v149_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _max(_f30_log_ratio(rv, cx.shift(504)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d curvature of 504d log-ratio revenue vs capex(t-504) level rel to 504d mean
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrlvl_504d_curv_v150_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    base = (_f30_log_ratio(rv, cx.shift(504)) - _mean(_f30_log_ratio(rv, cx.shift(504)), 504))
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)



