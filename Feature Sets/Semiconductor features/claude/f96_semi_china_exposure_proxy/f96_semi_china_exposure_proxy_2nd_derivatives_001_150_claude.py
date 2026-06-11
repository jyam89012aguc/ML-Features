import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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


# 5d slope of 21d rolling corr own vs china
def f96ce_f96_semi_china_exposure_proxy_corr_21d_slope_v001_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rolling corr own vs china
def f96ce_f96_semi_china_exposure_proxy_corr_63d_slope_v002_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rolling corr own vs china
def f96ce_f96_semi_china_exposure_proxy_corr_126d_slope_v003_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rolling corr own vs china
def f96ce_f96_semi_china_exposure_proxy_corr_252d_slope_v004_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d rolling corr own vs china
def f96ce_f96_semi_china_exposure_proxy_corr_504d_slope_v005_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d rolling beta own vs china
def f96ce_f96_semi_china_exposure_proxy_beta_21d_slope_v006_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rolling beta own vs china
def f96ce_f96_semi_china_exposure_proxy_beta_63d_slope_v007_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rolling beta own vs china
def f96ce_f96_semi_china_exposure_proxy_beta_126d_slope_v008_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rolling beta own vs china
def f96ce_f96_semi_china_exposure_proxy_beta_252d_slope_v009_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d rolling beta own vs china
def f96ce_f96_semi_china_exposure_proxy_beta_504d_slope_v010_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d conditional own return on china-drop days
def f96ce_f96_semi_china_exposure_proxy_condretdrop_21d_slope_v011_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 21)
    mask = (c < -sd).astype(float)
    base = (o * mask).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d conditional own return on china-drop days
def f96ce_f96_semi_china_exposure_proxy_condretdrop_63d_slope_v012_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 63)
    mask = (c < -sd).astype(float)
    base = (o * mask).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d conditional own return on china-drop days
def f96ce_f96_semi_china_exposure_proxy_condretdrop_126d_slope_v013_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 126)
    mask = (c < -sd).astype(float)
    base = (o * mask).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d conditional own return on china-drop days
def f96ce_f96_semi_china_exposure_proxy_condretdrop_252d_slope_v014_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 252)
    mask = (c < -sd).astype(float)
    base = (o * mask).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d conditional own return on china-drop days
def f96ce_f96_semi_china_exposure_proxy_condretdrop_504d_slope_v015_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 504)
    mask = (c < -sd).astype(float)
    base = (o * mask).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d conditional own return on china-rise days
def f96ce_f96_semi_china_exposure_proxy_condretrise_21d_slope_v016_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 21)
    mask = (c > sd).astype(float)
    base = (o * mask).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d conditional own return on china-rise days
def f96ce_f96_semi_china_exposure_proxy_condretrise_63d_slope_v017_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 63)
    mask = (c > sd).astype(float)
    base = (o * mask).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d conditional own return on china-rise days
def f96ce_f96_semi_china_exposure_proxy_condretrise_126d_slope_v018_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 126)
    mask = (c > sd).astype(float)
    base = (o * mask).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d conditional own return on china-rise days
def f96ce_f96_semi_china_exposure_proxy_condretrise_252d_slope_v019_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 252)
    mask = (c > sd).astype(float)
    base = (o * mask).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d conditional own return on china-rise days
def f96ce_f96_semi_china_exposure_proxy_condretrise_504d_slope_v020_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    sd = _std(c, 504)
    mask = (c > sd).astype(float)
    base = (o * mask).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d idio mean (china-residualized)
