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


def _f30_growth(s, n):
    return s.pct_change(periods=n)


# 21d rolling corr capex(t-21) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_21d_base_v001_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(21), rv, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling corr capex(t-21) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_63d_base_v002_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(21), rv, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling corr capex(t-21) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_126d_base_v003_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(21), rv, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling corr capex(t-21) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_252d_base_v004_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(21), rv, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling corr capex(t-21) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_corr_504d_base_v005_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(21), rv, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling corr capex(t-63) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_21d_base_v006_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(63), rv, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling corr capex(t-63) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_63d_base_v007_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(63), rv, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling corr capex(t-63) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_126d_base_v008_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(63), rv, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling corr capex(t-63) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_252d_base_v009_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(63), rv, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling corr capex(t-63) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_corr_504d_base_v010_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(63), rv, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling corr capex(t-126) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_21d_base_v011_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(126), rv, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling corr capex(t-126) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_63d_base_v012_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(126), rv, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling corr capex(t-126) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_126d_base_v013_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(126), rv, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling corr capex(t-126) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_252d_base_v014_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(126), rv, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling corr capex(t-126) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_corr_504d_base_v015_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(126), rv, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling corr capex(t-252) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_21d_base_v016_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(252), rv, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling corr capex(t-252) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_63d_base_v017_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(252), rv, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling corr capex(t-252) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_126d_base_v018_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(252), rv, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling corr capex(t-252) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_252d_base_v019_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(252), rv, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling corr capex(t-252) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_corr_504d_base_v020_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(252), rv, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling corr capex(t-504) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_21d_base_v021_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(504), rv, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling corr capex(t-504) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_63d_base_v022_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(504), rv, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling corr capex(t-504) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_126d_base_v023_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(504), rv, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling corr capex(t-504) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_252d_base_v024_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(504), rv, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling corr capex(t-504) vs revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_corr_504d_base_v025_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_corr(cx.shift(504), rv, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_21d_base_v026_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(21), 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_63d_base_v027_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(21), 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_126d_base_v028_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(21), 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_252d_base_v029_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(21), 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling beta revenue on capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_beta_504d_base_v030_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(21), 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_21d_base_v031_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(63), 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_63d_base_v032_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_126d_base_v033_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(63), 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_252d_base_v034_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(63), 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling beta revenue on capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_beta_504d_base_v035_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(63), 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_21d_base_v036_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(126), 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_63d_base_v037_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(126), 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_126d_base_v038_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(126), 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_252d_base_v039_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(126), 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling beta revenue on capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_beta_504d_base_v040_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(126), 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_21d_base_v041_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(252), 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_63d_base_v042_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(252), 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_126d_base_v043_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(252), 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_252d_base_v044_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(252), 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling beta revenue on capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_beta_504d_base_v045_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(252), 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_21d_base_v046_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(504), 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_63d_base_v047_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(504), 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_126d_base_v048_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(504), 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_252d_base_v049_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(504), 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d rolling beta revenue on capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_beta_504d_base_v050_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    result = _f30_beta(rv, cx.shift(504), 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_21d_base_v051_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_63d_base_v052_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_126d_base_v053_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_252d_base_v054_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_lrz_504d_base_v055_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_21d_base_v056_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_63d_base_v057_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_126d_base_v058_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_252d_base_v059_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_lrz_504d_base_v060_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_21d_base_v061_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_63d_base_v062_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_126d_base_v063_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_252d_base_v064_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_lrz_504d_base_v065_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_21d_base_v066_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_63d_base_v067_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_126d_base_v068_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_252d_base_v069_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_lrz_504d_base_v070_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_21d_base_v071_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    result = _z(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_63d_base_v072_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    result = _z(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_126d_base_v073_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    result = _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_252d_base_v074_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d z-score log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_lrz_504d_base_v075_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    result = _z(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



