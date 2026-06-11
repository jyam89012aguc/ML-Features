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
def _f02_own_ret(s):
    return s.pct_change()


def _f02_roll_beta(own_r, bas_r, w):
    cov = own_r.rolling(w, min_periods=max(2, w // 2)).cov(bas_r)
    var = bas_r.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f02_roll_alpha(own_r, bas_r, w):
    beta = _f02_roll_beta(own_r, bas_r, w)
    return _mean(own_r, w) - beta * _mean(bas_r, w)

# 21d rolling alpha (mean own - beta * mean basket)
def f02bb_f02_semi_basket_beta_alpha_21d_base_v076_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_alpha(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling alpha (mean own - beta * mean basket)
def f02bb_f02_semi_basket_beta_alpha_63d_base_v077_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_alpha(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling alpha (mean own - beta * mean basket)
def f02bb_f02_semi_basket_beta_alpha_126d_base_v078_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_alpha(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling alpha (mean own - beta * mean basket)
def f02bb_f02_semi_basket_beta_alpha_252d_base_v079_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_alpha(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling alpha (mean own - beta * mean basket)
def f02bb_f02_semi_basket_beta_alpha_504d_base_v080_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_alpha(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of rolling alpha
def f02bb_f02_semi_basket_beta_alphaz_21d_base_v081_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    a = _f02_roll_alpha(o, b, 21)
    result = _z(a, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of rolling alpha
def f02bb_f02_semi_basket_beta_alphaz_63d_base_v082_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    a = _f02_roll_alpha(o, b, 63)
    result = _z(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of rolling alpha
def f02bb_f02_semi_basket_beta_alphaz_126d_base_v083_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    a = _f02_roll_alpha(o, b, 126)
    result = _z(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of rolling alpha
def f02bb_f02_semi_basket_beta_alphaz_252d_base_v084_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    a = _f02_roll_alpha(o, b, 252)
    result = _z(a, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of rolling alpha
def f02bb_f02_semi_basket_beta_alphaz_504d_base_v085_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    a = _f02_roll_alpha(o, b, 504)
    result = _z(a, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d idiosyncratic vol (std of o - beta*b)
def f02bb_f02_semi_basket_beta_idiovol_21d_base_v086_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    resid = o - beta * b
    result = _std(resid, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d idiosyncratic vol (std of o - beta*b)
def f02bb_f02_semi_basket_beta_idiovol_63d_base_v087_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    resid = o - beta * b
    result = _std(resid, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d idiosyncratic vol (std of o - beta*b)
def f02bb_f02_semi_basket_beta_idiovol_126d_base_v088_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    resid = o - beta * b
    result = _std(resid, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d idiosyncratic vol (std of o - beta*b)
def f02bb_f02_semi_basket_beta_idiovol_252d_base_v089_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    resid = o - beta * b
    result = _std(resid, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d idiosyncratic vol (std of o - beta*b)
def f02bb_f02_semi_basket_beta_idiovol_504d_base_v090_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    resid = o - beta * b
    result = _std(resid, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d explained variance ratio 1 - var(resid)/var(own)
def f02bb_f02_semi_basket_beta_explvar_21d_base_v091_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    resid = o - beta * b
    vr = resid.rolling(21, min_periods=max(2, 21 // 2)).var()
    vo = o.rolling(21, min_periods=max(2, 21 // 2)).var()
    result = 1.0 - vr / vo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d explained variance ratio 1 - var(resid)/var(own)
def f02bb_f02_semi_basket_beta_explvar_63d_base_v092_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    resid = o - beta * b
    vr = resid.rolling(63, min_periods=max(2, 63 // 2)).var()
    vo = o.rolling(63, min_periods=max(2, 63 // 2)).var()
    result = 1.0 - vr / vo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d explained variance ratio 1 - var(resid)/var(own)
def f02bb_f02_semi_basket_beta_explvar_126d_base_v093_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    resid = o - beta * b
    vr = resid.rolling(126, min_periods=max(2, 126 // 2)).var()
    vo = o.rolling(126, min_periods=max(2, 126 // 2)).var()
    result = 1.0 - vr / vo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d explained variance ratio 1 - var(resid)/var(own)
def f02bb_f02_semi_basket_beta_explvar_252d_base_v094_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    resid = o - beta * b
    vr = resid.rolling(252, min_periods=max(2, 252 // 2)).var()
    vo = o.rolling(252, min_periods=max(2, 252 // 2)).var()
    result = 1.0 - vr / vo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d explained variance ratio 1 - var(resid)/var(own)
def f02bb_f02_semi_basket_beta_explvar_504d_base_v095_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    resid = o - beta * b
    vr = resid.rolling(504, min_periods=max(2, 504 // 2)).var()
    vo = o.rolling(504, min_periods=max(2, 504 // 2)).var()
    result = 1.0 - vr / vo.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta conditioned on basket-up days
def f02bb_f02_semi_basket_beta_betaup_21d_base_v096_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = _f02_roll_beta(om, bm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta conditioned on basket-up days
def f02bb_f02_semi_basket_beta_betaup_63d_base_v097_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = _f02_roll_beta(om, bm, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta conditioned on basket-up days
def f02bb_f02_semi_basket_beta_betaup_126d_base_v098_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = _f02_roll_beta(om, bm, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta conditioned on basket-up days
def f02bb_f02_semi_basket_beta_betaup_252d_base_v099_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = _f02_roll_beta(om, bm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta conditioned on basket-up days
def f02bb_f02_semi_basket_beta_betaup_504d_base_v100_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b > 0), b.where(b > 0)
    result = _f02_roll_beta(om, bm, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta conditioned on basket-down days
def f02bb_f02_semi_basket_beta_betadn_21d_base_v101_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = _f02_roll_beta(om, bm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta conditioned on basket-down days
def f02bb_f02_semi_basket_beta_betadn_63d_base_v102_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = _f02_roll_beta(om, bm, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta conditioned on basket-down days
def f02bb_f02_semi_basket_beta_betadn_126d_base_v103_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = _f02_roll_beta(om, bm, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta conditioned on basket-down days
def f02bb_f02_semi_basket_beta_betadn_252d_base_v104_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = _f02_roll_beta(om, bm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta conditioned on basket-down days
def f02bb_f02_semi_basket_beta_betadn_504d_base_v105_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    om, bm = o.where(b < 0), b.where(b < 0)
    result = _f02_roll_beta(om, bm, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta asymmetry (up-beta minus down-beta)
def f02bb_f02_semi_basket_beta_betaasym_21d_base_v106_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    bu = _f02_roll_beta(o.where(b > 0), b.where(b > 0), 21)
    bd = _f02_roll_beta(o.where(b < 0), b.where(b < 0), 21)
    result = bu - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta asymmetry (up-beta minus down-beta)
def f02bb_f02_semi_basket_beta_betaasym_63d_base_v107_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    bu = _f02_roll_beta(o.where(b > 0), b.where(b > 0), 63)
    bd = _f02_roll_beta(o.where(b < 0), b.where(b < 0), 63)
    result = bu - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta asymmetry (up-beta minus down-beta)
def f02bb_f02_semi_basket_beta_betaasym_126d_base_v108_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    bu = _f02_roll_beta(o.where(b > 0), b.where(b > 0), 126)
    bd = _f02_roll_beta(o.where(b < 0), b.where(b < 0), 126)
    result = bu - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta asymmetry (up-beta minus down-beta)
def f02bb_f02_semi_basket_beta_betaasym_252d_base_v109_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    bu = _f02_roll_beta(o.where(b > 0), b.where(b > 0), 252)
    bd = _f02_roll_beta(o.where(b < 0), b.where(b < 0), 252)
    result = bu - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta asymmetry (up-beta minus down-beta)
def f02bb_f02_semi_basket_beta_betaasym_504d_base_v110_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    bu = _f02_roll_beta(o.where(b > 0), b.where(b > 0), 504)
    bd = _f02_roll_beta(o.where(b < 0), b.where(b < 0), 504)
    result = bu - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling covariance own,basket
def f02bb_f02_semi_basket_beta_cov_21d_base_v111_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = o.rolling(21, min_periods=max(2, 21 // 2)).cov(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling covariance own,basket
def f02bb_f02_semi_basket_beta_cov_63d_base_v112_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = o.rolling(63, min_periods=max(2, 63 // 2)).cov(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling covariance own,basket
def f02bb_f02_semi_basket_beta_cov_126d_base_v113_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = o.rolling(126, min_periods=max(2, 126 // 2)).cov(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling covariance own,basket
def f02bb_f02_semi_basket_beta_cov_252d_base_v114_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = o.rolling(252, min_periods=max(2, 252 // 2)).cov(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling covariance own,basket
def f02bb_f02_semi_basket_beta_cov_504d_base_v115_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = o.rolling(504, min_periods=max(2, 504 // 2)).cov(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basket variance
def f02bb_f02_semi_basket_beta_basketvar_21d_base_v116_signal(closeadj, semi_basket_closeadj):
    b = _f02_own_ret(semi_basket_closeadj)
    result = b.rolling(21, min_periods=max(2, 21 // 2)).var()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basket variance
def f02bb_f02_semi_basket_beta_basketvar_63d_base_v117_signal(closeadj, semi_basket_closeadj):
    b = _f02_own_ret(semi_basket_closeadj)
    result = b.rolling(63, min_periods=max(2, 63 // 2)).var()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basket variance
def f02bb_f02_semi_basket_beta_basketvar_126d_base_v118_signal(closeadj, semi_basket_closeadj):
    b = _f02_own_ret(semi_basket_closeadj)
    result = b.rolling(126, min_periods=max(2, 126 // 2)).var()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basket variance
def f02bb_f02_semi_basket_beta_basketvar_252d_base_v119_signal(closeadj, semi_basket_closeadj):
    b = _f02_own_ret(semi_basket_closeadj)
    result = b.rolling(252, min_periods=max(2, 252 // 2)).var()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d basket variance
def f02bb_f02_semi_basket_beta_basketvar_504d_base_v120_signal(closeadj, semi_basket_closeadj):
    b = _f02_own_ret(semi_basket_closeadj)
    result = b.rolling(504, min_periods=max(2, 504 // 2)).var()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d minus 63d rolling beta (beta term spread)
def f02bb_f02_semi_basket_beta_betadiff_21v63_base_v121_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 21) - _f02_roll_beta(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d minus 126d rolling beta (beta term spread)
def f02bb_f02_semi_basket_beta_betadiff_21v126_base_v122_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 21) - _f02_roll_beta(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minus 126d rolling beta (beta term spread)
def f02bb_f02_semi_basket_beta_betadiff_63v126_base_v123_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 63) - _f02_roll_beta(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d minus 252d rolling beta (beta term spread)
def f02bb_f02_semi_basket_beta_betadiff_63v252_base_v124_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 63) - _f02_roll_beta(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d minus 504d rolling beta (beta term spread)
def f02bb_f02_semi_basket_beta_betadiff_126v504_base_v125_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 126) - _f02_roll_beta(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d / 63d rolling beta ratio
def f02bb_f02_semi_basket_beta_betaratio_21v63_base_v126_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    sb = _f02_roll_beta(o, b, 21)
    lb = _f02_roll_beta(o, b, 63)
    result = sb / lb.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d / 126d rolling beta ratio
def f02bb_f02_semi_basket_beta_betaratio_21v126_base_v127_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    sb = _f02_roll_beta(o, b, 21)
    lb = _f02_roll_beta(o, b, 126)
    result = sb / lb.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d / 126d rolling beta ratio
def f02bb_f02_semi_basket_beta_betaratio_63v126_base_v128_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    sb = _f02_roll_beta(o, b, 63)
    lb = _f02_roll_beta(o, b, 126)
    result = sb / lb.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d / 252d rolling beta ratio
def f02bb_f02_semi_basket_beta_betaratio_63v252_base_v129_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    sb = _f02_roll_beta(o, b, 63)
    lb = _f02_roll_beta(o, b, 252)
    result = sb / lb.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d / 504d rolling beta ratio
def f02bb_f02_semi_basket_beta_betaratio_126v504_base_v130_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    sb = _f02_roll_beta(o, b, 126)
    lb = _f02_roll_beta(o, b, 504)
    result = sb / lb.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of rolling beta
def f02bb_f02_semi_basket_beta_betaskew_21d_base_v131_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = beta.rolling(63, min_periods=max(2, 63 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of rolling beta
def f02bb_f02_semi_basket_beta_betaskew_63d_base_v132_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = beta.rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of rolling beta
def f02bb_f02_semi_basket_beta_betaskew_126d_base_v133_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = beta.rolling(252, min_periods=max(2, 252 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of rolling beta
def f02bb_f02_semi_basket_beta_betaskew_252d_base_v134_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = beta.rolling(504, min_periods=max(2, 504 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of rolling beta
def f02bb_f02_semi_basket_beta_betaskew_504d_base_v135_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = beta.rolling(756, min_periods=max(2, 756 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of rolling beta
def f02bb_f02_semi_basket_beta_betakurt_21d_base_v136_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = beta.rolling(63, min_periods=max(2, 63 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of rolling beta
def f02bb_f02_semi_basket_beta_betakurt_63d_base_v137_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = beta.rolling(126, min_periods=max(2, 126 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of rolling beta
def f02bb_f02_semi_basket_beta_betakurt_126d_base_v138_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = beta.rolling(252, min_periods=max(2, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of rolling beta
def f02bb_f02_semi_basket_beta_betakurt_252d_base_v139_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = beta.rolling(504, min_periods=max(2, 504 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of rolling beta
def f02bb_f02_semi_basket_beta_betakurt_504d_base_v140_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = beta.rolling(756, min_periods=max(2, 756 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative beta trend (sum of diffs)
def f02bb_f02_semi_basket_beta_betatrend_21d_base_v141_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = beta.diff().rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative beta trend (sum of diffs)
def f02bb_f02_semi_basket_beta_betatrend_63d_base_v142_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = beta.diff().rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative beta trend (sum of diffs)
def f02bb_f02_semi_basket_beta_betatrend_126d_base_v143_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = beta.diff().rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative beta trend (sum of diffs)
def f02bb_f02_semi_basket_beta_betatrend_252d_base_v144_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = beta.diff().rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative beta trend (sum of diffs)
def f02bb_f02_semi_basket_beta_betatrend_504d_base_v145_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = beta.diff().rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# short composite: 21z + 63z + 126z of rolling beta
def f02bb_f02_semi_basket_beta_betacomposite_short_base_v146_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    b21 = _f02_roll_beta(o, b, 21)
    b63 = _f02_roll_beta(o, b, 63)
    b126 = _f02_roll_beta(o, b, 126)
    result = _z(b21, 63) + _z(b63, 126) + _z(b126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite: 63z + 126z + 252z of rolling beta
def f02bb_f02_semi_basket_beta_betacomposite_long_base_v147_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    b63 = _f02_roll_beta(o, b, 63)
    b126 = _f02_roll_beta(o, b, 126)
    b252 = _f02_roll_beta(o, b, 252)
    result = _z(b63, 126) + _z(b126, 252) + _z(b252, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# beta regime divergence (sign short ema cross - sign long ema cross)
def f02bb_f02_semi_basket_beta_betaregime_divergence_base_v148_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    short = np.sign(beta.ewm(span=21, adjust=False).mean() - beta.ewm(span=63, adjust=False).mean())
    long = np.sign(beta.ewm(span=126, adjust=False).mean() - beta.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=beta.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta quality: alpha / idiosyncratic vol
def f02bb_f02_semi_basket_beta_betaquality_63d_base_v149_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    alpha = _mean(o, 63) - beta * _mean(b, 63)
    resid = o - beta * b
    result = alpha / _std(resid, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta quality: alpha / idiosyncratic vol
def f02bb_f02_semi_basket_beta_betaquality_252d_base_v150_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    alpha = _mean(o, 252) - beta * _mean(b, 252)
    resid = o - beta * b
    result = alpha / _std(resid, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