def f96ce_f96_semi_china_exposure_proxy_idio_21d_slope_v021_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 21).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d idio mean
def f96ce_f96_semi_china_exposure_proxy_idio_63d_slope_v022_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 63).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d idio mean
def f96ce_f96_semi_china_exposure_proxy_idio_126d_slope_v023_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 126).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d idio mean
def f96ce_f96_semi_china_exposure_proxy_idio_252d_slope_v024_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 252).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d idio mean
def f96ce_f96_semi_china_exposure_proxy_idio_504d_slope_v025_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 504).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d cumulative idio
def f96ce_f96_semi_china_exposure_proxy_cumidio_21d_slope_v026_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 21).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cumulative idio
def f96ce_f96_semi_china_exposure_proxy_cumidio_63d_slope_v027_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 63).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d cumulative idio
def f96ce_f96_semi_china_exposure_proxy_cumidio_126d_slope_v028_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 126).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d cumulative idio
def f96ce_f96_semi_china_exposure_proxy_cumidio_252d_slope_v029_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 252).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d cumulative idio
def f96ce_f96_semi_china_exposure_proxy_cumidio_504d_slope_v030_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_idio(o, c, 504).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d lead/lag1 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag1_21d_slope_v031_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(1), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d lead/lag1 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag1_63d_slope_v032_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(1), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d lead/lag1 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag1_126d_slope_v033_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(1), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d lead/lag1 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag1_252d_slope_v034_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(1), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d lead/lag1 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag1_504d_slope_v035_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(1), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d lead/lag3 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag3_21d_slope_v036_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(3), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d lead/lag3 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag3_63d_slope_v037_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(3), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d lead/lag3 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag3_126d_slope_v038_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(3), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d lead/lag3 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag3_252d_slope_v039_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(3), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d lead/lag3 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag3_504d_slope_v040_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(3), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d lead/lag5 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag5_21d_slope_v041_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(5), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d lead/lag5 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag5_63d_slope_v042_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(5), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d lead/lag5 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag5_126d_slope_v043_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(5), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d lead/lag5 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag5_252d_slope_v044_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(5), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d lead/lag5 corr
def f96ce_f96_semi_china_exposure_proxy_leadlag5_504d_slope_v045_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(china_exposure_index).shift(5), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d outperformance during china drawdown
def f96ce_f96_semi_china_exposure_proxy_outperfdd_21d_slope_v046_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 21)
    mask = (dd < 0).astype(float)
    base = ((o - c) * mask).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d outperformance during china drawdown
def f96ce_f96_semi_china_exposure_proxy_outperfdd_63d_slope_v047_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 63)
    mask = (dd < 0).astype(float)
    base = ((o - c) * mask).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d outperformance during china drawdown
def f96ce_f96_semi_china_exposure_proxy_outperfdd_126d_slope_v048_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 126)
    mask = (dd < 0).astype(float)
    base = ((o - c) * mask).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d outperformance during china drawdown
def f96ce_f96_semi_china_exposure_proxy_outperfdd_252d_slope_v049_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 252)
    mask = (dd < 0).astype(float)
    base = ((o - c) * mask).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d outperformance during china drawdown
def f96ce_f96_semi_china_exposure_proxy_outperfdd_504d_slope_v050_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    c = _f96ce_logret(china_exposure_index)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 504)
    mask = (dd < 0).astype(float)
    base = ((o - c) * mask).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d tracking error
