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


# ===== folder domain primitives =====
def _f01_own_ret(s):
    return s.pct_change()


def _f01_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f01_rs_log_ratio(own, bas):
    return np.log(own.replace(0, np.nan).abs() / bas.replace(0, np.nan).abs())


def _f01_roll_beta(own_r, bas_r, w):
    cov = own_r.rolling(w, min_periods=max(2, w // 2)).cov(bas_r)
    var = bas_r.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f01_roll_corr(own_r, bas_r, w):
    return own_r.rolling(w, min_periods=max(2, w // 2)).corr(bas_r)


# 21d rolling beta vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsbeta_21d_base_v076_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_beta(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsbeta_63d_base_v077_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_beta(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsbeta_126d_base_v078_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_beta(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsbeta_252d_base_v079_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_beta(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta vs semi basket
def f01prs_f01_semi_peer_relative_strength_rsbeta_504d_base_v080_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_beta(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling correlation vs semi basket
def f01prs_f01_semi_peer_relative_strength_rscorr_21d_base_v081_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_corr(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation vs semi basket
def f01prs_f01_semi_peer_relative_strength_rscorr_63d_base_v082_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_corr(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation vs semi basket
def f01prs_f01_semi_peer_relative_strength_rscorr_126d_base_v083_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_corr(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation vs semi basket
def f01prs_f01_semi_peer_relative_strength_rscorr_252d_base_v084_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_corr(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation vs semi basket
def f01prs_f01_semi_peer_relative_strength_rscorr_504d_base_v085_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _f01_roll_corr(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d tracking error (std of return spread)
def f01prs_f01_semi_peer_relative_strength_rste_21d_base_v086_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _std(diff, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tracking error (std of return spread)
def f01prs_f01_semi_peer_relative_strength_rste_63d_base_v087_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _std(diff, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d tracking error (std of return spread)
def f01prs_f01_semi_peer_relative_strength_rste_126d_base_v088_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _std(diff, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tracking error (std of return spread)
def f01prs_f01_semi_peer_relative_strength_rste_252d_base_v089_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _std(diff, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tracking error (std of return spread)
def f01prs_f01_semi_peer_relative_strength_rste_504d_base_v090_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _std(diff, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d information ratio (mean / std of spread)
def f01prs_f01_semi_peer_relative_strength_rsir_21d_base_v091_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _mean(diff, 21) / _std(diff, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d information ratio (mean / std of spread)
def f01prs_f01_semi_peer_relative_strength_rsir_63d_base_v092_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _mean(diff, 63) / _std(diff, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d information ratio (mean / std of spread)
def f01prs_f01_semi_peer_relative_strength_rsir_126d_base_v093_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _mean(diff, 126) / _std(diff, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d information ratio (mean / std of spread)
def f01prs_f01_semi_peer_relative_strength_rsir_252d_base_v094_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _mean(diff, 252) / _std(diff, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d information ratio (mean / std of spread)
def f01prs_f01_semi_peer_relative_strength_rsir_504d_base_v095_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = _mean(diff, 504) / _std(diff, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up-capture ratio (own ret avg / basket ret avg, basket-up days)
def f01prs_f01_semi_peer_relative_strength_rsupcap_21d_base_v096_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    result = _mean(o.where(mask), 21) / _mean(b.where(mask), 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsupcap_63d_base_v097_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    result = _mean(o.where(mask), 63) / _mean(b.where(mask), 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d up-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsupcap_126d_base_v098_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    result = _mean(o.where(mask), 126) / _mean(b.where(mask), 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsupcap_252d_base_v099_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    result = _mean(o.where(mask), 252) / _mean(b.where(mask), 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d up-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsupcap_504d_base_v100_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    result = _mean(o.where(mask), 504) / _mean(b.where(mask), 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down-capture ratio (basket-down days)
def f01prs_f01_semi_peer_relative_strength_rsdncap_21d_base_v101_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    result = _mean(o.where(mask), 21) / _mean(b.where(mask), 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d down-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsdncap_63d_base_v102_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    result = _mean(o.where(mask), 63) / _mean(b.where(mask), 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d down-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsdncap_126d_base_v103_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    result = _mean(o.where(mask), 126) / _mean(b.where(mask), 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d down-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsdncap_252d_base_v104_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    result = _mean(o.where(mask), 252) / _mean(b.where(mask), 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d down-capture ratio
def f01prs_f01_semi_peer_relative_strength_rsdncap_504d_base_v105_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    result = _mean(o.where(mask), 504) / _mean(b.where(mask), 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol ratio (own std / basket std)
def f01prs_f01_semi_peer_relative_strength_rsvolratio_21d_base_v106_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _std(o, 21) / _std(b, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol ratio (own std / basket std)
def f01prs_f01_semi_peer_relative_strength_rsvolratio_63d_base_v107_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _std(o, 63) / _std(b, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vol ratio (own std / basket std)
def f01prs_f01_semi_peer_relative_strength_rsvolratio_126d_base_v108_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _std(o, 126) / _std(b, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d vol ratio (own std / basket std)
def f01prs_f01_semi_peer_relative_strength_rsvolratio_252d_base_v109_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _std(o, 252) / _std(b, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d vol ratio (own std / basket std)
def f01prs_f01_semi_peer_relative_strength_rsvolratio_504d_base_v110_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    result = _std(o, 504) / _std(b, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of RS spread
def f01prs_f01_semi_peer_relative_strength_rsskew_21d_base_v111_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of RS spread
def f01prs_f01_semi_peer_relative_strength_rsskew_63d_base_v112_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of RS spread
def f01prs_f01_semi_peer_relative_strength_rsskew_126d_base_v113_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of RS spread
def f01prs_f01_semi_peer_relative_strength_rsskew_252d_base_v114_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of RS spread
def f01prs_f01_semi_peer_relative_strength_rsskew_504d_base_v115_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of RS spread
def f01prs_f01_semi_peer_relative_strength_rskurt_21d_base_v116_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of RS spread
def f01prs_f01_semi_peer_relative_strength_rskurt_63d_base_v117_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of RS spread
def f01prs_f01_semi_peer_relative_strength_rskurt_126d_base_v118_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of RS spread
def f01prs_f01_semi_peer_relative_strength_rskurt_252d_base_v119_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of RS spread
def f01prs_f01_semi_peer_relative_strength_rskurt_504d_base_v120_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative RS spread (sum)
def f01prs_f01_semi_peer_relative_strength_rscumspread_21d_base_v121_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative RS spread (sum)
def f01prs_f01_semi_peer_relative_strength_rscumspread_63d_base_v122_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative RS spread (sum)
def f01prs_f01_semi_peer_relative_strength_rscumspread_126d_base_v123_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative RS spread (sum)
def f01prs_f01_semi_peer_relative_strength_rscumspread_252d_base_v124_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative RS spread (sum)
def f01prs_f01_semi_peer_relative_strength_rscumspread_504d_base_v125_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = diff.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of cumulative RS spread from peak
def f01prs_f01_semi_peer_relative_strength_rscumdd_21d_base_v126_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(21, min_periods=11).sum()
    result = cum - _max(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of cumulative RS spread from peak
def f01prs_f01_semi_peer_relative_strength_rscumdd_63d_base_v127_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(63, min_periods=32).sum()
    result = cum - _max(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of cumulative RS spread from peak
def f01prs_f01_semi_peer_relative_strength_rscumdd_126d_base_v128_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(126, min_periods=63).sum()
    result = cum - _max(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of cumulative RS spread from peak
def f01prs_f01_semi_peer_relative_strength_rscumdd_252d_base_v129_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(252, min_periods=126).sum()
    result = cum - _max(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of cumulative RS spread from peak
def f01prs_f01_semi_peer_relative_strength_rscumdd_504d_base_v130_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(504, min_periods=252).sum()
    result = cum - _max(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional RS on basket-up days
def f01prs_f01_semi_peer_relative_strength_rscondup_21d_base_v131_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b > 0)
    result = _mean(diff, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional RS on basket-up days
def f01prs_f01_semi_peer_relative_strength_rscondup_63d_base_v132_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b > 0)
    result = _mean(diff, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional RS on basket-up days
def f01prs_f01_semi_peer_relative_strength_rscondup_126d_base_v133_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b > 0)
    result = _mean(diff, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional RS on basket-up days
def f01prs_f01_semi_peer_relative_strength_rscondup_252d_base_v134_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b > 0)
    result = _mean(diff, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional RS on basket-up days
def f01prs_f01_semi_peer_relative_strength_rscondup_504d_base_v135_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b > 0)
    result = _mean(diff, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d conditional RS on basket-down days
def f01prs_f01_semi_peer_relative_strength_rsconddn_21d_base_v136_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b < 0)
    result = _mean(diff, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d conditional RS on basket-down days
def f01prs_f01_semi_peer_relative_strength_rsconddn_63d_base_v137_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b < 0)
    result = _mean(diff, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d conditional RS on basket-down days
def f01prs_f01_semi_peer_relative_strength_rsconddn_126d_base_v138_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b < 0)
    result = _mean(diff, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d conditional RS on basket-down days
def f01prs_f01_semi_peer_relative_strength_rsconddn_252d_base_v139_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b < 0)
    result = _mean(diff, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d conditional RS on basket-down days
def f01prs_f01_semi_peer_relative_strength_rsconddn_504d_base_v140_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    diff = (o - b).where(b < 0)
    result = _mean(diff, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d RS ema half-life proxy (1 - corr of own to lagged spread)
def f01prs_f01_semi_peer_relative_strength_rshalflife_21d_base_v141_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = 1.0 - diff.rolling(21, min_periods=11).corr(diff.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RS ema half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_63d_base_v142_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = 1.0 - diff.rolling(63, min_periods=32).corr(diff.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d RS ema half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_126d_base_v143_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = 1.0 - diff.rolling(126, min_periods=63).corr(diff.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d RS ema half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_252d_base_v144_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = 1.0 - diff.rolling(252, min_periods=126).corr(diff.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d RS ema half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_504d_base_v145_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    result = 1.0 - diff.rolling(504, min_periods=252).corr(diff.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RS composite: 21d z + 63d z + 126d z (trend strength)
def f01prs_f01_semi_peer_relative_strength_rscomposite_short_base_v146_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _z(r, 21) + _z(r, 63) + _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d RS composite: 63d z + 126d z + 252d z
def f01prs_f01_semi_peer_relative_strength_rscomposite_long_base_v147_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    result = _z(r, 63) + _z(r, 126) + _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RS regime: sign of EMA21 - EMA63 minus sign of EMA126 - EMA252 (regime divergence)
def f01prs_f01_semi_peer_relative_strength_rsregime_divergence_base_v148_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    short = np.sign(r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean())
    long = np.sign(r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=r.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d RS composite (IR x hit ratio) outperformance quality
def f01prs_f01_semi_peer_relative_strength_rsquality_63d_base_v149_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    ir = _mean(diff, 63) / _std(diff, 63).replace(0, np.nan)
    hit = (diff > 0).astype(float).rolling(63, min_periods=32).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 252d RS composite (IR x hit ratio) outperformance quality
def f01prs_f01_semi_peer_relative_strength_rsquality_252d_base_v150_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    ir = _mean(diff, 252) / _std(diff, 252).replace(0, np.nan)
    hit = (diff > 0).astype(float).rolling(252, min_periods=126).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)
