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
def _f96ce_ret(s):
    return s.pct_change()


def _f96ce_logret(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f96ce_roll_corr(a, b, w):
    return a.rolling(w, min_periods=max(2, w // 2)).corr(b)


def _f96ce_roll_beta(a, b, w):
    cov = a.rolling(w, min_periods=max(2, w // 2)).cov(b)
    var = b.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f96ce_idio(own_r, x_r, w):
    cov = own_r.rolling(w, min_periods=max(2, w // 2)).cov(x_r)
    var = x_r.rolling(w, min_periods=max(2, w // 2)).var()
    beta = cov / var.replace(0, np.nan)
    return own_r - beta * x_r


# 21d rolling correlation of own returns with china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_corr_21d_base_v001_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation of own returns with china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_corr_63d_base_v002_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation of own returns with china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_corr_126d_base_v003_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation of own returns with china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_corr_252d_base_v004_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation of own returns with china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_corr_504d_base_v005_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta of own returns on china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_beta_21d_base_v006_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_beta(o, c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta of own returns on china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_beta_63d_base_v007_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_beta(o, c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta of own returns on china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_beta_126d_base_v008_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_beta(o, c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta of own returns on china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_beta_252d_base_v009_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_beta(o, c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta of own returns on china_exposure_index returns
def f96ce_f96_semi_china_exposure_proxy_beta_504d_base_v010_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_beta(o, c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional own return on days china_exposure drops > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretdrop_21d_base_v011_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 21)
    mask = (c < -sd).astype(float)
    result = (o * mask).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional own return on days china_exposure drops > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretdrop_63d_base_v012_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 63)
    mask = (c < -sd).astype(float)
    result = (o * mask).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional own return on days china_exposure drops > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretdrop_126d_base_v013_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 126)
    mask = (c < -sd).astype(float)
    result = (o * mask).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional own return on days china_exposure drops > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretdrop_252d_base_v014_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 252)
    mask = (c < -sd).astype(float)
    result = (o * mask).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional own return on days china_exposure drops > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretdrop_504d_base_v015_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 504)
    mask = (c < -sd).astype(float)
    result = (o * mask).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional own return on days china_exposure rises > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretrise_21d_base_v016_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 21)
    mask = (c > sd).astype(float)
    result = (o * mask).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional own return on days china_exposure rises > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretrise_63d_base_v017_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 63)
    mask = (c > sd).astype(float)
    result = (o * mask).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional own return on days china_exposure rises > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretrise_126d_base_v018_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 126)
    mask = (c > sd).astype(float)
    result = (o * mask).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional own return on days china_exposure rises > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretrise_252d_base_v019_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 252)
    mask = (c > sd).astype(float)
    result = (o * mask).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional own return on days china_exposure rises > 1 std
def f96ce_f96_semi_china_exposure_proxy_condretrise_504d_base_v020_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 504)
    mask = (c > sd).astype(float)
    result = (o * mask).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d idiosyncratic return after removing china_exposure beta (rolling mean)
