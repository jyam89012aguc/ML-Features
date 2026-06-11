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
def _f14_own_ret(s):
    return s.pct_change()


def _f14_roll_beta(o, b, w):
    cov = o.rolling(w, min_periods=max(2, w // 2)).cov(b)
    var = b.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f14_residual(o, b, w):
    beta = _f14_roll_beta(o, b, w)
    return o - beta * b


def _f14_idio_vol(o, b, w):
    res = o - _f14_roll_beta(o, b, w) * b
    return res.rolling(w, min_periods=max(2, w // 2)).std()


# 21d ratio of idio to total vol
def f14iv_f14_semi_idiosyncratic_volatility_idiototratio_21d_base_v076_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    tv = _std(o, 21)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of idio to total vol
def f14iv_f14_semi_idiosyncratic_volatility_idiototratio_63d_base_v077_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    tv = _std(o, 63)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio of idio to total vol
def f14iv_f14_semi_idiosyncratic_volatility_idiototratio_126d_base_v078_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    tv = _std(o, 126)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of idio to total vol
def f14iv_f14_semi_idiosyncratic_volatility_idiototratio_252d_base_v079_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    tv = _std(o, 252)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of idio to total vol
def f14iv_f14_semi_idiosyncratic_volatility_idiototratio_504d_base_v080_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    tv = _std(o, 504)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of cumulative residual from peak
def f14iv_f14_semi_idiosyncratic_volatility_alphadd_21d_base_v081_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    cum = res.rolling(21, min_periods=11).sum()
    result = cum - _max(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of cumulative residual from peak
def f14iv_f14_semi_idiosyncratic_volatility_alphadd_63d_base_v082_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    cum = res.rolling(63, min_periods=32).sum()
    result = cum - _max(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of cumulative residual from peak
def f14iv_f14_semi_idiosyncratic_volatility_alphadd_126d_base_v083_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    cum = res.rolling(126, min_periods=63).sum()
    result = cum - _max(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of cumulative residual from peak
def f14iv_f14_semi_idiosyncratic_volatility_alphadd_252d_base_v084_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    cum = res.rolling(252, min_periods=126).sum()
    result = cum - _max(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of cumulative residual from peak
def f14iv_f14_semi_idiosyncratic_volatility_alphadd_504d_base_v085_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    cum = res.rolling(504, min_periods=252).sum()
    result = cum - _max(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of cumulative residual from trough
def f14iv_f14_semi_idiosyncratic_volatility_alphaup_21d_base_v086_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    cum = res.rolling(21, min_periods=11).sum()
    result = cum - _min(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of cumulative residual from trough
def f14iv_f14_semi_idiosyncratic_volatility_alphaup_63d_base_v087_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    cum = res.rolling(63, min_periods=32).sum()
    result = cum - _min(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of cumulative residual from trough
def f14iv_f14_semi_idiosyncratic_volatility_alphaup_126d_base_v088_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    cum = res.rolling(126, min_periods=63).sum()
    result = cum - _min(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of cumulative residual from trough
def f14iv_f14_semi_idiosyncratic_volatility_alphaup_252d_base_v089_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    cum = res.rolling(252, min_periods=126).sum()
    result = cum - _min(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of cumulative residual from trough
def f14iv_f14_semi_idiosyncratic_volatility_alphaup_504d_base_v090_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    cum = res.rolling(504, min_periods=252).sum()
    result = cum - _min(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolpos_21d_base_v091_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    lo = _min(iv, 21)
    hi = _max(iv, 21)
    result = (iv - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolpos_63d_base_v092_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    lo = _min(iv, 63)
    hi = _max(iv, 63)
    result = (iv - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolpos_126d_base_v093_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    lo = _min(iv, 126)
    hi = _max(iv, 126)
    result = (iv - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolpos_252d_base_v094_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    lo = _min(iv, 252)
    hi = _max(iv, 252)
    result = (iv - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolpos_504d_base_v095_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    lo = _min(iv, 504)
    hi = _max(iv, 504)
    result = (iv - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in idio vol over 21d
def f14iv_f14_semi_idiosyncratic_volatility_idiovolroc_21d_base_v096_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    result = iv - iv.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in idio vol over 63d
def f14iv_f14_semi_idiosyncratic_volatility_idiovolroc_63d_base_v097_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    result = iv - iv.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in idio vol over 126d
def f14iv_f14_semi_idiosyncratic_volatility_idiovolroc_126d_base_v098_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    result = iv - iv.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in idio vol over 252d
def f14iv_f14_semi_idiosyncratic_volatility_idiovolroc_252d_base_v099_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    result = iv - iv.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in idio vol over 504d
def f14iv_f14_semi_idiosyncratic_volatility_idiovolroc_504d_base_v100_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    result = iv - iv.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lag-1 autocorr of residual
def f14iv_f14_semi_idiosyncratic_volatility_resac1_21d_base_v101_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = res.rolling(21, min_periods=10).corr(res.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lag-1 autocorr of residual
def f14iv_f14_semi_idiosyncratic_volatility_resac1_63d_base_v102_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = res.rolling(63, min_periods=31).corr(res.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lag-1 autocorr of residual
def f14iv_f14_semi_idiosyncratic_volatility_resac1_126d_base_v103_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = res.rolling(126, min_periods=63).corr(res.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lag-1 autocorr of residual
def f14iv_f14_semi_idiosyncratic_volatility_resac1_252d_base_v104_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = res.rolling(252, min_periods=126).corr(res.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lag-1 autocorr of residual
def f14iv_f14_semi_idiosyncratic_volatility_resac1_504d_base_v105_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = res.rolling(504, min_periods=252).corr(res.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d idio vol vs basket vol normalized
def f14iv_f14_semi_idiosyncratic_volatility_idiobasnorm_21d_base_v106_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    bv = _std(b, 21)
    result = iv / bv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d idio vol vs basket vol normalized
def f14iv_f14_semi_idiosyncratic_volatility_idiobasnorm_63d_base_v107_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    bv = _std(b, 63)
    result = iv / bv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d idio vol vs basket vol normalized
def f14iv_f14_semi_idiosyncratic_volatility_idiobasnorm_126d_base_v108_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    bv = _std(b, 126)
    result = iv / bv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d idio vol vs basket vol normalized
def f14iv_f14_semi_idiosyncratic_volatility_idiobasnorm_252d_base_v109_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    bv = _std(b, 252)
    result = iv / bv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d idio vol vs basket vol normalized
def f14iv_f14_semi_idiosyncratic_volatility_idiobasnorm_504d_base_v110_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    bv = _std(b, 504)
    result = iv / bv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of extreme residual days (|res| > 2-sigma)
def f14iv_f14_semi_idiosyncratic_volatility_resextrct_21d_base_v111_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    sd = _std(res, 21)
    result = (res.abs() > 2 * sd).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of extreme residual days (|res| > 2-sigma)
def f14iv_f14_semi_idiosyncratic_volatility_resextrct_63d_base_v112_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    sd = _std(res, 63)
    result = (res.abs() > 2 * sd).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of extreme residual days (|res| > 2-sigma)
def f14iv_f14_semi_idiosyncratic_volatility_resextrct_126d_base_v113_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    sd = _std(res, 126)
    result = (res.abs() > 2 * sd).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of extreme residual days (|res| > 2-sigma)
def f14iv_f14_semi_idiosyncratic_volatility_resextrct_252d_base_v114_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    sd = _std(res, 252)
    result = (res.abs() > 2 * sd).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of extreme residual days (|res| > 2-sigma)
def f14iv_f14_semi_idiosyncratic_volatility_resextrct_504d_base_v115_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    sd = _std(res, 504)
    result = (res.abs() > 2 * sd).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative absolute residual
def f14iv_f14_semi_idiosyncratic_volatility_abscumres_21d_base_v116_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = res.abs().rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative absolute residual
def f14iv_f14_semi_idiosyncratic_volatility_abscumres_63d_base_v117_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = res.abs().rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative absolute residual
def f14iv_f14_semi_idiosyncratic_volatility_abscumres_126d_base_v118_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = res.abs().rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative absolute residual
def f14iv_f14_semi_idiosyncratic_volatility_abscumres_252d_base_v119_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = res.abs().rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative absolute residual
def f14iv_f14_semi_idiosyncratic_volatility_abscumres_504d_base_v120_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = res.abs().rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# idio-vol EMA crossover 5v21
def f14iv_f14_semi_idiosyncratic_volatility_idioema_5v21_base_v121_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    result = iv.ewm(span=5, adjust=False).mean() - iv.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# idio-vol EMA crossover 21v63
def f14iv_f14_semi_idiosyncratic_volatility_idioema_21v63_base_v122_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    result = iv.ewm(span=21, adjust=False).mean() - iv.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# idio-vol EMA crossover 63v126
def f14iv_f14_semi_idiosyncratic_volatility_idioema_63v126_base_v123_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    result = iv.ewm(span=63, adjust=False).mean() - iv.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# idio-vol EMA crossover 126v252
def f14iv_f14_semi_idiosyncratic_volatility_idioema_126v252_base_v124_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    result = iv.ewm(span=126, adjust=False).mean() - iv.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# idio-vol EMA crossover 252v504
def f14iv_f14_semi_idiosyncratic_volatility_idioema_252v504_base_v125_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    result = iv.ewm(span=252, adjust=False).mean() - iv.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of rolling beta (beta stability)
def f14iv_f14_semi_idiosyncratic_volatility_betastab_21d_base_v126_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    beta = _f14_roll_beta(o, b, 21)
    result = _std(beta, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of rolling beta (beta stability)
def f14iv_f14_semi_idiosyncratic_volatility_betastab_63d_base_v127_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    beta = _f14_roll_beta(o, b, 63)
    result = _std(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of rolling beta (beta stability)
def f14iv_f14_semi_idiosyncratic_volatility_betastab_126d_base_v128_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    beta = _f14_roll_beta(o, b, 126)
    result = _std(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of rolling beta (beta stability)
def f14iv_f14_semi_idiosyncratic_volatility_betastab_252d_base_v129_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    beta = _f14_roll_beta(o, b, 252)
    result = _std(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of rolling beta (beta stability)
def f14iv_f14_semi_idiosyncratic_volatility_betastab_504d_base_v130_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    beta = _f14_roll_beta(o, b, 504)
    result = _std(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d alpha t-stat proxy
def f14iv_f14_semi_idiosyncratic_volatility_alphat_21d_base_v131_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = _mean(res, 21) / (_std(res, 21) / np.sqrt(21)).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d alpha t-stat proxy
def f14iv_f14_semi_idiosyncratic_volatility_alphat_63d_base_v132_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = _mean(res, 63) / (_std(res, 63) / np.sqrt(63)).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d alpha t-stat proxy
def f14iv_f14_semi_idiosyncratic_volatility_alphat_126d_base_v133_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = _mean(res, 126) / (_std(res, 126) / np.sqrt(126)).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d alpha t-stat proxy
def f14iv_f14_semi_idiosyncratic_volatility_alphat_252d_base_v134_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = _mean(res, 252) / (_std(res, 252) / np.sqrt(252)).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d alpha t-stat proxy
def f14iv_f14_semi_idiosyncratic_volatility_alphat_504d_base_v135_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = _mean(res, 504) / (_std(res, 504) / np.sqrt(504)).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of |residual| sum to |basket| sum
def f14iv_f14_semi_idiosyncratic_volatility_idiopath_21d_base_v136_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    num = res.abs().rolling(21, min_periods=11).sum()
    den = b.abs().rolling(21, min_periods=11).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of |residual| sum to |basket| sum
def f14iv_f14_semi_idiosyncratic_volatility_idiopath_63d_base_v137_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    num = res.abs().rolling(63, min_periods=32).sum()
    den = b.abs().rolling(63, min_periods=32).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio of |residual| sum to |basket| sum
def f14iv_f14_semi_idiosyncratic_volatility_idiopath_126d_base_v138_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    num = res.abs().rolling(126, min_periods=63).sum()
    den = b.abs().rolling(126, min_periods=63).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of |residual| sum to |basket| sum
def f14iv_f14_semi_idiosyncratic_volatility_idiopath_252d_base_v139_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    num = res.abs().rolling(252, min_periods=126).sum()
    den = b.abs().rolling(252, min_periods=126).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of |residual| sum to |basket| sum
def f14iv_f14_semi_idiosyncratic_volatility_idiopath_504d_base_v140_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    num = res.abs().rolling(504, min_periods=252).sum()
    den = b.abs().rolling(504, min_periods=252).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# idio vol composite short (z21+z63+z126)
def f14iv_f14_semi_idiosyncratic_volatility_idiovolcompshort_63d_base_v141_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    result = _z(iv, 21) + _z(iv, 63) + _z(iv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# idio vol composite long (z63+z126+z252)
def f14iv_f14_semi_idiosyncratic_volatility_idiovolcomplong_252d_base_v142_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    result = _z(iv, 63) + _z(iv, 126) + _z(iv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# idio vol regime divergence
def f14iv_f14_semi_idiosyncratic_volatility_idiovolregdiv_63d_base_v143_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    short = np.sign(iv.ewm(span=21, adjust=False).mean() - iv.ewm(span=63, adjust=False).mean())
    long = np.sign(iv.ewm(span=126, adjust=False).mean() - iv.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=iv.index)
    return result.replace([np.inf, -np.inf], np.nan)


# alpha quality 63d (IR x hit)
def f14iv_f14_semi_idiosyncratic_volatility_alphaquality63_63d_base_v144_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    ir = _mean(res, 63) / _std(res, 63).replace(0, np.nan)
    hit = (res > 0).astype(float).rolling(63, min_periods=32).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


# alpha quality 252d (IR x hit)
def f14iv_f14_semi_idiosyncratic_volatility_alphaquality252_252d_base_v145_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    ir = _mean(res, 252) / _std(res, 252).replace(0, np.nan)
    hit = (res > 0).astype(float).rolling(252, min_periods=126).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 21d residual conditional on basket-up days
def f14iv_f14_semi_idiosyncratic_volatility_rescondup_21d_base_v146_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = _mean(res.where(b > 0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d residual conditional on basket-up days
def f14iv_f14_semi_idiosyncratic_volatility_rescondup_63d_base_v147_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = _mean(res.where(b > 0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d residual conditional on basket-up days
def f14iv_f14_semi_idiosyncratic_volatility_rescondup_126d_base_v148_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = _mean(res.where(b > 0), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d residual conditional on basket-up days
def f14iv_f14_semi_idiosyncratic_volatility_rescondup_252d_base_v149_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = _mean(res.where(b > 0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d residual conditional on basket-up days
def f14iv_f14_semi_idiosyncratic_volatility_rescondup_504d_base_v150_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = _mean(res.where(b > 0), 504)
    return result.replace([np.inf, -np.inf], np.nan)
