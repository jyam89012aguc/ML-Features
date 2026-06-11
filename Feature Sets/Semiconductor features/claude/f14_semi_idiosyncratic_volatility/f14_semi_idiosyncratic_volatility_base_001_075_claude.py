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


# 21d idiosyncratic volatility (residual std)
def f14iv_f14_semi_idiosyncratic_volatility_idiovol_21d_base_v001_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    result = _f14_idio_vol(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d idiosyncratic volatility (residual std)
def f14iv_f14_semi_idiosyncratic_volatility_idiovol_63d_base_v002_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    result = _f14_idio_vol(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d idiosyncratic volatility (residual std)
def f14iv_f14_semi_idiosyncratic_volatility_idiovol_126d_base_v003_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    result = _f14_idio_vol(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d idiosyncratic volatility (residual std)
def f14iv_f14_semi_idiosyncratic_volatility_idiovol_252d_base_v004_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    result = _f14_idio_vol(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d idiosyncratic volatility (residual std)
def f14iv_f14_semi_idiosyncratic_volatility_idiovol_504d_base_v005_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    result = _f14_idio_vol(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d idio-vol share of total vol
def f14iv_f14_semi_idiosyncratic_volatility_idioshare_21d_base_v006_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    tv = _std(o, 21)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d idio-vol share of total vol
def f14iv_f14_semi_idiosyncratic_volatility_idioshare_63d_base_v007_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    tv = _std(o, 63)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d idio-vol share of total vol
def f14iv_f14_semi_idiosyncratic_volatility_idioshare_126d_base_v008_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    tv = _std(o, 126)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d idio-vol share of total vol
def f14iv_f14_semi_idiosyncratic_volatility_idioshare_252d_base_v009_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    tv = _std(o, 252)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d idio-vol share of total vol
def f14iv_f14_semi_idiosyncratic_volatility_idioshare_504d_base_v010_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    tv = _std(o, 504)
    result = iv / tv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of residual (rolling alpha)
def f14iv_f14_semi_idiosyncratic_volatility_alpha_21d_base_v011_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = _mean(res, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of residual (rolling alpha)
def f14iv_f14_semi_idiosyncratic_volatility_alpha_63d_base_v012_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = _mean(res, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of residual (rolling alpha)
def f14iv_f14_semi_idiosyncratic_volatility_alpha_126d_base_v013_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = _mean(res, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of residual (rolling alpha)
def f14iv_f14_semi_idiosyncratic_volatility_alpha_252d_base_v014_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = _mean(res, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of residual (rolling alpha)
def f14iv_f14_semi_idiosyncratic_volatility_alpha_504d_base_v015_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = _mean(res, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolz_21d_base_v016_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    result = _z(iv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolz_63d_base_v017_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    result = _z(iv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolz_126d_base_v018_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    result = _z(iv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolz_252d_base_v019_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    result = _z(iv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolz_504d_base_v020_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    result = _z(iv, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolrz_21d_base_v021_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    med = iv.rolling(21, min_periods=11).median()
    mad = (iv - med).abs().rolling(21, min_periods=11).median()
    result = (iv - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolrz_63d_base_v022_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    med = iv.rolling(63, min_periods=32).median()
    mad = (iv - med).abs().rolling(63, min_periods=32).median()
    result = (iv - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolrz_126d_base_v023_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    med = iv.rolling(126, min_periods=63).median()
    mad = (iv - med).abs().rolling(126, min_periods=63).median()
    result = (iv - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolrz_252d_base_v024_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    med = iv.rolling(252, min_periods=126).median()
    mad = (iv - med).abs().rolling(252, min_periods=126).median()
    result = (iv - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of idio vol
def f14iv_f14_semi_idiosyncratic_volatility_idiovolrz_504d_base_v025_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    med = iv.rolling(504, min_periods=252).median()
    mad = (iv - med).abs().rolling(504, min_periods=252).median()
    result = (iv - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of residual
def f14iv_f14_semi_idiosyncratic_volatility_resskew_21d_base_v026_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = res.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of residual
def f14iv_f14_semi_idiosyncratic_volatility_resskew_63d_base_v027_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = res.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of residual
def f14iv_f14_semi_idiosyncratic_volatility_resskew_126d_base_v028_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = res.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of residual
def f14iv_f14_semi_idiosyncratic_volatility_resskew_252d_base_v029_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = res.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of residual
def f14iv_f14_semi_idiosyncratic_volatility_resskew_504d_base_v030_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = res.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of residual
def f14iv_f14_semi_idiosyncratic_volatility_reskurt_21d_base_v031_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = res.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of residual
def f14iv_f14_semi_idiosyncratic_volatility_reskurt_63d_base_v032_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = res.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of residual
def f14iv_f14_semi_idiosyncratic_volatility_reskurt_126d_base_v033_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = res.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of residual
def f14iv_f14_semi_idiosyncratic_volatility_reskurt_252d_base_v034_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = res.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of residual
def f14iv_f14_semi_idiosyncratic_volatility_reskurt_504d_base_v035_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = res.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative residual return
def f14iv_f14_semi_idiosyncratic_volatility_alphacum_21d_base_v036_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = res.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative residual return
def f14iv_f14_semi_idiosyncratic_volatility_alphacum_63d_base_v037_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = res.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative residual return
def f14iv_f14_semi_idiosyncratic_volatility_alphacum_126d_base_v038_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = res.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative residual return
def f14iv_f14_semi_idiosyncratic_volatility_alphacum_252d_base_v039_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = res.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative residual return
def f14iv_f14_semi_idiosyncratic_volatility_alphacum_504d_base_v040_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = res.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max residual
def f14iv_f14_semi_idiosyncratic_volatility_maxres_21d_base_v041_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = _max(res, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max residual
def f14iv_f14_semi_idiosyncratic_volatility_maxres_63d_base_v042_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = _max(res, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max residual
def f14iv_f14_semi_idiosyncratic_volatility_maxres_126d_base_v043_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = _max(res, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max residual
def f14iv_f14_semi_idiosyncratic_volatility_maxres_252d_base_v044_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = _max(res, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max residual
def f14iv_f14_semi_idiosyncratic_volatility_maxres_504d_base_v045_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = _max(res, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min residual
def f14iv_f14_semi_idiosyncratic_volatility_minres_21d_base_v046_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = _min(res, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min residual
def f14iv_f14_semi_idiosyncratic_volatility_minres_63d_base_v047_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = _min(res, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min residual
def f14iv_f14_semi_idiosyncratic_volatility_minres_126d_base_v048_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = _min(res, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min residual
def f14iv_f14_semi_idiosyncratic_volatility_minres_252d_base_v049_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = _min(res, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min residual
def f14iv_f14_semi_idiosyncratic_volatility_minres_504d_base_v050_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = _min(res, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of residual
def f14iv_f14_semi_idiosyncratic_volatility_resrange_21d_base_v051_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = _max(res, 21) - _min(res, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of residual
def f14iv_f14_semi_idiosyncratic_volatility_resrange_63d_base_v052_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = _max(res, 63) - _min(res, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of residual
def f14iv_f14_semi_idiosyncratic_volatility_resrange_126d_base_v053_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = _max(res, 126) - _min(res, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of residual
def f14iv_f14_semi_idiosyncratic_volatility_resrange_252d_base_v054_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = _max(res, 252) - _min(res, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of residual
def f14iv_f14_semi_idiosyncratic_volatility_resrange_504d_base_v055_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = _max(res, 504) - _min(res, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive residuals
def f14iv_f14_semi_idiosyncratic_volatility_reshit_21d_base_v056_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = (res > 0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive residuals
def f14iv_f14_semi_idiosyncratic_volatility_reshit_63d_base_v057_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = (res > 0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive residuals
def f14iv_f14_semi_idiosyncratic_volatility_reshit_126d_base_v058_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = (res > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive residuals
def f14iv_f14_semi_idiosyncratic_volatility_reshit_252d_base_v059_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = (res > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive residuals
def f14iv_f14_semi_idiosyncratic_volatility_reshit_504d_base_v060_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = (res > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R-squared proxy (basket explanatory power)
def f14iv_f14_semi_idiosyncratic_volatility_r2proxy_21d_base_v061_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv2 = _f14_idio_vol(o, b, 21) ** 2
    tv2 = _std(o, 21) ** 2
    result = 1.0 - iv2 / tv2.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d R-squared proxy (basket explanatory power)
def f14iv_f14_semi_idiosyncratic_volatility_r2proxy_63d_base_v062_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv2 = _f14_idio_vol(o, b, 63) ** 2
    tv2 = _std(o, 63) ** 2
    result = 1.0 - iv2 / tv2.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d R-squared proxy (basket explanatory power)
def f14iv_f14_semi_idiosyncratic_volatility_r2proxy_126d_base_v063_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv2 = _f14_idio_vol(o, b, 126) ** 2
    tv2 = _std(o, 126) ** 2
    result = 1.0 - iv2 / tv2.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R-squared proxy (basket explanatory power)
def f14iv_f14_semi_idiosyncratic_volatility_r2proxy_252d_base_v064_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv2 = _f14_idio_vol(o, b, 252) ** 2
    tv2 = _std(o, 252) ** 2
    result = 1.0 - iv2 / tv2.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R-squared proxy (basket explanatory power)
def f14iv_f14_semi_idiosyncratic_volatility_r2proxy_504d_base_v065_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv2 = _f14_idio_vol(o, b, 504) ** 2
    tv2 = _std(o, 504) ** 2
    result = 1.0 - iv2 / tv2.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d alpha-to-idio-vol ratio (idio Sharpe)
def f14iv_f14_semi_idiosyncratic_volatility_idiosharpe_21d_base_v066_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 21)
    result = _mean(res, 21) / _std(res, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d alpha-to-idio-vol ratio (idio Sharpe)
def f14iv_f14_semi_idiosyncratic_volatility_idiosharpe_63d_base_v067_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 63)
    result = _mean(res, 63) / _std(res, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d alpha-to-idio-vol ratio (idio Sharpe)
def f14iv_f14_semi_idiosyncratic_volatility_idiosharpe_126d_base_v068_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 126)
    result = _mean(res, 126) / _std(res, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d alpha-to-idio-vol ratio (idio Sharpe)
def f14iv_f14_semi_idiosyncratic_volatility_idiosharpe_252d_base_v069_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 252)
    result = _mean(res, 252) / _std(res, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d alpha-to-idio-vol ratio (idio Sharpe)
def f14iv_f14_semi_idiosyncratic_volatility_idiosharpe_504d_base_v070_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    res = _f14_residual(o, b, 504)
    result = _mean(res, 504) / _std(res, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d idio vol minus basket vol
def f14iv_f14_semi_idiosyncratic_volatility_idiominusbasvol_21d_base_v071_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 21)
    bv = _std(b, 21)
    result = iv - bv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d idio vol minus basket vol
def f14iv_f14_semi_idiosyncratic_volatility_idiominusbasvol_63d_base_v072_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 63)
    bv = _std(b, 63)
    result = iv - bv
    return result.replace([np.inf, -np.inf], np.nan)


# 126d idio vol minus basket vol
def f14iv_f14_semi_idiosyncratic_volatility_idiominusbasvol_126d_base_v073_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 126)
    bv = _std(b, 126)
    result = iv - bv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d idio vol minus basket vol
def f14iv_f14_semi_idiosyncratic_volatility_idiominusbasvol_252d_base_v074_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 252)
    bv = _std(b, 252)
    result = iv - bv
    return result.replace([np.inf, -np.inf], np.nan)


# 504d idio vol minus basket vol
def f14iv_f14_semi_idiosyncratic_volatility_idiominusbasvol_504d_base_v075_signal(closeadj, semi_basket_closeadj):
    o = _f14_own_ret(closeadj)
    b = _f14_own_ret(semi_basket_closeadj)
    iv = _f14_idio_vol(o, b, 504)
    bv = _std(b, 504)
    result = iv - bv
    return result.replace([np.inf, -np.inf], np.nan)