def f96ce_f96_semi_china_exposure_proxy_idio_21d_base_v021_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 21).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d idiosyncratic return after removing china_exposure beta (rolling mean)
def f96ce_f96_semi_china_exposure_proxy_idio_63d_base_v022_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 63).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d idiosyncratic return after removing china_exposure beta (rolling mean)
def f96ce_f96_semi_china_exposure_proxy_idio_126d_base_v023_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 126).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d idiosyncratic return after removing china_exposure beta (rolling mean)
def f96ce_f96_semi_china_exposure_proxy_idio_252d_base_v024_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 252).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d idiosyncratic return after removing china_exposure beta (rolling mean)
def f96ce_f96_semi_china_exposure_proxy_idio_504d_base_v025_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 504).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative idio (sum) after removing china_exposure beta
def f96ce_f96_semi_china_exposure_proxy_cumidio_21d_base_v026_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 21).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative idio (sum) after removing china_exposure beta
def f96ce_f96_semi_china_exposure_proxy_cumidio_63d_base_v027_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 63).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative idio (sum) after removing china_exposure beta
def f96ce_f96_semi_china_exposure_proxy_cumidio_126d_base_v028_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 126).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative idio (sum) after removing china_exposure beta
def f96ce_f96_semi_china_exposure_proxy_cumidio_252d_base_v029_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 252).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative idio (sum) after removing china_exposure beta
def f96ce_f96_semi_china_exposure_proxy_cumidio_504d_base_v030_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_idio(o, c, 504).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead/lag corr own with china shifted +1 day (china lags own by 1d)
def f96ce_f96_semi_china_exposure_proxy_leadlag1_21d_base_v031_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(1)
    result = _f96ce_roll_corr(o, c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead/lag corr own with china shifted +1 day
def f96ce_f96_semi_china_exposure_proxy_leadlag1_63d_base_v032_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(1)
    result = _f96ce_roll_corr(o, c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead/lag corr own with china shifted +1 day
def f96ce_f96_semi_china_exposure_proxy_leadlag1_126d_base_v033_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(1)
    result = _f96ce_roll_corr(o, c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead/lag corr own with china shifted +1 day
def f96ce_f96_semi_china_exposure_proxy_leadlag1_252d_base_v034_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(1)
    result = _f96ce_roll_corr(o, c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead/lag corr own with china shifted +1 day
def f96ce_f96_semi_china_exposure_proxy_leadlag1_504d_base_v035_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(1)
    result = _f96ce_roll_corr(o, c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead/lag corr own with china shifted +3 days
def f96ce_f96_semi_china_exposure_proxy_leadlag3_21d_base_v036_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(3)
    result = _f96ce_roll_corr(o, c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead/lag corr own with china shifted +3 days
def f96ce_f96_semi_china_exposure_proxy_leadlag3_63d_base_v037_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(3)
    result = _f96ce_roll_corr(o, c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead/lag corr own with china shifted +3 days
def f96ce_f96_semi_china_exposure_proxy_leadlag3_126d_base_v038_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(3)
    result = _f96ce_roll_corr(o, c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead/lag corr own with china shifted +3 days
def f96ce_f96_semi_china_exposure_proxy_leadlag3_252d_base_v039_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(3)
    result = _f96ce_roll_corr(o, c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead/lag corr own with china shifted +3 days
def f96ce_f96_semi_china_exposure_proxy_leadlag3_504d_base_v040_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(3)
    result = _f96ce_roll_corr(o, c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lead/lag corr own with china shifted +5 days
def f96ce_f96_semi_china_exposure_proxy_leadlag5_21d_base_v041_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(5)
    result = _f96ce_roll_corr(o, c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lead/lag corr own with china shifted +5 days
def f96ce_f96_semi_china_exposure_proxy_leadlag5_63d_base_v042_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(5)
    result = _f96ce_roll_corr(o, c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lead/lag corr own with china shifted +5 days
def f96ce_f96_semi_china_exposure_proxy_leadlag5_126d_base_v043_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(5)
    result = _f96ce_roll_corr(o, c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lead/lag corr own with china shifted +5 days
def f96ce_f96_semi_china_exposure_proxy_leadlag5_252d_base_v044_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(5)
    result = _f96ce_roll_corr(o, c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lead/lag corr own with china shifted +5 days
def f96ce_f96_semi_china_exposure_proxy_leadlag5_504d_base_v045_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index).shift(5)
    result = _f96ce_roll_corr(o, c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative own outperformance during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_outperfdd_21d_base_v046_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    cmax = _max(np.log(china_exposure_index.replace(0, np.nan).abs()), 21)
    dd = np.log(china_exposure_index.replace(0, np.nan).abs()) - cmax
    mask = (dd < 0).astype(float)
    result = ((o - c) * mask).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative own outperformance during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_outperfdd_63d_base_v047_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    cmax = _max(np.log(china_exposure_index.replace(0, np.nan).abs()), 63)
    dd = np.log(china_exposure_index.replace(0, np.nan).abs()) - cmax
    mask = (dd < 0).astype(float)
    result = ((o - c) * mask).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative own outperformance during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_outperfdd_126d_base_v048_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    cmax = _max(np.log(china_exposure_index.replace(0, np.nan).abs()), 126)
    dd = np.log(china_exposure_index.replace(0, np.nan).abs()) - cmax
    mask = (dd < 0).astype(float)
    result = ((o - c) * mask).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative own outperformance during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_outperfdd_252d_base_v049_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    cmax = _max(np.log(china_exposure_index.replace(0, np.nan).abs()), 252)
    dd = np.log(china_exposure_index.replace(0, np.nan).abs()) - cmax
    mask = (dd < 0).astype(float)
    result = ((o - c) * mask).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative own outperformance during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_outperfdd_504d_base_v050_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    cmax = _max(np.log(china_exposure_index.replace(0, np.nan).abs()), 504)
    dd = np.log(china_exposure_index.replace(0, np.nan).abs()) - cmax
    mask = (dd < 0).astype(float)
    result = ((o - c) * mask).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d tracking error of own vs china_exposure_index (std of log-return diff)
def f96ce_f96_semi_china_exposure_proxy_trackerr_21d_base_v051_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = _std(diff, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tracking error of own vs china_exposure_index
def f96ce_f96_semi_china_exposure_proxy_trackerr_63d_base_v052_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = _std(diff, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d tracking error of own vs china_exposure_index
def f96ce_f96_semi_china_exposure_proxy_trackerr_126d_base_v053_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = _std(diff, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tracking error of own vs china_exposure_index
def f96ce_f96_semi_china_exposure_proxy_trackerr_252d_base_v054_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = _std(diff, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tracking error of own vs china_exposure_index
def f96ce_f96_semi_china_exposure_proxy_trackerr_504d_base_v055_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = _std(diff, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d china z-score regime times own return (interaction)
def f96ce_f96_semi_china_exposure_proxy_chinazx_21d_base_v056_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 21)
    o = _f96ce_ret(closeadj)
    result = (cz * o).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d china z-score regime times own return (interaction)
def f96ce_f96_semi_china_exposure_proxy_chinazx_63d_base_v057_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 63)
    o = _f96ce_ret(closeadj)
    result = (cz * o).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d china z-score regime times own return (interaction)
def f96ce_f96_semi_china_exposure_proxy_chinazx_126d_base_v058_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 126)
    o = _f96ce_ret(closeadj)
    result = (cz * o).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d china z-score regime times own return (interaction)
def f96ce_f96_semi_china_exposure_proxy_chinazx_252d_base_v059_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 252)
    o = _f96ce_ret(closeadj)
    result = (cz * o).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d china z-score regime times own return (interaction)
def f96ce_f96_semi_china_exposure_proxy_chinazx_504d_base_v060_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 504)
    o = _f96ce_ret(closeadj)
    result = (cz * o).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of own log price minus ema crossover of china index (5 vs 21)
def f96ce_f96_semi_china_exposure_proxy_emacross_21d_base_v061_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    ox = lo.ewm(span=5, adjust=False).mean() - lo.ewm(span=21, adjust=False).mean()
    cx = lc.ewm(span=5, adjust=False).mean() - lc.ewm(span=21, adjust=False).mean()
    result = ox - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover own vs china (21 vs 63)
def f96ce_f96_semi_china_exposure_proxy_emacross_63d_base_v062_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    ox = lo.ewm(span=21, adjust=False).mean() - lo.ewm(span=63, adjust=False).mean()
    cx = lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=63, adjust=False).mean()
    result = ox - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover own vs china (63 vs 126)
def f96ce_f96_semi_china_exposure_proxy_emacross_126d_base_v063_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    ox = lo.ewm(span=63, adjust=False).mean() - lo.ewm(span=126, adjust=False).mean()
    cx = lc.ewm(span=63, adjust=False).mean() - lc.ewm(span=126, adjust=False).mean()
    result = ox - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover own vs china (126 vs 252)
def f96ce_f96_semi_china_exposure_proxy_emacross_252d_base_v064_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    ox = lo.ewm(span=126, adjust=False).mean() - lo.ewm(span=252, adjust=False).mean()
    cx = lc.ewm(span=126, adjust=False).mean() - lc.ewm(span=252, adjust=False).mean()
    result = ox - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover own vs china (252 vs 504)
def f96ce_f96_semi_china_exposure_proxy_emacross_504d_base_v065_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    ox = lo.ewm(span=252, adjust=False).mean() - lo.ewm(span=504, adjust=False).mean()
    cx = lc.ewm(span=252, adjust=False).mean() - lc.ewm(span=504, adjust=False).mean()
    result = ox - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling corr of own returns with semi basket returns (control corr)
def f96ce_f96_semi_china_exposure_proxy_corrbasket_21d_base_v066_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_corr(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling corr of own returns with semi basket returns
def f96ce_f96_semi_china_exposure_proxy_corrbasket_63d_base_v067_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_corr(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling corr of own returns with semi basket returns
def f96ce_f96_semi_china_exposure_proxy_corrbasket_126d_base_v068_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_corr(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling corr of own returns with semi basket returns
def f96ce_f96_semi_china_exposure_proxy_corrbasket_252d_base_v069_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_corr(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling corr of own returns with semi basket returns
def f96ce_f96_semi_china_exposure_proxy_corrbasket_504d_base_v070_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_corr(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta of own on semi basket (control beta)
def f96ce_f96_semi_china_exposure_proxy_betabasket_21d_base_v071_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_beta(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta of own on semi basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_63d_base_v072_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_beta(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta of own on semi basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_126d_base_v073_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_beta(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta of own on semi basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_252d_base_v074_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_beta(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta of own on semi basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_504d_base_v075_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_roll_beta(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)
