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


# 21d hit-rate sign(rev growth) == sign(capex growth lagged 21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_hit_21d_base_v076_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=21)
    cg = cx.pct_change(periods=21).shift(21)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(21, min_periods=max(2, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 63d hit-rate sign(rev growth) == sign(capex growth lagged 21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_hit_63d_base_v077_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=63)
    cg = cx.pct_change(periods=63).shift(21)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(63, min_periods=max(2, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 126d hit-rate sign(rev growth) == sign(capex growth lagged 21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_hit_126d_base_v078_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=126)
    cg = cx.pct_change(periods=126).shift(21)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(126, min_periods=max(2, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 252d hit-rate sign(rev growth) == sign(capex growth lagged 21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_hit_252d_base_v079_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=252)
    cg = cx.pct_change(periods=252).shift(21)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(252, min_periods=max(2, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 504d hit-rate sign(rev growth) == sign(capex growth lagged 21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_hit_504d_base_v080_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=504)
    cg = cx.pct_change(periods=504).shift(21)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(504, min_periods=max(2, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 21d hit-rate sign(rev growth) == sign(capex growth lagged 63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_hit_21d_base_v081_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=21)
    cg = cx.pct_change(periods=21).shift(63)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(21, min_periods=max(2, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 63d hit-rate sign(rev growth) == sign(capex growth lagged 63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_hit_63d_base_v082_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=63)
    cg = cx.pct_change(periods=63).shift(63)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(63, min_periods=max(2, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 126d hit-rate sign(rev growth) == sign(capex growth lagged 63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_hit_126d_base_v083_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=126)
    cg = cx.pct_change(periods=126).shift(63)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(126, min_periods=max(2, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 252d hit-rate sign(rev growth) == sign(capex growth lagged 63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_hit_252d_base_v084_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=252)
    cg = cx.pct_change(periods=252).shift(63)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(252, min_periods=max(2, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 504d hit-rate sign(rev growth) == sign(capex growth lagged 63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_hit_504d_base_v085_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=504)
    cg = cx.pct_change(periods=504).shift(63)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(504, min_periods=max(2, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 21d hit-rate sign(rev growth) == sign(capex growth lagged 126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_hit_21d_base_v086_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=21)
    cg = cx.pct_change(periods=21).shift(126)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(21, min_periods=max(2, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 63d hit-rate sign(rev growth) == sign(capex growth lagged 126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_hit_63d_base_v087_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=63)
    cg = cx.pct_change(periods=63).shift(126)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(63, min_periods=max(2, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 126d hit-rate sign(rev growth) == sign(capex growth lagged 126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_hit_126d_base_v088_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=126)
    cg = cx.pct_change(periods=126).shift(126)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(126, min_periods=max(2, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 252d hit-rate sign(rev growth) == sign(capex growth lagged 126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_hit_252d_base_v089_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=252)
    cg = cx.pct_change(periods=252).shift(126)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(252, min_periods=max(2, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 504d hit-rate sign(rev growth) == sign(capex growth lagged 126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_hit_504d_base_v090_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=504)
    cg = cx.pct_change(periods=504).shift(126)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(504, min_periods=max(2, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 21d hit-rate sign(rev growth) == sign(capex growth lagged 252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_hit_21d_base_v091_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=21)
    cg = cx.pct_change(periods=21).shift(252)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(21, min_periods=max(2, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 63d hit-rate sign(rev growth) == sign(capex growth lagged 252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_hit_63d_base_v092_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=63)
    cg = cx.pct_change(periods=63).shift(252)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(63, min_periods=max(2, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 126d hit-rate sign(rev growth) == sign(capex growth lagged 252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_hit_126d_base_v093_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=126)
    cg = cx.pct_change(periods=126).shift(252)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(126, min_periods=max(2, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 252d hit-rate sign(rev growth) == sign(capex growth lagged 252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_hit_252d_base_v094_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=252)
    cg = cx.pct_change(periods=252).shift(252)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(252, min_periods=max(2, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 504d hit-rate sign(rev growth) == sign(capex growth lagged 252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_hit_504d_base_v095_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=504)
    cg = cx.pct_change(periods=504).shift(252)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(504, min_periods=max(2, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 21d hit-rate sign(rev growth) == sign(capex growth lagged 504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_hit_21d_base_v096_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=21)
    cg = cx.pct_change(periods=21).shift(504)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(21, min_periods=max(2, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 63d hit-rate sign(rev growth) == sign(capex growth lagged 504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_hit_63d_base_v097_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=63)
    cg = cx.pct_change(periods=63).shift(504)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(63, min_periods=max(2, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 126d hit-rate sign(rev growth) == sign(capex growth lagged 504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_hit_126d_base_v098_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=126)
    cg = cx.pct_change(periods=126).shift(504)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(126, min_periods=max(2, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 252d hit-rate sign(rev growth) == sign(capex growth lagged 504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_hit_252d_base_v099_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=252)
    cg = cx.pct_change(periods=252).shift(504)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(252, min_periods=max(2, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 504d hit-rate sign(rev growth) == sign(capex growth lagged 504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_hit_504d_base_v100_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    rg = rv.pct_change(periods=504)
    cg = cx.pct_change(periods=504).shift(504)
    hit = (np.sign(rg) == np.sign(cg)).astype(float)
    result = hit.rolling(504, min_periods=max(2, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_21d_base_v101_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(21), rv)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_63d_base_v102_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(21), rv)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_126d_base_v103_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(21), rv)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_252d_base_v104_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(21), rv)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of capex(t-21) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag21_cxrv_504d_base_v105_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(21), rv)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_21d_base_v106_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(63), rv)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_63d_base_v107_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(63), rv)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_126d_base_v108_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(63), rv)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_252d_base_v109_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(63), rv)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of capex(t-63) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag63_cxrv_504d_base_v110_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(63), rv)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_21d_base_v111_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(126), rv)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_63d_base_v112_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(126), rv)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_126d_base_v113_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(126), rv)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_252d_base_v114_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(126), rv)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of capex(t-126) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag126_cxrv_504d_base_v115_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(126), rv)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_21d_base_v116_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(252), rv)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_63d_base_v117_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(252), rv)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_126d_base_v118_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(252), rv)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_252d_base_v119_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(252), rv)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of capex(t-252) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag252_cxrv_504d_base_v120_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(252), rv)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_21d_base_v121_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(504), rv)
    result = _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)



# 63d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_63d_base_v122_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(504), rv)
    result = _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)



# 126d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_126d_base_v123_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(504), rv)
    result = _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)



# 252d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_252d_base_v124_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(504), rv)
    result = _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)



# 504d mean of capex(t-504) / revenue(t)
def f30clr_f30_semi_capex_lead_revenue_cllag504_cxrv_504d_base_v125_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_ratio(cx.shift(504), rv)
    result = _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)



# 21d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_21d_base_v126_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 63d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_63d_base_v127_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 126d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_126d_base_v128_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 252d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_252d_base_v129_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 504d drawdown of log-ratio revenue vs capex(t-21)
def f30clr_f30_semi_capex_lead_revenue_cllag21_dd_504d_base_v130_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(21))
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 21d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_21d_base_v131_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 63d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_63d_base_v132_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 126d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_126d_base_v133_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 252d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_252d_base_v134_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 504d drawdown of log-ratio revenue vs capex(t-63)
def f30clr_f30_semi_capex_lead_revenue_cllag63_dd_504d_base_v135_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(63))
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 21d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_21d_base_v136_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 63d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_63d_base_v137_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 126d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_126d_base_v138_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 252d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_252d_base_v139_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 504d drawdown of log-ratio revenue vs capex(t-126)
def f30clr_f30_semi_capex_lead_revenue_cllag126_dd_504d_base_v140_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(126))
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 21d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_21d_base_v141_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 63d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_63d_base_v142_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 126d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_126d_base_v143_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 252d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_252d_base_v144_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 504d drawdown of log-ratio revenue vs capex(t-252)
def f30clr_f30_semi_capex_lead_revenue_cllag252_dd_504d_base_v145_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(252))
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 21d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_21d_base_v146_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    peak = _max(r, 21)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 63d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_63d_base_v147_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    peak = _max(r, 63)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 126d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_126d_base_v148_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    peak = _max(r, 126)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 252d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_252d_base_v149_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    peak = _max(r, 252)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



# 504d drawdown of log-ratio revenue vs capex(t-504)
def f30clr_f30_semi_capex_lead_revenue_cllag504_dd_504d_base_v150_signal(capex, revenue, closeadj):
    cx = _f30_daily(capex, closeadj)
    rv = _f30_daily(revenue, closeadj)
    r = _f30_log_ratio(rv, cx.shift(504))
    peak = _max(r, 504)
    result = r - peak
    return result.replace([np.inf, -np.inf], np.nan)



