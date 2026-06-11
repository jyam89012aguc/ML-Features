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


# 21d basket-residualized idio (own minus basket-beta times basket return) rolling mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_21d_base_v076_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_idio(o, b, 21).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basket-residualized idio rolling mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_63d_base_v077_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_idio(o, b, 63).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basket-residualized idio rolling mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_126d_base_v078_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_idio(o, b, 126).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basket-residualized idio rolling mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_252d_base_v079_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_idio(o, b, 252).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d basket-residualized idio rolling mean
def f96ce_f96_semi_china_exposure_proxy_idiobasket_504d_base_v080_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    result = _f96ce_idio(o, b, 504).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dual-residualized idio: own minus china-beta times china minus basket-beta times basket
def f96ce_f96_semi_china_exposure_proxy_dualidio_21d_base_v081_signal(closeadj, semi_basket_closeadj, china_exposure_index):
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
    result = (resid1 - beta_b * b).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_63d_base_v082_signal(closeadj, semi_basket_closeadj, china_exposure_index):
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
    result = (resid1 - beta_b * b).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_126d_base_v083_signal(closeadj, semi_basket_closeadj, china_exposure_index):
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
    result = (resid1 - beta_b * b).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_252d_base_v084_signal(closeadj, semi_basket_closeadj, china_exposure_index):
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
    result = (resid1 - beta_b * b).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dual-residualized idio
def f96ce_f96_semi_china_exposure_proxy_dualidio_504d_base_v085_signal(closeadj, semi_basket_closeadj, china_exposure_index):
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
    result = (resid1 - beta_b * b).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d relative log-return spread own vs semi basket (cumulative over window)
def f96ce_f96_semi_china_exposure_proxy_relretbasket_21d_base_v086_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    result = diff.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d relative log-return spread own vs semi basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_63d_base_v087_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    result = diff.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d relative log-return spread own vs semi basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_126d_base_v088_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    result = diff.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d relative log-return spread own vs semi basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_252d_base_v089_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    result = diff.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d relative log-return spread own vs semi basket
def f96ce_f96_semi_china_exposure_proxy_relretbasket_504d_base_v090_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(semi_basket_closeadj)
    result = diff.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d relative log-return spread own vs china exposure index
def f96ce_f96_semi_china_exposure_proxy_relretchina_21d_base_v091_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = diff.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d relative log-return spread own vs china exposure index
def f96ce_f96_semi_china_exposure_proxy_relretchina_63d_base_v092_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = diff.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d relative log-return spread own vs china exposure index
def f96ce_f96_semi_china_exposure_proxy_relretchina_126d_base_v093_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = diff.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d relative log-return spread own vs china exposure index
def f96ce_f96_semi_china_exposure_proxy_relretchina_252d_base_v094_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = diff.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d relative log-return spread own vs china exposure index
def f96ce_f96_semi_china_exposure_proxy_relretchina_504d_base_v095_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = diff.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down-day corr: corr of own with china only on china negative-return days
def f96ce_f96_semi_china_exposure_proxy_corrneg_21d_base_v096_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d down-day corr: corr of own with china only on china negative-return days
def f96ce_f96_semi_china_exposure_proxy_corrneg_63d_base_v097_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d down-day corr: corr of own with china only on china negative-return days
def f96ce_f96_semi_china_exposure_proxy_corrneg_126d_base_v098_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d down-day corr
def f96ce_f96_semi_china_exposure_proxy_corrneg_252d_base_v099_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d down-day corr
def f96ce_f96_semi_china_exposure_proxy_corrneg_504d_base_v100_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c < 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up-day corr: corr of own with china only on china positive-return days
def f96ce_f96_semi_china_exposure_proxy_corrpos_21d_base_v101_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_63d_base_v102_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_126d_base_v103_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_252d_base_v104_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d up-day corr
def f96ce_f96_semi_china_exposure_proxy_corrpos_504d_base_v105_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    mask = (c > 0)
    o2 = o.where(mask)
    c2 = c.where(mask)
    result = _f96ce_roll_corr(o2, c2, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of china drawdown depth (regime indicator)
def f96ce_f96_semi_china_exposure_proxy_chinadd_21d_base_v106_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 21)
    result = _z(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of china drawdown depth
def f96ce_f96_semi_china_exposure_proxy_chinadd_63d_base_v107_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 63)
    result = _z(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of china drawdown depth
def f96ce_f96_semi_china_exposure_proxy_chinadd_126d_base_v108_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 126)
    result = _z(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of china drawdown depth
def f96ce_f96_semi_china_exposure_proxy_chinadd_252d_base_v109_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 252)
    result = _z(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of china drawdown depth
def f96ce_f96_semi_china_exposure_proxy_chinadd_504d_base_v110_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 504)
    result = _z(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own cumulative log return during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_owninchidd_21d_base_v111_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 21)
    mask = (dd < 0).astype(float)
    result = (o * mask).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own cumulative log return during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_owninchidd_63d_base_v112_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 63)
    mask = (dd < 0).astype(float)
    result = (o * mask).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own cumulative log return during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_owninchidd_126d_base_v113_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 126)
    mask = (dd < 0).astype(float)
    result = (o * mask).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own cumulative log return during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_owninchidd_252d_base_v114_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 252)
    mask = (dd < 0).astype(float)
    result = (o * mask).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own cumulative log return during china drawdown days