def f96ce_f96_semi_china_exposure_proxy_trackerr_21d_slope_v051_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = _std(diff, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d tracking error
def f96ce_f96_semi_china_exposure_proxy_trackerr_63d_slope_v052_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = _std(diff, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d tracking error
def f96ce_f96_semi_china_exposure_proxy_trackerr_126d_slope_v053_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = _std(diff, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d tracking error
def f96ce_f96_semi_china_exposure_proxy_trackerr_252d_slope_v054_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = _std(diff, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d tracking error
def f96ce_f96_semi_china_exposure_proxy_trackerr_504d_slope_v055_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = _std(diff, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d china z-score interaction
def f96ce_f96_semi_china_exposure_proxy_chinazx_21d_slope_v056_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 21)
    o = _f96ce_ret(closeadj)
    base = (cz * o).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d china z-score interaction
def f96ce_f96_semi_china_exposure_proxy_chinazx_63d_slope_v057_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 63)
    o = _f96ce_ret(closeadj)
    base = (cz * o).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d china z-score interaction
def f96ce_f96_semi_china_exposure_proxy_chinazx_126d_slope_v058_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 126)
    o = _f96ce_ret(closeadj)
    base = (cz * o).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d china z-score interaction
def f96ce_f96_semi_china_exposure_proxy_chinazx_252d_slope_v059_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 252)
    o = _f96ce_ret(closeadj)
    base = (cz * o).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d china z-score interaction
def f96ce_f96_semi_china_exposure_proxy_chinazx_504d_slope_v060_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    cz = _z(_f96ce_ret(china_exposure_index), 504)
    o = _f96ce_ret(closeadj)
    base = (cz * o).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ema crossover diff own vs china
def f96ce_f96_semi_china_exposure_proxy_emacross_21d_slope_v061_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    base = (lo.ewm(span=5, adjust=False).mean() - lo.ewm(span=21, adjust=False).mean()) - (lc.ewm(span=5, adjust=False).mean() - lc.ewm(span=21, adjust=False).mean())
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ema crossover diff own vs china
def f96ce_f96_semi_china_exposure_proxy_emacross_63d_slope_v062_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    base = (lo.ewm(span=21, adjust=False).mean() - lo.ewm(span=63, adjust=False).mean()) - (lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=63, adjust=False).mean())
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ema crossover diff own vs china
def f96ce_f96_semi_china_exposure_proxy_emacross_126d_slope_v063_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    base = (lo.ewm(span=63, adjust=False).mean() - lo.ewm(span=126, adjust=False).mean()) - (lc.ewm(span=63, adjust=False).mean() - lc.ewm(span=126, adjust=False).mean())
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ema crossover diff own vs china
def f96ce_f96_semi_china_exposure_proxy_emacross_252d_slope_v064_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    base = (lo.ewm(span=126, adjust=False).mean() - lo.ewm(span=252, adjust=False).mean()) - (lc.ewm(span=126, adjust=False).mean() - lc.ewm(span=252, adjust=False).mean())
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ema crossover diff own vs china
def f96ce_f96_semi_china_exposure_proxy_emacross_504d_slope_v065_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lo = np.log(closeadj.replace(0, np.nan).abs())
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    base = (lo.ewm(span=252, adjust=False).mean() - lo.ewm(span=504, adjust=False).mean()) - (lc.ewm(span=252, adjust=False).mean() - lc.ewm(span=504, adjust=False).mean())
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d rolling corr own vs basket
def f96ce_f96_semi_china_exposure_proxy_corrbasket_21d_slope_v066_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rolling corr own vs basket
def f96ce_f96_semi_china_exposure_proxy_corrbasket_63d_slope_v067_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rolling corr own vs basket
def f96ce_f96_semi_china_exposure_proxy_corrbasket_126d_slope_v068_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rolling corr own vs basket
def f96ce_f96_semi_china_exposure_proxy_corrbasket_252d_slope_v069_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d rolling corr own vs basket
def f96ce_f96_semi_china_exposure_proxy_corrbasket_504d_slope_v070_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_corr(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d rolling beta own vs basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_21d_slope_v071_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rolling beta own vs basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_63d_slope_v072_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rolling beta own vs basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_126d_slope_v073_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rolling beta own vs basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_252d_slope_v074_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d rolling beta own vs basket
def f96ce_f96_semi_china_exposure_proxy_betabasket_504d_slope_v075_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _f96ce_roll_beta(_f96ce_ret(closeadj), _f96ce_ret(semi_basket_closeadj), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d basket-residualized idio mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_21d_slope_v076_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    base = _f96ce_idio(o, b, 21).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d basket-residualized idio mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_63d_slope_v077_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    base = _f96ce_idio(o, b, 63).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d basket-residualized idio mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_126d_slope_v078_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    base = _f96ce_idio(o, b, 126).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d basket-residualized idio mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_252d_slope_v079_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    base = _f96ce_idio(o, b, 252).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d basket-residualized idio mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_504d_slope_v080_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    base = _f96ce_idio(o, b, 504).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_21d_slope_v081_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    cov1 = o.rolling(21, min_periods=11).cov(c)
    var1 = c.rolling(21, min_periods=11).var()
    beta_c = cov1 / var1.replace(0, np.nan)
    resid1 = o - beta_c * c
    cov2 = resid1.rolling(21, min_periods=11).cov(b)
    var2 = b.rolling(21, min_periods=11).var()
    beta_b = cov2 / var2.replace(0, np.nan)
    base = (resid1 - beta_b * b).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_63d_slope_v082_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    cov1 = o.rolling(63, min_periods=32).cov(c)
    var1 = c.rolling(63, min_periods=32).var()
    beta_c = cov1 / var1.replace(0, np.nan)
    resid1 = o - beta_c * c
    cov2 = resid1.rolling(63, min_periods=32).cov(b)
    var2 = b.rolling(63, min_periods=32).var()
    beta_b = cov2 / var2.replace(0, np.nan)
    base = (resid1 - beta_b * b).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_126d_slope_v083_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    cov1 = o.rolling(126, min_periods=63).cov(c)
    var1 = c.rolling(126, min_periods=63).var()
    beta_c = cov1 / var1.replace(0, np.nan)
    resid1 = o - beta_c * c
    cov2 = resid1.rolling(126, min_periods=63).cov(b)
    var2 = b.rolling(126, min_periods=63).var()
    beta_b = cov2 / var2.replace(0, np.nan)
    base = (resid1 - beta_b * b).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_252d_slope_v084_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    cov1 = o.rolling(252, min_periods=126).cov(c)
    var1 = c.rolling(252, min_periods=126).var()
    beta_c = cov1 / var1.replace(0, np.nan)
    resid1 = o - beta_c * c
    cov2 = resid1.rolling(252, min_periods=126).cov(b)
    var2 = b.rolling(252, min_periods=126).var()
    beta_b = cov2 / var2.replace(0, np.nan)
    base = (resid1 - beta_b * b).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_504d_slope_v085_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    cov1 = o.rolling(504, min_periods=252).cov(c)
    var1 = c.rolling(504, min_periods=252).var()
    beta_c = cov1 / var1.replace(0, np.nan)
    resid1 = o - beta_c * c
    cov2 = resid1.rolling(504, min_periods=252).cov(b)
    var2 = b.rolling(504, min_periods=252).var()
    beta_b = cov2 / var2.replace(0, np.nan)
    base = (resid1 - beta_b * b).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d relative log return vs basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_21d_slope_v086_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    base = diff.rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d relative log return vs basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_63d_slope_v087_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    base = diff.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d relative log return vs basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_126d_slope_v088_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    base = diff.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d relative log return vs basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_252d_slope_v089_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    base = diff.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d relative log return vs basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_504d_slope_v090_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    base = diff.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d relative log return vs china
def f96ce_f96_semi_china_exposure_proxy_relretchina_21d_slope_v091_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = diff.rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d relative log return vs china
def f96ce_f96_semi_china_exposure_proxy_relretchina_63d_slope_v092_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = diff.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d relative log return vs china
def f96ce_f96_semi_china_exposure_proxy_relretchina_126d_slope_v093_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = diff.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d relative log return vs china
def f96ce_f96_semi_china_exposure_proxy_relretchina_252d_slope_v094_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = diff.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d relative log return vs china
def f96ce_f96_semi_china_exposure_proxy_relretchina_504d_slope_v095_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = diff.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d down-day corr
def f96ce_f96_semi_china_exposure_proxy_corrneg_21d_slope_v096_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d down-day corr
def f96ce_f96_semi_china_exposure_proxy_corrneg_63d_slope_v097_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d down-day corr
def f96ce_f96_semi_china_exposure_proxy_corrneg_126d_slope_v098_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d down-day corr
def f96ce_f96_semi_china_exposure_proxy_corrneg_252d_slope_v099_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d down-day corr
def f96ce_f96_semi_china_exposure_proxy_corrneg_504d_slope_v100_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_21d_slope_v101_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_63d_slope_v102_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_126d_slope_v103_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_252d_slope_v104_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_504d_slope_v105_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    base = _f96ce_roll_corr(o.where(mask), c.where(mask), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d china drawdown z-score
def f96ce_f96_semi_china_exposure_proxy_chinadd_21d_slope_v106_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 21)
    base = _z(dd, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d china drawdown z-score
def f96ce_f96_semi_china_exposure_proxy_chinadd_63d_slope_v107_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 63)
    base = _z(dd, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d china drawdown z-score
def f96ce_f96_semi_china_exposure_proxy_chinadd_126d_slope_v108_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 126)
    base = _z(dd, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d china drawdown z-score
def f96ce_f96_semi_china_exposure_proxy_chinadd_252d_slope_v109_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 252)
    base = _z(dd, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d china drawdown z-score
def f96ce_f96_semi_china_exposure_proxy_chinadd_504d_slope_v110_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 504)
    base = _z(dd, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d own log-return during china drawdown
def f96ce_f96_semi_china_exposure_proxy_owninchidd_21d_slope_v111_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 21)
    mask = (dd < 0).astype(float)
    base = (o * mask).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d own log-return during china drawdown
def f96ce_f96_semi_china_exposure_proxy_owninchidd_63d_slope_v112_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 63)
    mask = (dd < 0).astype(float)
    base = (o * mask).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d own log-return during china drawdown
def f96ce_f96_semi_china_exposure_proxy_owninchidd_126d_slope_v113_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 126)
    mask = (dd < 0).astype(float)
    base = (o * mask).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d own log-return during china drawdown
