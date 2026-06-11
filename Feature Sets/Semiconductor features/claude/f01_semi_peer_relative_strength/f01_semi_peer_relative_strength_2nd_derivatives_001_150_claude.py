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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


# ===== folder domain primitives =====
def _f01_own_ret(s):
    return s.pct_change()


def _f01_rs_log_ratio(own, bas):
    return np.log(own.replace(0, np.nan).abs() / bas.replace(0, np.nan).abs())


def _f01_rs_spread(own, bas, n):
    return np.log(own / own.shift(n)) - np.log(bas / bas.shift(n))


def _f01_roll_beta(own_r, bas_r, w):
    cov = own_r.rolling(w, min_periods=max(2, w // 2)).cov(bas_r)
    var = bas_r.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f01_roll_corr(own_r, bas_r, w):
    return own_r.rolling(w, min_periods=max(2, w // 2)).corr(bas_r)


# 5d slope of 21d RS log-ratio level
def f01prs_f01_semi_peer_relative_strength_rsratio_21d_slope_v001_signal(closeadj, semi_basket_closeadj):
    base = _f01_rs_log_ratio(closeadj, semi_basket_closeadj) - _mean(_f01_rs_log_ratio(closeadj, semi_basket_closeadj), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d RS log-ratio level
def f01prs_f01_semi_peer_relative_strength_rsratio_21d_slope_v002_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - _mean(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d RS log-ratio level
def f01prs_f01_semi_peer_relative_strength_rsratio_63d_slope_v003_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - _mean(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d RS log-ratio level
def f01prs_f01_semi_peer_relative_strength_rsratio_63d_slope_v004_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - _mean(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d RS log-ratio level
def f01prs_f01_semi_peer_relative_strength_rsratio_126d_slope_v005_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - _mean(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log-return spread
def f01prs_f01_semi_peer_relative_strength_rsret_21d_slope_v006_signal(closeadj, semi_basket_closeadj):
    base = _f01_rs_spread(closeadj, semi_basket_closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log-return spread
def f01prs_f01_semi_peer_relative_strength_rsret_21d_slope_v007_signal(closeadj, semi_basket_closeadj):
    base = _f01_rs_spread(closeadj, semi_basket_closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log-return spread
def f01prs_f01_semi_peer_relative_strength_rsret_63d_slope_v008_signal(closeadj, semi_basket_closeadj):
    base = _f01_rs_spread(closeadj, semi_basket_closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log-return spread
def f01prs_f01_semi_peer_relative_strength_rsret_63d_slope_v009_signal(closeadj, semi_basket_closeadj):
    base = _f01_rs_spread(closeadj, semi_basket_closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log-return spread
def f01prs_f01_semi_peer_relative_strength_rsret_126d_slope_v010_signal(closeadj, semi_basket_closeadj):
    base = _f01_rs_spread(closeadj, semi_basket_closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_21d_slope_v011_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = (r - _mean(r, 21)) / _std(r, 21).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_63d_slope_v012_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = (r - _mean(r, 63)) / _std(r, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_63d_slope_v013_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = (r - _mean(r, 63)) / _std(r, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_126d_slope_v014_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = (r - _mean(r, 126)) / _std(r, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z-score of RS log-ratio
def f01prs_f01_semi_peer_relative_strength_rsz_252d_slope_v015_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = (r - _mean(r, 252)) / _std(r, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d hit ratio
def f01prs_f01_semi_peer_relative_strength_rsfrac_21d_slope_v016_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d hit ratio
def f01prs_f01_semi_peer_relative_strength_rsfrac_21d_slope_v017_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(21, min_periods=11).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hit ratio
def f01prs_f01_semi_peer_relative_strength_rsfrac_63d_slope_v018_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d hit ratio
def f01prs_f01_semi_peer_relative_strength_rsfrac_126d_slope_v019_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d hit ratio
def f01prs_f01_semi_peer_relative_strength_rsfrac_252d_slope_v020_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d RS vol (std)
def f01prs_f01_semi_peer_relative_strength_rsstd_21d_slope_v021_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    base = _std(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d RS vol
def f01prs_f01_semi_peer_relative_strength_rsstd_21d_slope_v022_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    base = _std(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d RS vol
def f01prs_f01_semi_peer_relative_strength_rsstd_63d_slope_v023_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    base = _std(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d RS vol
def f01prs_f01_semi_peer_relative_strength_rsstd_126d_slope_v024_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    base = _std(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d RS vol
def f01prs_f01_semi_peer_relative_strength_rsstd_252d_slope_v025_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj).diff()
    base = _std(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d beta
def f01prs_f01_semi_peer_relative_strength_rsbeta_21d_slope_v026_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_beta(o, b, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d beta
def f01prs_f01_semi_peer_relative_strength_rsbeta_21d_slope_v027_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_beta(o, b, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d beta
def f01prs_f01_semi_peer_relative_strength_rsbeta_63d_slope_v028_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_beta(o, b, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d beta
def f01prs_f01_semi_peer_relative_strength_rsbeta_126d_slope_v029_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_beta(o, b, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d beta
def f01prs_f01_semi_peer_relative_strength_rsbeta_252d_slope_v030_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_beta(o, b, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d correlation
def f01prs_f01_semi_peer_relative_strength_rscorr_21d_slope_v031_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_corr(o, b, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d correlation
def f01prs_f01_semi_peer_relative_strength_rscorr_21d_slope_v032_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_corr(o, b, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d correlation
def f01prs_f01_semi_peer_relative_strength_rscorr_63d_slope_v033_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_corr(o, b, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d correlation
def f01prs_f01_semi_peer_relative_strength_rscorr_126d_slope_v034_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_corr(o, b, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d correlation
def f01prs_f01_semi_peer_relative_strength_rscorr_252d_slope_v035_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _f01_roll_corr(o, b, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d tracking error
def f01prs_f01_semi_peer_relative_strength_rste_21d_slope_v036_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _std(diff, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d tracking error
def f01prs_f01_semi_peer_relative_strength_rste_21d_slope_v037_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _std(diff, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d tracking error
def f01prs_f01_semi_peer_relative_strength_rste_63d_slope_v038_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _std(diff, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d tracking error
def f01prs_f01_semi_peer_relative_strength_rste_126d_slope_v039_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _std(diff, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d tracking error
def f01prs_f01_semi_peer_relative_strength_rste_252d_slope_v040_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _std(diff, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d IR
def f01prs_f01_semi_peer_relative_strength_rsir_21d_slope_v041_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _mean(diff, 21) / _std(diff, 21).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d IR
def f01prs_f01_semi_peer_relative_strength_rsir_21d_slope_v042_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _mean(diff, 21) / _std(diff, 21).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d IR
def f01prs_f01_semi_peer_relative_strength_rsir_63d_slope_v043_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _mean(diff, 63) / _std(diff, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d IR
def f01prs_f01_semi_peer_relative_strength_rsir_126d_slope_v044_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _mean(diff, 126) / _std(diff, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d IR
def f01prs_f01_semi_peer_relative_strength_rsir_252d_slope_v045_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = _mean(diff, 252) / _std(diff, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d up-capture
def f01prs_f01_semi_peer_relative_strength_rsupcap_21d_slope_v046_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    base = _mean(o.where(mask), 21) / _mean(b.where(mask), 21).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d up-capture
def f01prs_f01_semi_peer_relative_strength_rsupcap_63d_slope_v047_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    base = _mean(o.where(mask), 63) / _mean(b.where(mask), 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d up-capture
def f01prs_f01_semi_peer_relative_strength_rsupcap_126d_slope_v048_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    base = _mean(o.where(mask), 126) / _mean(b.where(mask), 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d up-capture
def f01prs_f01_semi_peer_relative_strength_rsupcap_252d_slope_v049_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    base = _mean(o.where(mask), 252) / _mean(b.where(mask), 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d up-capture
def f01prs_f01_semi_peer_relative_strength_rsupcap_504d_slope_v050_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b > 0
    base = _mean(o.where(mask), 504) / _mean(b.where(mask), 504).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d down-capture
def f01prs_f01_semi_peer_relative_strength_rsdncap_21d_slope_v051_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    base = _mean(o.where(mask), 21) / _mean(b.where(mask), 21).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d down-capture
def f01prs_f01_semi_peer_relative_strength_rsdncap_63d_slope_v052_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    base = _mean(o.where(mask), 63) / _mean(b.where(mask), 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d down-capture
def f01prs_f01_semi_peer_relative_strength_rsdncap_126d_slope_v053_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    base = _mean(o.where(mask), 126) / _mean(b.where(mask), 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d down-capture
def f01prs_f01_semi_peer_relative_strength_rsdncap_252d_slope_v054_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    base = _mean(o.where(mask), 252) / _mean(b.where(mask), 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d down-capture
def f01prs_f01_semi_peer_relative_strength_rsdncap_504d_slope_v055_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    mask = b < 0
    base = _mean(o.where(mask), 504) / _mean(b.where(mask), 504).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d vol ratio
def f01prs_f01_semi_peer_relative_strength_rsvolratio_21d_slope_v056_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _std(o, 21) / _std(b, 21).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d vol ratio
def f01prs_f01_semi_peer_relative_strength_rsvolratio_63d_slope_v057_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _std(o, 63) / _std(b, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d vol ratio
def f01prs_f01_semi_peer_relative_strength_rsvolratio_126d_slope_v058_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _std(o, 126) / _std(b, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d vol ratio
def f01prs_f01_semi_peer_relative_strength_rsvolratio_252d_slope_v059_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _std(o, 252) / _std(b, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d vol ratio
def f01prs_f01_semi_peer_relative_strength_rsvolratio_504d_slope_v060_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _std(o, 504) / _std(b, 504).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d drawdown
def f01prs_f01_semi_peer_relative_strength_rsdd_21d_slope_v061_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(21, min_periods=11).max()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown
def f01prs_f01_semi_peer_relative_strength_rsdd_63d_slope_v062_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(63, min_periods=32).max()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d drawdown
def f01prs_f01_semi_peer_relative_strength_rsdd_126d_slope_v063_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(126, min_periods=63).max()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown
def f01prs_f01_semi_peer_relative_strength_rsdd_252d_slope_v064_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(252, min_periods=126).max()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d drawdown
def f01prs_f01_semi_peer_relative_strength_rsdd_504d_slope_v065_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(504, min_periods=252).max()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d run-up
def f01prs_f01_semi_peer_relative_strength_rsup_21d_slope_v066_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(21, min_periods=11).min()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up
def f01prs_f01_semi_peer_relative_strength_rsup_63d_slope_v067_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(63, min_periods=32).min()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d run-up
def f01prs_f01_semi_peer_relative_strength_rsup_126d_slope_v068_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(126, min_periods=63).min()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d run-up
def f01prs_f01_semi_peer_relative_strength_rsup_252d_slope_v069_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(252, min_periods=126).min()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d run-up
def f01prs_f01_semi_peer_relative_strength_rsup_504d_slope_v070_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r - r.rolling(504, min_periods=252).min()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d range
def f01prs_f01_semi_peer_relative_strength_rsrng_21d_slope_v071_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(21, min_periods=11).max() - r.rolling(21, min_periods=11).min()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range
def f01prs_f01_semi_peer_relative_strength_rsrng_63d_slope_v072_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(63, min_periods=32).max() - r.rolling(63, min_periods=32).min()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d range
def f01prs_f01_semi_peer_relative_strength_rsrng_126d_slope_v073_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(126, min_periods=63).max() - r.rolling(126, min_periods=63).min()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d range
def f01prs_f01_semi_peer_relative_strength_rsrng_252d_slope_v074_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(252, min_periods=126).max() - r.rolling(252, min_periods=126).min()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d range
def f01prs_f01_semi_peer_relative_strength_rsrng_504d_slope_v075_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(504, min_periods=252).max() - r.rolling(504, min_periods=252).min()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d position-in-range
def f01prs_f01_semi_peer_relative_strength_rspos_21d_slope_v076_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = r.rolling(21, min_periods=11).min()
    hi = r.rolling(21, min_periods=11).max()
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d position-in-range
def f01prs_f01_semi_peer_relative_strength_rspos_63d_slope_v077_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = r.rolling(63, min_periods=32).min()
    hi = r.rolling(63, min_periods=32).max()
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d position-in-range
def f01prs_f01_semi_peer_relative_strength_rspos_126d_slope_v078_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = r.rolling(126, min_periods=63).min()
    hi = r.rolling(126, min_periods=63).max()
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d position-in-range
def f01prs_f01_semi_peer_relative_strength_rspos_252d_slope_v079_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = r.rolling(252, min_periods=126).min()
    hi = r.rolling(252, min_periods=126).max()
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d position-in-range
def f01prs_f01_semi_peer_relative_strength_rspos_504d_slope_v080_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    lo = r.rolling(504, min_periods=252).min()
    hi = r.rolling(504, min_periods=252).max()
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_21d_slope_v081_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = pd.Series(np.sign(o - b), index=o.index).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_63d_slope_v082_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = pd.Series(np.sign(o - b), index=o.index).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_126d_slope_v083_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = pd.Series(np.sign(o - b), index=o.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_252d_slope_v084_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = pd.Series(np.sign(o - b), index=o.index).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d signed cumulative outperformance
def f01prs_f01_semi_peer_relative_strength_rssigncum_504d_slope_v085_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = pd.Series(np.sign(o - b), index=o.index).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d cumulative spread
def f01prs_f01_semi_peer_relative_strength_rscumspread_21d_slope_v086_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cumulative spread
def f01prs_f01_semi_peer_relative_strength_rscumspread_63d_slope_v087_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d cumulative spread
def f01prs_f01_semi_peer_relative_strength_rscumspread_126d_slope_v088_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d cumulative spread
def f01prs_f01_semi_peer_relative_strength_rscumspread_252d_slope_v089_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d cumulative spread
def f01prs_f01_semi_peer_relative_strength_rscumspread_504d_slope_v090_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d skew
def f01prs_f01_semi_peer_relative_strength_rsskew_21d_slope_v091_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(21, min_periods=11).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew
def f01prs_f01_semi_peer_relative_strength_rsskew_63d_slope_v092_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(63, min_periods=32).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d skew
def f01prs_f01_semi_peer_relative_strength_rsskew_126d_slope_v093_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d skew
def f01prs_f01_semi_peer_relative_strength_rsskew_252d_slope_v094_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(252, min_periods=126).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d skew
def f01prs_f01_semi_peer_relative_strength_rsskew_504d_slope_v095_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(504, min_periods=252).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d kurtosis
def f01prs_f01_semi_peer_relative_strength_rskurt_21d_slope_v096_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(21, min_periods=11).kurt()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d kurtosis
def f01prs_f01_semi_peer_relative_strength_rskurt_63d_slope_v097_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(63, min_periods=32).kurt()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d kurtosis
def f01prs_f01_semi_peer_relative_strength_rskurt_126d_slope_v098_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(126, min_periods=63).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d kurtosis
def f01prs_f01_semi_peer_relative_strength_rskurt_252d_slope_v099_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d kurtosis
def f01prs_f01_semi_peer_relative_strength_rskurt_504d_slope_v100_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = diff.rolling(504, min_periods=252).kurt()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of conditional up-day RS (21d)
def f01prs_f01_semi_peer_relative_strength_rscondup_21d_slope_v101_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b > 0), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d conditional up-day RS
def f01prs_f01_semi_peer_relative_strength_rscondup_63d_slope_v102_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b > 0), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d conditional up-day RS
def f01prs_f01_semi_peer_relative_strength_rscondup_126d_slope_v103_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b > 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d conditional up-day RS
def f01prs_f01_semi_peer_relative_strength_rscondup_252d_slope_v104_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b > 0), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d conditional up-day RS
def f01prs_f01_semi_peer_relative_strength_rscondup_504d_slope_v105_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b > 0), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d conditional down-day RS
def f01prs_f01_semi_peer_relative_strength_rsconddn_21d_slope_v106_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b < 0), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d conditional down-day RS
def f01prs_f01_semi_peer_relative_strength_rsconddn_63d_slope_v107_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b < 0), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d conditional down-day RS
def f01prs_f01_semi_peer_relative_strength_rsconddn_126d_slope_v108_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b < 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d conditional down-day RS
def f01prs_f01_semi_peer_relative_strength_rsconddn_252d_slope_v109_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b < 0), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d conditional down-day RS
def f01prs_f01_semi_peer_relative_strength_rsconddn_504d_slope_v110_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = _mean((o - b).where(b < 0), 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d hits count
def f01prs_f01_semi_peer_relative_strength_rshits_21d_slope_v111_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(21, min_periods=11).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d hits count
def f01prs_f01_semi_peer_relative_strength_rshits_63d_slope_v112_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d hits count
def f01prs_f01_semi_peer_relative_strength_rshits_126d_slope_v113_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d hits count
def f01prs_f01_semi_peer_relative_strength_rshits_252d_slope_v114_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d hits count
def f01prs_f01_semi_peer_relative_strength_rshits_504d_slope_v115_signal(closeadj, semi_basket_closeadj):
    o, b = _f01_own_ret(closeadj), _f01_own_ret(semi_basket_closeadj)
    base = (o > b).astype(float).rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d max RS
def f01prs_f01_semi_peer_relative_strength_rsmax_21d_slope_v116_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(21, min_periods=11).max()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max RS
def f01prs_f01_semi_peer_relative_strength_rsmax_63d_slope_v117_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(63, min_periods=32).max()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d max RS
def f01prs_f01_semi_peer_relative_strength_rsmax_126d_slope_v118_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(126, min_periods=63).max()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max RS
def f01prs_f01_semi_peer_relative_strength_rsmax_252d_slope_v119_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(252, min_periods=126).max()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d max RS
def f01prs_f01_semi_peer_relative_strength_rsmax_504d_slope_v120_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(504, min_periods=252).max()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d min RS
def f01prs_f01_semi_peer_relative_strength_rsmin_21d_slope_v121_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(21, min_periods=11).min()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min RS
def f01prs_f01_semi_peer_relative_strength_rsmin_63d_slope_v122_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(63, min_periods=32).min()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d min RS
def f01prs_f01_semi_peer_relative_strength_rsmin_126d_slope_v123_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(126, min_periods=63).min()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d min RS
def f01prs_f01_semi_peer_relative_strength_rsmin_252d_slope_v124_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(252, min_periods=126).min()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d min RS
def f01prs_f01_semi_peer_relative_strength_rsmin_504d_slope_v125_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.rolling(504, min_periods=252).min()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EMA 5v21 crossover
def f01prs_f01_semi_peer_relative_strength_rsema_5v21_slope_v126_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.ewm(span=5, adjust=False).mean() - r.ewm(span=21, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21v63 EMA crossover
def f01prs_f01_semi_peer_relative_strength_rsema_21v63_slope_v127_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63v126 EMA crossover
def f01prs_f01_semi_peer_relative_strength_rsema_63v126_slope_v128_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.ewm(span=63, adjust=False).mean() - r.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126v252 EMA crossover
def f01prs_f01_semi_peer_relative_strength_rsema_126v252_slope_v129_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252v504 EMA crossover
def f01prs_f01_semi_peer_relative_strength_rsema_252v504_slope_v130_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = r.ewm(span=252, adjust=False).mean() - r.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of cumulative drawdown 21d
def f01prs_f01_semi_peer_relative_strength_rscumdd_21d_slope_v131_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(21, min_periods=11).sum()
    base = cum - cum.rolling(21, min_periods=11).max()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of cumulative drawdown 63d
def f01prs_f01_semi_peer_relative_strength_rscumdd_63d_slope_v132_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(63, min_periods=32).sum()
    base = cum - cum.rolling(63, min_periods=32).max()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cumulative drawdown 126d
def f01prs_f01_semi_peer_relative_strength_rscumdd_126d_slope_v133_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(126, min_periods=63).sum()
    base = cum - cum.rolling(126, min_periods=63).max()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cumulative drawdown 252d
def f01prs_f01_semi_peer_relative_strength_rscumdd_252d_slope_v134_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(252, min_periods=126).sum()
    base = cum - cum.rolling(252, min_periods=126).max()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of cumulative drawdown 504d
def f01prs_f01_semi_peer_relative_strength_rscumdd_504d_slope_v135_signal(closeadj, semi_basket_closeadj):
    cum = (_f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)).rolling(504, min_periods=252).sum()
    base = cum - cum.rolling(504, min_periods=252).max()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d robust z
def f01prs_f01_semi_peer_relative_strength_rsrobustz_21d_slope_v136_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(21, min_periods=11).median()
    mad = (r - med).abs().rolling(21, min_periods=11).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robust z
def f01prs_f01_semi_peer_relative_strength_rsrobustz_63d_slope_v137_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(63, min_periods=32).median()
    mad = (r - med).abs().rolling(63, min_periods=32).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d robust z
def f01prs_f01_semi_peer_relative_strength_rsrobustz_126d_slope_v138_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(126, min_periods=63).median()
    mad = (r - med).abs().rolling(126, min_periods=63).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d robust z
def f01prs_f01_semi_peer_relative_strength_rsrobustz_252d_slope_v139_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(252, min_periods=126).median()
    mad = (r - med).abs().rolling(252, min_periods=126).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d robust z
def f01prs_f01_semi_peer_relative_strength_rsrobustz_504d_slope_v140_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    med = r.rolling(504, min_periods=252).median()
    mad = (r - med).abs().rolling(504, min_periods=252).median()
    base = (r - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_21d_slope_v141_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = 1.0 - diff.rolling(21, min_periods=11).corr(diff.shift(1))
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_63d_slope_v142_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = 1.0 - diff.rolling(63, min_periods=32).corr(diff.shift(1))
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_126d_slope_v143_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = 1.0 - diff.rolling(126, min_periods=63).corr(diff.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_252d_slope_v144_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = 1.0 - diff.rolling(252, min_periods=126).corr(diff.shift(1))
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d half-life proxy
def f01prs_f01_semi_peer_relative_strength_rshalflife_504d_slope_v145_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    base = 1.0 - diff.rolling(504, min_periods=252).corr(diff.shift(1))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of short composite (sum of 21/63/126 z-scores)
def f01prs_f01_semi_peer_relative_strength_rscomposite_short_slope_v146_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = (r - _mean(r, 21)) / _std(r, 21).replace(0, np.nan) + (r - _mean(r, 63)) / _std(r, 63).replace(0, np.nan) + (r - _mean(r, 126)) / _std(r, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of long composite (sum of 63/126/252 z-scores)
def f01prs_f01_semi_peer_relative_strength_rscomposite_long_slope_v147_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    base = (r - _mean(r, 63)) / _std(r, 63).replace(0, np.nan) + (r - _mean(r, 126)) / _std(r, 126).replace(0, np.nan) + (r - _mean(r, 252)) / _std(r, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of regime divergence
def f01prs_f01_semi_peer_relative_strength_rsregime_slope_v148_signal(closeadj, semi_basket_closeadj):
    r = _f01_rs_log_ratio(closeadj, semi_basket_closeadj)
    short = np.sign(r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean())
    long = np.sign(r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean())
    base = pd.Series(short - long, index=r.index)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d quality (IR x hit)
def f01prs_f01_semi_peer_relative_strength_rsquality_63d_slope_v149_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    ir = _mean(diff, 63) / _std(diff, 63).replace(0, np.nan)
    hit = (diff > 0).astype(float).rolling(63, min_periods=32).mean()
    base = ir * hit
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d quality (IR x hit)
def f01prs_f01_semi_peer_relative_strength_rsquality_252d_slope_v150_signal(closeadj, semi_basket_closeadj):
    diff = _f01_own_ret(closeadj) - _f01_own_ret(semi_basket_closeadj)
    ir = _mean(diff, 252) / _std(diff, 252).replace(0, np.nan)
    hit = (diff > 0).astype(float).rolling(252, min_periods=126).mean()
    base = ir * hit
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