def f96ce_f96_semi_china_exposure_proxy_owninchidd_504d_base_v115_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_logret(closeadj)
    lc = np.log(china_exposure_index.replace(0, np.nan).abs())
    dd = lc - _max(lc, 504)
    mask = (dd < 0).astype(float)
    result = (o * mask).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed-outperformance count: sign of own return minus china return rolling sum
def f96ce_f96_semi_china_exposure_proxy_signoutperf_21d_base_v116_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = pd.Series(np.sign(diff), index=diff.index).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed-outperformance count
def f96ce_f96_semi_china_exposure_proxy_signoutperf_63d_base_v117_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = pd.Series(np.sign(diff), index=diff.index).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed-outperformance count
def f96ce_f96_semi_china_exposure_proxy_signoutperf_126d_base_v118_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = pd.Series(np.sign(diff), index=diff.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed-outperformance count
def f96ce_f96_semi_china_exposure_proxy_signoutperf_252d_base_v119_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = pd.Series(np.sign(diff), index=diff.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed-outperformance count
def f96ce_f96_semi_china_exposure_proxy_signoutperf_504d_base_v120_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    result = pd.Series(np.sign(diff), index=diff.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-ratio of semi basket vs china exposure (basket relative strength) deviation
def f96ce_f96_semi_china_exposure_proxy_basketchina_21d_base_v121_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-ratio of semi basket vs china exposure deviation
def f96ce_f96_semi_china_exposure_proxy_basketchina_63d_base_v122_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-ratio of semi basket vs china exposure deviation
def f96ce_f96_semi_china_exposure_proxy_basketchina_126d_base_v123_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-ratio of semi basket vs china exposure deviation
def f96ce_f96_semi_china_exposure_proxy_basketchina_252d_base_v124_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-ratio of semi basket vs china exposure deviation
def f96ce_f96_semi_china_exposure_proxy_basketchina_504d_base_v125_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    r = np.log(semi_basket_closeadj.replace(0, np.nan).abs() / china_exposure_index.replace(0, np.nan).abs())
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own log-return rolling std (own vol baseline)
def f96ce_f96_semi_china_exposure_proxy_ownvol_21d_base_v126_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    result = _std(_f96ce_logret(closeadj), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own log-return rolling std
def f96ce_f96_semi_china_exposure_proxy_ownvol_63d_base_v127_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    result = _std(_f96ce_logret(closeadj), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own log-return rolling std
def f96ce_f96_semi_china_exposure_proxy_ownvol_126d_base_v128_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    result = _std(_f96ce_logret(closeadj), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own log-return rolling std
def f96ce_f96_semi_china_exposure_proxy_ownvol_252d_base_v129_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    result = _std(_f96ce_logret(closeadj), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own log-return rolling std
def f96ce_f96_semi_china_exposure_proxy_ownvol_504d_base_v130_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    result = _std(_f96ce_logret(closeadj), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta ratio: beta(own,basket) divided by beta(own,china) (china-loading inverse)
def f96ce_f96_semi_china_exposure_proxy_betaratio_21d_base_v131_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 21)
    bc = _f96ce_roll_beta(o, c, 21)
    result = bb / bc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta ratio: beta(own,basket) divided by beta(own,china)
def f96ce_f96_semi_china_exposure_proxy_betaratio_63d_base_v132_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 63)
    bc = _f96ce_roll_beta(o, c, 63)
    result = bb / bc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta ratio: beta(own,basket) divided by beta(own,china)
def f96ce_f96_semi_china_exposure_proxy_betaratio_126d_base_v133_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 126)
    bc = _f96ce_roll_beta(o, c, 126)
    result = bb / bc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta ratio: beta(own,basket) divided by beta(own,china)
def f96ce_f96_semi_china_exposure_proxy_betaratio_252d_base_v134_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 252)
    bc = _f96ce_roll_beta(o, c, 252)
    result = bb / bc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta ratio: beta(own,basket) divided by beta(own,china)
def f96ce_f96_semi_china_exposure_proxy_betaratio_504d_base_v135_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    bb = _f96ce_roll_beta(o, b, 504)
    bc = _f96ce_roll_beta(o, c, 504)
    result = bb / bc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr-difference: corr(own,china) minus corr(own,basket) (china-specific exposure)
def f96ce_f96_semi_china_exposure_proxy_corrdiff_21d_base_v136_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 21) - _f96ce_roll_corr(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr-difference: corr(own,china) minus corr(own,basket)
def f96ce_f96_semi_china_exposure_proxy_corrdiff_63d_base_v137_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 63) - _f96ce_roll_corr(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr-difference: corr(own,china) minus corr(own,basket)
def f96ce_f96_semi_china_exposure_proxy_corrdiff_126d_base_v138_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 126) - _f96ce_roll_corr(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr-difference: corr(own,china) minus corr(own,basket)
def f96ce_f96_semi_china_exposure_proxy_corrdiff_252d_base_v139_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 252) - _f96ce_roll_corr(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr-difference: corr(own,china) minus corr(own,basket)
def f96ce_f96_semi_china_exposure_proxy_corrdiff_504d_base_v140_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    b = _f96ce_ret(semi_basket_closeadj)
    c = _f96ce_ret(china_exposure_index)
    result = _f96ce_roll_corr(o, c, 504) - _f96ce_roll_corr(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite china exposure score (z corr + z beta - z idio)
def f96ce_f96_semi_china_exposure_proxy_composite_21d_base_v141_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 21)
    bb = _f96ce_roll_beta(o, c, 21)
    idio = _f96ce_idio(o, c, 21).rolling(21, min_periods=11).mean()
    result = _z(cc, 252) + _z(bb, 252) - _z(idio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite china exposure score
def f96ce_f96_semi_china_exposure_proxy_composite_63d_base_v142_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 63)
    bb = _f96ce_roll_beta(o, c, 63)
    idio = _f96ce_idio(o, c, 63).rolling(63, min_periods=32).mean()
    result = _z(cc, 252) + _z(bb, 252) - _z(idio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite china exposure score
def f96ce_f96_semi_china_exposure_proxy_composite_126d_base_v143_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 126)
    bb = _f96ce_roll_beta(o, c, 126)
    idio = _f96ce_idio(o, c, 126).rolling(126, min_periods=63).mean()
    result = _z(cc, 252) + _z(bb, 252) - _z(idio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite china exposure score
def f96ce_f96_semi_china_exposure_proxy_composite_252d_base_v144_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 252)
    bb = _f96ce_roll_beta(o, c, 252)
    idio = _f96ce_idio(o, c, 252).rolling(252, min_periods=126).mean()
    result = _z(cc, 504) + _z(bb, 504) - _z(idio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite china exposure score
def f96ce_f96_semi_china_exposure_proxy_composite_504d_base_v145_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    o = _f96ce_ret(closeadj)
    c = _f96ce_ret(china_exposure_index)
    cc = _f96ce_roll_corr(o, c, 504)
    bb = _f96ce_roll_beta(o, c, 504)
    idio = _f96ce_idio(o, c, 504).rolling(504, min_periods=252).mean()
    result = _z(cc, 504) + _z(bb, 504) - _z(idio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of own minus china log-return spread (median/MAD)
def f96ce_f96_semi_china_exposure_proxy_robustz_21d_base_v146_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(21, min_periods=11).median()
    mad = (diff - med).abs().rolling(21, min_periods=11).median()
    result = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of own minus china log-return spread (median/MAD)
def f96ce_f96_semi_china_exposure_proxy_robustz_63d_base_v147_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(63, min_periods=32).median()
    mad = (diff - med).abs().rolling(63, min_periods=32).median()
    result = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of own minus china log-return spread
def f96ce_f96_semi_china_exposure_proxy_robustz_126d_base_v148_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(126, min_periods=63).median()
    mad = (diff - med).abs().rolling(126, min_periods=63).median()
    result = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of own minus china log-return spread
def f96ce_f96_semi_china_exposure_proxy_robustz_252d_base_v149_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(252, min_periods=126).median()
    mad = (diff - med).abs().rolling(252, min_periods=126).median()
    result = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of own minus china log-return spread
def f96ce_f96_semi_china_exposure_proxy_robustz_504d_base_v150_signal(closeadj, semi_basket_closeadj, china_exposure_index):
    diff = _f96ce_logret(closeadj) - _f96ce_logret(china_exposure_index)
    med = diff.rolling(504, min_periods=252).median()
    mad = (diff - med).abs().rolling(504, min_periods=252).median()
    result = (diff - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