def f96ce_f96_semi_china_exposure_proxy_owninchidd_252d_slope_v114_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 252)
    mask = (dd < 0).astype(float)
    base = (o * mask).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d own log-return during china drawdown
def f96ce_f96_semi_china_exposure_proxy_owninchidd_504d_slope_v115_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 504)
    mask = (dd < 0).astype(float)
    base = (o * mask).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d signed outperformance
def f96ce_f96_semi_china_exposure_proxy_signoutperf_21d_slope_v116_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = pd.Series(np.sign(diff), index=diff.index).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed outperformance
def f96ce_f96_semi_china_exposure_proxy_signoutperf_63d_slope_v117_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = pd.Series(np.sign(diff), index=diff.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d signed outperformance
def f96ce_f96_semi_china_exposure_proxy_signoutperf_126d_slope_v118_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = pd.Series(np.sign(diff), index=diff.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signed outperformance
def f96ce_f96_semi_china_exposure_proxy_signoutperf_252d_slope_v119_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = pd.Series(np.sign(diff), index=diff.index).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d signed outperformance
def f96ce_f96_semi_china_exposure_proxy_signoutperf_504d_slope_v120_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    base = pd.Series(np.sign(diff), index=diff.index).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d basket vs china log ratio
def f96ce_f96_semi_china_exposure_proxy_basketchina_21d_slope_v121_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    base = r - _mean(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d basket vs china log ratio
def f96ce_f96_semi_china_exposure_proxy_basketchina_63d_slope_v122_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    base = r - _mean(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d basket vs china log ratio
def f96ce_f96_semi_china_exposure_proxy_basketchina_126d_slope_v123_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    base = r - _mean(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d basket vs china log ratio
def f96ce_f96_semi_china_exposure_proxy_basketchina_252d_slope_v124_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    base = r - _mean(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d basket vs china log ratio
def f96ce_f96_semi_china_exposure_proxy_basketchina_504d_slope_v125_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    base = r - _mean(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d own vol
def f96ce_f96_semi_china_exposure_proxy_ownvol_21d_slope_v126_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _std(_f96ce_logret(closeadj), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d own vol
def f96ce_f96_semi_china_exposure_proxy_ownvol_63d_slope_v127_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _std(_f96ce_logret(closeadj), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d own vol
def f96ce_f96_semi_china_exposure_proxy_ownvol_126d_slope_v128_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _std(_f96ce_logret(closeadj), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d own vol
def f96ce_f96_semi_china_exposure_proxy_ownvol_252d_slope_v129_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _std(_f96ce_logret(closeadj), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d own vol
def f96ce_f96_semi_china_exposure_proxy_ownvol_504d_slope_v130_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    base = _std(_f96ce_logret(closeadj), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d beta ratio basket/china
def f96ce_f96_semi_china_exposure_proxy_betaratio_21d_slope_v131_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 21)
    bc = _f96ce_roll_beta(o, c, 21)
    base = bb / bc.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d beta ratio basket/china
def f96ce_f96_semi_china_exposure_proxy_betaratio_63d_slope_v132_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 63)
    bc = _f96ce_roll_beta(o, c, 63)
    base = bb / bc.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d beta ratio basket/china
def f96ce_f96_semi_china_exposure_proxy_betaratio_126d_slope_v133_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 126)
    bc = _f96ce_roll_beta(o, c, 126)
    base = bb / bc.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d beta ratio basket/china
def f96ce_f96_semi_china_exposure_proxy_betaratio_252d_slope_v134_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 252)
    bc = _f96ce_roll_beta(o, c, 252)
    base = bb / bc.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d beta ratio basket/china
def f96ce_f96_semi_china_exposure_proxy_betaratio_504d_slope_v135_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 504)
    bc = _f96ce_roll_beta(o, c, 504)
    base = bb / bc.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d corr-difference (own,china) minus (own,basket)
def f96ce_f96_semi_china_exposure_proxy_corrdiff_21d_slope_v136_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_roll_corr(o, c, 21) - _f96ce_roll_corr(o, b, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d corr-difference
def f96ce_f96_semi_china_exposure_proxy_corrdiff_63d_slope_v137_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_roll_corr(o, c, 63) - _f96ce_roll_corr(o, b, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d corr-difference
def f96ce_f96_semi_china_exposure_proxy_corrdiff_126d_slope_v138_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_roll_corr(o, c, 126) - _f96ce_roll_corr(o, b, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d corr-difference
def f96ce_f96_semi_china_exposure_proxy_corrdiff_252d_slope_v139_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_roll_corr(o, c, 252) - _f96ce_roll_corr(o, b, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d corr-difference
def f96ce_f96_semi_china_exposure_proxy_corrdiff_504d_slope_v140_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    base = _f96ce_roll_corr(o, c, 504) - _f96ce_roll_corr(o, b, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d composite score
def f96ce_f96_semi_china_exposure_proxy_composite_21d_slope_v141_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 21)
    bb = _f96ce_roll_beta(o, c, 21)
    idio = _f96ce_idio(o, c, 21).rolling(21, min_periods=11).mean()
    base = _z(cc, 252) + _z(bb, 252) - _z(idio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d composite score
def f96ce_f96_semi_china_exposure_proxy_composite_63d_slope_v142_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 63)
    bb = _f96ce_roll_beta(o, c, 63)
    idio = _f96ce_idio(o, c, 63).rolling(63, min_periods=32).mean()
    base = _z(cc, 252) + _z(bb, 252) - _z(idio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d composite score
def f96ce_f96_semi_china_exposure_proxy_composite_126d_slope_v143_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 126)
    bb = _f96ce_roll_beta(o, c, 126)
    idio = _f96ce_idio(o, c, 126).rolling(126, min_periods=63).mean()
    base = _z(cc, 252) + _z(bb, 252) - _z(idio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d composite score
def f96ce_f96_semi_china_exposure_proxy_composite_252d_slope_v144_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 252)
    bb = _f96ce_roll_beta(o, c, 252)
    idio = _f96ce_idio(o, c, 252).rolling(252, min_periods=126).mean()
    base = _z(cc, 504) + _z(bb, 504) - _z(idio, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d composite score
def f96ce_f96_semi_china_exposure_proxy_composite_504d_slope_v145_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 504)
    bb = _f96ce_roll_beta(o, c, 504)
    idio = _f96ce_idio(o, c, 504).rolling(504, min_periods=252).mean()
    base = _z(cc, 504) + _z(bb, 504) - _z(idio, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d robust z of own minus china return
def f96ce_f96_semi_china_exposure_proxy_robustz_21d_slope_v146_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(21, min_periods=11).median()
    mad = (diff - med).abs().rolling(21, min_periods=11).median()
    base = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z of own minus china return
def f96ce_f96_semi_china_exposure_proxy_robustz_63d_slope_v147_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(63, min_periods=32).median()
    mad = (diff - med).abs().rolling(63, min_periods=32).median()
    base = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d robust z of own minus china return
def f96ce_f96_semi_china_exposure_proxy_robustz_126d_slope_v148_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(126, min_periods=63).median()
    mad = (diff - med).abs().rolling(126, min_periods=63).median()
    base = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d robust z of own minus china return
def f96ce_f96_semi_china_exposure_proxy_robustz_252d_slope_v149_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(252, min_periods=126).median()
    mad = (diff - med).abs().rolling(252, min_periods=126).median()
    base = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d robust z of own minus china return
def f96ce_f96_semi_china_exposure_proxy_robustz_504d_slope_v150_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(504, min_periods=252).median()
    mad = (diff - med).abs().rolling(504, min_periods=252).median()
    base = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)
