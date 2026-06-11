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
def _f03_own_ret(s):
    return s.pct_change()


def _f03_roll_corr(own_r, bas_r, w):
    return own_r.rolling(w, min_periods=max(2, w // 2)).corr(bas_r)


def _f03_roll_cov(own_r, bas_r, w):
    return own_r.rolling(w, min_periods=max(2, w // 2)).cov(bas_r)

# 21d rolling covariance
def f03bc_f03_semi_basket_correlation_cov_21d_base_v076_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_cov(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling covariance
def f03bc_f03_semi_basket_correlation_cov_63d_base_v077_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_cov(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling covariance
def f03bc_f03_semi_basket_correlation_cov_126d_base_v078_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_cov(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling covariance
def f03bc_f03_semi_basket_correlation_cov_252d_base_v079_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_cov(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling covariance
def f03bc_f03_semi_basket_correlation_cov_504d_base_v080_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_cov(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of rolling covariance
def f03bc_f03_semi_basket_correlation_covz_21d_base_v081_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_cov(o, b, 21)
    result = _z(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of rolling covariance
def f03bc_f03_semi_basket_correlation_covz_63d_base_v082_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_cov(o, b, 63)
    result = _z(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of rolling covariance
def f03bc_f03_semi_basket_correlation_covz_126d_base_v083_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_cov(o, b, 126)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of rolling covariance
def f03bc_f03_semi_basket_correlation_covz_252d_base_v084_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_cov(o, b, 252)
    result = _z(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of rolling covariance
def f03bc_f03_semi_basket_correlation_covz_504d_base_v085_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_cov(o, b, 504)
    result = _z(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation on basket-up days
def f03bc_f03_semi_basket_correlation_corrbasketup_21d_base_v086_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = om.rolling(21, min_periods=max(2, 21 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation on basket-up days
def f03bc_f03_semi_basket_correlation_corrbasketup_63d_base_v087_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = om.rolling(63, min_periods=max(2, 63 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation on basket-up days
def f03bc_f03_semi_basket_correlation_corrbasketup_126d_base_v088_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = om.rolling(126, min_periods=max(2, 126 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation on basket-up days
def f03bc_f03_semi_basket_correlation_corrbasketup_252d_base_v089_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = om.rolling(252, min_periods=max(2, 252 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation on basket-up days
def f03bc_f03_semi_basket_correlation_corrbasketup_504d_base_v090_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = om.rolling(504, min_periods=max(2, 504 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation on basket-down days
def f03bc_f03_semi_basket_correlation_corrbasketdn_21d_base_v091_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = om.rolling(21, min_periods=max(2, 21 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation on basket-down days
def f03bc_f03_semi_basket_correlation_corrbasketdn_63d_base_v092_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = om.rolling(63, min_periods=max(2, 63 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation on basket-down days
def f03bc_f03_semi_basket_correlation_corrbasketdn_126d_base_v093_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = om.rolling(126, min_periods=max(2, 126 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation on basket-down days
def f03bc_f03_semi_basket_correlation_corrbasketdn_252d_base_v094_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = om.rolling(252, min_periods=max(2, 252 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation on basket-down days
def f03bc_f03_semi_basket_correlation_corrbasketdn_504d_base_v095_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = om.rolling(504, min_periods=max(2, 504 // 2)).corr(bm)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asymmetric correlation (up minus down)
def f03bc_f03_semi_basket_correlation_corrasym_21d_base_v096_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    cu = o.where(b > 0).rolling(21, min_periods=max(2, 21 // 2)).corr(b.where(b > 0))
    cd = o.where(b < 0).rolling(21, min_periods=max(2, 21 // 2)).corr(b.where(b < 0))
    result = cu - cd
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asymmetric correlation (up minus down)
def f03bc_f03_semi_basket_correlation_corrasym_63d_base_v097_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    cu = o.where(b > 0).rolling(63, min_periods=max(2, 63 // 2)).corr(b.where(b > 0))
    cd = o.where(b < 0).rolling(63, min_periods=max(2, 63 // 2)).corr(b.where(b < 0))
    result = cu - cd
    return result.replace([np.inf, -np.inf], np.nan)


# 126d asymmetric correlation (up minus down)
def f03bc_f03_semi_basket_correlation_corrasym_126d_base_v098_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    cu = o.where(b > 0).rolling(126, min_periods=max(2, 126 // 2)).corr(b.where(b > 0))
    cd = o.where(b < 0).rolling(126, min_periods=max(2, 126 // 2)).corr(b.where(b < 0))
    result = cu - cd
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asymmetric correlation (up minus down)
def f03bc_f03_semi_basket_correlation_corrasym_252d_base_v099_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    cu = o.where(b > 0).rolling(252, min_periods=max(2, 252 // 2)).corr(b.where(b > 0))
    cd = o.where(b < 0).rolling(252, min_periods=max(2, 252 // 2)).corr(b.where(b < 0))
    result = cu - cd
    return result.replace([np.inf, -np.inf], np.nan)


# 504d asymmetric correlation (up minus down)
def f03bc_f03_semi_basket_correlation_corrasym_504d_base_v100_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    cu = o.where(b > 0).rolling(504, min_periods=max(2, 504 // 2)).corr(b.where(b > 0))
    cd = o.where(b < 0).rolling(504, min_periods=max(2, 504 // 2)).corr(b.where(b < 0))
    result = cu - cd
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling rank correlation
def f03bc_f03_semi_basket_correlation_rankcorr_21d_base_v101_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    ro = o.rolling(21, min_periods=max(2, 21 // 2)).rank()
    rb = b.rolling(21, min_periods=max(2, 21 // 2)).rank()
    result = ro.rolling(21, min_periods=max(2, 21 // 2)).corr(rb)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling rank correlation
def f03bc_f03_semi_basket_correlation_rankcorr_63d_base_v102_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    ro = o.rolling(63, min_periods=max(2, 63 // 2)).rank()
    rb = b.rolling(63, min_periods=max(2, 63 // 2)).rank()
    result = ro.rolling(63, min_periods=max(2, 63 // 2)).corr(rb)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling rank correlation
def f03bc_f03_semi_basket_correlation_rankcorr_126d_base_v103_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    ro = o.rolling(126, min_periods=max(2, 126 // 2)).rank()
    rb = b.rolling(126, min_periods=max(2, 126 // 2)).rank()
    result = ro.rolling(126, min_periods=max(2, 126 // 2)).corr(rb)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling rank correlation
def f03bc_f03_semi_basket_correlation_rankcorr_252d_base_v104_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    ro = o.rolling(252, min_periods=max(2, 252 // 2)).rank()
    rb = b.rolling(252, min_periods=max(2, 252 // 2)).rank()
    result = ro.rolling(252, min_periods=max(2, 252 // 2)).corr(rb)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling rank correlation
def f03bc_f03_semi_basket_correlation_rankcorr_504d_base_v105_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    ro = o.rolling(504, min_periods=max(2, 504 // 2)).rank()
    rb = b.rolling(504, min_periods=max(2, 504 // 2)).rank()
    result = ro.rolling(504, min_periods=max(2, 504 // 2)).corr(rb)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr of own vs basket lagged 1d
def f03bc_f03_semi_basket_correlation_lagcorr_21d_base_v106_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(21, min_periods=max(2, 21 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr of own vs basket lagged 1d
def f03bc_f03_semi_basket_correlation_lagcorr_63d_base_v107_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(63, min_periods=max(2, 63 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr of own vs basket lagged 1d
def f03bc_f03_semi_basket_correlation_lagcorr_126d_base_v108_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(126, min_periods=max(2, 126 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr of own vs basket lagged 1d
def f03bc_f03_semi_basket_correlation_lagcorr_252d_base_v109_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(252, min_periods=max(2, 252 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr of own vs basket lagged 1d
def f03bc_f03_semi_basket_correlation_lagcorr_504d_base_v110_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(504, min_periods=max(2, 504 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr of own lagged 1d vs basket (past basket lag 1d)
def f03bc_f03_semi_basket_correlation_leadcorr_21d_base_v111_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(21, min_periods=max(2, 21 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr of own lagged 1d vs basket (past basket lag 1d)
def f03bc_f03_semi_basket_correlation_leadcorr_63d_base_v112_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(63, min_periods=max(2, 63 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr of own lagged 1d vs basket (past basket lag 1d)
def f03bc_f03_semi_basket_correlation_leadcorr_126d_base_v113_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(126, min_periods=max(2, 126 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr of own lagged 1d vs basket (past basket lag 1d)
def f03bc_f03_semi_basket_correlation_leadcorr_252d_base_v114_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(252, min_periods=max(2, 252 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d corr of own lagged 1d vs basket (past basket lag 1d)
def f03bc_f03_semi_basket_correlation_leadcorr_504d_base_v115_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = o.rolling(504, min_periods=max(2, 504 // 2)).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation of absolute returns
def f03bc_f03_semi_basket_correlation_corrabs_21d_base_v116_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj).abs(), _f03_own_ret(semi_basket_closeadj).abs()
    result = o.rolling(21, min_periods=max(2, 21 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation of absolute returns
def f03bc_f03_semi_basket_correlation_corrabs_63d_base_v117_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj).abs(), _f03_own_ret(semi_basket_closeadj).abs()
    result = o.rolling(63, min_periods=max(2, 63 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation of absolute returns
def f03bc_f03_semi_basket_correlation_corrabs_126d_base_v118_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj).abs(), _f03_own_ret(semi_basket_closeadj).abs()
    result = o.rolling(126, min_periods=max(2, 126 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation of absolute returns
def f03bc_f03_semi_basket_correlation_corrabs_252d_base_v119_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj).abs(), _f03_own_ret(semi_basket_closeadj).abs()
    result = o.rolling(252, min_periods=max(2, 252 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation of absolute returns
def f03bc_f03_semi_basket_correlation_corrabs_504d_base_v120_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj).abs(), _f03_own_ret(semi_basket_closeadj).abs()
    result = o.rolling(504, min_periods=max(2, 504 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation of squared returns
def f03bc_f03_semi_basket_correlation_corrsq_21d_base_v121_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj) ** 2, _f03_own_ret(semi_basket_closeadj) ** 2
    result = o.rolling(21, min_periods=max(2, 21 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation of squared returns
def f03bc_f03_semi_basket_correlation_corrsq_63d_base_v122_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj) ** 2, _f03_own_ret(semi_basket_closeadj) ** 2
    result = o.rolling(63, min_periods=max(2, 63 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation of squared returns
def f03bc_f03_semi_basket_correlation_corrsq_126d_base_v123_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj) ** 2, _f03_own_ret(semi_basket_closeadj) ** 2
    result = o.rolling(126, min_periods=max(2, 126 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation of squared returns
def f03bc_f03_semi_basket_correlation_corrsq_252d_base_v124_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj) ** 2, _f03_own_ret(semi_basket_closeadj) ** 2
    result = o.rolling(252, min_periods=max(2, 252 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation of squared returns
def f03bc_f03_semi_basket_correlation_corrsq_504d_base_v125_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj) ** 2, _f03_own_ret(semi_basket_closeadj) ** 2
    result = o.rolling(504, min_periods=max(2, 504 // 2)).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation of return signs
def f03bc_f03_semi_basket_correlation_signcorr_21d_base_v126_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    so = pd.Series(np.sign(o), index=o.index)
    sb = pd.Series(np.sign(b), index=b.index)
    result = so.rolling(21, min_periods=max(2, 21 // 2)).corr(sb)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation of return signs
def f03bc_f03_semi_basket_correlation_signcorr_63d_base_v127_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    so = pd.Series(np.sign(o), index=o.index)
    sb = pd.Series(np.sign(b), index=b.index)
    result = so.rolling(63, min_periods=max(2, 63 // 2)).corr(sb)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation of return signs
def f03bc_f03_semi_basket_correlation_signcorr_126d_base_v128_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    so = pd.Series(np.sign(o), index=o.index)
    sb = pd.Series(np.sign(b), index=b.index)
    result = so.rolling(126, min_periods=max(2, 126 // 2)).corr(sb)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation of return signs
def f03bc_f03_semi_basket_correlation_signcorr_252d_base_v129_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    so = pd.Series(np.sign(o), index=o.index)
    sb = pd.Series(np.sign(b), index=b.index)
    result = so.rolling(252, min_periods=max(2, 252 // 2)).corr(sb)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation of return signs
def f03bc_f03_semi_basket_correlation_signcorr_504d_base_v130_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    so = pd.Series(np.sign(o), index=o.index)
    sb = pd.Series(np.sign(b), index=b.index)
    result = so.rolling(504, min_periods=max(2, 504 // 2)).corr(sb)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation on high-basket-vol days
def f03bc_f03_semi_basket_correlation_corrhighvol_21d_base_v131_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    sd = _std(b, 21)
    thr = sd.rolling(42, min_periods=max(2, 21 // 2)).median()
    mask = sd > thr
    result = o.where(mask).rolling(21, min_periods=max(2, 21 // 2)).corr(b.where(mask))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation on high-basket-vol days
def f03bc_f03_semi_basket_correlation_corrhighvol_63d_base_v132_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    sd = _std(b, 63)
    thr = sd.rolling(126, min_periods=max(2, 63 // 2)).median()
    mask = sd > thr
    result = o.where(mask).rolling(63, min_periods=max(2, 63 // 2)).corr(b.where(mask))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation on high-basket-vol days
def f03bc_f03_semi_basket_correlation_corrhighvol_126d_base_v133_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    sd = _std(b, 126)
    thr = sd.rolling(252, min_periods=max(2, 126 // 2)).median()
    mask = sd > thr
    result = o.where(mask).rolling(126, min_periods=max(2, 126 // 2)).corr(b.where(mask))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation on high-basket-vol days
def f03bc_f03_semi_basket_correlation_corrhighvol_252d_base_v134_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    sd = _std(b, 252)
    thr = sd.rolling(504, min_periods=max(2, 252 // 2)).median()
    mask = sd > thr
    result = o.where(mask).rolling(252, min_periods=max(2, 252 // 2)).corr(b.where(mask))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation on high-basket-vol days
def f03bc_f03_semi_basket_correlation_corrhighvol_504d_base_v135_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    sd = _std(b, 504)
    thr = sd.rolling(1008, min_periods=max(2, 504 // 2)).median()
    mask = sd > thr
    result = o.where(mask).rolling(504, min_periods=max(2, 504 // 2)).corr(b.where(mask))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation times basket vol
def f03bc_f03_semi_basket_correlation_corrxvol_21d_base_v136_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    v_ = _std(b, 21)
    result = c * v_
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation times basket vol
def f03bc_f03_semi_basket_correlation_corrxvol_63d_base_v137_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    v_ = _std(b, 63)
    result = c * v_
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation times basket vol
def f03bc_f03_semi_basket_correlation_corrxvol_126d_base_v138_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    v_ = _std(b, 126)
    result = c * v_
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation times basket vol
def f03bc_f03_semi_basket_correlation_corrxvol_252d_base_v139_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    v_ = _std(b, 252)
    result = c * v_
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation times basket vol
def f03bc_f03_semi_basket_correlation_corrxvol_504d_base_v140_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    v_ = _std(b, 504)
    result = c * v_
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R-squared (corr squared)
def f03bc_f03_semi_basket_correlation_rsq_21d_base_v141_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = c ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# 63d R-squared (corr squared)
def f03bc_f03_semi_basket_correlation_rsq_63d_base_v142_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = c ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# 126d R-squared (corr squared)
def f03bc_f03_semi_basket_correlation_rsq_126d_base_v143_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = c ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R-squared (corr squared)
def f03bc_f03_semi_basket_correlation_rsq_252d_base_v144_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = c ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R-squared (corr squared)
def f03bc_f03_semi_basket_correlation_rsq_504d_base_v145_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = c ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# short composite: 21z + 63z + 126z of correlation
def f03bc_f03_semi_basket_correlation_corrcomposite_short_base_v146_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c21 = _f03_roll_corr(o, b, 21)
    c63 = _f03_roll_corr(o, b, 63)
    c126 = _f03_roll_corr(o, b, 126)
    result = _z(c21, 63) + _z(c63, 126) + _z(c126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite: 63z + 126z + 252z of correlation
def f03bc_f03_semi_basket_correlation_corrcomposite_long_base_v147_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c63 = _f03_roll_corr(o, b, 63)
    c126 = _f03_roll_corr(o, b, 126)
    c252 = _f03_roll_corr(o, b, 252)
    result = _z(c63, 126) + _z(c126, 252) + _z(c252, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# regime divergence (sign short ema cross - sign long ema cross) of corr
def f03bc_f03_semi_basket_correlation_corrregime_divergence_base_v148_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    short = np.sign(c.ewm(span=21, adjust=False).mean() - c.ewm(span=63, adjust=False).mean())
    long = np.sign(c.ewm(span=126, adjust=False).mean() - c.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=c.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr quality: corr / std-of-corr
def f03bc_f03_semi_basket_correlation_corrquality_63d_base_v149_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = c / _std(c, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d corr quality: corr / std-of-corr
def f03bc_f03_semi_basket_correlation_corrquality_252d_base_v150_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = c / _std(c, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


